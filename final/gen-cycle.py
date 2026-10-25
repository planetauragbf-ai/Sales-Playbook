#!/usr/bin/env python3
# Le cycle de vente en bref - 6 cartes "ETAPE N" (design de la maquette PPT)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

STEPS = [
    ('1', 'Lead', 'Salon, inbound, recommandation, prospection', False),
    ('2', 'Qualification', 'Volume de clientèle étrangère, destinations, saisonnalité', False),
    ('3', 'Démo', "Simulateur Planet'Connect + grille", False),
    ('4', 'Adhésion', 'Signature électronique + SEPA éventuel + commande cartons', False),
    ('5', 'Activation', 'Formation caveau, 1er envoi sous 30 jours', True),
    ('6', 'Fidélisation', 'Suivi saisonnier, upsell stockage / spiritueux / API', False),
]
cards = ''
for num, title, body, hot in STEPS:
    cls = 'card hot' if hot else 'card'
    cards += f'''<div class="{cls}">
      <div class="et">É T A P E&nbsp;&nbsp;{num}</div>
      <div class="ti">{title}</div>
      <div class="bo">{body}</div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:16px;font-family:Inter,Arial,sans-serif;background:#fff;width:1370px}}
.row{{display:flex;gap:14px}}
.card{{flex:1;border:1px solid #DCE8EC;border-top:4px solid #20768B;border-radius:6px;
      background:#fff;padding:14px 13px;min-height:170px;box-sizing:border-box}}
.et{{font-size:10.5px;font-weight:700;letter-spacing:2px;color:#20768B;margin-bottom:8px}}
.ti{{font-size:16.5px;font-weight:700;color:#12475B;margin-bottom:8px}}
.bo{{font-size:12px;color:#3A4A50;line-height:1.42}}
.hot{{background:#12475B;border-color:#12475B}}
.hot .et{{color:#9EC5CE}}
.hot .ti{{color:#fff}}
.hot .bo{{color:#D7E5EA}}
</style></head><body><div class="row">{cards}</div></body></html>'''

p = f'{HTML}/d00_cycle.html'
open(p, 'w').write(html)
png = f'{OUT}/d00_cycle.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1402,230', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 20))).save(png)
print('d00_cycle:', Image.open(png).size)
