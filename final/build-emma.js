// Sales Playbook Planet Aura - édition finale 2026 (v2.1)
// Générateur au design de la maquette v2.0 d'Emma : A4, serif éditorial, stat-blocs,
// encadrés à fond plat, exergues, ouvertures de partie en chiffres romains.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, Table, TableRow, TableCell,
  HeadingLevel, AlignmentType, WidthType, ShadingType, BorderStyle,
  LevelFormat, PageBreak, Footer, Header, PageNumber, VerticalAlign,
  Bookmark, InternalHyperlink, ExternalHyperlink, TabStopType, LeaderType, TextDirection, HeightRule, UnderlineType,
  HorizontalPositionRelativeFrom, VerticalPositionRelativeFrom, TextWrappingType
} = require('docx');

const SRC = path.join(__dirname, 'content-emma');
const A = path.join(__dirname, '../build/assets');

// ---- Charte (maquette v2.0)
const NAVY = '12475B';
const TEAL = '2D92A8';
const TEALD = '12475B';
const ORANGE = 'F66803';
const RED = 'C0392B';
const GREEN = '2E8B57';
const CREAM = 'FDF0E4';
const LTEAL = 'EAF3F6';
const LGREEN = 'EDF6F0';
const LRED = 'FAEDEB';
const ZEBRA = 'F4F8F9';
const GRAY = '5F7078';
const INK = '3A4A50';
const DARKBG = '12475B';
const SERIF = 'Playfair Display';
const SANS = 'Inter';
const LABEL = 'Poppins';
const PBORDEAUX = '722F45';
const POCRE = 'C6A15B';
// Déclinaisons par accent de partie : variante foncée (petits textes, en-têtes de tableaux)
// et teinte claire (fonds d'encadrés) - cohérence de couleurs au sein de chaque partie.
const DEEP_OF = { [TEAL]: '20768B', [PBORDEAUX]: '722F45', [POCRE]: '8A6A33', [NAVY]: NAVY, [ORANGE]: 'C2520A' };
const TINT_OF = { [TEAL]: 'EAF3F6', [PBORDEAUX]: 'F6EEF1', [POCRE]: 'F8F3E9', [NAVY]: 'EAF0F4', [ORANGE]: 'FDEFE2' };

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
  { id: 'A', file: 'A.md' }, { id: 'B', file: 'B.md' }, { id: 'C', file: 'C.md' }, { id: 'D', file: 'D.md' },
  { id: 'E', file: 'E.md' }, { id: 'F', file: 'F.md' }, { id: 'G', file: 'G.md' }, { id: 'H', file: 'H.md' },
  { id: 'I', file: 'I.md' }, { id: 'J', file: 'J.md' }, { id: 'K', file: 'K.md' }, { id: 'L', file: 'L.md' },
  { id: 'M', file: 'M.md' }, { id: 'N', file: 'N.md' }, { id: 'O', file: 'O.md' }, { id: 'P', file: 'P.md' },
  { id: 'Q', file: 'Q.md' }, { id: 'R', file: 'R.md' }, { id: 'S', file: 'S.md' }, { id: 'T', file: 'T.md' },
  { id: 'U', file: 'U.md' },
];

