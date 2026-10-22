#!/usr/bin/env python3
# Le cycle de vente en bref - 6 cartes "ETAPE N" (design de la maquette PPT)
# Version lisibilité : affiché à 520 px dans le document -> plus petite police
# >= 10,7 x (935/520) = 19,3 px CSS (ici 19,5 px = 8,1 pt affiché).
# Canevas réduit à 935 px (méthode recommandée) au lieu d'agrandir tout le dessin.
# Césures douces (&shy;) sur les mots longs pour tenir en <= 5 lignes par carte
# et respecter le ratio H/L <= 1,4 x l'ancien (392/2804).
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

W = 935  # largeur canevas CSS (PNG = 2x)

STEPS = [
    ('1', 'Lead', 'Salon, inbound, re&shy;com&shy;man&shy;da&shy;tion, pros&shy;pec&shy;tion', False),
    ('2', 'Qualification', 'Volume de clien&shy;tèle étran&shy;gère, des&shy;ti&shy;na&shy;tions, sai&shy;son&shy;na&shy;lité', False),
    ('3', 'Démo', "Simu&shy;la&shy;teur Planet'<wbr>Connect + grille", False),
    ('4', 'Adhésion', 'Signa&shy;ture élec&shy;tro&shy;nique + SEPA éven&shy;tuel + com&shy;mande cartons', False),
    ('5', 'Activation', 'For&shy;ma&shy;tion caveau, 1er envoi sous 30 jours', True),
    ('6', 'Fidélisation', 'Suivi sai&shy;son&shy;nier, upsell stockage / spi&shy;ri&shy;tueux / API', False),
]
cards = ''
for num, title, body, hot in STEPS:
    cls = 'card hot' if hot else 'card'
    cards += f'''<div class="{cls}">
      <div class="et">É T A P E&nbsp;&nbsp;{num}</div>
      <div class="ti">{title}</div>
      <div class="bo">{body}</div>
    </div>'''

html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
body{{margin:0;padding:3px 3px 0;font-family:Inter,Arial,sans-serif;background:#fff;
     width:{W}px;box-sizing:border-box}}
.row{{display:flex;gap:4.5px}}
.card{{flex:1;border:0.75px solid #DCE8EC;border-top:2.6px solid #20768B;border-radius:4px;
      background:#fff;padding:4px 3px;box-sizing:border-box}}
.et{{font-size:19.5px;font-weight:700;letter-spacing:1.1px;color:#20768B;line-height:1.05;margin-bottom:2.2px}}
.ti{{font-size:21.7px;font-weight:700;color:#12475B;line-height:1.08;margin-bottom:2.2px}}
.bo{{font-size:19.5px;color:#3A4A50;line-height:1.17}}
.hot{{background:#12475B;border-color:#12475B}}
.hot .et{{color:#9EC5CE}}
.hot .ti{{color:#fff}}
.hot .bo{{color:#D7E5EA}}
</style></head><body><div class="row">{cards}</div></body></html>'''

p = f'{HTML}/d00_cycle.html'
open(p, 'w').write(html)
png = f'{OUT}/d00_cycle.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', f'--window-size={W},400', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 4))).save(png)
sz = Image.open(png).size
print('d00_cycle:', sz, 'ratio', round(sz[1]/sz[0], 4), 'x ancien', round((sz[1]/sz[0])/(392/2804), 3))
