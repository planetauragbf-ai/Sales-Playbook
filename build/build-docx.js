const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, WidthType, ShadingType, BorderStyle,
  LevelFormat, PageBreak, Footer, PageNumber, VerticalAlign
} = require('docx');

const SRC = require('path').join(__dirname, '..');
const A = require('path').join(__dirname, 'assets');
const FILES = [
  'README.md','00-resume-executif.md','01-entreprise.md','02-marche.md',
  '03-offres-services.md','04-tarifs.md','05-cibles-personas.md','06-proposition-valeur.md',
  '07-processus-vente.md','08-prospection-scripts.md','09-objections.md','10-concurrence.md',
  '11-preuves-references.md','12-onboarding-retention.md','13-sav-sinistres.md',
  '14-conformite-reglementation.md','15-kpis-pilotage.md','16-annexes-outils.md','17-annexes-documentaires.md'
];

// ---- Charte Planet Aura (issue des playbooks maquettés : teal logo, navy, accent orange)
const NAVY   = '1B3A4B';
const DARKBG = '12414A';
const TEAL   = '1B7F8C';
const TEALD  = '166E82';
const RED    = 'C0392B';
const GREEN  = '2E8B57';
const ORANGE = 'E87722';
const LIGHT  = 'E8F3F6';
const ZEBRA  = 'F4F7F8';
const GRAY   = '5A6B75';
const DARK   = '2B3A42';
const CONTENT_W = 9026;

const CHAPTER_ICONS = {
  'README.md':'ch-readme','00-resume-executif.md':'ch-00','01-entreprise.md':'ch-01',
  '02-marche.md':'ch-02','03-offres-services.md':'ch-03','04-tarifs.md':'ch-04',
  '05-cibles-personas.md':'ch-05','06-proposition-valeur.md':'ch-06','07-processus-vente.md':'ch-07',
  '08-prospection-scripts.md':'ch-08','09-objections.md':'ch-09','10-concurrence.md':'ch-10',
  '11-preuves-references.md':'ch-11','12-onboarding-retention.md':'ch-12','13-sav-sinistres.md':'ch-13',
  '14-conformite-reglementation.md':'ch-14','15-kpis-pilotage.md':'ch-15','16-annexes-outils.md':'ch-16','17-annexes-documentaires.md':'ch-17'
};

// Placements d'images : fichier md -> [{after: regex ligne de titre, img, w(px), caption}]
// (ajusté après la synthèse du workflow d'analyse)
const IMAGE_PLACEMENTS = require('./image-placements.js');

// Schémas "codés" : un bloc ``` dont le contenu matche `match` est remplacé par l'image
const DIAGRAMS = [
  { match: /Cibler.*Diagnostiquer/s, img: 'diagrams/d00_loop.png', w: 500 },
  { match: /LE POINT DE VENTE \(adhérent\)/, img: 'diagrams/d01_triangle.png', w: 520 },
  { match: /2019 ─+ 2023/, img: 'diagrams/d01_timeline.png', w: 520 },
  { match: /Flux prévisible.*sailing/s, img: 'diagrams/d03_vela.png', w: 500 },
  { match: /PICK-UP → FIRST MILES/, img: 'diagrams/d03_status.png', w: 480 },
  { match: /P1\s+\| Maison premium/, img: 'diagrams/d05_segments.png', w: 500 },
  { match: /Économie ──► Exécution/, img: 'diagrams/d05_comite.png', w: 500 },
  { match: /FLUX CLIENT & DÉCISION/, img: 'diagrams/d08_influence.png', w: 400 },
  { match: /Prospect ──► Adhérent/, img: 'diagrams/d05_cycle.png', w: 360 },
  { match: /PLANET AURA.*NOTRE CLIENT PRO/s, img: 'diagrams/d06_b2b2c.png', w: 520 },
  { match: /1\. LEAD → 2\. QUALIFIÉ/, img: 'diagrams/d07_pipeline.png', w: 520 },
  { match: /300 comptes ciblés/, img: 'diagrams/d07_funnel.png', w: 400 },
  { match: /GÉNÉRALISTE\s+SPÉCIALISTE VIN/, img: 'diagrams/d10_mapping.png', w: 500 },
  { match: /Signalement \(≤48 h/, img: 'diagrams/d13_sinistre.png', w: 520 },
  { match: /SOURCES\s+──►\s+HUBSPOT/, img: 'diagrams/d14_data.png', w: 440 },
  { match: /Leads → Qualifiés → RDV tenus/, img: 'diagrams/d15_funnel.png', w: 520 },
];

function img(name, wPx, hPx) {
  const p = path.join(A, name);
  const data = fs.readFileSync(p);
  return new ImageRun({ type: 'png', data, transformation: { width: wPx, height: hPx } });
}
function imgAuto(name, wPx) {
  const { PNG } = require('./png-size.js');
  const [w, h] = PNG(path.join(A, name));
  return img(name, wPx, Math.round(h * wPx / w));
}
function figure(name, wPx, caption) {
  const paras = [new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 120, after: caption ? 40 : 160 }, children: [imgAuto(name, wPx)] })];
  if (caption) paras.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 160 },
    children: [new TextRun({ text: caption, italics: true, size: 16, color: GRAY })]
  }));
  return paras;
}

