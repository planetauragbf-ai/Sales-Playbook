#!/usr/bin/env python3
# Organigramme Planet Aura 2026 - charte maquette (HTML -> PNG)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

html = '''<!doctype html><html><head><meta charset="utf-8"><style>
body{margin:0;padding:26px;font-family:Inter,Arial,sans-serif;background:#fff;width:1340px}
.title{font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:26px;color:#12475B;text-align:center;margin:0 0 4px}
.sub{font-size:12px;color:#5F7078;text-align:center;margin:0 0 20px;letter-spacing:1px}
.lvl1{display:flex;justify-content:center;margin-bottom:0}
.dir{background:#12475B;color:#fff;border-radius:8px;padding:14px 34px;text-align:center;min-width:420px}
.dir .pole{font-size:11px;letter-spacing:2.5px;font-weight:700;color:#9EC5CE;margin-bottom:6px}
.dir .who{font-size:15px;font-weight:700}
.dir .role{font-size:11.5px;color:#D7E5EA;margin-top:2px}
.trunk{width:2px;height:22px;background:#BCCFD6;margin:0 auto}
.bar{height:2px;background:#BCCFD6;margin:0 90px}
.cols{display:flex;gap:18px;justify-content:center;margin-top:0}
.col{flex:1;display:flex;flex-direction:column;align-items:center}
.drop{width:2px;height:20px;background:#BCCFD6}
.box{border-radius:8px;padding:12px 14px;width:100%;box-sizing:border-box;border-top:5px solid;background:#F6FAFB;min-height:188px}
.box .pole{font-size:10.5px;letter-spacing:1.8px;font-weight:700;margin-bottom:8px}
.p{font-size:12.5px;color:#3A4A50;margin:0 0 6px;line-height:1.35}
.p b{color:#12475B}
.ct{font-size:10.5px;color:#5F7078;margin-top:8px;border-top:1px solid #DCE8EC;padding-top:6px}
.c-com{border-color:#20768B;background:#EAF3F6}.c-com .pole{color:#20768B}
.c-usa{border-color:#F66803;background:#FDF0E4}.c-usa .pole{color:#C2560A}
.c-log{border-color:#722F45;background:#F6EEF1}.c-log .pole{color:#722F45}
.c-adm{border-color:#8A6A33;background:#F8F3E9}.c-adm .pole{color:#8A6A33}
.note{font-size:10.5px;color:#5F7078;text-align:center;margin-top:16px;font-style:italic}
</style></head><body>
<div class="title">Organigramme Planet Aura - 2026</div>
<div class="sub">SARL PLANET AURA, CASTRES &nbsp;·&nbsp; FILIALE PLANET AURA INC., NEW YORK</div>
<div class="lvl1"><div class="dir">
  <div class="pole">D I R E C T I O N</div>
  <div class="who">Floriane Février <span style="font-weight:400">- Fondatrice &amp; Gérante</span></div>
  <div class="role">Brice de Monplanet - Associé fondateur</div>
  <div class="role" style="margin-top:6px;color:#9EC5CE">Arbitrages tarifaires · comptes stratégiques · risque &amp; contrats · décision finale</div>
</div></div>
<div class="trunk"></div><div class="bar"></div>
<div class="cols">
  <div class="col"><div class="drop"></div><div class="box c-com">
    <div class="pole">COMMERCE &amp; DÉVELOPPEMENT</div>
    <div class="p"><b>Adam</b> - Commercial : pipeline, prospection, supports de vente</div>
    <div class="p"><b>Emma</b> - Chargée de projets &amp; développement : partenariats, projets, développement logiciel</div>
    <div class="ct">relationcommerciale@planet-aura.com</div>
  </div></div>
  <div class="col"><div class="drop"></div><div class="box c-usa">
    <div class="pole">PLANET AURA INC. (NEW YORK)</div>
    <div class="p"><b>Alessandro</b> - Business Developer : relais marché USA</div>
    <div class="p">Licences TTB importateur &amp; grossiste · 95 Inip Dr, Inwood (NY)</div>
    <div class="ct">a.bosruel-marino@planet-aura.com</div>
  </div></div>
  <div class="col"><div class="drop"></div><div class="box c-log">
    <div class="pole">LOGISTIQUE / EXPLOITATION</div>
    <div class="p"><b>Vincent</b> - Chef d'entrepôt · <b>Frantz</b> - Cariste</div>
    <div class="p">Juliana · Sarah · Robin · Sofian · Swan</div>
    <div class="p">Enlèvements, suivi, cut-off, litiges, cotations hors grille</div>
    <div class="ct">contact@planet-aura.com · 09 79 11 45 07</div>
  </div></div>
  <div class="col"><div class="drop"></div><div class="box c-adm">
    <div class="pole">ADMINISTRATION</div>
    <div class="p"><b>Teddy</b> - Comptabilité &amp; RH</div>
    <div class="p">Facturation, mandats SEPA, impayés, RH</div>
    <div class="ct">compta@planet-aura.com</div>
  </div></div>
</div>
<div class="note">Équipe resserrée : chaque commercial parle directement à la direction, à l'exploitation et à l'administration - les règles de délégation sont au chapitre 03.</div>
</body></html>'''

p = f'{HTML}/d03_org.html'
open(p, 'w').write(html)
png = f'{OUT}/d03_org.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1392,760', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 30))).save(png)
print('d03_org:', Image.open(png).size)
