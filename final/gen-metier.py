#!/usr/bin/env python3
# NOTRE MÉTIER EN UNE IMAGE - le flux de bout en bout, Planet Aura chef d'orchestre
# Canevas 1408 px CSS affiché à 520 px -> police mini 29 px (29x520/1408 = 10,71 px = 8,03 pt affiché).
# Largeurs de cartes calculées sur les métriques Inter (voir solve_widths.py) pour 5 lignes max par corps.
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

STEPS = [
    ('1', 'Au caveau', "Le client étranger achète son vin, l'adhérent vend l'expé&shy;dition (order form ou e&#8209;shop API)", '#20768B', 286),
    ('2', 'Préparation', "Carton homo&shy;logué ISTA 3A, enlève&shy;ment chez l'adhé&shy;rent ou stock à Castres", '#20768B', 242),
    ('3', 'Documents & douane', "DA / EMCS, certificat CIVC, POA, accises&nbsp;: tout est géré par Planet Aura", '#12475B', 292),
    ('4', 'Transport', "UPS / FedEx / parte&shy;naires - groupage DDP ou direct DAP - option VELA bas-carbone", '#20768B', 271),
    ('5', 'Livraison', "Chez le client final, taxes payées d'avance (DDP)&nbsp;: zéro surprise à l'arrivée", '#F66803', 265),
]
cards = ''
for num, t, b, col, w in STEPS:
    cards += f'''<div class="st" style="flex:0 0 {w}px"><div class="hd"><div class="num" style="background:{col}">{num}</div>
      <div class="ti">{t}</div></div><div class="bo">{b}</div></div>'''

css = '''
*{box-sizing:border-box;margin:0;padding:0}
body{margin:0;padding:2px;font-family:Inter,Arial,sans-serif;background:#fff;width:1408px}
.flow{display:flex;align-items:stretch;gap:12px}
.st{position:relative;background:#F6FAFB;border:1px solid #DCE8EC;border-radius:10px;padding:3px;text-align:center}
.st:not(:last-child):after{content:'\\2192';position:absolute;right:-18px;top:50%;transform:translateY(-50%);
  width:24px;text-align:center;color:#9EC5CE;font-size:29px;font-weight:700;line-height:1}
.hd{display:flex;align-items:center;justify-content:center;gap:5px;margin-bottom:2px}
.num{flex:0 0 31px;width:31px;height:31px;border-radius:50%;color:#fff;font-weight:700;font-size:29px;line-height:31px}
.ti{font-size:29px;font-weight:700;color:#12475B;line-height:1.05;text-wrap:balance}
.bo{font-size:29px;color:#3A4A50;line-height:1.04}
.brace{margin:3px 10px 0;border:2px solid #12475B;border-top:none;border-radius:0 0 10px 10px;height:9px}
.resp{text-align:center;margin-top:3px}
.resp .b1{font-size:29px;font-weight:700;color:#12475B;line-height:1.05}
.resp .b2{font-size:29px;color:#5F7078;margin-top:2px;line-height:1.1;text-wrap:pretty}
'''

html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{css}</style></head><body>
<div class="flow">{cards}</div>
<div class="brace"></div>
<div class="resp">
  <div class="b1">PLANET AURA, COMMISSIONNAIRE DE TRANSPORT&nbsp;: UN SEUL RESPONSABLE DE BOUT EN BOUT</div>
  <div class="b2">Obligation de résultat (art. L.132-1 C. com.)&nbsp;: nous agissons en notre nom propre, de l'enlèvement à la livraison - l'adhérent n'a qu'un interlocuteur, le client final n'a aucune démarche.</div>
</div>
</body></html>'''

p = f'{HTML}/d00_metier.html'
open(p, 'w').write(html)
png = f'{OUT}/d00_metier.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1408,900', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image, ImageChops
im = Image.open(png).convert('RGB')
bg = Image.new('RGB', im.size, 'white')
bbox = ImageChops.difference(im, bg).getbbox()
if bbox:
    pad = 8
    bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(im.size[0], bbox[2]+pad), min(im.size[1], bbox[3]+pad))
    im = im.crop(bbox)
im.save(png)
print('d00_metier:', im.size, 'ratio', round(im.size[1]/im.size[0], 4))
