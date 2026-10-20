#!/usr/bin/env python3
# NOTRE MÉTIER EN UNE IMAGE - le flux de bout en bout, Planet Aura chef d'orchestre
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

STEPS = [
    ('1', 'Au caveau', "Le client étranger achète son vin, l'adhérent vend l'expédition (order form ou e-shop API)", '#20768B'),
    ('2', 'Préparation', "Carton homologué ISTA 3A, enlèvement chez l'adhérent ou stock à Castres", '#20768B'),
    ('3', 'Documents & douane', "DA / EMCS, certificat CIVC, POA, accises : tout est géré par Planet Aura", '#12475B'),
    ('4', 'Transport', "UPS / FedEx / partenaires - groupage DDP ou direct DAP - option VELA bas-carbone", '#20768B'),
    ('5', 'Livraison', "Chez le client final, taxes payées d'avance (DDP) : zéro surprise à l'arrivée", '#F66803'),
]
cards = ''
for num, t, b, col in STEPS:
    cards += f'''<div class="st"><div class="num" style="background:{col}">{num}</div>
      <div class="ti">{t}</div><div class="bo">{b}</div></div><div class="arr">&#8594;</div>'''
cards = cards.rsplit('<div class="arr">', 1)[0]

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:22px 20px 14px;font-family:Inter,Arial,sans-serif;background:#fff;width:1380px}}
.flow{{display:flex;align-items:stretch;gap:8px}}
.st{{flex:1;background:#F6FAFB;border:1px solid #DCE8EC;border-radius:8px;padding:13px 12px;text-align:center}}
.num{{width:34px;height:34px;border-radius:50%;color:#fff;font-weight:700;font-size:16px;line-height:34px;margin:0 auto 8px}}
.ti{{font-size:14.5px;font-weight:700;color:#12475B;margin-bottom:6px}}
.bo{{font-size:11.3px;color:#3A4A50;line-height:1.4}}
.arr{{align-self:center;color:#9EC5CE;font-size:26px;font-weight:700}}
.brace{{margin-top:14px;border:2px solid #12475B;border-top:none;border-radius:0 0 10px 10px;height:16px}}
.resp{{text-align:center;margin-top:8px}}
.resp .b1{{font-size:13px;font-weight:700;letter-spacing:2px;color:#12475B}}
.resp .b2{{font-size:11.5px;color:#5F7078;margin-top:3px}}
</style></head><body>
<div class="flow">{cards}</div>
<div class="brace"></div>
<div class="resp">
  <div class="b1">PLANET AURA, COMMISSIONNAIRE DE TRANSPORT : UN SEUL RESPONSABLE DE BOUT EN BOUT</div>
  <div class="b2">Obligation de résultat (art. L.132-1 C. com.) : nous agissons en notre nom propre, de l'enlèvement à la livraison - l'adhérent n'a qu'un interlocuteur, le client final n'a aucune démarche.</div>
</div>
</body></html>'''

p = f'{HTML}/d00_metier.html'
open(p, 'w').write(html)
png = f'{OUT}/d00_metier.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1420,330', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 18))).save(png)
print('d00_metier:', Image.open(png).size)
