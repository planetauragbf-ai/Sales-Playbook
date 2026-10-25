// Imprime le guide HTML en PDF A4, avec numéro de page en pied.
const { chromium } = require('playwright');
const path = require('path');

const [, , src, out] = process.argv;
(async () => {
  const browser = await chromium.launch({ executablePath: require('fs').existsSync('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') ? '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' : undefined });
  const page = await browser.newPage();
  await page.goto(`file://${path.resolve(src)}`, { waitUntil: 'load' });
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({
    path: out,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;font-family:Inter,Arial;font-size:7.5pt;color:#6A7B82;padding:0 16mm;display:flex;justify-content:space-between"><span>Guide de soutenance · Sales Playbook Planet Aura · usage personnel</span><span class="pageNumber"></span></div>',
  });
  await browser.close();
  console.log('pdf ok', out);
})();