// ---------- inline parsing ----------
// Emojis -> pictos premium (image inline)
const EMOJI_ICONS = {
  '🇺🇸': 'b-us', '🇨🇦': 'b-ca', '☀️': 'mini-sun', '☀': 'mini-sun', '🍾': 'mini-bottle',
  '📦': 'mini-package', '✈️': 'mini-plane', '✈': 'mini-plane', '☎️': 'mini-phone', '☎': 'mini-phone',
  '✅': 'b-ok', '⚠️': 'b-warn', '⚠': 'b-warn', '💡': 'b-tip', '🚫': 'b-no', '📌': 'b-pin',
  '🚨': 'b-warn', '❗': 'b-warn', '🕐': 'mini-clock',
};
const EMOJI_RE = new RegExp('(' + Object.keys(EMOJI_ICONS).sort((a, b) => b.length - a.length).map(e => e.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'g');

function pushText(runs, text, style) {
  let last = 0, m;
  EMOJI_RE.lastIndex = 0;
  while ((m = EMOJI_RE.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...style }));
    runs.push(img(`icons/${EMOJI_ICONS[m[1]]}.png`, 14, 14));
    last = m.index + m[1].length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...style }));
}

function inlineRuns(text, base = {}) {
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1').replace(/\\\*/g, '*');
  const runs = [];
  const re = /(\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) pushText(runs, text.slice(last, m.index), base);
    if (m[2] !== undefined) pushText(runs, m[2], { bold: true, ...base });
    else if (m[3] !== undefined) pushText(runs, m[3], { italics: true, ...base });
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], font: 'Consolas', size: 18, shading: { type: ShadingType.CLEAR, fill: 'EDF2F4' }, ...base }));
    last = m.index + m[0].length;
  }
  if (last < text.length) pushText(runs, text.slice(last), base);
  if (runs.length === 0) runs.push(new TextRun({ text: '', ...base }));
  return runs;
}

