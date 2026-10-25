# Kit de composants pour la refonte du deck de soutenance (format Slides, sous-ensemble fermé).
import re

T = "'Playfair Display', Georgia, serif"
# grands chiffres : Poppins (chiffres alignés) ; Playfair a des chiffres elzéviriens
B = "'Inter', Arial, sans-serif"
L = "'Poppins', Arial, sans-serif"

NUIT, PETROLE, SARC, SARCF, BLEU, BRUME = '#0E3846', '#12475B', '#2D92A8', '#20768B', '#9EC5CE', '#CFE3E8'
FOND, BLANC, ENCRE, GRIS, GRISD, FILET = '#F6F8F7', '#FFFFFF', '#14303B', '#3E5058', '#6A7B82', '#DCE6E9'
BORD, CHAMP, ORF, ORANGE, OR = '#722F45', '#E8D3A6', '#8A6A33', '#C8642A', '#C8A45C'
CLAIR = '#F4F8F9'

PART = {'Analyser': SARCF, 'Cibler': BORD, 'Vendre': ORF, 'Piloter': PETROLE}


def fr(s):
    """Espaces insécables de la typographie française, sur du texte seul."""
    s = re.sub(r' ([:;?!»%€])', '\u00a0\\1', s)
    s = s.replace('« ', '«\u00a0')
    s = re.sub(r'(\d) (\d{3})\b', '\\1\u00a0\\2', s)
    s = re.sub(r'(\d) (\d{3})\b', '\\1\u00a0\\2', s)
    s = re.sub(r'(\d) (?=[^\s\d])', '\\1\u00a0', s)
    s = s.replace("'", '’')
    s = s.replace('New York', 'New\u00a0York').replace('Grain de Sail', 'Grain\u00a0de\u00a0Sail').replace('DB Schenker', 'DB\u00a0Schenker').replace('sous-traitants', 'sous\u2011traitants').replace('Brevo-HubSpot', 'Brevo\u2011HubSpot').replace('PA-FIT', 'PA\u2011FIT').replace('30-60-90', '30\u201160\u201190')
    s = s.replace('n° ', 'n°\u00a0').replace(' →', '\u00a0→').replace('≈ ', '≈\u00a0').replace('~ ', '~\u00a0').replace('≥ ', '≥\u00a0').replace('≤ ', '≤\u00a0').replace('&lt; ', '&lt;\u00a0').replace('&gt; ', '&gt;\u00a0')
    return s


def _frhtml(html):
    # n'agit que sur les nœuds texte (jamais dans les attributs ni dans le SVG, qui n'a pas de texte)
    return re.sub(r'>([^<]+)<', lambda m: '>' + fr(m.group(1)) + '<', html)


def eyebrow(text, color):
    return (f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:4px;'
            f'text-transform:uppercase;color:{color}">{text}</p>')


def tag(text):
    """Marqueur de contribution personnelle (« MON ANALYSE », « MON OUTIL »…)."""
    return (f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:#5A4321;'
            f'background:{CHAMP};padding:4px 18px;border-radius:999px;white-space:nowrap">{text}</p>')


def header(eb, title, color, tcolor=PETROLE, tg=None, tsize=64):
    # la pastille « MON … » est épinglée : le titre reste au même endroit sur toutes les diapos
    t = ''
    if tg:
        w = len(tg) * 19 + 44
        t = (f'<p style="position:absolute;right:128px;top:120px;width:{w}px;text-align:center;font-family:{L};font-size:24px;'
             f'font-weight:600;letter-spacing:2px;color:#5A4321;background:{CHAMP};padding:4px 0px;border-radius:999px">{tg}</p>')
    return (f'{t}<div style="display:flex;flex-direction:column;gap:12px">{eyebrow(eb, color)}'
            f'<h2 style="font-family:{T};font-size:{tsize}px;font-weight:700;line-height:1.1;color:{tcolor}">{title}</h2></div>')


STAT = {
    'CONSTATÉ': f'background:{SARCF};color:#FFFFFF',
    'OBJECTIF': f'background:{BORD};color:#FFFFFF',
    'HYPOTHÈSE': f'background:{ORF};color:#FFFFFF',
    'PROJET': f'border:2px dashed {GRISD};color:{GRISD}',
    'POINT ZÉRO': f'border:2px solid {SARCF};color:{SARCF};background:#FFFFFF',
    'GRILLE 2026': f'background:{PETROLE};color:#FFFFFF',
    'PROPOSÉ': f'border:2px dashed {SARCF};color:{SARCF}',
    'EXTERNE': f'border:2px solid {GRISD};color:{GRISD}',
}


