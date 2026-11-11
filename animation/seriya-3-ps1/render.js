// Рендер: node render.js [out.mp4]      Кадры для проверки: node render.js --stills 5,15,20
// Страница грузится через локальный http-сервер (ES-модули не работают с file://).
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const TYPES = { '.html': 'text/html', '.js': 'text/javascript' };
const server = http.createServer((req, res) => {
  const f = path.join(__dirname, decodeURIComponent(req.url.split('?')[0]) === '/' ? 'index.html' : decodeURIComponent(req.url.split('?')[0]));
  if (!f.startsWith(__dirname) || !fs.existsSync(f)) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
});

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const args = process.argv.slice(2);
  const stillsIdx = args.indexOf('--stills');
  const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const page = await browser.newPage({ viewport: { width: 960, height: 720 } });
  page.on('pageerror', e => { console.error('PAGE ERROR', e); process.exit(1); });
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') console.log('console:', m.text()); });
  await page.addInitScript(() => { window.__RENDER_MODE = true; });
  await page.goto(`http://127.0.0.1:${port}/`);
  await page.waitForFunction(() => window.__ready);
  console.log('font ok:', await page.evaluate(() => window.__ready));
  const grab = (t, q) => page.evaluate(([t, q]) => { render(t); return document.getElementById('out').toDataURL('image/jpeg', q); }, [t, q]);

  if (stillsIdx >= 0) {
    const dir = path.resolve(__dirname, 'stills'); fs.mkdirSync(dir, { recursive: true });
    for (const s of args[stillsIdx + 1].split(',')) {
      const d = await grab(parseFloat(s), 0.9);
      fs.writeFileSync(path.join(dir, `t${String(parseFloat(s).toFixed(1)).padStart(5, '0')}.jpg`), Buffer.from(d.split(',')[1], 'base64'));
    }
  } else {
    const out = path.resolve(args[0] || path.join(__dirname, 'seriya-3-ps1.mp4'));
    const [T, FPS] = await page.evaluate(() => [window.T, window.FPS]), N = Math.round(T * FPS);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-vf', 'scale=1440:1080:flags=neighbor,fps=30,format=yuv420p', '-c:v', 'libx264', '-crf', '24', '-preset', 'medium', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
    for (let i = 0; i < N; i++) {
      const d = await grab(i / FPS, 0.95);
      if (!ff.stdin.write(Buffer.from(d.split(',')[1], 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
      if (i % 150 === 0) console.log(`frame ${i}/${N}`);
    }
    ff.stdin.end(); await new Promise(r => ff.on('close', r));
    console.log('done', out);
  }
  await browser.close(); server.close();
})();