// ---------- tables ----------
function parseTableBlock(lines) {
  const rows = lines.map(l => l.replace(/^\s*\|/, '').replace(/\|\s*$/, '').split('|').map(c => c.trim()));
  const header = rows[0];
  const body = rows.slice(2);
  const nCols = header.length;
  const fontSize = nCols >= 8 ? 14 : nCols >= 5 ? 16 : 18;
  const MIN_W = nCols >= 8 ? 620 : 900;
  const maxLens = header.map((h, i) => Math.max(h.length, ...body.map(r => (r[i] || '').length), 4));
  // largeur mini par colonne : le mot le plus long ne doit pas être coupé
  const charW = Math.round(105 * fontSize / 18);
  const longestWord = (i) => Math.max(...[header[i], ...body.map(r => r[i] || '')].flatMap(c => (c || '').replace(/\*/g, '').split(/\s+/).map(w => w.length)), 3);
  const minCol = header.map((_, i) => Math.min(Math.max(MIN_W, longestWord(i) * charW + 220), 2600));
  const total = maxLens.reduce((a, b) => a + b, 0);
  let widths = maxLens.map(l => Math.round((l / total) * CONTENT_W));
  for (let pass = 0; pass < 8; pass++) {
    let deficit = 0;
    widths = widths.map((w, i) => { if (w < minCol[i]) { deficit += minCol[i] - w; return minCol[i]; } return w; });
    if (deficit === 0) break;
    const flexIdx = widths.map((w, i) => [w, i]).filter(([w, i]) => w > minCol[i]);
    const flexTotal = flexIdx.reduce((a, [w, i]) => a + (w - minCol[i]), 0);
    if (flexTotal <= 0) break;
    flexIdx.forEach(([w, i]) => { widths[i] = Math.max(minCol[i], Math.round(w - deficit * (w - minCol[i]) / flexTotal)); });
  }
  widths[0] = Math.max(widths[0], 0) + (CONTENT_W - widths.reduce((a, b) => a + b, 0));

  const mkRow = (cells, isHeader, rowIdx) => new TableRow({
    tableHeader: isHeader,
    children: Array.from({ length: nCols }, (_, i) => new TableCell({
      width: { size: widths[i], type: WidthType.DXA },
      verticalAlign: VerticalAlign.CENTER,
      shading: isHeader
        ? { type: ShadingType.CLEAR, fill: DARKBG }
        : (rowIdx % 2 === 1 ? { type: ShadingType.CLEAR, fill: ZEBRA } : undefined),
      margins: { top: 60, bottom: 60, left: 100, right: 100 },
      children: [new Paragraph({
        spacing: { before: 20, after: 20 },
        children: inlineRuns(cells[i] || '', isHeader ? { bold: true, color: 'FFFFFF', size: fontSize } : { size: fontSize })
      })]
    }))
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: 'C9DEE5' },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'C9DEE5' },
      left: { style: BorderStyle.SINGLE, size: 4, color: 'C9DEE5' },
      right: { style: BorderStyle.SINGLE, size: 4, color: 'C9DEE5' },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 4, color: 'D8E8ED' },
      insideVertical: { style: BorderStyle.SINGLE, size: 4, color: 'D8E8ED' },
    },
    rows: [mkRow(header, true, 0), ...body.map((r, k) => mkRow(r, false, k))]
  });
}

// ---------- fichier markdown -> blocs docx ----------
let orderedInstance = 1;