const PARTS = {
  '01': { big: '1', col: TEAL, tab: 'PARTIE 1 · ANALYSER', rom: 'I', num: 'PARTIE 1', title: 'Analyser l’entreprise et son offre', sub: 'Comprendre avant de convaincre', chapters: ['01 · Contexte et enjeux commerciaux', '02 · Diagnostic de l’entreprise', '03 · Organisation et interlocuteurs', '04 · Offres et politique tarifaire', '05 · Concurrence et différenciation'] },
  '06': { big: '2', col: PBORDEAUX, tab: 'PARTIE 2 · CIBLER', rom: 'II', num: 'PARTIE 2', title: 'Définir les cibles et les solutions adaptées', sub: 'Les bons comptes, les bonnes réponses', chapters: ['06 · Profils de clients idéaux (ICP)', '07 · Personas et acteurs de la décision', '08 · Correspondance entre enjeux et solutions'] },
  '09': { big: '3', col: POCRE, tab: 'PARTIE 3 · VENDRE', rom: 'III', num: 'PARTIE 3', title: 'Formaliser la prospection et la vente', sub: 'Du premier contact à la signature', chapters: ['09 · Processus d’acquisition et pipeline', '10 · Séquences de prospection et scripts', '11 · Qualification et processus de vente', '12 · Conduite des entretiens (méthode SPIN)', '13 · Argumentaires et objections'] },
  '14': { big: '4', col: NAVY, tab: 'PARTIE 4 · PILOTER', rom: 'IV', num: 'PARTIE 4', title: 'Fournir les outils et organiser le pilotage', sub: 'Outiller, mesurer, faire vivre', chapters: ['14 · Ressources d’aide à la vente', '15 · Organisation et outils', '16 · Activation, fidélisation et SAV', '17 · Indicateurs et méthode de suivi', '18 · Mise à jour et appropriation'] },
  'A': { big: 'A', col: ORANGE, tab: 'ANNEXES', rom: 'V', num: 'ANNEXES', title: 'Annexes', sub: 'Documents complémentaires', chapters: ['A · Fiches ICP & personas', 'B · Fiche réflexe, checklists et modèles', 'C · Chiffres officiels, preuve et avis', 'D · Grille tarifaire shipping 2026', 'E · Grille stockage & picking 2026', 'F · Order Form 2026', 'G · Mandat SEPA', 'H · CGS : l\u2019essentiel', 'I · Conformité et fiches pays', 'J · Cartes de zones USA & Norvège', 'K · POA Canada : formulaire vierge', 'L · Certificat de Champagne', 'M · Mode d\u2019emploi Planet\u2019Connect', 'N · Manuel utilisateur & procédure Suède', 'O · Formulaire de shipping par email', 'P · Planet\u2019Stock en images', 'Q · Flyer de prospection', 'R · Organigramme et documents officiels', 'S · Parcours d\u2019onboarding 0-90 jours', 'T · Glossaire', 'U · Liens utiles'] },
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
// deux figures côte à côte (disposition deux colonnes de la maquette)
function pairFigure(items) {
  const half = Math.floor(CONTENT_W / 2);
  return [new Table({
    width: { size: CONTENT_W, type: WidthType.DXA },
    columnWidths: [half, CONTENT_W - half],
    borders: {
      top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
      left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
      insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
    },
    rows: [new TableRow({
      cantSplit: true,
      children: items.map((it, i) => new TableCell({
        width: { size: i === 0 ? half : CONTENT_W - half, type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        margins: { top: 48, bottom: 34, left: 40, right: 40 },
        children: [
          new Paragraph({ alignment: AlignmentType.CENTER, keepNext: !!it.caption, spacing: { after: it.caption ? 36 : 0 }, children: [imgAuto(it.img, it.w || 280)] }),
          ...(it.caption ? [new Paragraph({
            alignment: AlignmentType.CENTER,
            children: [new TextRun({ text: it.caption, italics: true, size: 16, color: GRAY, font: SERIF })]
          })] : []),
        ]
      }))
    })]
  }), spacerPara(110)];
}

function figure(name, wPx, caption) {
  const paras = [new Paragraph({ alignment: AlignmentType.CENTER, keepNext: !!caption, spacing: { before: 54, after: caption ? 28 : 86 }, children: [imgAuto(name, wPx)] })];
  if (caption) paras.push(new Paragraph({
    alignment: AlignmentType.CENTER, spacing: { after: 88 },
    children: [new TextRun({ text: caption, italics: true, size: 16, color: GRAY, font: SERIF })]
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

function pushTextEmoji(runs, text, style) {
  let last = 0, m;
  EMOJI_RE.lastIndex = 0;
  while ((m = EMOJI_RE.exec(text)) !== null) {
    if (m.index > last) runs.push(new TextRun({ text: text.slice(last, m.index), ...style }));
    runs.push(img(`icons/${EMOJI_ICONS[m[1]]}.png`, 13, 13));
    last = m.index + m[1].length;
  }
  if (last < text.length) runs.push(new TextRun({ text: text.slice(last), ...style }));
}

// ---------- glossaire lié au contenu ----------
// Les termes définis à l'annexe E sont détectés dans le corps : la première occurrence
// de chaque terme dans un chapitre est colorée (accent de la partie), soulignée de
// pointillés et cliquable vers sa définition.
const GLO_VARIANT_OVERRIDES = {
  'DDP / DAP': ['DDP', 'DAP'],
  'DA / EMCS / DAU': ['EMCS', 'DAU'],
  'MQL / SQL': ['MQL', 'SQL'],
  'POA / SSN': ['POA', 'SSN'],
  'FEVS / OIV': ['FEVS', 'OIV'],
  'Groupage / Direct': ['Groupage', 'groupage'],
  'Tiers A/B/C': ['Tiers A', 'Tiers B', 'Tiers C'],
  'Three-tier system': ['Three-tier system', 'three-tier system', 'three-tier'],
  'Ad valorem': ['Assurance ad valorem', 'assurance ad valorem', 'ad valorem'],
  '5 forces de Porter': ['5 forces de Porter', 'forces de Porter'],
  'Œnotourisme': ['Œnotourisme', 'œnotourisme', 'oenotourisme'],
  'Jours ouvrés': ['Jours ouvrés', 'jours ouvrés', 'jours ouvrables'],
  'Matrice « Missions Planet Aura »': ['Missions Planet Aura'],
  'Motifs de perte CRM': ['Motifs de perte', 'motifs de perte'],
  'Ticketing (à venir)': ['Ticketing', 'ticketing'],
  'PO Box': ['PO Box', 'PO BOX', 'PO box'],
  'Win/loss': ['Win/loss', 'win/loss', 'Win/Loss'],
  'Golden Circle': ['Golden Circle'],
  'InMail': ['InMail'],
  'SogeCommerce': ['SogeCommerce'],
  'Jobs-to-be-Done': ['Jobs-to-be-Done'],
  'Certification J+30': ['Certification J+30', 'certification J+30'],
  // mots courants ou expressions : définis au glossaire mais jamais liés automatiquement
  'Direct': null, 'Touche': null, 'Preuve': null, 'Signal': null, 'Palier': null,
  'Périmètre': null, 'Pièce': null, 'Quadrant': null, 'Réserves': null,
  'Combinaison': null, 'Contingence': null, 'Substitution': null, 'Sponsor': null,
  'Close': null, 'Accountable': null, 'Best-seller': null, 'Consolidation': null,
  'Vedette / parité / bruit': null, 'Statuts particuliers': null, 'CE 761901191': null,
  'Comptes de référence publics': null, 'Cartographier un flux': null, 'Courtier': null,
  'Claim': null, 'Quota': null, 'Déchéance': null, 'Mhl': null,
};
const GLO_ACRONYM = /^[A-Z0-9\-\s/.'+]+$/;
const GLO_SLUG = {}; const TERM_SLUG = {}; let GLO_RE = null;
{
  try {
    const emd = fs.readFileSync(path.join(SRC, 'T.md'), 'utf8');
    const variants = [];
    const expand = (v) => v.includes("'") || v.includes('’')
      ? [v.replace(/’/g, "'"), v.replace(/'/g, '’')] : [v];
    emd.split('\n').forEach(l => {
      const mm = l.match(/^\|\s*\*\*([^*]+)\*\*\s*\|/);
      if (!mm) return;
      const term = mm[1].trim();
      const slug = term.normalize('NFD').replace(/[^A-Za-z0-9]+/g, '').slice(0, 24);
      TERM_SLUG[term] = slug;
      let vars;
      if (term in GLO_VARIANT_OVERRIDES) vars = GLO_VARIANT_OVERRIDES[term];
      else if (term.includes(' / ')) vars = term.split(' / ').map(s => s.trim());
      else if (GLO_ACRONYM.test(term)) vars = [term];
      else vars = [term, term.charAt(0).toLowerCase() + term.slice(1)];
      if (!vars) return;
      vars.flatMap(expand).forEach(v => { if (!(v in GLO_SLUG)) { GLO_SLUG[v] = slug; variants.push(v); } });
    });
    variants.sort((a, b) => b.length - a.length);
    const esc = variants.map(v => v.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'));
    GLO_RE = new RegExp('(?<![A-Za-z0-9À-ſ])(' + esc.join('|') + ')(s?)(?![A-Za-z0-9À-ſ])', 'g');
  } catch (e) { GLO_RE = null; }
}
const gloSeen = new Set();

// URLs (Drive, sites) rendues cliquables dans tout le document
const URL_RE = /((?:https?:\/\/|www\.|drive\.google\.com\/|docs\.google\.com\/|app\.planet-aura\.com)[^\s|)»«;,]+)/g;
function pushTextLinks(runs, text, style) {
  let last = 0, m;
  URL_RE.lastIndex = 0;
  while ((m = URL_RE.exec(text)) !== null) {
    let url = m[1].replace(/[.,;:]+$/, '');
    if (m.index > last) pushTextRefs(runs, text.slice(last, m.index), style);
    runs.push(new ExternalHyperlink({
      link: /^https?:\/\//.test(url) ? url : 'https://' + url,
      children: [new TextRun({ ...style, text: url, color: '20768B', underline: { type: UnderlineType.SINGLE, color: '20768B' } })]
    }));
    last = m.index + url.length;
  }
  if (last < text.length) pushTextRefs(runs, text.slice(last), style);
}

// renvois internes cliquables : « annexe X » vers la tête d'annexe, « chap. NN » vers la tête de chapitre
const REF_RE = /([Aa]nnexes?\s+([A-U])|[Cc]hap(?:itres?)?\.?\s*(0\d|1[0-8]))(?![A-Za-z0-9\u00c0-\u017f])/g;
function pushTextRefs(runs, text, style) {
  let last = 0, m;
  REF_RE.lastIndex = 0;
  while ((m = REF_RE.exec(text)) !== null) {
    const target = m[2] || m[3];
    if (m.index > last) pushTextEmoji(runs, text.slice(last, m.index), style);
    runs.push(new InternalHyperlink({
      anchor: 'chap' + target,
      children: [new TextRun({ ...style, text: m[1].replace(/\s+/g, '\u00a0'), color: style.color && style.color !== INK ? style.color : TEALD, bold: true })]
    }));
    last = m.index + m[1].length;
  }
  if (last < text.length) pushTextEmoji(runs, text.slice(last), style);
}

function pushText(runs, text, style) {
  const { glo, gloAcc, ...st } = style;
  if (!glo || !GLO_RE) { pushTextLinks(runs, text, st); return; }
  let last = 0, m;
  GLO_RE.lastIndex = 0;
  while ((m = GLO_RE.exec(text)) !== null) {
    const slug = GLO_SLUG[m[1]];
    if (!slug) continue;
    const key = glo + ':' + slug;
    if (gloSeen.has(key)) continue;
    gloSeen.add(key);
    if (m.index > last) pushTextLinks(runs, text.slice(last, m.index), st);
    runs.push(new InternalHyperlink({
      anchor: 'glo' + slug,
      children: [new TextRun({ ...st, text: m[0], color: gloAcc || TEAL, underline: { type: UnderlineType.DOTTED, color: gloAcc || TEAL } })]
    }));
    last = m.index + m[0].length;
  }
  if (last < text.length) pushTextLinks(runs, text.slice(last), st);
}

function inlineRuns(text, base = {}) {
  text = text.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1').replace(/\\\*/g, '*');
  const { glo: _g, gloAcc: _ga, ...safe } = base;
  const runs = [];
  const re = /(\*\*([^*]+)\*\*|\*([^*]+)\*|`([^`]+)`)/g;
  let last = 0, m;
  while ((m = re.exec(text)) !== null) {
    if (m.index > last) pushText(runs, text.slice(last, m.index), base);
    if (m[2] !== undefined) pushText(runs, m[2], { bold: true, ...base });
    else if (m[3] !== undefined) pushText(runs, m[3], { italics: true, ...base });
    else if (m[4] !== undefined) runs.push(new TextRun({ text: m[4], font: 'Consolas', size: 17, shading: { type: ShadingType.CLEAR, fill: 'EDF2F4' }, ...safe }));
    last = m.index + m[0].length;
  }
  if (last < text.length) pushText(runs, text.slice(last), base);
  if (runs.length === 0) runs.push(new TextRun({ text: '', ...base }));
  return runs;
}

// ---------- tables ----------
function parseTableBlock(lines, accent = TEALD, gloAnchors = false) {
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
    cantSplit: true,
    children: Array.from({ length: nCols }, (_, i) => {
      const cellRuns = inlineRuns(cells[i] || '', isHeader ? { bold: true, color: 'FFFFFF', size: fontSize } : { size: fontSize });
      // annexe E : chaque terme du glossaire porte une ancre, cible des liens du corps
      let kids = cellRuns;
      if (gloAnchors && !isHeader && i === 0) {
        const term = (cells[0] || '').replace(/\*\*/g, '').trim();
        const slug = TERM_SLUG[term];
        if (slug) kids = [new Bookmark({ id: 'glo' + slug, children: cellRuns })];
      }
      // annexe E, dernière colonne : retour cliquable vers les chapitres qui citent le terme
      if (gloAnchors && !isHeader && i === nCols - 1) {
        const slug = TERM_SLUG[(cells[0] || '').replace(/\*\*/g, '').trim()];
        const refs = (slug && typeof GLO_BACKREFS !== 'undefined' && GLO_BACKREFS[slug]) || [];
        if (refs.length) {
          kids = kids.concat([new TextRun({ text: '  ', size: 11, color: GRAY }), new TextRun({ text: '\u21a9\u00a0', size: 11, color: GRAY })]);
          refs.slice(0, 8).forEach((rid, ri) => {
            if (ri > 0) kids.push(new TextRun({ text: ' \u00b7 ', size: 11, color: GRAY }));
            kids.push(new InternalHyperlink({ anchor: 'chap' + rid, children: [new TextRun({ text: rid, bold: true, size: 11, color: TEAL })] }));
          });
          if (refs.length > 8) kids.push(new TextRun({ text: ' \u2026', size: 11, color: GRAY }));
        }
      }
      return new TableCell({
        width: { size: widths[i], type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        shading: isHeader
          ? { type: ShadingType.CLEAR, fill: accent }
          : (rowIdx % 2 === 1 ? { type: ShadingType.CLEAR, fill: ZEBRA } : undefined),
        margins: { top: 30, bottom: 30, left: 96, right: 96 },
        children: [new Paragraph({
          spacing: { before: 12, after: 12 },
          children: kids
        })]
      });
    })
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
function statBlock(lines, accent = TEAL) {
  const deep = DEEP_OF[accent] || accent;
  const STAT_COLORS = deep === NAVY ? [NAVY, ORANGE, DEEP_OF[TEAL], NAVY, ORANGE] : [deep, ORANGE, NAVY, deep, ORANGE];
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
        margins: { top: 64, bottom: 64, left: 70, right: 70 },
        children: [
          new Paragraph({
            alignment: AlignmentType.CENTER, spacing: { after: 40 },
            children: [new TextRun({ text: v, bold: true, size: n >= 5 ? 34 : 44, color: STAT_COLORS[i % STAT_COLORS.length], font: SERIF })]
          }),
          new Paragraph({
            alignment: AlignmentType.CENTER,
            children: inlineRuns(c, { size: 16, color: GRAY })
          }),
        ]
      }))
    })]
  });
}

// ---------- conversion md -> blocs ----------
let orderedInstance = 1;

// paragraphe d'espacement marqué : purgé en fin d'unité pour éviter une page blanche
function spacerPara(after) { const p = new Paragraph({ spacing: { after }, children: [] }); p.__spacer = true; return p; }

function convertBody(md, unit, opts = {}) {
  const out = [];
  const placements = (IMAGE_PLACEMENTS[unit.id] || []).slice();
  const lines = md.split('\n');
  let i = 0;
  let h1Seen = false;
  // accent de partie : tous les éléments structurels du chapitre suivent la couleur de sa partie
  const partAcc = PART_OF_UNIT[unit.id];
  const ACC = partAcc ? partAcc.col : TEAL;
  const DEEP = DEEP_OF[ACC] || TEALD;
  const TINT = TINT_OF[ACC] || LTEAL;
  const gloId = (unit.id === 'T' || unit.id === 'avantpre' || unit.id === 'avantpre2') ? null : unit.id;
  const BODY = { size: 19, glo: gloId, gloAcc: DEEP };
  const CP = opts.letter ? 112 : opts.compact ? 48 : 62;   // after des paragraphes
  const CL = opts.letter ? 36 : opts.compact ? 14 : 16;   // after des listes

  const tryPlace = (headingText) => {
    const out2 = [];
    for (let k = 0; k < placements.length; ) {
      if (new RegExp(placements[k].after, 'i').test(headingText)) {
        const p = placements.splice(k, 1)[0];
        out2.push(...(p.pair ? pairFigure(p.pair) : figure(p.img, p.w, p.caption)));
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
        out.push(statBlock(code, ACC));
        out.push(spacerPara(88));
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
      out.push(spacerPara(100));
      continue;
    }

    if (/^\s*\|/.test(line) && i + 1 < lines.length && /^\s*\|[\s:|-]+\|?\s*$/.test(lines[i + 1])) {
      const tbl = [];
      while (i < lines.length && /^\s*\|/.test(lines[i])) { tbl.push(lines[i]); i++; }
      out.push(parseTableBlock(tbl, DEEP, unit.id === 'T'));
      out.push(spacerPara(92));
      continue;
    }

    if (/^\\page\s*$/.test(line)) {
      out.push(new Paragraph({ children: [new PageBreak()] }));
      i++; continue;
    }

    if (/^---+\s*$/.test(line)) {
      out.push(new Paragraph({
        border: { bottom: { style: BorderStyle.SINGLE, size: 5, color: 'CCDDE3' } },
        spacing: { before: 90, after: 190 }, children: []
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
        const hm = txt.match(/^(Annexe\s+)?([0-9A-U]{1,2})\s*[—–-]\s*(.*)$/) || [null, '', '', txt];
        const isAnnex = !!hm[1];
        const num = hm[2]; const title = hm[3] || txt;
        const part = PARTS[unit.id];
        const kpart = part || PART_OF_UNIT[unit.id];
        const kicker = unit.head || (isAnnex || (kpart && kpart.num === 'ANNEXES')
          ? 'ANNEXES  ·  DOCUMENTS COMPLÉMENTAIRES'
          : kpart ? `${kpart.num}  ·  ${kpart.title.toUpperCase()}` : 'SALES PLAYBOOK 2026');
        const kickerPara = new Paragraph({
          spacing: { before: 60, after: 110 },
          children: [new Bookmark({
            id: 'chap' + unit.id,
            children: [new TextRun({ text: kicker, bold: true, size: 15, color: DEEP, font: LABEL })]
          })]
        });
        let key = null;
        if (!opts.noToc) {
          key = `toc${tocRegistry.length}`;
          tocRegistry.push({ key, level: 1, text: plainHeading(txt), id: unit.id });
        }
        const titleRuns = [];
        if (num) titleRuns.push(new TextRun({ text: (isAnnex ? 'Annexe ' + num : num) + '   ', bold: true, size: 76, color: ACC, font: SERIF }));
        titleRuns.push(new TextRun({ text: title, bold: true, size: 46, color: NAVY, font: SERIF }));
        const titlePara = new Paragraph({
          heading: HeadingLevel.HEADING_1,
          spacing: { after: 70 },
          children: key ? [new Bookmark({ id: key, children: titleRuns })] : titleRuns
        });
        // sous-titre italique (ligne suivante '*...*')
        let subPara = null;
        let j = i + 1;
        while (j < lines.length && lines[j].trim() === '') j++;
        if (j < lines.length && /^\*[^*].*\*$/.test(lines[j].trim())) {
          subPara = new Paragraph({
            spacing: { after: 110 },
            children: [new TextRun({ text: lines[j].trim().replace(/^\*|\*$/g, ''), italics: true, size: 23, color: GRAY, font: SERIF })]
          });
          i = j;
        }
        // mini-sommaire « DANS CE CHAPITRE » à droite du titre : la tête de chapitre
        // tient en deux colonnes au lieu de s'empiler (gain d'une demi-page par chapitre)
        const h2lines = opts.noMiniToc ? [] : lines.slice(i + 1).filter(l => /^##\s/.test(l)).map(l => plainHeading(l.replace(/^##\s+/, '')));
        const NOB = {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
          insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
        };
        if (h2lines.length >= 3) {
          const RW = 3700, LW = CONTENT_W - RW;
          const baseIdx = tocRegistry.length;
          const tocParas = [new Paragraph({
            border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: ACC } },
            spacing: { after: 46 },
            children: [new TextRun({ text: 'D A N S   C E   C H A P I T R E', bold: true, size: 13, color: DEEP, font: LABEL })]
          })];
          h2lines.forEach((h, k) => {
            const kk = `toc${baseIdx + k}`;
            const page = tocPages[kk] !== undefined ? String(tocPages[kk]) : '';
            tocParas.push(new Paragraph({
              tabStops: [{ type: TabStopType.RIGHT, position: RW - 300 }],
              border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' } },
              spacing: { before: 26, after: 30 },
              children: [
                new InternalHyperlink({ anchor: kk, children: [new TextRun({ text: h, size: 15, color: INK })] }),
                new TextRun({ text: '\t' }),
                new TextRun({ text: page, bold: true, size: 15, color: DEEP, font: LABEL }),
              ]
            }));
          });
          const leftKids = [kickerPara, titlePara];
          if (subPara) leftKids.push(subPara);
          leftKids.push(new Paragraph({
            border: { bottom: { style: BorderStyle.SINGLE, size: 11, color: ACC } },
            spacing: { after: 20 }, children: []
          }));
          out.push(new Table({
            width: { size: CONTENT_W, type: WidthType.DXA },
            columnWidths: [LW, RW],
            borders: NOB,
            rows: [new TableRow({ children: [
              new TableCell({
                width: { size: LW, type: WidthType.DXA },
                margins: { top: 0, bottom: 0, left: 0, right: 280 },
                children: leftKids
              }),
              new TableCell({
                width: { size: RW, type: WidthType.DXA },
                margins: { top: 50, bottom: 0, left: 220, right: 0 },
                borders: { left: { style: BorderStyle.SINGLE, size: 4, color: 'DCE8EC' } },
                children: tocParas
              }),
            ] })]
          }));
          out.push(new Paragraph({ spacing: { after: 160 }, children: [] }));
        } else {
          out.push(kickerPara, titlePara);
          if (subPara) out.push(subPara);
          const axRefs = (isAnnex && typeof ANNEX_BACKREFS !== 'undefined' && ANNEX_BACKREFS[unit.id]) || [];
          out.push(new Paragraph({
            border: { bottom: { style: BorderStyle.SINGLE, size: 11, color: ACC } },
            spacing: { after: axRefs.length ? 70 : 170 }, children: []
          }));
          // annexes : retour cliquable vers les chapitres qui renvoient à cette annexe
          if (axRefs.length) {
            const axKids = [new TextRun({ text: '\u21a9 CIT\u00c9E DANS LE TEXTE :  ', bold: true, size: 13, color: GRAY, font: LABEL })];
            axRefs.slice(0, 10).forEach((rid, ri) => {
              if (ri > 0) axKids.push(new TextRun({ text: '  \u00b7  ', size: 13, color: GRAY, font: LABEL }));
              axKids.push(new InternalHyperlink({ anchor: 'chap' + rid, children: [new TextRun({ text: /^[A-U]$/.test(rid) ? 'annexe\u00a0' + rid : 'chap.\u00a0' + rid, bold: true, size: 13, color: DEEP, font: LABEL })] }));
            });
            if (axRefs.length > 10) axKids.push(new TextRun({ text: '  \u2026', size: 13, color: GRAY, font: LABEL }));
            out.push(new Paragraph({ spacing: { after: 150 }, children: axKids }));
          }
        }
        out.push(...tryPlace(txt));
        i++; continue;
      }

      if (lvl === 2) {
        let h2runs = inlineRuns(txt, { bold: true, size: 30, color: NAVY, font: SERIF });
        if (!opts.noToc) {
          const k2 = `toc${tocRegistry.length}`;
          tocRegistry.push({ key: k2, level: 2, text: plainHeading(txt), id: unit.id });
          h2runs = [new Bookmark({ id: k2, children: h2runs })];
        }
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_2,
          keepNext: true,
          spacing: { before: 184, after: 56 },
          children: h2runs
        }));
      } else if (lvl === 3) {
        out.push(new Paragraph({
          heading: HeadingLevel.HEADING_3,
          keepNext: true,
          spacing: { before: opts.letter ? 190 : 148, after: opts.letter ? 56 : 48 },
          children: inlineRuns(txt.toUpperCase(), { bold: true, size: 18, color: DEEP, font: LABEL })
        }));
      } else {
        out.push(new Paragraph({
          keepNext: true,
          spacing: { before: 140, after: 52 },
          children: inlineRuns(txt, { bold: true, size: 21, color: NAVY })
        }));
      }
      out.push(...tryPlace(txt));
      i++; continue;
    }

    if (/^>\s?/.test(line)) {
      // de l'air avant l'encadré, sauf s'il suit directement un titre
      const prevLine = lines.slice(0, i).reverse().find(l => l.trim() !== '') || '';
      const afterHeading = /^#{1,4}\s/.test(prevLine);
      const quote = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) { quote.push(lines[i].replace(/^>\s?/, '')); i++; }
      const head = quote[0] || '';

      // Exergue : citation seule « ... »
      if (quote.length === 1 && /^«/.test(head.trim()) && !/\*\*/.test(head)) {
        out.push(new Paragraph({
          alignment: AlignmentType.CENTER,
          spacing: { before: opts.compact ? 100 : 130, after: opts.compact ? 100 : 130 },
          indent: { left: 500, right: 500 },
          children: [new TextRun({ text: head.trim(), italics: true, size: 25, color: DEEP, font: SERIF })]
        }));
        continue;
      }

      // Encadrés à fond plat (maquette) : pas de bordure, étiquette colorée (sans icône)
      let fill = TINT, txtColor = INK, labelColor = DEEP;
      if (/^(🚫|❗)|\*\*(INTERDIT|ALERTE|NON-ÉLIGIBLE)/.test(head)) { fill = LRED; labelColor = RED; }
      else if (/^💡|\*\*(LE CONSEIL|BONNE PRATIQUE)/.test(head)) { fill = CREAM; labelColor = ORANGE; }
      else if (/^⚠️|\*\*(LE POINT DE VIGILANCE|POINT DE VIGILANCE|À CONFIRMER|RÈGLE)/.test(head)) { fill = CREAM; labelColor = ORANGE; }
      else if (/^✅|\*\*CE QUI FONCTIONNE/.test(head)) { fill = LGREEN; labelColor = GREEN; }
      else if (/^📌|\*\*À RETENIR/.test(head)) { fill = DARKBG; txtColor = 'FFFFFF'; labelColor = 'F4C9A8'; }
      const calloutParas = [];
      quote.forEach((q, qi) => {
        if (q.trim() === '') { calloutParas.push(new Paragraph({ spacing: { after: 44 }, children: [] })); return; }
        let kids;
        const lm = qi === 0 ? q.match(/^([⚠️💡🚫❗✅📌🚨]*\s*)\*\*([^*]+?)(\s*[—:-])?\*\*\s*(.*)$/) : null;
        if (lm) {
          kids = [
            new TextRun({ text: lm[2].toUpperCase().replace(/^LE POINT/, 'LE POINT') + (lm[3] ? ' -' : ''), bold: true, size: 16, color: labelColor }),
            new TextRun({ text: '  ' }),
            ...inlineRuns(lm[4] || '', { size: 18, color: txtColor })
          ];
        } else {
          kids = inlineRuns(q, { size: 18, color: txtColor });
        }
        calloutParas.push(new Paragraph({ spacing: { before: 18, after: 18 }, children: kids }));
      });
      if (!afterHeading) out.push(spacerPara(16));
      out.push(new Table({
        width: { size: CONTENT_W, type: WidthType.DXA },
        columnWidths: [CONTENT_W],
        borders: {
          top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
          left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
          insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
        },
        rows: [new TableRow({ cantSplit: true, children: [new TableCell({
          width: { size: CONTENT_W, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill },
          margins: { top: 68, bottom: 68, left: 215, right: 195 },
          children: calloutParas
        })] })]
      }));
      out.push(spacerPara(92));
      continue;
    }

    if ((m = line.match(/^(\s*)-\s+\[( |x)\]\s+(.*)$/))) {
      out.push(new Paragraph({
        indent: { left: 360, hanging: 240 },
        spacing: { after: 28 },
        children: [new TextRun({ text: m[2] === 'x' ? '☑ ' : '☐ ', size: 19, color: DEEP }), ...inlineRuns(m[3], BODY)]
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)[-•]\s+(.*)$/))) {
      const level = Math.min(Math.floor(m[1].length / 2), 2);
      out.push(new Paragraph({
        numbering: { reference: 'bullets', level },
        spacing: { after: CL },
        children: inlineRuns(m[2], BODY)
      }));
      i++; continue;
    }

    if ((m = line.match(/^(\s*)(\d+)[.)]\s+(.*)$/))) {
      const startNew = !(i > 0 && /^\s*\d+[.)]\s/.test(lines[i - 1]));
      if (startNew) orderedInstance++;
      out.push(new Paragraph({
        numbering: { reference: 'ordered', level: 0, instance: orderedInstance },
        spacing: { after: CL },
        children: inlineRuns(m[3], BODY)
      }));
      i++; continue;
    }

    if (line.trim() === '') { i++; continue; }
    // sous-titre déjà consommé après H1
    if (h1Seen === 'skipnext') { h1Seen = true; i++; continue; }

    // une ligne d'annonce qui se termine par « : » reste collée au bloc qu'elle introduit
    out.push(new Paragraph({ spacing: opts.letter ? { after: CP, line: 276, lineRule: 'auto' } : { after: CP }, keepNext: /:\s*$/.test(line.trim()), children: inlineRuns(line, BODY) }));
    i++;
  }
  // purge des espaceurs de fin d'unité (sinon un espaceur vide peut déborder seul sur une page blanche)
  while (out.length && out[out.length - 1].__spacer) out.pop();
  return out;
}

// onglet de bordure par unité
// ordre explicite : Object.values remonterait la clé '14' (entier canonique JS) en tête
const PART_LIST = ['01', '06', '09', '14', 'A'].map(k => PARTS[k]);
function tabOf(id) {
  const part = PART_OF_UNIT[id];
  if (!part) return null;
  return { idx: PART_LIST.indexOf(part), col: part.col, label: part.tab };
}

// partie de rattachement de chaque unité (pour le kicker)
const PART_OF_UNIT = {};
{
  let cur = null;
  UNITS.forEach(u => { if (PARTS[u.id]) cur = PARTS[u.id]; PART_OF_UNIT[u.id] = cur; });
}

// ---------- ouverture de partie ----------
function partOpener(p) {
  // chaque chapitre list\u00e9 est cliquable (ancre \u00ab chap<id> \u00bb pos\u00e9e sur la t\u00eate de chapitre)
  const chapterLines = p.chapters.map(c => {
    const m = c.match(/^([0-9A-U]{1,2})\s*\u00b7\s*(.*)$/);
    const runs = m ? [
      new TextRun({ text: m[1], bold: true, size: 23, color: 'FFFFFF', font: SERIF }),
      new TextRun({ text: '    ' + m[2], size: 22, color: 'F2E9E4' }),
    ] : [new TextRun({ text: c, size: 22, color: 'F2E9E4' })];
    return new Paragraph({
      spacing: { after: 88 },
      children: m ? [new InternalHyperlink({ anchor: 'chap' + m[1], children: runs })] : runs
    });
  });
  return [
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: [CONTENT_W],
      borders: {
        top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
        left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
        insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
      },
      rows: [new TableRow({
        height: { value: 11600, rule: HeightRule.ATLEAST },
        children: [new TableCell({
          width: { size: CONTENT_W, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill: p.col },
          margins: { top: 950, bottom: 650, left: 680, right: 680 },
          children: [
            new Paragraph({
              spacing: { after: 160 },
              children: [new TextRun({ text: p.num.split('').join(' '), bold: true, size: 20, color: 'FFFFFF', font: LABEL })]
            }),
            new Paragraph({
              spacing: { after: 120 },
              children: [new TextRun({ text: p.big, bold: true, size: 170, color: 'FFFFFF', font: SERIF })]
            }),
            new Paragraph({
              spacing: { after: 120 },
              children: [new TextRun({ text: p.title, bold: true, size: 54, color: 'FFFFFF', font: SERIF })]
            }),
            new Paragraph({
              spacing: { after: 600 },
              children: [new TextRun({ text: p.sub, italics: true, size: 26, color: 'F2E9E4', font: SERIF })]
            }),
            new Paragraph({
              border: { top: { style: BorderStyle.SINGLE, size: 6, color: 'FFFFFF' } },
              spacing: { before: 100, after: 180 },
              children: [new TextRun({ text: 'D A N S   C E T T E   P A R T I E', bold: true, size: 14, color: 'FFFFFF', font: LABEL })]
            }),
            ...chapterLines,
          ]
        })]
      })]
    }),
    new Paragraph({ children: [new PageBreak()] }),
  ];
}

// ---------- couverture ----------
function coverChildren() {
  return [
    new Paragraph({ spacing: { before: 220 }, children: [] }),
    new Paragraph({ alignment: AlignmentType.CENTER, children: [imgAuto('pics/logo_btlplane.png', 150)] }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 290 },
      children: [new TextRun({ text: 'Sales', bold: true, size: 104, color: NAVY, font: SERIF })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 40 },
      children: [new TextRun({ text: 'Playbook', bold: true, size: 104, color: TEAL, font: SERIF })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 260 },
      children: [new TextRun({ text: 'Le guide de référence du commercial Planet Aura', size: 26, color: INK, font: SERIF })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 170 },
      children: [new TextRun({ text: 'Faire voyager chaque colis dans les règles, intact, à temps, partout dans le monde.', italics: true, size: 23, color: GRAY, font: SERIF })]
    }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 230 }, children: [imgAuto('pics/photo_cover.png', 185)] }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 300 },
      children: [new TextRun({ text: 'COMMISSIONNAIRE DE TRANSPORT  \u00b7  CHAMPAGNES, VINS & SPIRITUEUX', bold: true, size: 16, color: TEALD })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 110 },
      children: [new TextRun({ text: 'R\u00c9SERV\u00c9 \u00c0 L\u2019\u00c9QUIPE COMMERCIALE & MARKETING  \u00b7  CONFIDENTIEL', bold: true, size: 16, color: NAVY })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 110 },
      children: [new TextRun({ text: 'SARL Planet Aura  \u00b7  185 avenue de Roquecourbe, 81100 Castres  \u00b7  www.planet-aura.com', size: 15, color: GRAY })]
    }),
    new Paragraph({ alignment: AlignmentType.CENTER, spacing: { before: 160 }, children: [imgAuto('pics/logo_euridis.png', 120)] }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 110 },
      children: [new TextRun({ text: 'R\u00e9dig\u00e9 par Emma Soares Britschgy  \u00b7  Mast\u00e8re Marketing & Digital Business, promotion 547 (2024-2027)', size: 15, color: INK })]
    }),
    new Paragraph({
      alignment: AlignmentType.CENTER, spacing: { before: 110 },
      children: [new TextRun({ text: 'Tutrice entreprise : Floriane F\u00e9vrier  \u00b7  Suivi acad\u00e9mique : Thibaut du Cleuziou  \u00b7  Euridis Business School', size: 15, color: GRAY })]
    }),
  ];
}

// ---------- sommaire ----------
let tocPages = {};
try { tocPages = JSON.parse(fs.readFileSync(path.join(__dirname, 'toc-pages-emma.json'), 'utf8')); } catch (e) {}
// folio de reprise par partie : l'ouverture de partie ne compte pas dans la numérotation
let partStarts = {};
try { partStarts = JSON.parse(fs.readFileSync(path.join(__dirname, 'part-starts-emma.json'), 'utf8')); } catch (e) {}

function tocChildren() {
  const COL_W = Math.floor((CONTENT_W - 420) / 2);
  const paras = [];
  paras.push(new Paragraph({
    spacing: { before: 120, after: 20 },
    children: [new TextRun({ text: 'N A V I G A T I O N', bold: true, size: 14, color: TEAL, font: LABEL })]
  }));
  paras.push(new Paragraph({
    spacing: { after: 70 },
    children: [new Bookmark({ id: 'sommaire', children: [new TextRun({ text: 'Sommaire', bold: true, size: 52, color: NAVY, font: SERIF })] })]
  }));
  paras.push(new Paragraph({
    spacing: { after: 260 },
    children: [new TextRun({ text: 'Consultation par besoin ou par étape du cycle commercial - chaque entrée est cliquable. Les annexes regroupent les outils réutilisables séparément.', italics: true, size: 18, color: GRAY, font: SERIF })]
  }));

  // libellés raccourcis au sommaire pour éviter le folio orphelin en 2e ligne
  const TOC_SHORT = {
    'Séquences de prospection multicanales et scripts': 'Séquences multicanales et scripts',
    'Organisation et outils de la fonction commerciale': 'Organisation et outils commerciaux',
    'Chiffres officiels, hiérarchie de preuve et sources': 'Chiffres officiels et sources',
  };
  const entry = (h, labelColor) => {
    const page = tocPages[h.key] !== undefined ? String(tocPages[h.key]) : '0';
    const m = h.text.match(/^(Annexe\s+)?([0-9A-U]{1,2})\s*[—–-]\s*(.*)$/);
    if (m && TOC_SHORT[m[3]]) m[3] = TOC_SHORT[m[3]];
    const kids = [];
    if (m) {
      kids.push(new TextRun({ text: m[2], bold: true, size: 17, color: labelColor, font: LABEL }));
      kids.push(new TextRun({ text: '   ' + m[3], size: 18, color: INK }));
      // socle à maîtriser avant J+30 (marqué d'un point plein)
      if (['00', '02', '04', '06', '08', '13', 'B'].includes(m[2])) kids.push(new TextRun({ text: '  \u25cf', size: 13, color: labelColor }));
    } else {
      kids.push(new TextRun({ text: h.text, bold: true, size: 18, color: INK }));
    }
    return new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: COL_W }],
      spacing: { before: 54, after: 20 },
      border: { bottom: { style: BorderStyle.SINGLE, size: 2, color: 'E4EDF0' } },
      children: [
        new InternalHyperlink({ anchor: h.key, children: kids }),
        new TextRun({ text: '\t', size: 18 }),
        new TextRun({ text: page, bold: true, size: 17, color: labelColor, font: LABEL }),
      ]
    });
  };

  const level1 = tocRegistry.filter(h => h.level === 1);
  let lastPart = null;
  level1.forEach(h => {
    const part = PART_OF_UNIT[h.id];
    if (part && part !== lastPart) {
      lastPart = part;
      paras.push(new Paragraph({
        keepNext: true,
        spacing: { before: 300, after: 60 },
        children: [
          new TextRun({ text: part.big, bold: true, size: 44, color: part.col, font: SERIF }),
          new TextRun({ text: '  ' + part.title.toUpperCase(), bold: true, size: 15, color: DEEP_OF[part.col] || TEALD, font: LABEL }),
        ]
      }));
    }
    paras.push(entry(h, part ? (DEEP_OF[part.col] || TEAL) : DEEP_OF[TEAL]));
  });

  // légende : le code visuel du document (couleurs de partie, encadrés, glossaire)
  const sw = (color) => new TextRun({ text: '■ ', size: 16, color });
  const lgTitle = (t) => new Paragraph({
    keepNext: true, spacing: { before: 150, after: 40 },
    children: [new TextRun({ text: t, bold: true, size: 13, color: TEALD, font: LABEL })]
  });
  const lgLine = (kids) => new Paragraph({ spacing: { after: 30 }, children: kids });
  paras.push(new Paragraph({
    keepNext: true,
    border: { top: { style: BorderStyle.SINGLE, size: 6, color: TEAL } },
    spacing: { before: 380, after: 50 },
    children: [new TextRun({ text: 'C O M M E N T   L I R E   C E   D O C U M E N T', bold: true, size: 14, color: DEEP_OF[TEAL], font: LABEL })]
  }));
  paras.push(lgTitle('UNE COULEUR PAR PARTIE'));
  paras.push(lgLine([
    sw(TEAL), new TextRun({ text: 'Analyser   ', size: 16, color: INK }),
    sw(PBORDEAUX), new TextRun({ text: 'Cibler   ', size: 16, color: INK }),
    sw(POCRE), new TextRun({ text: 'Vendre   ', size: 16, color: INK }),
    sw(NAVY), new TextRun({ text: 'Piloter   ', size: 16, color: INK }),
    sw(ORANGE), new TextRun({ text: 'Annexes', size: 16, color: INK }),
  ]));
  paras.push(lgLine([new TextRun({ text: 'L’onglet de bordure, les titres, les tableaux et les encadrés de repère de chaque chapitre suivent la couleur de sa partie.', size: 15, color: GRAY })]));
  paras.push(lgLine([new TextRun({ text: '\u25cf  ', bold: true, size: 15, color: DEEP_OF[TEAL] }), new TextRun({ text: 'Le socle : six chapitres et la fiche r\u00e9flexe (annexe B) \u00e0 ma\u00eetriser avant J+30 (certification en annexe S) - le reste se consulte quand le cas se pr\u00e9sente.', size: 15, color: GRAY })]));
  paras.push(lgTitle('LES ENCADRÉS'));
  paras.push(lgLine([sw(TEAL), new TextRun({ text: 'REPÈRE', bold: true, size: 15, color: DEEP_OF[TEAL] }), new TextRun({ text: ' - contexte et points d’appui (teinte de la partie)', size: 15, color: GRAY })]));
  paras.push(lgLine([sw(ORANGE), new TextRun({ text: 'LE CONSEIL / LE POINT DE VIGILANCE', bold: true, size: 15, color: ORANGE }), new TextRun({ text: ' - bonnes pratiques et pièges', size: 15, color: GRAY })]));
  paras.push(lgLine([sw(RED), new TextRun({ text: 'INTERDIT', bold: true, size: 15, color: RED }), new TextRun({ text: ' - règles bloquantes, sans exception', size: 15, color: GRAY })]));
  paras.push(lgLine([sw(GREEN), new TextRun({ text: 'CE QUI FONCTIONNE', bold: true, size: 15, color: GREEN }), new TextRun({ text: ' - pratiques éprouvées sur le terrain', size: 15, color: GRAY })]));
  paras.push(lgLine([sw(NAVY), new TextRun({ text: 'À RETENIR', bold: true, size: 15, color: NAVY }), new TextRun({ text: ' - la synthèse à mémoriser, en fin de chapitre', size: 15, color: GRAY })]));
  paras.push(lgTitle('GLOSSAIRE ET NAVIGATION'));
  paras.push(lgLine([
    new TextRun({ text: 'Les termes comme ', size: 15, color: GRAY }),
    new TextRun({ text: 'adhérent', size: 15, color: DEEP_OF[TEAL], underline: { type: UnderlineType.DOTTED, color: DEEP_OF[TEAL] } }),
    new TextRun({ text: ' renvoient à leur définition au glossaire (annexe T) - à leur première apparition dans chaque chapitre, cliquables en version numérique. Toutes les entrées de ce sommaire et des sous-sommaires « DANS CE CHAPITRE » sont également cliquables.', size: 15, color: GRAY }),
  ]));
  return paras;
}

// ---------- en-têtes / pieds ----------
const TAB_IMG = { 0: 'tab-p1', 1: 'tab-p2', 2: 'tab-p3', 3: 'tab-p4', 4: 'tab-ann' };
// fond pleine page (image flottante derrière le contenu, bord à bord)
const BG_OF = { [TEAL]: 'bg-teal', [PBORDEAUX]: 'bg-bordeaux', [POCRE]: 'bg-ocre', [NAVY]: 'bg-navy', [ORANGE]: 'bg-orange' };
function bgRun(name) {
  const data = fs.readFileSync(path.join(A, `diagrams/${name}.png`));
  const PX = 9525;
  return new ImageRun({
    type: 'png', data,
    transformation: { width: 794, height: 1123 },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 0 },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: 0 },
      wrap: { type: TextWrappingType.NONE },
      behindDocument: true,
    }
  });
}

// logotype secondaire blanc, posé en bas à gauche des pages d'ouverture de partie
function openerLogoRun() {
  const data = fs.readFileSync(path.join(A, 'pics/logo_wordmark_nu_white.png'));
  const PX = 9525;
  const w = 128, h = Math.round(324 / 635 * 128);
  return new ImageRun({
    type: 'png', data,
    transformation: { width: w, height: h },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: 66 * PX },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: (1123 - h - 56) * PX },
      wrap: { type: TextWrappingType.NONE },
      behindDocument: false,
    }
  });
}

function sideTabRun(tab) {
  if (!tab) return [];
  const data = fs.readFileSync(path.join(A, `diagrams/${TAB_IMG[tab.idx] || 'tab-ann'}.png`));
  const PX = 9525; // EMU par pixel
  const wPx = 26, hPx = 230;
  const pageWpx = Math.round(PAGE.width / 1440 * 96);
  return [new ImageRun({
    type: 'png', data,
    transformation: { width: wPx, height: hPx },
    floating: {
      horizontalPosition: { relative: HorizontalPositionRelativeFrom.PAGE, offset: (pageWpx - wPx) * PX },
      verticalPosition: { relative: VerticalPositionRelativeFrom.PAGE, offset: (95 + tab.idx * 150) * PX },
      wrap: { type: TextWrappingType.NONE },
      behindDocument: false,
    }
  })];
}
function mkHeader(leftText, tab, bgName) {
  return new Header({
    children: [
      new Paragraph({
        tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
        border: { bottom: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' } },
        spacing: { after: 40 },
        children: [
          ...(bgName ? [bgRun(bgName)] : []),
          ...sideTabRun(tab),
          new TextRun({ text: leftText, bold: true, size: 13, color: tab ? (DEEP_OF[tab.col] || TEALD) : TEALD, font: LABEL }),
          new TextRun({ text: '\t', size: 11 }),
          new TextRun({ text: 'S A L E S   P L A Y B O O K   2 0 2 6   \u00b7   I N T E R N E', size: 11, color: GRAY, font: LABEL }),
          // retour au sommaire depuis chaque page (sauf le sommaire lui-même)
          ...(leftText === 'SOMMAIRE' ? [] : [
            new TextRun({ text: '   \u00b7   ', size: 11, color: GRAY, font: LABEL }),
            new InternalHyperlink({ anchor: 'sommaire', children: [new TextRun({ text: '\u21a9 S O M M A I R E', bold: true, size: 11, color: tab ? (DEEP_OF[tab.col] || TEALD) : TEALD, font: LABEL })] }),
          ]),
        ]
      }),
    ]
  });
}
function mkFooter(tab, noNum = false) {
  // folio en Playfair, dans la couleur pleine de la partie ; pas de folio sur le liminaire
  const col = tab ? tab.col : TEAL;
  return new Footer({
    children: [new Paragraph({
      tabStops: [{ type: TabStopType.RIGHT, position: CONTENT_W }],
      border: { top: { style: BorderStyle.SINGLE, size: 3, color: 'DCE8EC' } },
      spacing: { before: 50 },
      children: [
        new TextRun({ text: 'P L A N E T   A U R A   ·   C O M M I S S I O N N A I R E   D E   T R A N S P O R T   ·   C H A M P A G N E S ,   V I N S   &   S P I R I T U E U X', size: 10, color: GRAY, font: LABEL }),
        new TextRun({ text: '\t', size: 12 }),
        ...(noNum ? [] : [new TextRun({ children: [PageNumber.CURRENT], bold: true, size: 20, color: col, font: LABEL })]),
      ]
    })]
  });
}
const footerP = mkFooter(null);
const footerNoNum = mkFooter(null, true);
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
    const t = u.id === 'avant' ? '# Avant de commencer' : (/^[A-G]$/.test(u.id) ? `# Annexe ${u.id} - (en cours)` : `# ${u.id} - (en cours)`);
    unitMd[u.id] = `${t}\n\n*Unité en cours de rédaction.*\n\n## En attente\n\nContenu à venir.\n`;
    console.log('placeholder:', u.id);
  }
});

// renvois inverses : pour chaque terme du glossaire et chaque annexe, la liste
// des chapitres qui les citent (ancres 'chap'+id posées sur chaque tête de chapitre)
const GLO_BACKREFS = {}; // slug -> [ids d'unités]
const ANNEX_BACKREFS = {}; // lettre d'annexe -> [ids d'unités]
UNITS.filter(u => !['avant', 'T'].includes(u.id)).forEach(u => {
  const md = unitMd[u.id];
  if (GLO_RE) {
    GLO_RE.lastIndex = 0;
    const seen = new Set();
    let mm;
    while ((mm = GLO_RE.exec(md)) !== null) {
      const slug = GLO_SLUG[mm[1]];
      if (slug && !seen.has(slug)) { seen.add(slug); (GLO_BACKREFS[slug] = GLO_BACKREFS[slug] || []).push(u.id); }
    }
  }
  const seenAx = new Set();
  let ax; const AXRE = /annexes?\s+([A-U])(?![A-Za-z])/g;
  while ((ax = AXRE.exec(md)) !== null) {
    if (ax[1] !== u.id && !seenAx.has(ax[1])) { seenAx.add(ax[1]); (ANNEX_BACKREFS[ax[1]] = ANNEX_BACKREFS[ax[1]] || []).push(u.id); }
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
  headers: { default: mkHeader('AVANT DE COMMENCER') }, footers: { default: footerNoNum },
  children: (() => {
    // remerciements + confidentialité en présentation « lettre » aérée,
    // certitudes + mot d'accueil restent compacts (une page chacun)
    const cIx = avantPre.indexOf('## Les certitudes');
    const pre1 = avantPre.slice(0, cIx).replace(/^#\s+.*$/m, '# Remerciements & confidentialité');
    const pre2 = avantPre.slice(cIx);
    return [
      ...convertBody(pre1, { id: 'avantpre' }, { noMiniToc: true, noToc: true, letter: true }),
      ...convertBody(pre2, { id: 'avantpre2' }, { noMiniToc: true, noToc: true, compact: true }),
    ];
  })()
});

// 3. corps converti D'ABORD (pour remplir le registre du sommaire), inséré APRÈS le sommaire
const bodySections = [];
if (avantPost) {
  // la numérotation visible démarre ici, après le sommaire
  bodySections.push({
    properties: { page: { ...pageProps.page, pageNumbers: { start: 1 } } },
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
  const isPartStart = !!PARTS[u.id];
  if (isPartStart) kids.push(...partOpener(PARTS[u.id]));
  kids.push(...convertBody(md, u, { noMiniToc: isAnnex }));
  bodySections.push({
    // la page d'ouverture de partie (bloc de couleur) n'affiche ni en-tête ni folio,
    // mais reste comptée dans la numérotation ; l'onglet de bordure y demeure
    properties: {
      ...pageProps,
      ...(isPartStart ? { titlePage: true } : {}),
      ...(isPartStart && partStarts[u.id] ? { page: { ...pageProps.page, pageNumbers: { start: partStarts[u.id] } } } : {}),
    },
    headers: {
      default: mkHeader(headTxt, tabOf(u.id)),
      ...(isPartStart ? { first: new Header({ children: [new Paragraph({ children: [bgRun(BG_OF[PARTS[u.id].col] || 'bg-teal'), openerLogoRun(), ...sideTabRun(tabOf(u.id))] })] }) } : {}),
    },
    footers: {
      default: mkFooter(tabOf(u.id)),
      ...(isPartStart ? { first: new Footer({ children: [new Paragraph({ children: [] })] }) } : {}),
    },
    children: kids
  });
});

// 4. sommaire (registre complet), puis le corps
sections.push({
  properties: { ...pageProps, column: { count: 2, space: 420, equalWidth: true } },
  headers: { default: mkHeader('SOMMAIRE') }, footers: { default: footerNoNum },
  children: tocChildren()
});
sections.push(...bodySections);

// page de fin : pleine page marine (fond flottant + table pleine hauteur, comme les ouvertures)
sections.push({
  properties: { ...pageProps },
  headers: { default: new Header({ children: [new Paragraph({ children: [bgRun('bg-navy')] })] }) },
  footers: { default: new Footer({ children: [new Paragraph({ children: [] })] }) },
  children: [
    new Table({
      width: { size: CONTENT_W, type: WidthType.DXA },
      columnWidths: [CONTENT_W],
      borders: {
        top: { style: BorderStyle.NONE }, bottom: { style: BorderStyle.NONE },
        left: { style: BorderStyle.NONE }, right: { style: BorderStyle.NONE },
        insideHorizontal: { style: BorderStyle.NONE }, insideVertical: { style: BorderStyle.NONE },
      },
      rows: [new TableRow({
        height: { value: 13800, rule: HeightRule.ATLEAST },
        children: [new TableCell({
          width: { size: CONTENT_W, type: WidthType.DXA },
          shading: { type: ShadingType.CLEAR, fill: NAVY },
          verticalAlign: VerticalAlign.CENTER,
          margins: { top: 400, bottom: 400, left: 500, right: 500 },
          children: [
            new Paragraph({ spacing: { before: 2600 }, children: [] }),
            new Paragraph({ alignment: AlignmentType.CENTER, children: [imgAuto('pics/logo_wordmark_nu_white.png', 165)] }),
            new Paragraph({
              alignment: AlignmentType.CENTER, spacing: { before: 620, after: 160 },
              children: [new TextRun({ text: 'S A L E S   P L A Y B O O K   2 0 2 6', bold: true, size: 20, color: '9EC5CE', font: LABEL })]
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER, spacing: { after: 560 },
              indent: { left: 400, right: 400 },
              children: [new TextRun({ text: '\u00ab On ne vend pas du transport. On rassure des professionnels. \u00bb', italics: true, size: 38, color: 'FFFFFF', font: SERIF })]
            }),
            new Paragraph({
              border: { top: { style: BorderStyle.SINGLE, size: 6, color: '4A7B8E' } },
              alignment: AlignmentType.CENTER, spacing: { before: 220, after: 90 },
              indent: { left: 900, right: 900 },
              children: [new TextRun({ text: 'Document interne et confidentiel - r\u00e9serv\u00e9 \u00e0 l\u2019\u00e9quipe commerciale & marketing Planet Aura', size: 18, color: 'D7E5EA' })]
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER, spacing: { after: 900 },
              children: [new TextRun({ text: 'Retours et corrections : emma@planet-aura.com', size: 18, color: 'D7E5EA' })]
            }),
            new Paragraph({
              alignment: AlignmentType.CENTER,
              children: [new TextRun({ text: 'S A R L   P L A N E T   A U R A   \u00b7   1 8 5   A V E N U E   D E   R O Q U E C O U R B E ,   8 1 1 0 0   C A S T R E S   \u00b7   W W W . P L A N E T - A U R A . C O M', size: 11, color: '9EC5CE', font: LABEL })]
            }),
          ]
        })]
      })]
    }),
  ]
});

const doc = new Document({
  styles: { default: { document: { run: { font: SANS, size: 19, color: INK } } } },
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
  // registre du sommaire pour la passe de pagination (map-toc-emma.py)
  fs.writeFileSync(path.join(__dirname, 'toc-map-emma.json'), JSON.stringify(tocRegistry));
  console.log('OK', buf.length, 'bytes,', tocRegistry.length, 'entrées sommaire');
});
