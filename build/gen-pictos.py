#!/usr/bin/env python3
# Pictos premium Planet Aura : SVG filaires (charte teal/navy/orange) -> PNG via Chromium
import os, subprocess
from PIL import Image

S = '/tmp/claude-0/-home-user-Sales-Playbook/937d2675-9cdd-54b9-a3ad-2207ab8c8104/scratchpad'
OUT = f'{S}/assets/icons'
HTML = f'{S}/picto-html'
CHROME = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'
os.makedirs(OUT, exist_ok=True); os.makedirs(HTML, exist_ok=True)

TEAL='#1B7F8C'; NAVY='#1B3A4B'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'

def L(paths, color=TEAL, sw=3.2):
    inner=''.join(paths)
    return f'<g fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round">{inner}</g>'

# --- glyphes filaires 48x48 ---
GLYPH = {
 'compass': L(['<circle cx="24" cy="24" r="18"/>','<path d="M31 17 L27 27 L17 31 L21 21 Z" fill="#E87722" stroke="#E87722" stroke-width="1.5"/>']),
 'bolt': f'<path d="M27 6 L14 27 H23 L20 42 L34 20 H25 Z" fill="{ORANGE}" stroke="{ORANGE}" stroke-width="1.5" stroke-linejoin="round"/>',
 'building': L(['<rect x="10" y="8" width="20" height="32" rx="1.5"/>','<path d="M30 20 H38 V40 H30"/>','<path d="M10 40 H40"/>','<path d="M15 14 h4 M21 14 h4 M15 20 h4 M21 20 h4 M15 26 h4 M21 26 h4 M15 32 h4 M21 32 h4"/>','<path d="M33.5 25 h1.5 M33.5 31 h1.5" stroke="#E87722"/>']),
 'globe': L(['<circle cx="24" cy="24" r="17"/>','<ellipse cx="24" cy="24" rx="8" ry="17"/>','<path d="M7.5 19 H40.5 M7.5 29 H40.5"/>','<path d="M35 10 l4 -3" stroke="#E87722"/>']),
 'package': L(['<path d="M24 6 L41 14 V34 L24 42 L7 34 V14 Z"/>','<path d="M7 14 L24 22 L41 14"/>','<path d="M24 22 V42"/>','<path d="M15.5 10 L32.5 18" stroke="#E87722"/>']),
 'euro': f'<text x="24" y="35" font-family="Georgia,serif" font-size="34" font-weight="bold" fill="{TEAL}" text-anchor="middle">€</text><path d="M36 12 l6 -2" stroke="{ORANGE}" stroke-width="3" stroke-linecap="round"/>',
 'target': L(['<circle cx="24" cy="24" r="17"/>','<circle cx="24" cy="24" r="10.5"/>','<circle cx="24" cy="24" r="4" fill="#E87722" stroke="#E87722"/>']),
 'diamond': L(['<path d="M14 8 H34 L42 19 L24 42 L6 19 Z"/>','<path d="M6 19 H42 M14 8 L20 19 L24 42 M34 8 L28 19 L24 42"/>']),
 'flow': L(['<circle cx="10" cy="24" r="5"/>','<circle cx="24" cy="10" r="5"/>','<circle cx="24" cy="38" r="5"/>','<circle cx="39" cy="24" r="5" stroke="#E87722"/>','<path d="M14.5 21.5 L20 13.5 M14.5 26.5 L20 34.5 M28.5 12.5 L35.5 20.5 M28.5 35.5 L35.5 27.5"/>']),
 'phone': L(['<path d="M12 7 C10 7 8 9 8 11 C8 27 21 40 37 40 C39 40 41 38 41 36 V30 L32 27 L29 31 C24 29 19 24 17 19 L21 16 L18 7 Z"/>']),
 'shield': L(['<path d="M24 5 L40 11 V23 C40 33 33 40 24 43 C15 40 8 33 8 23 V11 Z"/>','<path d="M17 23 L22 28 L31 18" stroke="#E87722"/>']),
 'swords': L(['<path d="M10 8 L30 30 M38 8 L18 30"/>','<path d="M27 33 L33 27 M15 33 L21 27"/>','<path d="M9 39 L14 34 M39 39 L34 34" stroke="#E87722" stroke-width="4"/>']),
 'trophy': L(['<path d="M15 8 H33 V18 C33 25 29 29 24 29 C19 29 15 25 15 18 Z"/>','<path d="M15 11 H8 C8 18 11 21 16 22 M33 11 H40 C40 18 37 21 32 22"/>','<path d="M24 29 V34 M17 40 H31 M20 34 H28 L29 40 H19 Z" stroke="#E87722"/>']),
 'loyalty': L(['<path d="M40 24 A16 16 0 1 1 33 11"/>','<path d="M33 5 V11 H39" stroke="#E87722"/>','<path d="M18 24 L23 29 L31 19"/>']),
 'siren': L(['<path d="M14 34 V24 C14 17 18 12 24 12 C30 12 34 17 34 24 V34"/>','<rect x="9" y="34" width="30" height="6" rx="2"/>','<path d="M24 4 V8 M9 10 L12 13 M39 10 L36 13" stroke="#E87722"/>']),
 'scale': L(['<path d="M24 8 V38 M12 12 H36 M16 40 H32"/>','<path d="M12 12 L6 26 H18 Z M36 12 L30 26 H42 Z"/>','<circle cx="24" cy="8" r="2.4" fill="#E87722" stroke="#E87722"/>']),
 'chart': L(['<path d="M8 6 V40 H42"/>','<path d="M14 34 V24 M22 34 V16 M30 34 V20 M38 34 V10" stroke-width="4.5"/>','<path d="M14 20 L22 12 L30 16 L38 6" stroke="#E87722" stroke-width="2.4"/>']),
 'toolbox': L(['<rect x="6" y="16" width="36" height="22" rx="3"/>','<path d="M18 16 V12 C18 10.5 19 10 20.5 10 H27.5 C29 10 30 10.5 30 12 V16"/>','<path d="M6 26 H42 M21 24 H27 V29 H21 Z" stroke="#E87722"/>']),
 'archive': L(['<rect x="6" y="10" width="36" height="8" rx="2"/>','<path d="M9 18 V36 C9 38 10 39 12 39 H36 C38 39 39 38 39 36 V18"/>','<path d="M19 25 H29" stroke="#E87722" stroke-width="4"/>']),
 'sun': L(['<circle cx="24" cy="24" r="8" stroke="#E87722"/>','<path d="M24 6 V11 M24 37 V42 M6 24 H11 M37 24 H42 M11 11 L14.5 14.5 M33.5 33.5 L37 37 M37 11 L33.5 14.5 M14.5 33.5 L11 37" stroke="#E87722"/>']),
 'bottle': L(['<path d="M21 5 H27 V13 C27 16 31 17 31 22 V40 C31 42 30 43 28 43 H20 C18 43 17 42 17 40 V22 C17 17 21 16 21 13 Z"/>','<path d="M17 28 H31" stroke="#E87722"/>']),
 'plane': L(['<path d="M6 27 L42 15 L30 25 L33 40 L28 37 L24 29 L13 32 L10 29 L20 26 Z" fill="#1B7F8C" stroke="#1B7F8C" stroke-width="1.5"/>']),
 'clock': L(['<circle cx="24" cy="24" r="17"/>','<path d="M24 13 V24 L32 29" stroke="#E87722"/>']),
}