function convertFile(md, fileName) {
  const out = [new Paragraph({ children: [new PageBreak()] })];
  const placements = (IMAGE_PLACEMENTS[fileName] || []).slice();
  const iconName = CHAPTER_ICONS[fileName];
  let firstH1Done = false;
  const lines = md.split('\n');
  let i = 0;

  const tryPlace = (headingText) => {
    for (let k = 0; k < placements.length; k++) {
      if (new RegExp(placements[k].after, 'i').test(headingText)) {
        const p = placements.splice(k, 1)[0];
        return figure(p.img, p.w, p.caption);
      }
    }
    return [];
  };

  while (i < lines.length) {
    let line = lines[i];

    if (/^```/.test(line)) {
      i++;
      const code = [];
      while (i < lines.length && !/^```/.test(lines[i])) { code.push(lines[i]); i++; }
      i++;
      const blockText = code.join('\n');
      const diag = DIAGRAMS.find(d => d.match.test(blockText));
      if (diag) {
        out.push(...figure(diag.img, diag.w, diag.caption || ''));
        continue;
      }
      code.forEach(c => out.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, fill: 'F0F4F6' },
        spacing: { before: 0, after: 0 },
        children: [new TextRun({ text: c.length ? c : ' ', font: 'Consolas', size: 16, color: DARK })]
      })));
      out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
      continue;
    }

    if (/^\s*\|/.test(line) && i + 1 < lines.length && /^\s*\|[\s:|-]+\|?\s*$/.test(lines[i + 1])) {
      const tbl = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) { tbl.push(lines[i]); i++; }
      out.push(parseTableBlock(tbl));
      out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
      continue;
    }

    if (/^---+\s*$/.test(line)) {
      out.push(new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: TEAL } },
        spacing: { before: 120, after: 240 }, children: []
      }));
      i++; continue;
    }

    let m;
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      const lvl = m[1].length;
      const txt = m[2].replace(/\*\*/g, '');
      const H = [HeadingLevel.HEADING_1, HeadingLevel.HEADING_2, HeadingLevel.HEADING_3, HeadingLevel.HEADING_4][lvl - 1];
      const kids = [];
      if (lvl === 1 && iconName && !firstH1Done) {
        kids.push(img(`icons/${iconName}.png`, 30, 30));
        kids.push(new TextRun({ text: '  ' }));
        firstH1Done = true;
      }
      kids.push(...inlineRuns(txt, {
        bold: true,
        color: lvl === 1 ? NAVY : lvl === 2 ? TEALD : NAVY,
        size: lvl === 1 ? 34 : lvl === 2 ? 26 : lvl === 3 ? 23 : 21
      }));
      out.push(new Paragraph({
        heading: H,
        spacing: { before: lvl === 1 ? 240 : 200, after: 120 },
        border: lvl === 1 ? { bottom: { style: BorderStyle.SINGLE, size: 10, color: TEAL } } : undefined,
        children: kids
      }));
      out.push(...tryPlace(txt));
      i++; continue;
    }

    if (/^>\s?/.test(line)) {
      const quote = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { quote.push(lines[i].replace(/^>\s?/, '')); i++; }
      const head = quote[0] || '';
      // Système sémantique d'encadrés (charte Planet Aura) + badge picto premium
      let bar = TEAL, fill = 'E8F1F4', txtColor = DARK, labelColor = TEAL, badge = 'b-info';
      if (/^(🚫|❗)|\*\*(INTERDIT|ALERTE|DÉCISION IMMÉDIATE|NON-ÉLIGIBLE)/.test(head)) { bar = RED; fill = 'FDECEA'; labelColor = RED; badge = 'b-no'; }
      else if (/^💡|\*\*(LE CONSEIL|BONNE PRATIQUE)/.test(head)) { bar = ORANGE; fill = 'FDF0E4'; labelColor = ORANGE; badge = 'b-tip'; }
      else if (/^⚠️|\*\*(POINT DE VIGILANCE|À CONFIRMER|RÈGLE)/.test(head)) { bar = ORANGE; fill = 'FDF0E4'; labelColor = ORANGE; badge = 'b-warn'; }
      else if (/^✅|\*\*CE QUI FONCTIONNE/.test(head)) { bar = GREEN; fill = 'E8F3EC'; labelColor = GREEN; badge = 'b-ok'; }
      else if (/^📌|\*\*À RETENIR/.test(head)) { bar = ORANGE; fill = DARKBG; txtColor = 'FFFFFF'; labelColor = 'FFFFFF'; badge = 'b-pin'; }
      quote.forEach((q, qi) => {
        if (q.trim() === '') { out.push(new Paragraph({ spacing: { after: 60 }, children: [] })); return; }
        // colore le label en tête ("**LABEL —** reste"), emoji remplacé par le badge picto
        let kids;
        const lm = qi === 0 ? q.match(/^([⚠️💡🚫❗✅📌🚨]*\s*)\*\*([^*]+?)(\s*[—:-])?\*\*\s*(.*)$/) : null;
        if (lm) {
          kids = [
            img(`icons/${badge}.png`, 16, 16),
            new TextRun({ text: '  ' + lm[2].toUpperCase() + (lm[3] ? ' —' : ''), bold: true, size: 18, color: labelColor }),
            new TextRun({ text: '  ' }),
            ...inlineRuns(lm[4] || '', { size: 20, color: txtColor })
          ];
        } else {
          kids = inlineRuns(q, { size: 20, color: txtColor });
        }
        out.push(new Paragraph({
          indent: { left: 360 },
          border: { left: { style: BorderStyle.SINGLE, size: 18, color: bar } },
          shading: { type: ShadingType.CLEAR, fill },
          spacing: { before: 40, after: 40 },
          children: kids
        }));
      });
      out.push(new Paragraph({ spacing: { after: 100 }, children: [] }));
      continue;
    }

    if ((m = line.match(/^(\s*)-\s+\[( |x)\]\s+(.*)$/))) {
      out.push(new Paragraph({
        indent: { left: 360, hanging: 240 },
        spacing: { after: 40 },
        children: [new TextRun({ text: m[2] === 'x' ? '☑ ' : '☐ ', size: 20, color: TEALD }), ...inlineRuns(m[3], { size: 20 })]
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)[-•]\s+(.*)$/))) {
      const level = Math.min(Math.floor(m[1].length / 2), 2);
      out.push(new Paragraph({
        numbering: { reference: 'bullets', level },
        spacing: { after: 40 },
        children: inlineRuns(m[2], { size: 20 })
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)(\d+)[.)]\s+(.*)$/))) {
      const startNew = !(i > 0 && /^\s*\d+[.)]\s/.test(lines[i - 1]));
      if (startNew) orderedInstance++;
      out.push(new Paragraph({
        numbering: { reference: 'ordered', level: 0, instance: orderedInstance },
        spacing: { after: 40 },
        children: inlineRuns(m[3], { size: 20 })
      }));
      i++; continue;
    }

    if (line.trim() === '') { i++; continue; }

    out.push(new Paragraph({ spacing: { after: 120 }, children: inlineRuns(line, { size: 20 }) }));
    i++;
  }
  return out;
}

