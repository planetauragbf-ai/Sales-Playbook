// Sales Playbook Planet Aura - édition finale 2026 (v2.1)
// Générateur au design de la maquette v2.0 d'Emma : A4, serif éditorial, stat-blocs,
// encadrés à fond plat, exergues, ouvertures de partie en chiffres romains.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, WidthType, ShadingType, BorderStyle,
  LevelFormat, PageBreak, Footer, Header, PageNumber, VerticalAlign,
  Bookmark, InternalHyperlink, TabStopType, LeaderType
} = require('docx');

const SRC = path.join(__dirname, 'content-emma');
const A = require('path').join(__dirname, '..', 'build', 'assets');

// ---- Charte (maquette v2.0)
const NAVY = '1B3A4B';
const TEAL = '1B7F8C';
const TEALD = '16606E';
const ORANGE = 'E87722';
const RED = 'C0392B';
const GREEN = '2E8B57';
const CREAM = 'FDF0E4';
const LTEAL = 'EAF3F6';
const LGREEN = 'EDF6F0';
const LRED = 'FAEDEB';
const ZEBRA = 'F4F8F9';
const GRAY = '5A6B75';
const INK = '2B3A42';
const DARKBG = '12414A';

// A4
const PAGE = { width: 11906, height: 16838 };
const MARGIN = { top: 1080, bottom: 1020, left: 1250, right: 1250 };
const CONTENT_W = PAGE.width - MARGIN.left - MARGIN.right; // 9406

const UNITS = [
  { id: 'avant', file: 'avant.md', head: 'AVANT DE COMMENCER' },
  { id: '00', file: '00.md', head: 'OUVERTURE' },
  { id: '01', file: '01.md' }, { id: '02', file: '02.md' }, { id: '03', file: '03.md' },
  { id: '04', file: '04.md' }, { id: '05', file: '05.md' },
  { id: '06', file: '06.md' }, { id: '07', file: '07.md' }, { id: '08', file: '08.md' },
  { id: '09', file: '09.md' }, { id: '10', file: '10.md' }, { id: '11', file: '11.md' },
  { id: '12', file: '12.md' }, { id: '13', file: '13.md' },
  { id: '14', file: '14.md' }, { id: '15', file: '15.md' }, { id: '16', file: '16.md' },
  { id: '17', file: '17.md' }, { id: '18', file: '18.md' },
  { id: 'A', file: 'A.md' }, { id: 'B', file: 'B.md' }, { id: 'C', file: 'C.md' },
  { id: 'D', file: 'D.md' }, { id: 'E', file: 'E.md' }, { id: 'F', file: 'F.md' }, { id: 'G', file: 'G.md' },
];

const PARTS = {
  '01': { rom: 'I', num: 'PARTIE 1', title: 'Analyser l’entreprise et son offre', sub: 'Comprendre avant de convaincre', chapters: ['01 · Contexte et enjeux commerciaux', '02 · Diagnostic de l’entreprise', '03 · Organisation et interlocuteurs', '04 · Offres et politique tarifaire', '05 · Concurrence et différenciation'] },
  '06': { rom: 'II', num: 'PARTIE 2', title: 'Définir les cibles et les solutions adaptées', sub: 'Les bons comptes, les bonnes réponses', chapters: ['06 · Profils de clients idéaux (ICP)', '07 · Personas et acteurs de la décision', '08 · Correspondance entre enjeux et solutions'] },
  '09': { rom: 'III', num: 'PARTIE 3', title: 'Formaliser la prospection et la vente', sub: 'Du premier contact à la signature', chapters: ['09 · Processus d’acquisition et pipeline', '10 · Séquences de prospection et scripts', '11 · Qualification et processus de vente', '12 · Conduite des entretiens (méthode SPIN)', '13 · Argumentaires et objections'] },
  '14': { rom: 'IV', num: 'PARTIE 4', title: 'Fournir les outils et organiser le pilotage', sub: 'Outiller, mesurer, faire vivre', chapters: ['14 · Ressources d’aide à la vente', '15 · Organisation et outils', '16 · Activation, fidélisation et SAV', '17 · Indicateurs et méthode de suivi', '18 · Mise à jour et appropriation'] },
  'A': { rom: 'V', num: 'ANNEXES', title: 'Annexes', sub: 'Documents complémentaires', chapters: ['A · Grilles tarifaires officielles 2026', 'B · CGS : l’essentiel', 'C · Fiche réflexe, checklists et modèles', 'D · Conformité et fiches pays', 'E · Glossaire', 'F · Chiffres officiels et sources', 'G · Documents officiels'] },
};

