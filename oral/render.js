// Banc de rendu local : rend chaque diapo (1920x1080) avec les polices installées et signale les débordements.
// usage : node render.js <dossier slides> <dossier sortie> id1 id2 ...
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [, , slidesDir, outDir, ...ids] = process.argv;
const IMG = '/tmp/claude-0/-home-user-Sales-Playbook/937d2675-9cdd-54b9-a3ad-2207ab8c8104/scratchpad/oral/img';
const map = {};
for (const line of fs.readFileSync(path.join(path.dirname(IMG), 'assets-map.md'), 'utf8').split('\n')) {
  const m = line.match(/^(\S+) \/_blob\/([0-9a-f]+)/);
  if (m) map[m[2]] = `file://${IMG}/${m[1]}.png`;
}
const CSS = `
*{margin:0;padding:0;box-sizing:border-box}
body{width:1920px;height:1080px;overflow:hidden;background:#888}
section{position:relative;width:1920px;height:1080px;overflow:hidden}
p{font-size:32px;line-height:1.4}
h1{font-size:96px;font-weight:600;line-height:1.1}
h2{font-size:64px;font-weight:600;line-height:1.15}
h3{font-size:44px;font-weight:600;line-height:1.2}
aside{display:none}
x-shape{display:block}
table{border-collapse:collapse}
td,th{border-bottom:1px solid #DCE6E9;text-align:left;vertical-align:top}
ul,ol{padding-left:1.2em}
`;

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  for (const id of ids) {
    let html = fs.readFileSync(path.join(slidesDir, `${id}.html`), 'utf8');
    html = html.replace(/\/_blob\/([0-9a-f]+)/g, (m, b) => map[b] || m);
    const tmp = path.resolve(outDir, `_${id}.html`);
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${html}</body></html>`);
    await page.goto(`file://${tmp}`, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const report = await page.evaluate(() => {
      const sec = document.querySelector('section');
      const cs = getComputedStyle(sec);
      const padB = parseFloat(cs.paddingBottom);
      const limit = 1080 - padB;
      const issues = [];
      let maxBottom = 0;
      for (const el of sec.querySelectorAll('*')) {
        if (el.closest('aside')) continue;
        const st = getComputedStyle(el);
        const r = el.getBoundingClientRect();
        if (r.width === 0 && r.height === 0) continue;
        const pinned = st.position === 'absolute';
        if (!pinned && !el.closest('[style*="position:absolute"]')) maxBottom = Math.max(maxBottom, r.bottom);
        if (r.right > 1920.5 || r.bottom > 1080.5) issues.push(`HORS CADRE ${el.tagName} ${Math.round(r.right)}x${Math.round(r.bottom)} « ${(el.textContent || '').trim().slice(0, 40)} »`);
        // texte qui déborde de sa boîte
        if (['P', 'H1', 'H2', 'H3', 'TD', 'TH', 'LI'].includes(el.tagName) && el.scrollWidth > el.clientWidth + 2)
          issues.push(`MOT TROP LONG ${el.tagName} « ${(el.textContent || '').trim().slice(0, 50)} » (${el.scrollWidth}>${el.clientWidth})`);
      }
      if (maxBottom > limit + 1) issues.push(`FLUX DÉPASSE : bas ${Math.round(maxBottom)} > limite ${Math.round(limit)}`);
      return { maxBottom: Math.round(maxBottom), limit: Math.round(limit), issues };
    });
    await page.screenshot({ path: path.join(outDir, `${id}.png`) });
    console.log(`${id}: bas du flux ${report.maxBottom}/${report.limit}${report.issues.length ? '\n  - ' + report.issues.join('\n  - ') : '  OK'}`);
  }
  await browser.close();
})();
