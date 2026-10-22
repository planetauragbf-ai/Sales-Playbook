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
     'relationcommerciale@<wbr>planet-aura.com'),
    ('L&rsquo;EXPLOITATION DÉCIDE', '#8A6A33', '#F8F3E9',
     ['Faisabilité - date d&rsquo;enlèvement garantie, capacité, température',
      'Cotation hors grille (&gt; 120 btls, palette, B2B, pays absent) - devis écrit',
      'Cut-off, suivi, litiges, questions destinations',
      'Gestion des sinistres (gestionnaire dédié)'],
     'contact@<wbr>planet-aura.com &middot; 09 79 11 45 07'),
    ('LA DIRECTION DÉCIDE', '#722F45', '#F6EEF1',
     ['Prix hors grille et remises',
      'Arbitrages tarifaires, comptes stratégiques, risque, contrat',
      'Allégation ou cas client, promesse carbone',
      'Faisabilité, délai, capacité - décision finale',
      'Un seul &laquo; Accountable &raquo; par décision, jamais deux'],
     'direction@planet-aura.com &middot; 06 68 80 71 65'),
]

FLEX = [1.08, 1.0, 1.14]  # largeurs ~proportionnelles au contenu (équilibre la hauteur des 3 cartes)
cards = ''
for i, (head, accent, bg, items, contact) in enumerate(COLS):
    if i:
        cards += ('<div class="arr"><div class="fl">&rarr;</div>'
                  '<div class="es">ESCALADE</div></div>')
    lis = ''.join(f'<li style="--a:{accent}">{it}</li>' for it in items)
    cards += f'''<div class="card" style="background:{bg};border-top-color:{accent};flex:{FLEX[i]}">
      <div class="hd" style="color:{accent}">{head}</div>
      <ul>{lis}</ul>
      <div class="ct" style="border-top-color:{accent}">{contact}</div>
    </div>'''

# Passe 3 lisibilité : canevas resserré à 880 px CSS (affichage 520 px) avec
# polices mini 18,5 px => ~8,3 pt affiché (exigence : >= 10,7 x 880/520 = 18,1 px).
# Les contenus se réorganisent en colonnes plus étroites (plus de retours à la
# ligne) ; plafond de hauteur assoupli : ratio H/L du PNG <= 0,44.
# Libellés ESCALADE toujours à la verticale le long des flèches (texte/couleurs inchangés).
W = 880
html = f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
body{{margin:0;padding:4px 8px;font-family:Inter,Arial,sans-serif;background:#fff;width:{W}px;box-sizing:border-box}}
h1{{font-size:20px;font-weight:800;color:#12475B;margin:0 0 3px;text-align:center}}
.row{{display:flex;align-items:stretch;gap:0}}
.card{{border:1px solid #DCE8EC;border-top:4px solid #20768B;border-radius:8px;
      padding:6px 9px 5px;box-sizing:border-box;display:flex;flex-direction:column}}
.hd{{font-size:19px;font-weight:800;letter-spacing:.2px;margin-bottom:3px;line-height:1.1}}
ul{{list-style:none;margin:0;padding:0;flex:1}}
li{{font-size:18.5px;color:#3A4A50;line-height:1.1;padding-left:13px;position:relative;margin-bottom:2px}}
li:before{{content:'•';color:var(--a);position:absolute;left:1px;font-weight:700}}
.ct{{font-size:18.5px;font-weight:700;color:#12475B;border-top:1px solid #20768B;padding-top:2px;margin-top:2px;
    line-height:1.1;overflow-wrap:break-word}}
.arr{{display:flex;flex-direction:column;align-items:center;justify-content:center;padding:0 1px;width:30px;box-sizing:border-box}}
.fl{{color:#F66803;font-size:21px;font-weight:800;line-height:1}}
.es{{color:#F66803;font-size:18.5px;font-weight:800;letter-spacing:.5px;margin-top:3px;
    writing-mode:vertical-rl;transform:rotate(180deg)}}
</style></head><body>
<h1>Le circuit d&rsquo;escalade : qui décide quoi</h1>
<div class="row">{cards}</div></body></html>'''

p = f'{HTML}/d03_escalade.html'
open(p, 'w').write(html)
png = f'{OUT}/d03_escalade.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', f'--window-size={W+40},800', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image, ImageChops
im = Image.open(png).convert('RGB')
bg = Image.new('RGB', im.size, 'white')
bb = ImageChops.difference(im, bg).getbbox()
if bb:
    pad = 8
    bb = (max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.size[0], bb[2]+pad), min(im.size[1], bb[3]+pad))
    im = im.crop(bb)
im.save(png)
w, h = im.size
print('d03_escalade:', im.size, 'ratio', round(h/w, 4), 'vs cap', 0.44)