// ---- Sommaire interactif
const tocRegistry = [];
const plainHeading = (t) => t.replace(/\*\*/g, '').replace(/[⚠️💡🚫❗✅📌🚨🇺🇸🇨🇦☀️🍾📦✈️☎️]/g, '').trim();

let IMAGE_PLACEMENTS = {};
try { IMAGE_PLACEMENTS = require('./image-placements-emma.js'); } catch (e) {}

const DIAGRAMS = [
  { match: /Signalement \(≤48 h/, img: 'diagrams/d13_sinistre.png', w: 500 },
  { match: /LE CLIENT CHOISIT : RXP ou remboursement/, img: 'diagrams/d13_arbre.png', w: 500 },
  { match: /Le client demande un prix → On récupère/, img: 'diagrams/d07_cotation.png', w: 500 },
  { match: /1\. LEAD → 2\. QUALIFIÉ/, img: 'diagrams/d07_pipeline.png', w: 500 },
  { match: /Leads → Qualifiés → RDV tenus/, img: 'diagrams/d15_funnel.png', w: 500 },
  { match: /Prospect ──► Adhérent/, img: 'diagrams/d05_cycle.png', w: 360 },
];

function img(name, wPx, hPx) {
  const data = fs.readFileSync(path.join(A, name));
  return new ImageRun({ type: 'png', data, transformation: { width: wPx, height: hPx } });
}
function imgAuto(name, wPx) {
  const { PNG } = require('./png-size.js');
  const [w, h] = PNG(path.join(A, name));
  return img(name, wPx, Math.round(h * wPx / w));
}
function figure(name, wPx, caption) {
  const paras = [new Paragraph({ alignment: AlignmentType.CENTER, keepNext: !!caption, spacing: { before: 80, after: caption ? 34 : 110 }, children: [imgAuto(name, wPx)] })];
  if (caption) paras.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 110 },
    children: [new TextRun({ text: caption, italics: true, size: 15, color: GRAY, font: 'Georgia' })]
  }));
  return paras;
}

// ---------- inline ----------
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
    runs.push(img(`icons/${EMOJI_ICONS[m[1]]}.png`, 13, 13));
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
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], font: 'Consolas', size: 17, shading: { type: ShadingType.CLEAR, fill: 'EDF2F4' }, ...base }));
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
  const fontSize = nCols >= 8 ? 13 : nCols >= 5 ? 15 : 17;
  const MIN_W = nCols >= 8 ? 620 : 900;
  const maxLens = header.map((h, i) => Math.max(h.length, ...body.map(r => (r[i] || '').length), 4));
  const charW = Math.round(105 * fontSize / 18);
  const longestWord = (i) => Math.max(...[header[i], ...body.map(r => r[i] || '')].flatMap(c => (c || '').replace(/\*/g, '').split(/\s+/).map(w => w.length)), 3);
  const longestHeadWord = (i) => Math.max(...(header[i] || '').replace(/\*/g, '').split(/\s+/).map(w => w.length), 3);
  const minCol = header.map((_, i) => Math.min(Math.max(MIN_W, longestWord(i) * charW + 220, longestHeadWord(i) * Math.round(charW * 1.3) + 220), 2700));
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
        ? { type: ShadingType.CLEAR, fill: TEALD }
        : (rowIdx % 2 === 1 ? { type: ShadingType.CLEAR, fill: ZEBRA } : undefined),
      margins: { top: 34, bottom: 34, left: 90, right: 90 },
      children: [new Paragraph({
        spacing: { before: 10, after: 10 },
        children: inlineRuns(cells[i] || '', isHeader ? { bold: true, color: 'FFFFFF', size: fontSize } : { size: fontSize })
      })]
    }))
  });

  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 4, color: 'CCDDE3' },
      bottom: { style: BorderStyle.SINGLE, size: 4, color: 'CCDDE3' },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' },
      insideVertical: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' },
    },
    rows: [mkRow(header, true, 0), ...body.map((r, k) => mkRow(r, false, k))]
  });
}

