#!/usr/bin/env python3
# SWOT complet et lisible - remplace image réduite + listes redondantes
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

Q = {
 'forces': ("FORCES", '#20768B', '#EAF3F6', [
   "<b>Commissionnaire de transport</b> : obligation de résultat de bout en bout",
   "Spécialisation 100 % vins, champagnes & spiritueux (température, casse, valeur, accises)",
   "<b>Filiale US licenciée TTB</b> : maîtrise du three-tier system",
   "Plateforme propriétaire <b>Planet'Connect</b> (devis, dossiers, suivi) en développement constant",
   "Assurance casse/perte jusqu'à 20 000 €/envoi - en option (3 %), souscrite 9 fois sur 10",
   "Accès à l'offre décarbonée VELA (option conditionnelle)",
 ]),
 'faiblesses': ("FAIBLESSES", '#722F45', '#F6EEF1', [
   "Notoriété limitée face aux réseaux franchisés",
   "Structure PME : capacité commerciale / marketing à renforcer",
   "Dépendance à des partenaires (transporteurs, représentants fiscaux, IT)",
   "Forte concentration sur quelques grands comptes (matrice ABC : 20/80)",
 ]),
 'opportunites': ("OPPORTUNITÉS", '#2E8B57', '#EDF6F0', [
   "Désintermédiation / vente directe : petits envois à forte valeur",
   "Diversification des destinations (Canada, Asie hors Chine, Amérique latine)",
   "Demande RSE croissante : fret décarboné VELA",
   "Vivier de <b>vignerons indépendants</b> à équiper",
   "Événementiel premium international (salons, concours)",
   "Partenariats avec de grands groupes du secteur",
 ]),
 'menaces': ("MENACES", '#C0392B', '#FAEDEB', [
   "Droits de douane US et antidumping Chine (baisse des volumes)",
   "Volatilité réglementaire (accises, conformité, contrôles)",
   "Recul structurel de la consommation de vin",
   "Pression tarifaire des généralistes (UPS, FedEx, DHL), franchises (MBE) et spécialistes",
   "Hausse des coûts logistiques et de l'énergie",
 ]),
}

def quad(key):
    t, col, bg, items = Q[key]
    lis = ''.join(f'<li>{i}</li>' for i in items)
    return f'''<div class="q" style="background:{bg};border-top-color:{col}">
      <div class="qt" style="color:{col}">{t}</div><ul>{lis}</ul></div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:6px 10px 4px;font-family:Inter,Arial,sans-serif;background:#fff;width:880px}}
.axes{{display:grid;grid-template-columns:26px 1.13fr 0.87fr;grid-template-rows:22px 1fr 1fr;gap:0}}
.ax{{display:flex;align-items:center;justify-content:center;font-size:18.6px;font-weight:700;letter-spacing:2px;color:#5F7078}}
.axv{{writing-mode:vertical-rl;transform:rotate(180deg)}}
.grid2{{display:grid;grid-template-columns:1.13fr 0.87fr;grid-template-rows:1fr 1fr;gap:7px;grid-column:2/4;grid-row:2/4}}
.q{{border-radius:8px;border-top:4px solid;padding:6px 11px 4px}}
.qt{{font-size:20px;font-weight:700;letter-spacing:2px;margin-bottom:2px}}
ul{{margin:0;padding-left:19px}}
li{{font-size:18.6px;color:#3A4A50;line-height:1.15;margin-bottom:2px}}
li:last-child{{margin-bottom:0}}
b{{color:#12475B}}
</style></head><body>
<div class="axes">
  <div></div><div class="ax">A T O U T S</div><div class="ax">R I S Q U E S</div>
  <div class="ax axv">I N T E R N E</div>
  <div class="grid2">
    {quad('forces')}{quad('faiblesses')}{quad('opportunites')}{quad('menaces')}
  </div>
</div>
</body></html>'''

# grille manuelle : interne (forces/faiblesses) en haut, externe (opportunités/menaces) en bas
html = html.replace('<div class="ax axv">I N T E R N E</div>\n  <div class="grid2">',
  '''<div style="display:flex;flex-direction:column;grid-row:2/4"><div class="ax axv" style="flex:1">I N T E R N E</div><div class="ax axv" style="flex:1">E X T E R N E</div></div>
  <div class="grid2">''')

p = f'{HTML}/d01_swot2.html'
open(p, 'w').write(html)
png = f'{OUT}/d01_swot.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=900,1400', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 8))).save(png)
print('d01_swot:', Image.open(png).size)
