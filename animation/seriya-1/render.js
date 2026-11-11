// Рендер: node render.js [out.mp4]      Кадры для проверки: node render.js --stills 5,15,20
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

(async () => {
  const args = process.argv.slice(2);
  const stillsIdx = args.indexOf('--stills');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  page.on('pageerror', e => { console.error('PAGE ERROR', e); process.exit(1); });
  await page.addInitScript(() => { window.__RENDER_MODE = true; });
  await page.goto('file://' + path.resolve(__dirname, 'index.html'));
  await page.evaluate(async () => {
    await document.fonts.ready;
    await Promise.all(['700 40px Oswald', '500 40px Oswald', '700 40px "PT Serif"', 'italic 700 40px "PT Serif"', '40px "PT Mono"']
      .map(f => document.fonts.load(f, 'АаЁё')));
  });
  const ok = await page.evaluate(() => ['700 40px Oswald', 'italic 700 40px "PT Serif"', '40px "PT Mono"'].map(f => document.fonts.check(f, 'Аа')));
  console.log('fonts', ok);
  const grab = (t, q) => page.evaluate(([t, q]) => { render(t); return cv.toDataURL('image/jpeg', q); }, [t, q]);

  if (stillsIdx >= 0) {
    const dir = path.resolve(__dirname, 'stills'); fs.mkdirSync(dir, { recursive: true });
    for (const s of args[stillsIdx + 1].split(',')) {
      const d = await grab(parseFloat(s), 0.85);
      fs.writeFileSync(path.join(dir, `t${s}.jpg`), Buffer.from(d.split(',')[1], 'base64'));
    }
    await browser.close(); return;
  }

  const out = path.resolve(args[0] || path.join(__dirname, 'seriya-1.mp4'));
  const T = await page.evaluate(() => T), N = Math.round(T * 12);
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', '12', '-i', '-',
    '-vf', 'fps=24,format=yuv420p', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < N; i++) {
    const d = await grab(i / 12, 0.93);
    if (!ff.stdin.write(Buffer.from(d.split(',')[1], 'base64'))) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 60 === 0) console.log(`frame ${i}/${N}`);
  }
  ff.stdin.end();
  await new Promise(r => ff.on('close', r));
  await browser.close();
  console.log('done', out);
})();
