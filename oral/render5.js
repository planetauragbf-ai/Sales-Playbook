// Banc de rendu local : rend chaque diapo (1920x1080) avec les polices installées et signale les débordements.
// usage : node render5.js <dossier slides> <dossier sortie> id1 id2 ...
// STRESS=1.08 : agrandit tous les textes de 8 % avant contrôle (marge contre les écarts de métrique du moteur réel)
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const [, , slidesDir, outDir, ...ids] = process.argv;
// images sources locales (non versionnées) : dossier img/ à côté de ce script, ou IMG_DIR
const IMG = process.env.IMG_DIR || path.join(__dirname, 'img');
const map = {};
for (const line of fs.readFileSync(path.join(__dirname, 'assets-map.md'), 'utf8').split('\n')) {
  const m = line.match(/^(\S+) \/_blob\/([0-9a-f]+)/);
  if (m) map[m[2]] = `file://${IMG}/${m[1]}.png`;
}

const FONTS = path.join(__dirname, 'webfonts');
const ffc = (fam, file, w, st) => `@font-face{font-family:'${fam}';src:url(file://${FONTS}/${file}) format('woff2');font-weight:${w};font-style:${st};unicode-range:${file.includes('-ext-') ? 'U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF' : 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'}}`;
const FONTCSS = [
  ffc('Inter', 'inter-latin-wght-normal.woff2', '100 900', 'normal'), ffc('Inter', 'inter-latin-ext-wght-normal.woff2', '100 900', 'normal'),
  ffc('Inter', 'inter-latin-wght-italic.woff2', '100 900', 'italic'),
  ffc('Playfair Display', 'playfair-display-latin-wght-normal.woff2', '400 900', 'normal'), ffc('Playfair Display', 'playfair-display-latin-ext-wght-normal.woff2', '400 900', 'normal'),
  ffc('Playfair Display', 'playfair-display-latin-wght-italic.woff2', '400 900', 'italic'), ffc('Playfair Display', 'playfair-display-latin-ext-wght-italic.woff2', '400 900', 'italic'),
  ...['500', '600', '700'].flatMap(w => [ffc('Poppins', `poppins-latin-${w}-normal.woff2`, w, 'normal'), ffc('Poppins', `poppins-latin-ext-${w}-normal.woff2`, w, 'normal')]),
].join('\n');
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
    html = html.replace(/<x-icon name="(\w+)" style="([^"]*)"><\/x-icon>/g, (m, n, st) => `<span title="${n}" style="display:inline-block;flex:none;${st};border-radius:30%;border:3px solid currentColor;opacity:.8"></span>`);
    const tmp = path.resolve(outDir, `_${id}.html`);
    fs.writeFileSync(tmp, `<!doctype html><html><head><meta charset="utf-8"><style>${FONTCSS}\n${CSS}</style></head><body>${html}</body></html>`);
    await page.goto(`file://${tmp}`, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const STRESS = parseFloat(process.env.STRESS || '1');
    if (STRESS !== 1) {
      await page.evaluate((k) => {
        const els = [...document.querySelectorAll('section *')];
        const sizes = els.map(e => parseFloat(getComputedStyle(e).fontSize));
        els.forEach((e, i) => { e.style.fontSize = (sizes[i] * k) + 'px'; });
      }, STRESS);
    }
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
        let pinned = false;
        for (let a = el; a && a !== sec; a = a.parentElement) if (getComputedStyle(a).position === 'absolute') { pinned = true; break; }
        if (!pinned) {
          maxBottom = Math.max(maxBottom, r.bottom);
          // marge droite : le flux ne doit pas dépasser le padding droit de la section
          if (!el.closest('svg') && r.right > 1920 - parseFloat(cs.paddingRight) + 2)
            issues.push(`MARGE DROITE ${el.tagName} ${Math.round(r.right)} « ${(el.textContent || '').trim().slice(0, 40)} »`);
        }
        if (r.right > 1920.5 || r.bottom > 1080.5) issues.push(`HORS CADRE ${el.tagName} ${Math.round(r.right)}x${Math.round(r.bottom)} « ${(el.textContent || '').trim().slice(0, 40)} »`);
        // texte qui déborde de sa boîte
        if (['P', 'H1', 'H2', 'H3', 'TD', 'TH', 'LI'].includes(el.tagName) && el.scrollWidth > el.clientWidth + 2)
          issues.push(`MOT TROP LONG ${el.tagName} « ${(el.textContent || '').trim().slice(0, 50)} » (${el.scrollWidth}>${el.clientWidth})`);
      }
      if (maxBottom > limit + 1) issues.push(`FLUX DÉPASSE : bas ${Math.round(maxBottom)} > limite ${Math.round(limit)}`);
      // texte qui sort verticalement de sa boîte (le moteur réel le peint par-dessus le voisin, ou le rétrécit)
      for (const el of sec.querySelectorAll('*')) {
        if (el.closest('aside') || el.closest('svg')) continue;
        if (el.clientHeight > 0 && el.scrollHeight - el.clientHeight > Math.max(8, 0.6 * parseFloat(getComputedStyle(el).fontSize)) && getComputedStyle(el).overflow === 'visible' && (el.textContent || '').trim())
          issues.push(`DÉBORDE SA BOÎTE ${el.tagName} ${el.scrollHeight}>${el.clientHeight} « ${(el.textContent || '').trim().slice(0, 40)} »`);
      }
      // chevauchements entre éléments porteurs de texte (lignes réelles du texte, via Range)
      const leaves = [];
      const walker = document.createTreeWalker(sec, NodeFilter.SHOW_TEXT);
      let n;
      while ((n = walker.nextNode())) {
        if (!n.textContent.trim() || n.parentElement.closest('aside')) continue;
        const rg = document.createRange(); rg.selectNodeContents(n);
        for (const r of rg.getClientRects()) if (r.width > 1 && r.height > 1) leaves.push({ r, el: n.parentElement, t: n.textContent.trim().slice(0, 30) });
      }
      for (const im of sec.querySelectorAll('img, svg')) { const r = im.getBoundingClientRect(); if (r.width > 1) leaves.push({ r, el: im, t: im.tagName }); }
      const seen = new Set();
      for (let i = 0; i < leaves.length; i++) for (let j = i + 1; j < leaves.length; j++) {
        const a = leaves[i], b = leaves[j];
        if (a.el === b.el || a.el.contains(b.el) || b.el.contains(a.el)) continue;
        const ox = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
        const oy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
        if (ox > 3 && oy > 4) {
          const isGfx = x => x.t === 'IMG' || x.t === 'svg' || x.t === 'SVG';
          if (isGfx(a) && isGfx(b)) continue;
          const k = a.t + '|' + b.t; if (seen.has(k)) continue; seen.add(k);
          issues.push(`CHEVAUCHEMENT « ${a.t} » / « ${b.t} » (${Math.round(ox)}×${Math.round(oy)} px)`);
        }
      }
      // mots visibles (hors notes, en-tête de partie et pied de page compris)
      const words = (sec.innerText || '').replace(/\s+/g, ' ').trim().split(' ').filter(w => /[\wÀ-ÿ€%]/.test(w)).length;
      issues.words = words;
      return { maxBottom: Math.round(maxBottom), limit: Math.round(limit), issues, words: issues.words };
    });
    await page.screenshot({ path: path.join(outDir, STRESS !== 1 ? `${id}_stress.png` : `${id}.png`) });
    console.log(`${id}: ${report.words} mots visibles, bas du flux ${report.maxBottom}/${report.limit}${report.issues.length ? '\n  - ' + report.issues.join('\n  - ') : '  OK'}`);
  }
  await browser.close();
})();