// ---------- page de titre ----------
const titlePage = [
  new Paragraph({ spacing: { before: 900 }, children: [] }),
  new Paragraph({ alignment: AlignmentType.CENTER, children: [img('pics/logo.png', 190, 190)] }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 260 },
    children: [new TextRun({ text: 'COMMISSIONNAIRE DE TRANSPORT  ·  CHAMPAGNE, VINS & SPIRITUEUX', bold: true, size: 17, color: TEALD, font: 'Calibri' })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 320 },
    children: [new TextRun({ text: 'Sales', bold: true, size: 88, color: NAVY, font: 'Georgia' })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 60 },
    children: [new TextRun({ text: 'Playbook', bold: true, size: 76, color: TEAL, font: 'Georgia' })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 220 },
    children: [new TextRun({ text: 'Le guide de référence du commercial Planet Aura', italics: true, size: 26, color: DARK, font: 'Georgia' })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 200, after: 200 },
    children: [new TextRun({ text: '━━━━━━', size: 24, color: ORANGE })]
  }),
  new Paragraph({
    indent: { left: 700, right: 700 },
    alignment: AlignmentType.CENTER,
    shading: { type: ShadingType.CLEAR, fill: LIGHT },
    border: { left: { style: BorderStyle.SINGLE, size: 14, color: ORANGE } },
    spacing: { after: 60 },
    children: [
      new TextRun({ text: 'PROMESSE DE MARQUE  ', bold: true, size: 16, color: ORANGE }),
      new TextRun({ text: 'Vous permettre de vous concentrer sur votre savoir-faire : Planet Aura orchestre l’expédition, la douane, le suivi et la résolution des aléas.', size: 18, color: DARK })
    ]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 320 },
    children: [new TextRun({ text: 'ÉDITION 2026   ·   RÉSERVÉ À L’ÉQUIPE COMMERCIALE PLANET AURA   ·   CONFIDENTIEL', bold: true, size: 20, color: NAVY })]
  }),
  new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { before: 80 },
    children: [new TextRun({ text: 'SARL Planet Aura — 5 Impasse François Arago, 81100 Castres — www.planet-aura.com', size: 17, color: GRAY })]
  }),
  new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 260 }, children: [imgAuto('pics/photo_cover.png', 205)] }),
];