// ---------- stat-blocs ----------
const STAT_COLORS = [TEAL, ORANGE, NAVY, TEAL, ORANGE];
function statBlock(lines) {
  const items = lines.filter(l => l.trim()).map(l => {
    const ix = l.indexOf('|');
    return ix >= 0 ? [l.slice(0, ix).trim(), l.slice(ix + 1).trim()] : [l.trim(), ''];
  });
  const n = items.length;
  const w = Math.floor(CONTENT_W / n);
  const widths = Array.from({ length: n }, (_, i) => i === n - 1 ? CONTENT_W - w * (n - 1) : w);
  return new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: widths,
    borders: {
      top: { style: BorderStyle.SINGLE, size: 6, color: 'DCE8EC' },
      bottom: { style: BorderStyle.SINGLE, size: 6, color: 'DCE8EC' },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE },
      insideVertical: { style: BorderStyle.SINGLE, size: 4, color: 'E2ECEF' },
    },
    rows: [new TableRow({
      children: items.map(([v, c], i) => new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 78, bottom: 78, left: 60, right: 60 },
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER, spacing: { after: 40 },
            children: [new TextRun({ text: v, bold: true, size: n >= 5 ? 32 : 40, color: STAT_COLORS[i % STAT_COLORS.length], font: 'Georgia' })]
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: inlineRuns(c, { size: 15, color: GRAY })
          }),
        ]
      }))
    })]
  });
}

// ---------- conversion md -> blocs ----------
let orderedInstance = 1;

