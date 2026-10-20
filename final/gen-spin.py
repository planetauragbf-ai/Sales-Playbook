#!/usr/bin/env python3
# Trame de l'entretien de découverte SPIN - 35 min, 6 séquences (source : content-emma/12.md)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

STEPS = [
    ('0-3 MIN', 'Cadrer', 'Objectif, agenda, script d&rsquo;ouverture. Sortie : permission de diagnostiquer.', False),
    ('3-8 MIN', 'Contexte', 'Contexte et événement déclencheur. Sortie : le &laquo; pourquoi maintenant &raquo;.', False),
    ('8-20 MIN', 'Questions SPIN', 'Sur un flux réel. Sortie : problème + implication formulés par le prospect.', True),
    ('20-25 MIN', 'Reformulation à trous', 'Sortie : accord sur le diagnostic.', False),
    ('25-30 MIN', 'Besoin &rarr; solution', 'Correspondance avec l&rsquo;offre (chap. 08). Sortie : option pertinente (ou non) identifiée.', False),
    ('30-35 MIN', 'Décision sur la suite', 'Sortie : action + responsable + date.', False),
]
cards = ''
for i, (tag, title, body, hot) in enumerate(STEPS):
    if i:
        cards += '<div class="fl">&rarr;</div>'
    cls = 'card hot' if hot else 'card'
    cards += f'''<div class="{cls}">
      <div class="et">{tag}</div>
      <div class="ti">{title}</div>
      <div class="bo">{body}</div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:18px 16px 16px;font-family:Inter,Arial,sans-serif;background:#fff;width:1368px;box-sizing:border-box}}
h1{{font-size:21px;font-weight:800;color:#12475B;margin:0 0 3px;text-align:center}}
.sub{{font-size:12.5px;color:#3A4A50;text-align:center;margin:0 0 13px}}
.row{{display:flex;align-items:stretch;gap:0}}
.card{{flex:1;border:1px solid #DCE8EC;border-top:4px solid #20768B;border-radius:6px;
      background:#fff;padding:12px 11px;box-sizing:border-box}}
.et{{font-size:10.5px;font-weight:800;letter-spacing:1.8px;color:#20768B;margin-bottom:7px}}
.ti{{font-size:15px;font-weight:700;color:#12475B;margin-bottom:7px;line-height:1.2}}
.bo{{font-size:11.5px;color:#3A4A50;line-height:1.42}}
.hot{{background:#12475B;border-color:#12475B}}
.hot .et{{color:#9EC5CE}}
.hot .ti{{color:#fff}}
.hot .bo{{color:#D7E5EA}}
.fl{{color:#F66803;font-size:24px;font-weight:800;align-self:center;padding:0 5px}}
</style></head><body>
<h1>La trame d&rsquo;un entretien de découverte</h1>
<div class="sub">Le rendez-vous de découverte SPIN - 35 minutes, 6 séquences</div>
<div class="row">{cards}</div></body></html>'''

p = f'{HTML}/d12_trame.html'
open(p, 'w').write(html)
png = f'{OUT}/d12_trame.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1400,360', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 20))).save(png)
print('d12_trame:', Image.open(png).size)