def pill(kind, extra='', label=None):
    return (f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;padding:2px 14px;'
            f'border-radius:999px;white-space:nowrap;align-self:flex-start;{STAT[kind]};{extra}">{label or kind}</p>')


def footer(num, part=None, dark=False, label=None):
    off = '#8FB0BA' if dark else GRISD
    cur = '#FFFFFF' if dark else None
    if label:
        left = f'<span style="color:{cur or PETROLE}">{label}</span>'
    else:
        bits = []
        for p in ['Analyser', 'Cibler', 'Vendre', 'Piloter']:
            bits.append(f'<b><span style="color:{cur or PART[p]}">{p}</span></b>' if p == part else p)
        left = ' · '.join(bits)
    numc = '#FFFFFF' if dark else PETROLE
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1300px;font-family:{L};font-size:24px;'
            f'font-weight:500;letter-spacing:1px;color:{off}">{left}</p>'
            f'<p style="position:absolute;right:128px;bottom:64px;width:120px;text-align:right;font-family:{L};'
            f'font-size:24px;font-weight:600;color:{numc}">{num}</p>')


def section(sid, inner, notes, bg=FOND, color=ENCRE, pad='128px 128px 160px', gap=40,
            justify=None, trans='fade', sect=None):
    js = f';justify-content:{justify}' if justify else ''
    ds = f' data-section="{sect}"' if sect else ''
    html = (f'<section id="{sid}"{ds} data-transition="{trans}" style="background:{bg};color:{color};'
            f'font-family:{B};padding:{pad};display:flex;flex-direction:column;gap:{gap}px{js}">\n'
            f'{inner}\n<aside>{notes}</aside>\n</section>\n')
    return _frhtml(html)


# ---------- graphismes ----------
BOTTLE = ('M15 2 H25 V8 H24 V30 C24 37 36 41 36 54 V113 C36 116.5 33.5 119 30 119 H10 '
          'C6.5 119 4 116.5 4 113 V54 C4 41 16 37 16 30 V8 H15 Z')


def bottles(n_fill, total=24, width=1664, bw=46, bh=138, fill=CHAMP, stroke=BLEU, label=NUIT, op=0.55):
    s = bw / 40.0
    gap = (width - total * bw) / (total - 1)
    parts = []
    for i in range(total):
        x = i * (bw + gap)
        if i < n_fill:
            parts.append(f'<g transform="translate({x:.1f} 0) scale({s:.4f})"><path d="{BOTTLE}" fill="{fill}"/>'
                         f'<rect x="8" y="66" width="24" height="28" rx="2" fill="{label}" opacity="0.22"/></g>')
        else:
            parts.append(f'<g transform="translate({x:.1f} 0) scale({s:.4f})"><path d="{BOTTLE}" fill="none" '
                         f'stroke="{stroke}" stroke-width="{2.4 / s:.2f}" opacity="{op}"/></g>')
    h = int(bh)
    return (f'<svg width="{width}" height="{h}" viewBox="0 0 {width} {h}" '
            f'aria-label="{total} bouteilles, dont {n_fill} pleines">{"".join(parts)}</svg>')


def arrow(w=56, h=32, color=BLEU, sw=4):
    m = h / 2
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="M3 {m} H{w - 6}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" fill="none"/><path d="M{w - 18} 5 L{w - 4} {m} L{w - 18} {h - 5}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def arrow_down(w=32, h=40, color=BLEU, sw=4):
    m = w / 2
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}"><path d="M{m} 3 V{h - 6}" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linecap="round" fill="none"/><path d="M5 {h - 18} L{m} {h - 4} L{w - 5} {h - 18}" '
            f'fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def p(text, size=32, color=None, weight=None, font=None, extra=''):
    st = [f'font-size:{size}px']
    if font == 'T':
        st.append(f'font-family:{T}')
    elif font == 'L':
        st.append(f'font-family:{L}')
    if color:
        st.append(f'color:{color}')
    if weight:
        st.append(f'font-weight:{weight}')
    if extra:
        st.append(extra)
    return f'<p style="{";".join(st)}">{text}</p>'


def label(text, color, size=24, ls=3):
    return (f'<p style="font-family:{L};font-size:{size}px;font-weight:600;letter-spacing:{ls}px;'
            f'text-transform:uppercase;color:{color}">{text}</p>')


def num(value, size, color, weight=700, extra=''):
    """Grand chiffre en Poppins (chiffres alignés), interlettrage resserré."""
    ls = -2 if size >= 80 else (-1 if size >= 44 else 0)
    return (f'<p style="font-family:{L};font-size:{size}px;font-weight:{weight};line-height:1.05;letter-spacing:{ls}px;'
            f'color:{color};{extra}">{value}</p>')
