// Рендер серии: node render.js ep01            Кадры для проверки: node render.js ep01 --stills 5,15,20
// Сервер отдаёт всю папку mandela/, чтобы серия могла импортировать ../common/*.js
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = __dirname;
const TYPES = { '.html': 'text/html', '.js': 'text/javascript' };
const server = http.createServer((req, res) => {
  const f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]));
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { res.writeHead(404); return res.end(); }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(res);
});

(async () => {
  const args = process.argv.slice(2), ep = args[0];
  if (!ep || !fs.existsSync(path.join(ROOT, ep, 'index.html'))) { console.error('usage: node render.js epNN [--stills a,b,c]'); process.exit(1); }
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const stillsIdx = args.indexOf('--stills');
  const browser = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
  const page = await browser.newPage({ viewport: { width: 960, height: 720 } });
  page.on('pageerror', e => { console.error('PAGE ERROR', e); process.exit(1); });
  page.on('console', m => { if (m.type() === 'error') console.log('console:', m.text()); });
  await page.addInitScript(() => { window.__RENDER_MODE = true; });
  await page.goto(`http://127.0.0.1:${port}/${ep}/index.html`);
  await page.waitForFunction(() => window.__ready);
  console.log('font ok:', await page.evaluate(() => window.__ready));
  const grab = (t, q) => page.evaluate(([t, q]) => { render(t); return document.getElementById('out').toDataURL('image/jpeg', q); }, [t, q]);
  if (stillsIdx >= 0) {
    const dir = path.join(ROOT, ep, 'stills'); fs.mkdirSync(dir, { recursive: true });
    for (const s of args[stillsIdx + 1].split(',')) {
      const d = await grab(parseFloat(s), 0.9);
      fs.writeFileSync(path.join(dir, `t${parseFloat(s).toFixed(1).padStart(5, '0')}.jpg`), Buffer.from(d.split(',')[1], 'base64'));
    }
  } else {
    const out = path.join(ROOT, ep, `${ep}.mp4`);
    const [T, FPS, OW, OH] = await page.evaluate(() => [window.T, window.FPS, ...(window.OUT_SIZE || [1440, 1080])]), N = Math.round(T * FPS);
    const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
      '-vf', `scale=${OW}:${OH}:flags=neighbor,fps=30,format=yuv420p`, '-c:v', 'libx264', '-crf', '30', '-preset', 'medium', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
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
