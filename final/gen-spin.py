#!/usr/bin/env python3
# Trame de l'entretien de découverte SPIN - 35 min, 6 séquences (source : content-emma/12.md)
# Affiché à 520 px dans le document -> UNE SEULE rangée de 6 séquences (ratio H/W <= 0,213),
# canevas ~1070 px CSS, plus petite police 19,5 px (règle assouplie : >= 9,4 x canevas/520,
# le contenu est repris dans le tableau sous le schéma). En-tête sur une seule ligne.
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

# (tag, titre, corps, hot, poids_flex, min_width_px) - poids dosés pour que les titres
# longs (Questions SPIN, Besoin -> solution) tiennent sur 1 ligne et que les corps longs
# restent <= 6 lignes ; min_width pour les titres des cartes courtes (pas de coupure de mot).
STEPS = [
    ('0-3 MIN', 'Cadrer', 'Objectif, agenda, script d&rsquo;ouverture. Sortie : permission de diagnostiquer.', False, 156, 120),
    ('3-8 MIN', 'Contexte', 'Contexte et événement déclencheur. Sortie : le &laquo; pourquoi maintenant &raquo;.', False, 148, 120),
    ('8-20 MIN', 'Questions SPIN', 'Sur un flux réel. Sortie : problème + implication formulés par le prospect.', True, 182, 120),
    ('20-25 MIN', 'Reformulation à trous', 'Sortie : accord sur le diagnostic.', False, 154, 152),
    ('25-30 MIN', 'Besoin &rarr; solution', 'Correspondance avec l&rsquo;offre (chap. 08). Sortie : option pertinente (ou non) identifiée.', False, 206, 120),
    ('30-35 MIN', 'Décision sur la suite', 'Sortie : action + responsable + date.', False, 145, 143),
]

def card_html(step):
    tag, title, body, hot, grow, mw = step
    cls = 'card hot' if hot else 'card'
    return f'''<div class="{cls}" style="flex:{grow} 1 0;min-width:{mw}px">
      <div class="et">{tag}</div>
      <div class="ti">{title}</div>
      <div class="bo">{body}</div>
    </div>'''

cells = ''
for i, step in enumerate(STEPS):
    if i:
        cells += '<div class="fl">&rarr;</div>'
    cells += card_html(step)

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:2px 8px 3px;font-family:Inter,Arial,sans-serif;background:#fff;width:1070px;box-sizing:border-box}}
.hd{{text-align:center;margin:0 0 3px;line-height:1.15;white-space:nowrap}}
.t1{{font-size:21.5px;font-weight:800;color:#12475B}}
.t2{{font-size:19.5px;color:#3A4A50;margin-left:12px}}
.row{{display:flex;align-items:stretch}}
.card{{border:1px solid #DCE8EC;border-top:4px solid #20768B;border-radius:6px;
      background:#fff;padding:3px 5px 4px;box-sizing:border-box}}
.et{{font-size:19.5px;font-weight:800;letter-spacing:0.3px;color:#20768B;margin-bottom:1px;line-height:1.05}}
.ti{{font-size:20px;font-weight:700;color:#12475B;margin-bottom:1px;line-height:1.08}}
.bo{{font-size:19.5px;color:#3A4A50;line-height:1.07}}
.hot{{background:#12475B;border-color:#12475B}}
.hot .et{{color:#9EC5CE}}
.hot .ti{{color:#fff}}
.hot .bo{{color:#D7E5EA}}
.fl{{color:#F66803;font-size:14px;font-weight:800;align-self:center;padding:0 1px;flex:0 0 auto}}
</style></head><body>
<div class="hd"><span class="t1">La trame d&rsquo;un entretien de découverte</span><span class="t2">Le rendez-vous de découverte SPIN - 35 minutes, 6 séquences</span></div>
<div class="row">{cells}</div>
</body></html>'''

p = f'{HTML}/d12_trame.html'
open(p, 'w').write(html)
png = f'{OUT}/d12_trame.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1200,700', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
PAD = 12  # px device (= 6 px CSS) de marge blanche conservée autour du contenu
im.crop((max(0, bb[0] - PAD), 0, min(im.size[0], bb[2] + PAD), min(im.size[1], bb[3] + PAD))).save(png)
w, h = Image.open(png).size
print('d12_trame:', (w, h), 'ratio H/W =', round(h / w, 4))