def badge(color, glyph):
    return f'<rect x="2" y="2" width="44" height="44" rx="10" fill="{color}"/>{glyph}'

W = '#FFFFFF'
BADGE = {
 'b-info': badge(TEAL, f'<circle cx="24" cy="14.5" r="3" fill="{W}"/><rect x="21" y="21" width="6" height="16" rx="3" fill="{W}"/>'),
 'b-tip': badge(ORANGE, f'<g fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round"><path d="M24 8 C17.5 8 13 13 13 18.5 C13 23 16 25.5 18 28 C19 29.2 19.5 30.5 19.5 32 H28.5 C28.5 30.5 29 29.2 30 28 C32 25.5 35 23 35 18.5 C35 13 30.5 8 24 8 Z"/><path d="M20 37 H28 M22 41 H26"/></g>'),
 'b-warn': badge(ORANGE, f'<path d="M24 9 L41 38 H7 Z" fill="none" stroke="{W}" stroke-width="3.4" stroke-linejoin="round"/><rect x="22.2" y="19" width="3.6" height="10" rx="1.8" fill="{W}"/><circle cx="24" cy="33.2" r="2.2" fill="{W}"/>'),
 'b-no': badge(RED, f'<circle cx="24" cy="24" r="14" fill="none" stroke="{W}" stroke-width="3.6"/><path d="M14.5 14.5 L33.5 33.5" stroke="{W}" stroke-width="3.6" stroke-linecap="round"/>'),
 'b-ok': badge(GREEN, f'<path d="M13 25 L21 33 L35 16" fill="none" stroke="{W}" stroke-width="4.2" stroke-linecap="round" stroke-linejoin="round"/>'),
 'b-pin': badge(DARK, f'<path d="M16 6 H32 V34 L24 27 L16 34 Z" fill="none" stroke="{W}" stroke-width="3.2" stroke-linejoin="round"/>'),
 'b-us': badge(NAVY, f'<text x="24" y="31" font-family="DejaVu Sans" font-size="17" font-weight="bold" fill="{W}" text-anchor="middle">US</text>'),
 'b-ca': badge(RED, f'<text x="24" y="31" font-family="DejaVu Sans" font-size="17" font-weight="bold" fill="{W}" text-anchor="middle">CA</text>'),
}

ICONS = {
 'ch-readme':'compass','ch-00':'bolt','ch-01':'building','ch-02':'globe','ch-03':'package','ch-04':'euro',
 'ch-05':'target','ch-06':'diamond','ch-07':'flow','ch-08':'phone','ch-09':'shield','ch-10':'swords',
 'ch-11':'trophy','ch-12':'loyalty','ch-13':'siren','ch-14':'scale','ch-15':'chart','ch-16':'toolbox','ch-17':'archive',
 'mini-sun':'sun','mini-bottle':'bottle','mini-plane':'plane','mini-package':'package','mini-phone':'phone','mini-clock':'clock',
}

def render(name, inner):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48" width="192" height="192">{inner}</svg>'
    p = f'{HTML}/{name}.html'
    open(p,'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>body{{margin:0;background:transparent}}</style></head><body>{svg}</body></html>')
    png = f'{OUT}/{name}.png'
    subprocess.run([CHROME,'--headless','--no-sandbox','--disable-gpu','--hide-scrollbars','--default-background-color=00000000',
                    f'--screenshot={png}','--window-size=192,192',f'file://{p}'], check=True, capture_output=True)
    im = Image.open(png)
    im.save(png)

for name, g in ICONS.items():
    render(name, GLYPH[g])
for name, inner in BADGE.items():
    render(name, inner)
print('pictos:', len(ICONS)+len(BADGE))