// ---------- pages d'ouverture de partie ----------
const PARTS = {
  '00-resume-executif.md': { num: 'PARTIE 1', title: 'Comprendre', chapters: ['00 · Résumé exécutif', '01 · L’entreprise Planet Aura', '02 · Le marché', '03 · Offre & services', '04 · Tarification 2026'] },
  '05-cibles-personas.md': { num: 'PARTIE 2', title: 'Vendre', chapters: ['05 · Cibles & personas', '06 · Proposition de valeur', '07 · Processus de vente', '08 · Prospection', '09 · Objections', '10 · Concurrence', '11 · Preuves & références'] },
  '12-onboarding-retention.md': { num: 'PARTIE 3', title: 'Fidéliser & opérer', chapters: ['12 · Onboarding & fidélisation', '13 · SAV & sinistres', '14 · Conformité & réglementation'] },
  '15-kpis-pilotage.md': { num: 'PARTIE 4', title: 'Piloter', chapters: ['15 · KPIs & pilotage', '16 · Annexes & boîte à outils', '17 · Annexes documentaires & sources'] },
};

function partOpener(p) {
  return [
    new Paragraph({ children: [new PageBreak()] }),
    new Paragraph({ spacing: { before: 2600 }, children: [] }),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: p.num.split('').join(' '), bold: true, size: 24, color: TEAL })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 160 },
      children: [new TextRun({ text: p.title, bold: true, size: 64, color: NAVY, font: 'Georgia' })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 160, after: 300 },
      children: [new TextRun({ text: '━━━━━━', size: 24, color: ORANGE })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 120 },
      children: [new TextRun({ text: 'DANS CETTE PARTIE', bold: true, size: 17, color: GRAY })]
    }),
    ...p.chapters.map(c => new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { after: 60 },
      children: [new TextRun({ text: c, size: 21, color: DARK })]
    })),
  ];
}

// ---------- build ----------
let children = [...titlePage];
FILES.forEach(f => {
  if (PARTS[f]) children = children.concat(partOpener(PARTS[f]));
  const md = fs.readFileSync(path.join(SRC, f), 'utf8');
  children = children.concat(convertFile(md, f));
});

const footerP = new Footer({
  children: [new Paragraph({
    tabStops: [{ type: 'right', position: CONTENT_W }],
    border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'C9DEE5' } },
    spacing: { before: 60 },
    children: [
      new TextRun({ text: 'PLANET AURA · COMMISSIONNAIRE DE TRANSPORT VINS & SPIRITUEUX', size: 14, color: GRAY }),
      new TextRun({ text: '\t', size: 14 }),
      new TextRun({ text: 'PAGE ', size: 14, color: ORANGE, bold: true }),
      new TextRun({ children: [PageNumber.CURRENT], size: 14, color: ORANGE, bold: true }),
    ]
  })]
});

const { Header } = require('docx');
const headerP = new Header({
  children: [new Paragraph({
    tabStops: [{ type: 'right', position: CONTENT_W }],
    spacing: { after: 40 },
    children: [
      new TextRun({ text: 'P L A N E T   A U R A  ·  WINE DELIVERY WORLDWIDE', size: 13, color: GRAY }),
      new TextRun({ text: '\t', size: 13 }),
      new TextRun({ text: 'SALES PLAYBOOK 2026  |  INTERNE', size: 13, color: GRAY }),
    ]
  })]
});

const doc = new Document({
  styles: { default: { document: { run: { font: 'Calibri', size: 20, color: DARK } } } },
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [0, 1, 2].map(l => ({
          level: l, format: LevelFormat.BULLET, text: ['•', '◦', '▪'][l],
          style: { paragraph: { indent: { left: 360 + l * 360, hanging: 240 } } },
        }))
      },
      {
        reference: 'ordered',
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: '%1.',
          style: { paragraph: { indent: { left: 400, hanging: 280 } } }
        }]
      }
    ]
  },
  sections: [{
    properties: {
      page: { margin: { top: 1240, bottom: 1240, left: 1440, right: 1440 } },
      titlePage: true,
    },
    headers: { default: headerP, first: new Header({ children: [new Paragraph({ children: [] })] }) },
    footers: { default: footerP, first: new Footer({ children: [new Paragraph({ children: [] })] }) },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(path.join(__dirname, 'Planet_Aura_Sales_Playbook_2026.docx'), buf);
  console.log('OK', buf.length, 'bytes');
});
