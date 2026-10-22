#!/usr/bin/env python3
# Organigramme Planet Aura 2026 - charte maquette (HTML -> PNG)
# Canevas 896 px CSS (affiché 520 px dans le document) : min police 18.5 px = 8 pt affiché.
# Passe 2 : hauteur compactée (direction sur 2 lignes, paddings/line-height resserrés,
# largeurs de colonnes rééquilibrées) pour H/W <= 0.478 (1,4 x ratio original 0.341).
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

html = '''<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>
body{margin:0;padding:5px 12px 2px;font-family:Inter,Arial,sans-serif;background:#fff;width:896px;box-sizing:border-box}
.title{font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:23px;color:#12475B;text-align:center;margin:0 0 1px;line-height:1.08}
.sub{font-size:18.5px;color:#5F7078;text-align:center;margin:0 0 2px;letter-spacing:.2px;line-height:1.08}
.dir{background:#12475B;color:#fff;border-radius:8px;padding:3px 10px;text-align:center}
.dir .l1{font-size:18.5px;line-height:1.1}
.dir .l1 .pole{letter-spacing:1.2px;font-weight:700;color:#9EC5CE;margin-right:7px;font-size:18.5px}
.dir .l2{font-size:18.5px;color:#9EC5CE;line-height:1.1;margin-top:1px}
.trunk{width:2px;height:4px;background:#BCCFD6;margin:0 auto}
.bar{height:2px;background:#BCCFD6;margin:0 70px}
.cols{display:flex;gap:5px;justify-content:center}
.col{display:flex;flex-direction:column;align-items:center;min-width:0}
.w1{flex:0 0 240px}.w2{flex:0 0 200px}.w3{flex:0 0 241px}.w4{flex:0 0 176px}
.nw{white-space:nowrap}
.drop{width:2px;height:4px;background:#BCCFD6}
.box{border-radius:8px;padding:4px 5px;width:100%;box-sizing:border-box;border-top:4px solid;background:#F6FAFB;flex:1;min-width:0}
.box .pole{font-size:18.5px;letter-spacing:.1px;font-weight:700;margin-bottom:1px;line-height:1.07;font-family:'Inter Display',Inter,Arial,sans-serif}
.p{font-size:18.5px;color:#3A4A50;margin:0 0 1px;line-height:1.08;hyphens:auto}
.p b{color:#12475B}
.ct{font-size:18.5px;color:#5F7078;margin-top:1px;border-top:1px solid #DCE8EC;padding-top:1px;line-height:1.08;overflow-wrap:anywhere}
.c-com{border-color:#20768B;background:#EAF3F6}.c-com .pole{color:#20768B}
.c-usa{border-color:#F66803;background:#FDF0E4}.c-usa .pole{color:#C2560A}
.c-log{border-color:#722F45;background:#F6EEF1}.c-log .pole{color:#722F45}
.c-adm{border-color:#8A6A33;background:#F8F3E9}.c-adm .pole{color:#8A6A33}
.note{font-size:18.5px;color:#5F7078;text-align:center;margin-top:2px;font-style:italic;line-height:1.1}
</style></head><body>
<div class="title">Organigramme Planet Aura - 2026</div>
<div class="sub">SARL PLANET AURA, CASTRES &nbsp;·&nbsp; FILIALE PLANET AURA INC., NEW YORK</div>
<div class="dir">
  <div class="l1"><span class="pole">DIRECTION</span><b>Floriane Février</b> - Fondatrice &amp; Gérante &nbsp;·&nbsp; Brice de Monplanet - Associé fondateur</div>
  <div class="l2">Arbitrages tarifaires · comptes stratégiques · risque &amp; contrats · décision finale</div>
</div>
<div class="trunk"></div><div class="bar"></div>
<div class="cols">
  <div class="col w1"><div class="drop"></div><div class="box c-com">
    <div class="pole">COMMERCE &amp; DÉVELOPPEMENT</div>
    <div class="p"><b>Adam</b> - Commercial : pipeline, prospection, supports de vente</div>
    <div class="p"><b>Emma</b> - Chargée de projets &amp; développement : partenariats, projets, développement logiciel</div>
    <div class="ct"><span class="nw">relationcommerciale</span><wbr><span class="nw">@planet-aura.com</span></div>
  </div></div>
  <div class="col w2"><div class="drop"></div><div class="box c-usa">
    <div class="pole">PLANET AURA INC. (NEW YORK)</div>
    <div class="p"><b>Alessandro</b> - Business Developer : relais marché USA</div>
    <div class="p">Licences TTB importateur &amp; grossiste · 95 Inip Dr, Inwood (NY)</div>
    <div class="ct"><span class="nw">a.bosruel-marino</span><wbr><span class="nw">@planet-aura.com</span></div>
  </div></div>
  <div class="col w3"><div class="drop"></div><div class="box c-log">
    <div class="pole">LOGISTIQUE / EXPLOITATION</div>
    <div class="p"><b>Vincent</b> - Chef d'entrepôt · <b>Frantz</b> - Cariste</div>
    <div class="p">Juliana · Sarah · Robin · Sofian · Swan</div>
    <div class="p">Enlèvements, suivi, cut-off, litiges, cotations hors grille</div>
    <div class="ct"><span class="nw">contact@planet-aura.com</span> · <span class="nw">09 79 11 45 07</span></div>
  </div></div>
  <div class="col w4"><div class="drop"></div><div class="box c-adm">
    <div class="pole">ADMINISTRATION</div>
    <div class="p"><b>Teddy</b> - Comptabilité &amp; RH</div>
    <div class="p">Facturation, mandats SEPA, impayés, RH</div>
    <div class="ct"><span class="nw">compta</span><wbr><span class="nw">@planet-aura.com</span></div>
  </div></div>
</div>
<div class="note">Équipe resserrée : chaque commercial parle directement à la direction, à l'exploitation et à l'administration - les règles de délégation sont au chapitre 03.</div>
</body></html>'''

p = f'{HTML}/d03_org.html'
open(p, 'w').write(html)
png = f'{OUT}/d03_org.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=896,1400', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 8))).save(png)
print('d03_org:', Image.open(png).size)
