#!/usr/bin/env python3
# Circuit d'escalade : qui décide quoi (source : content-emma/03.md)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

COLS = [
    ('LE COMMERCIAL DÉCIDE SEUL', '#20768B', '#EAF3F6',
     ['Pipeline, prospection et supports de vente',
      'Réalise la proposition de prix (la direction la décide)',
      'Trace toute exception dans le deal (CRM), pas seulement dans un e-mail',
      'Rassure l&rsquo;adhérent sinistré - règle 48 h + photos (sans gérer le dossier)'],
     'relationcommerciale@planet-aura.com'),
    ('L&rsquo;EXPLOITATION DÉCIDE', '#8A6A33', '#F8F3E9',
     ['Faisabilité - date d&rsquo;enlèvement garantie, capacité, température',
      'Cotation hors grille (&gt; 120 btls, palette, B2B, pays absent) - devis écrit',
      'Cut-off, suivi, litiges, questions destinations',
      'Gestion des sinistres (gestionnaire dédié)'],
     'contact@planet-aura.com &middot; 09 79 11 45 07'),
    ('LA DIRECTION DÉCIDE', '#722F45', '#F6EEF1',
     ['Prix hors grille et remises',
      'Arbitrages tarifaires, comptes stratégiques, risque, contrat',
      'Allégation ou cas client, promesse carbone',
      'Faisabilité, délai, capacité - décision finale',
      'Un seul &laquo; Accountable &raquo; par décision, jamais deux'],
     'direction@planet-aura.com &middot; 06 68 80 71 65'),
]

cards = ''
for i, (head, accent, bg, items, contact) in enumerate(COLS):
    if i:
        cards += ('<div class="arr"><div class="fl">&rarr;</div>'
                  '<div class="es">ESCALADE</div></div>')
    lis = ''.join(f'<li style="--a:{accent}">{it}</li>' for it in items)
    cards += f'''<div class="card" style="background:{bg};border-top-color:{accent}">
      <div class="hd" style="color:{accent}">{head}</div>
      <ul>{lis}</ul>
      <div class="ct" style="border-top-color:{accent}">{contact}</div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:18px 16px 16px;font-family:Inter,Arial,sans-serif;background:#fff;width:1368px;box-sizing:border-box}}
h1{{font-size:21px;font-weight:800;color:#12475B;margin:0 0 14px;text-align:center}}
.row{{display:flex;align-items:stretch;gap:0}}
.card{{flex:1;border:1px solid #DCE8EC;border-top:4px solid #20768B;border-radius:8px;
      padding:14px 16px 10px;box-sizing:border-box;display:flex;flex-direction:column}}
.hd{{font-size:14px;font-weight:800;letter-spacing:1.2px;margin-bottom:9px}}
ul{{list-style:none;margin:0;padding:0;flex:1}}
li{{font-size:12.5px;color:#3A4A50;line-height:1.38;padding-left:14px;position:relative;margin-bottom:6px}}
li:before{{content:'•';color:var(--a);position:absolute;left:1px;font-weight:700}}
.ct{{font-size:11.5px;font-weight:700;color:#12475B;border-top:1px solid #20768B;padding-top:7px;margin-top:8px}}
.arr{{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 10px;width:92px;box-sizing:border-box}}
.fl{{color:#F66803;font-size:34px;font-weight:800;line-height:1}}
.es{{color:#F66803;font-size:10px;font-weight:800;letter-spacing:1.6px;margin-top:3px}}
</style></head><body>
<h1>Le circuit d&rsquo;escalade : qui décide quoi</h1>
<div class="row">{cards}</div></body></html>'''

p = f'{HTML}/d03_escalade.html'
open(p, 'w').write(html)
png = f'{OUT}/d03_escalade.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1400,420', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 20))).save(png)
print('d03_escalade:', Image.open(png).size)