function convertBody(md, unit, opts = {}) {
  const out = [];
  const placements = (IMAGE_PLACEMENTS[unit.id] || []).slice();
  const lines = md.split('\n');
  let i = 0;
  let h1Seen = false;

  const tryPlace = (headingText) => {
    const out2 = [];
    for (let k = 0; k < placements.length; ) {
      if (new RegExp(placements[k].after, 'i').test(headingText)) {
        const p = placements.splice(k, 1)[0];
        out2.push(...figure(p.img, p.w, p.caption));
      } else k++;
    }
    return out2;
  };

  while (i < lines.length) {
    let line = lines[i];

    if (/^```/.test(line)) {
      const isStats = /^```\s*stats/.test(line);
      i++;
      const code = [];
      while (i < lines.length && !/^```/.test(lines[i])) { code.push(lines[i]); i++; }
      i++;
      if (isStats) {
        out.push(statBlock(code));
        out.push(new Paragraph({ spacing: { after: 84 }, children: [] }));
        continue;
      }
      const blockText = code.join('\n');
      const diag = DIAGRAMS.find(d => d.match.test(blockText));
      if (diag) { out.push(...figure(diag.img, diag.w, '')); continue; }
      code.forEach(c => out.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, fill: 'F0F4F6' },
        spacing: { before: 0, after: 0 },
        children: [new TextRun({ text: c.length ? c : ' ', font: 'Consolas', size: 15, color: INK })]
      })));
      out.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
      continue;
    }

    if (/^\s*\|/.test(line) && i + 1 < lines.length && /^\s*\|[\s:|-]+\|?\s*$/.test(lines[i + 1])) {
      const tbl = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) { tbl.push(lines[i]); i++; }
      out.push(parseTableBlock(tbl));
      out.push(new Paragraph({ spacing: { after: 84 }, children: [] }));
      continue;
    }

    if (/^---+\s*$/.test(line)) {
      out.push(new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 5, color: 'CCDDE3' } },
        spacing: { before: 100, after: 220 }, children: []
      }));
      i++; continue;
    }

    let m;
    if ((m = line.match(/^(#{1,4})\s+(.*)$/))) {
      const lvl = m[1].length;
      const txt = m[2].replace(/\*\*/g, '');

      if (lvl === 1) {
        // Tête de chapitre : kicker partie, numéro · titre serif, sous-titre, filet, mini-sommaire
        h1Seen = true;
        const hm = txt.match(/^(Annexe\s+)?([0-9A-G]{1,2})\s*[—–-]\s*(.*)$/) || [null, '', '', txt];
        const isAnnex = !!hm[1];
        const num = hm[2]; const title = hm[3] || txt;
        const part = PARTS[unit.id];
        const kicker = part ? `${part.num}  ·  ${part.title.toUpperCase()}` : (unit.head || (isAnnex ? 'ANNEXES · DOCUMENTS COMPLÉMENTAIRES' : PART_OF_UNIT[unit.id] ? `${PART_OF_UNIT[unit.id].num}  ·  ${PART_OF_UNIT[unit.id].title.toUpperCase()}` : 'SALES PLAYBOOK 2026'));
        out.push(new Paragraph({
          spacing: { before: 60, after: 120 },
          children: [new TextRun({ text: kicker, bold: true, size: 14, color: TEAL })]
        }));
        let key = null;
        if (!opts.noToc) {
          key = `toc${tocRegistry.length}`;
          tocRegistry.push({ key, level: 1, text: plainHeading(txt), id: unit.id });
        }
        const titleRuns = [];
        if (num) titleRuns.push(new TextRun({ text: (isAnnex ? 'Annexe ' : '') + num + '  ·  ', bold: true, size: 44, color: ORANGE, font: 'Georgia' }));
        titleRuns.push(new TextRun({ text: title, bold: true, size: 44, color: NAVY, font: 'Georgia' }));
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_1,
          spacing: { after: 70 },
          children: key ? [new Bookmark({ id: key, children: titleRuns })] : titleRuns
        }));
        // sous-titre italique (ligne suivante '*...*')
        let j = i + 1;
        while (j < lines.length && lines[j].trim() === '') j++;
        if (j < lines.length && /^\*[^*].*\*$/.test(lines[j].trim())) {
          out.push(new Paragraph({
            spacing: { after: 110 },
            children: [new TextRun({ text: lines[j].trim().replace(/^\*|\*$/g, ''), italics: true, size: 21, color: GRAY, font: 'Georgia' })]
          }));
          i = j;
        }
        out.push(new Paragraph({
          border: { bottom: { style: BorderStyle.SINGLE, size: 11, color: TEAL } },
          spacing: { after: 126 }, children: []
        }));
        // mini-sommaire du chapitre (H2, sans numéros de page)
        if (!opts.noMiniToc) {
          const h2s = lines.slice(i + 1).filter(l => /^##\s/.test(l)).map(l => plainHeading(l.replace(/^##\s+/, '')));
          if (h2s.length >= 3) {
            out.push(new Paragraph({
              spacing: { after: 40 },
              children: [new TextRun({ text: 'DANS CE CHAPITRE', bold: true, size: 13, color: GRAY })]
            }));
            out.push(new Paragraph({
              spacing: { after: 156 },
              children: h2s.flatMap((h, k) => [
                ...(k ? [new TextRun({ text: '   ·   ', size: 16, color: ORANGE })] : []),
                new TextRun({ text: h, size: 16, color: TEALD })
              ])
            }));
          }
        }
        out.push(...tryPlace(txt));
        i++; continue;
      }

      if (lvl === 2) {
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_2,
          spacing: { before: 198, after: 56 },
          children: inlineRuns(txt, { bold: true, size: 27, color: NAVY, font: 'Georgia' })
        }));
      } else if (lvl === 3) {
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_3,
          spacing: { before: 148, after: 44 },
          children: inlineRuns(txt.toUpperCase(), { bold: true, size: 17, color: TEALD })
        }));
      } else {
        out.push(new Paragraph({
          spacing: { before: 130, after: 48 },
          children: inlineRuns(txt, { bold: true, size: 19, color: NAVY })
        }));
      }
      out.push(...tryPlace(txt));
      i++; continue;
    }

    if (/^>\s?/.test(line)) {
      const quote = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { quote.push(lines[i].replace(/^>\s?/, '')); i++; }
      const head = quote[0] || '';

      // Exergue : citation seule « ... »
      if (quote.length === 1 && /^«/.test(head.trim()) && !/\*\*/.test(head)) {
        out.push(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: 128, after: 128 },
          indent: { left: 500, right: 500 },
          children: [new TextRun({ text: head.trim(), italics: true, size: 25, color: TEAL, font: 'Georgia' })]
        }));
        continue;
      }

      // Encadrés à fond plat (maquette) : pas de bordure, étiquette colorée
      let fill = LTEAL, txtColor = INK, labelColor = TEALD, badge = 'b-info';
      if (/^(🚫|❗)|\*\*(INTERDIT|ALERTE|NON-ÉLIGIBLE)/.test(head)) { fill = LRED; labelColor = RED; badge = 'b-no'; }
      else if (/^💡|\*\*(LE CONSEIL|BONNE PRATIQUE)/.test(head)) { fill = CREAM; labelColor = ORANGE; badge = 'b-tip'; }
      else if (/^⚠️|\*\*(LE POINT DE VIGILANCE|POINT DE VIGILANCE|À CONFIRMER|RÈGLE)/.test(head)) { fill = CREAM; labelColor = ORANGE; badge = 'b-warn'; }
      else if (/^✅|\*\*CE QUI FONCTIONNE/.test(head)) { fill = LGREEN; labelColor = GREEN; badge = 'b-ok'; }
      else if (/^📌|\*\*À RETENIR/.test(head)) { fill = DARKBG; txtColor = 'FFFFFF'; labelColor = 'F4C9A8'; badge = 'b-pin'; }
      const calloutParas = [];
      quote.forEach((q, qi) => {
        if (q.trim() === '') { calloutParas.push(new Paragraph({ spacing: { after: 50 }, children: [] })); return; }
        let kids;
        const lm = qi === 0 ? q.match(/^([⚠️💡🚫❗✅📌🚨]*\s*)\*\*([^*]+?)(\s*[—:-])?\*\*\s*(.*)$/) : null;
        if (lm) {
          kids = [
            img(`icons/${badge}.png`, 15, 15),
            new TextRun({ text: '  ' + lm[2].toUpperCase().replace(/^LE POINT/, 'LE POINT') + (lm[3] ? ' —' : ''), bold: true, size: 16, color: labelColor }),
            new TextRun({ text: '  ' }),
            ...inlineRuns(lm[4] || '', { size: 17, color: txtColor })
          ];
        } else {
          kids = inlineRuns(q, { size: 17, color: txtColor });
        }
        calloutParas.push(new Paragraph({ spacing: { before: 18, after: 18 }, children: kids }));
      });
      out.push(new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [CONTENT_W],
        borders: {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
          insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
        },
        rows: [new TableRow({ children: [new TableCell({
          width: { size: CONTENT_W, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill },
          margins: { top: 68, bottom: 68, left: 200, right: 185 },
          children: calloutParas
        })] })]
      }));
      out.push(new Paragraph({ spacing: { after: 80 }, children: [] }));
      continue;
    }

    if ((m = line.match(/^(\s*)-\s+\[( |x)\]\s+(.*)$/))) {
      out.push(new Paragraph({
        indent: { left: 360, hanging: 240 },
        spacing: { after: 20 },
        children: [new TextRun({ text: m[2] === 'x' ? '☑ ' : '☐ ', size: 19, color: TEALD }), ...inlineRuns(m[3], { size: 17 })]
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)[-•]\s+(.*)$/))) {
      const level = Math.min(Math.floor(m[1].length / 2), 2);
      out.push(new Paragraph({
        numbering: { reference: 'bullets', level },
        spacing: { after: 20 },
        children: inlineRuns(m[2], { size: 17 })
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)(\d+)[.)]\s+(.*)$/))) {
      const startNew = !(i > 0 && /^\s*\d+[.)]\s/.test(lines[i - 1]));
      if (startNew) orderedInstance++;
      out.push(new Paragraph({
        numbering: { reference: 'ordered', level: 0, instance: orderedInstance },
        spacing: { after: 20 },
        children: inlineRuns(m[3], { size: 17 })
      }));
      i++; continue;
    }

    if (line.trim() === '') { i++; continue; }
    // sous-titre déjà consommé après H1
    if (h1Seen === 'skipnext') { h1Seen = true; i++; continue; }

    out.push(new Paragraph({ spacing: { after: 66 }, children: inlineRuns(line, { size: 17 }) }));
    i++;
  }
  return out;
}

// partie de rattachement de chaque unité (pour le kicker)
const PART_OF_UNIT = {};
{
  let cur = null;
  UNITS.forEach(u => { if (PARTS[u.id]) cur = PARTS[u.id]; PART_OF_UNIT[u.id] = cur; });
}

// ---------- ouverture de partie ----------
function partOpener(p) {
  return [
    new Paragraph({ spacing: { before: 2600 }, children: [] }),
    new Paragraph({
      spacing: { after: 140 },
      children: [new TextRun({ text: p.num.split('').join(' '), bold: true, size: 21, color: ORANGE })]
    }),
    new Paragraph({
      spacing: { after: 60 },
      children: [new TextRun({ text: p.rom + '.', bold: true, size: 150, color: NAVY, font: 'Georgia' })]
    }),
    new Paragraph({
      spacing: { after: 90 },
      children: [new TextRun({ text: p.title, bold: true, size: 52, color: NAVY, font: 'Georgia' })]
    }),
    new Paragraph({
      spacing: { after: 420 },
      children: [new TextRun({ text: p.sub, italics: true, size: 24, color: ORANGE, font: 'Georgia' })]
    }),
    new Paragraph({
      border: { top: { style: BorderStyle.SINGLE, size: 8, color: 'CCDDE3' } },
      spacing: { before: 60, after: 160 },
      children: [new TextRun({ text: 'DANS CETTE PARTIE', bold: true, size: 14, color: GRAY })]
    }),
    ...p.chapters.map(c => {
      const m = c.match(/^([0-9A-G]{1,2})\s*·\s*(.*)$/);
      return new Paragraph({
        spacing: { after: 80 },
        children: m ? [
          new TextRun({ text: m[1], bold: true, size: 22, color: ORANGE, font: 'Georgia' }),
          new TextRun({ text: '   ' + m[2], size: 22, color: INK }),
        ] : [new TextRun({ text: c, size: 22, color: INK })]
      });
    }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

// ---------- couverture ----------
function coverChildren() {
  return [
    new Paragraph({ spacing: { before: 700 }, children: [] }),
    new Paragraph({ alignment: AlignmentType.CENTER, children: [img('pics/logo.png', 150, 150)] }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 420 },
      children: [new TextRun({ text: 'Sales', bold: true, size: 104, color: NAVY, font: 'Georgia' })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 40 },
      children: [new TextRun({ text: 'Playbook', bold: true, size: 104, color: TEAL, font: 'Georgia' })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 260 },
      children: [new TextRun({ text: 'Le guide de référence du commercial Planet Aura', size: 26, color: INK, font: 'Georgia' })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 170 },
      children: [new TextRun({ text: 'Faire voyager chaque colis dans les règles, intact, à temps, partout dans le monde.', italics: true, size: 21, color: GRAY, font: 'Georgia' })]
    }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 380 }, children: [imgAuto('pics/photo_cover.png', 215)] }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 420 },
      children: [new TextRun({ text: 'COMMISSIONNAIRE DE TRANSPORT  ·  CHAMPAGNES, VINS & SPIRITUEUX', bold: true, size: 17, color: TEALD })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 150 },
      children: [new TextRun({ text: 'VERSION 2.1 · OCTOBRE 2026  ·  RÉSERVÉ À L’ÉQUIPE COMMERCIALE & MARKETING  ·  CONFIDENTIEL', bold: true, size: 16, color: NAVY })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 90 },
      children: [new TextRun({ text: 'SARL Planet Aura — 5 Impasse François Arago, 81100 Castres — www.planet-aura.com', size: 15, color: GRAY })]
    }),
  ];
}

// ---------- sommaire ----------
let tocPages = {};
try { tocPages = JSON.parse(fs.readFileSync(path.join(__dirname, 'toc-pages-emma.json'), 'utf8')); } catch (e) {}

function tocChildren() {
  const paras = [];
  paras.push(new Paragraph({
    spacing: { before: 140, after: 20 },
    children: [new TextRun({ text: 'NAVIGATION', bold: true, size: 14, color: TEAL })]
  }));
  paras.push(new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: 'Sommaire', bold: true, size: 48, color: NAVY, font: 'Georgia' })]
  }));
  paras.push(new Paragraph({
    border: { bottom: { style: BorderStyle.SINGLE, size: 11, color: TEAL } },
    spacing: { after: 90 }, children: []
  }));
  paras.push(new Paragraph({
    spacing: { after: 200 },
    children: [new TextRun({ text: 'Consultation par besoin ou par étape du cycle commercial — chaque entrée est cliquable. Les annexes regroupent les outils réutilisables séparément.', italics: true, size: 17, color: GRAY, font: 'Georgia' })]
  }));
  let lastPart = null;
  tocRegistry.forEach(h => {
    const part = PART_OF_UNIT[h.id];
    if (part && part !== lastPart) {
      lastPart = part;
      paras.push(new Paragraph({
        shading: { type: ShadingType.CLEAR, fill: LTEAL },
        spacing: { before: 190, after: 70 },
        children: [
          new TextRun({ text: `  ${part.rom}.  `, bold: true, size: 21, color: ORANGE, font: 'Georgia' }),
          new TextRun({ text: part.title.toUpperCase(), bold: true, size: 17, color: TEALD }),
        ]
      }));
    }
    const page = tocPages[h.key] !== undefined ? String(tocPages[h.key]) : '0';
    paras.push(new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W, leader: LeaderType.DOT }],
      spacing: { before: 60, after: 20 },
      children: [
        new InternalHyperlink({
          anchor: h.key,
          children: [new TextRun({ text: h.text, bold: true, size: 19, color: NAVY })]
        }),
        new TextRun({ text: '\t', size: 19 }),
        new TextRun({ text: page, bold: true, size: 18, color: ORANGE }),
      ]
    }));
  });
  return paras;
}

// ---------- en-têtes / pieds ----------
function mkHeader(leftText) {
  return new Header({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' } },
      spacing: { after: 40 },
      children: [
        new TextRun({ text: leftText, bold: true, size: 12, color: TEALD }),
        new TextRun({ text: '\t', size: 12 }),
        new TextRun({ text: 'SALES PLAYBOOK 2026 · INTERNE', size: 12, color: GRAY }),
      ]
    })]
  });
}
const footerP = new Footer({
  children: [new Paragraph({
    tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
    border: { top: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' } },
    spacing: { before: 50 },
    children: [
      new TextRun({ text: 'PLANET AURA · COMMISSIONNAIRE DE TRANSPORT VINS, CHAMPAGNES & SPIRITUEUX', size: 12, color: GRAY }),
      new TextRun({ text: '\t', size: 12 }),
      new TextRun({ children: [PageNumber.CURRENT], bold: true, size: 15, color: NAVY }),
    ]
  })]
});
const emptyHF = { headers: { default: new Header({ children: [new Paragraph({ children: [] })] }) }, footers: { default: new Footer({ children: [new Paragraph({ children: [] })] }) } };

// ---------- assemblage ----------
const pageProps = { page: { size: PAGE, margin: MARGIN } };
const sections = [];

// lecture des unités (placeholder si l'unité n'est pas encore rédigée - builds partiels de mise au point)
const unitMd = {};
UNITS.forEach(u => {
  const p = path.join(SRC, u.file);
  if (fs.existsSync(p)) unitMd[u.id] = fs.readFileSync(p, 'utf8');
  else {
    const t = u.id === 'avant' ? '# Avant de commencer' : (/^[A-G]$/.test(u.id) ? `# Annexe ${u.id} — (en cours)` : `# ${u.id} — (en cours)`);
    unitMd[u.id] = `${t}\n\n*Unité en cours de rédaction.*\n\n## En attente\n\nContenu à venir.\n`;
    console.log('placeholder:', u.id);
  }
});

// l'avant-propos est scindé : (remerciements + confidentialité) AVANT le sommaire, le reste APRÈS
const avant = unitMd['avant'];
const splitIx = avant.search(/^##\s+À propos/m);
const avantPre = splitIx > 0 ? avant.slice(0, splitIx) : avant;
const avantPost = splitIx > 0 ? '# Avant de commencer\n\n*Mode d’emploi du playbook : à lire avant le premier rendez-vous.*\n\n' + avant.slice(splitIx) : '';

// 1. couverture
sections.push({ properties: { ...pageProps }, ...emptyHF, children: coverChildren() });

// 2. remerciements + confidentialité (sans entrée au sommaire)
sections.push({
  properties: { ...pageProps },
  headers: { default: mkHeader('AVANT DE COMMENCER') }, footers: { default: footerP },
  children: convertBody(avantPre.replace(/^#\s+.*$/m, '# Remerciements & confidentialité'), { id: 'avantpre' }, { noMiniToc: true, noToc: true })
});

// 3. corps converti D'ABORD (pour remplir le registre du sommaire), inséré APRÈS le sommaire
const bodySections = [];
if (avantPost) {
  bodySections.push({
    properties: { ...pageProps },
    headers: { default: mkHeader('AVANT DE COMMENCER') }, footers: { default: footerP },
    children: convertBody(avantPost, { id: 'avant', head: 'OUVERTURE' }, { noMiniToc: true })
  });
}
UNITS.filter(u => u.id !== 'avant').forEach(u => {
  const md = unitMd[u.id];
  const h1 = (md.match(/^#\s+(.*)$/m) || [null, u.id])[1];
  const isAnnex = /^Annexe/.test(h1);
  const headTxt = plainHeading(h1).toUpperCase();
  const kids = [];
  if (PARTS[u.id]) kids.push(...partOpener(PARTS[u.id]));
  kids.push(...convertBody(md, u, { noMiniToc: isAnnex }));
  bodySections.push({
    properties: { ...pageProps },
    headers: { default: mkHeader(headTxt) }, footers: { default: footerP },
    children: kids
  });
});

// 4. sommaire (registre complet), puis le corps
sections.push({
  properties: { ...pageProps },
  headers: { default: mkHeader('SOMMAIRE') }, footers: { default: footerP },
  children: tocChildren()
});
sections.push(...bodySections);

fs.writeFileSync(path.join(__dirname, 'toc-map-emma.json'), JSON.stringify(tocRegistry, null, 1));

const doc = new Document({
  styles: { default: { document: { run: { font: 'Calibri', size: 17, color: INK } } } },
  numbering: {
    config: [
      {
        reference: 'bullets',
        levels: [0, 1, 2].map(l => ({
          level: l, format: LevelFormat.BULLET, text: ['•', '◦', '▪'][l],
          style: { paragraph: { indent: { left: 340 + l * 340, hanging: 230 } } },
        }))
      },
      {
        reference: 'ordered',
        levels: [{
          level: 0, format: LevelFormat.DECIMAL, text: '%1.',
          style: { paragraph: { indent: { left: 380, hanging: 270 } } }
        }]
      }
    ]
  },
  sections
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync(path.join(__dirname, 'Planet_Aura_Sales_Playbook_FINAL_2026.docx'), buf);
  console.log('OK', buf.length, 'bytes,', tocRegistry.length, 'entrées sommaire');
});
