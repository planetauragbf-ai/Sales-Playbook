#!/usr/bin/env python3
# Génère les schémas "codés" du playbook (charte Planet Aura) : HTML -> PNG via Chromium headless
import os, subprocess, glob
from PIL import Image

S = '/tmp/claude-0/-home-user-Sales-Playbook/937d2675-9cdd-54b9-a3ad-2207ab8c8104/scratchpad'
OUT = f'{S}/assets/diagrams'
HTML = f'{S}/diag-html'
CHROME = '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell'
os.makedirs(OUT, exist_ok=True); os.makedirs(HTML, exist_ok=True)

CSS = """
<style>
:root{--navy:#1B3A4B;--teal:#1B7F8C;--dark:#12414A;--orange:#E87722;--red:#C0392B;
--green:#2E8B57;--light:#E8F1F4;--cream:#FDF0E4;--gray:#5A6B75;--ink:#2B3A42;}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'DejaVu Sans','Segoe UI',Arial,sans-serif;background:#fff;padding:26px;width:1360px;color:var(--ink)}
.row{display:flex;align-items:center;justify-content:center;gap:0;flex-wrap:nowrap}
.col{display:flex;flex-direction:column;align-items:center}
.chip{background:var(--dark);color:#fff;font-weight:600;font-size:21px;padding:14px 22px;border-radius:10px;white-space:nowrap;text-align:center}
.chip.teal{background:var(--teal)}
.chip.o{background:var(--orange)}
.chip.outline{background:#fff;color:var(--dark);border:2.5px solid var(--teal)}
.arr{color:var(--orange);font-size:30px;font-weight:700;padding:0 12px}
.card{background:#fff;border:1.5px solid #D8E4E9;border-radius:14px;padding:20px 22px;box-shadow:0 3px 10px rgba(18,65,74,.08)}
.card .t{font-size:19px;font-weight:700;letter-spacing:.06em;margin-bottom:12px;padding-bottom:8px;border-bottom:3px solid var(--teal)}
.card ul{list-style:none}
.card li{font-size:17.5px;line-height:1.5;padding-left:20px;position:relative;margin-bottom:6px}
.card li:before{content:'•';color:var(--orange);position:absolute;left:2px;font-weight:700}
.num{min-width:44px;height:44px;border-radius:50%;background:var(--orange);color:#fff;font-weight:700;font-size:21px;display:flex;align-items:center;justify-content:center}
.cap{font-size:15.5px;color:var(--gray);text-align:center;line-height:1.35;margin-top:8px;max-width:190px}
.lbl{font-size:16px;font-weight:700;letter-spacing:.14em;color:var(--teal);text-align:center;margin-bottom:14px}
.pill{padding:9px 18px;border-radius:999px;font-weight:700;font-size:17px;color:#fff}
.kicker{font-size:15px;font-weight:700;letter-spacing:.18em;color:var(--teal);margin-bottom:16px;text-align:center}
</style>"""

def shot(name, html, width=1360):
    p = f'{HTML}/{name}.html'
    open(p, 'w').write(f'<!doctype html><html><head><meta charset="utf-8">{CSS}</head><body>{html}</body></html>')
    png = f'{OUT}/{name}.png'
    subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                    f'--screenshot={png}', f'--window-size={width},1400', '--force-device-scale-factor=2',
                    f'file://{p}'], check=True, capture_output=True)
    im = Image.open(png).convert('RGB')
    from PIL import ImageChops
    bg = Image.new('RGB', im.size, 'white')
    bbox = ImageChops.difference(im, bg).getbbox()
    if bbox:
        pad = 8
        bbox = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(im.size[0], bbox[2]+pad), min(im.size[1], bbox[3]+pad))
        im = im.crop(bbox)
    im.save(png)
    print(name, im.size)

def chain(items, cls='', num=False, caps=None):
    h = '<div class="row">'
    for i, it in enumerate(items):
        if i: h += '<div class="arr">→</div>'
        if num:
            h += f'<div class="col"><div class="num">{i+1}</div><div class="chip {cls}" style="margin-top:10px">{it}</div>'
        else:
            h += f'<div class="col"><div class="chip {cls}">{it}</div>'
        if caps and caps[i]: h += f'<div class="cap">{caps[i]}</div>'
        h += '</div>'
    return h + '</div>'

# 1 — 00 : boucle de méthode
loop = chain(['Cibler','Diagnostiquer','Concevoir','Sécuriser','Prouver','Apprendre'], cls='teal')
loop += """<div style="margin:6px 60px 0"><div style="border:2.5px dashed var(--orange);border-top:none;height:34px;border-radius:0 0 16px 16px"></div>
<div style="text-align:center;color:var(--orange);font-weight:700;font-size:16px;margin-top:6px">↺ &nbsp;la boucle recommence — chaque cycle nourrit le suivant</div></div>"""
shot('d00_loop', loop)

# 2 — 01 : triangle point de vente / Planet Aura / client final
tri = """<div class="row" style="gap:0;align-items:stretch">
<div class="card" style="width:400px"><div class="t" style="color:var(--teal)">LE POINT DE VENTE <span style="font-weight:400;color:var(--gray)">(adhérent)</span></div>
<ul><li>Vend le vin, encaisse le vin</li><li>Saisit la demande sur Planet'Connect</li><li>Emballe dans les cartons homologués</li><li>Remet le colis au transporteur</li></ul></div>
<div class="arr" style="align-self:center">→</div>
<div class="card" style="width:430px;background:var(--dark);border-color:var(--dark)"><div class="t" style="color:#fff;border-color:var(--orange)">PLANET AURA</div>
<ul style="color:#EAF3F5"><li style="color:#EAF3F5">Encaisse le transport (+ taxes DDP, assurance) par CB client ou SEPA magasin</li><li style="color:#EAF3F5">Édite bon de transport + DA amendé, organise l'enlèvement</li><li style="color:#EAF3F5">Gère douane, accises, certificats</li><li style="color:#EAF3F5">Suit l'acheminement, gère les sinistres (remplacement / remboursement)</li><li style="color:#EAF3F5">Fournit les justificatifs d'exportation</li></ul></div>
<div class="arr" style="align-self:center">→</div>
<div class="card" style="width:390px"><div class="t" style="color:var(--orange);border-color:var(--orange)">LE CLIENT FINAL <span style="font-weight:400;color:var(--gray)">(destinataire)</span></div>
<ul><li>Achète au caveau, repart les mains libres</li><li>Reçoit chez lui, taxes déjà payées (DDP)</li></ul></div></div>"""
shot('d01_triangle', tri)

# 3 — 01 : timeline
jalons = [('2019','Fondation','6 mai — par Floriane et Brice'),('2023','Agrandissement','bureau + entrepôt + 1er salarié'),
('janv. 2024','Cap des USA','filiale Planet Aura Inc. (Inwood, NY)'),('mai 2025','Plateforme','Planet’Connect + API en ligne'),
('fin 2025','Force de vente','Adam, premier commercial dédié'),('mai 2026','Plus d’espace','entrepôt de plus de 300 m²'),
('demain','Voilier-cargo VELA','−90 % CO2 transatlantique, nouveaux marchés')]
tl = '<div style="position:relative;padding-top:8px"><div style="position:absolute;top:59px;left:40px;right:40px;height:4px;background:var(--teal);border-radius:2px"></div><div class="row" style="justify-content:space-between;align-items:flex-start">'
for i,(y,t,d) in enumerate(jalons):
    dot = 'var(--orange)' if i in (0, len(jalons)-1) else 'var(--dark)'
    tl += f'''<div class="col" style="width:186px"><div style="font-weight:800;font-size:19px;color:var(--navy)">{y}</div>
    <div style="width:22px;height:22px;border-radius:50%;background:{dot};border:4px solid #fff;box-shadow:0 0 0 3px {dot};margin:14px 0;z-index:1"></div>
    <div style="font-weight:700;font-size:16.5px;color:var(--teal);text-align:center">{t}</div><div class="cap" style="max-width:180px">{d}</div></div>'''
tl += '</div></div>'
shot('d01_timeline', tl)

# 4 — 03 : VELA éligibilité
vela = '<div class="kicker">ÉLIGIBILITÉ VELA — LES 5 VÉRIFICATIONS, DANS L’ORDRE</div>'
vela += chain(['Flux prévisible','Date compatible<br>sailing','Importateur<br>& documents','Économie<br>viable','Preuve carbone<br>qualifiée'], cls='outline', num=True)
vela += '''<div class="row" style="margin-top:26px;gap:14px"><div style="font-weight:700;color:var(--gray);font-size:17px">Verdict :</div>
<div class="pill" style="background:var(--green)">ÉLIGIBLE</div><div class="pill" style="background:var(--orange)">À SÉCURISER</div><div class="pill" style="background:var(--red)">NON-ÉLIGIBLE</div></div>'''
shot('d03_vela', vela)

# 5 — 03 : statuts de suivi
st = '<div class="lbl">GROUPAGE USA</div>'
st += chain(['PICK-UP','FIRST MILES','LISTE DE PROD','TRANSIT','END MILES','LIVRÉ'], cls='teal')
st += '<div class="lbl" style="margin-top:26px">AUTRES FLUX</div>'
st += chain(['PICK-UP','TRANSIT','LIVRÉ'])
shot('d03_status', st)

# 6 — 05 : segments P1/P2/Nurture
seg = ''
for name, col, who, act in [('P1','var(--dark)','Maison premium · Domaine engagé · Importateur','Diagnostic prioritaire / ABM 1:1'),
('P2','var(--teal)','Caviste / e-commerce · Indépendant · Groupe','Motion adaptée au potentiel'),
('NURTURE','var(--gray)','Sans export · Urgence seule · Aucun signal','Contenu, veille ou offre standard')]:
    seg += f'''<div class="row" style="justify-content:flex-start;gap:18px;margin-bottom:14px">
    <div class="pill" style="background:{col};min-width:130px;text-align:center">{name}</div>
    <div style="font-size:18px;width:600px">{who}</div><div class="arr">→</div>
    <div style="font-size:18px;font-weight:600;color:var(--navy)">{act}</div></div>'''
shot('d05_segments', seg)

# 7 — 05 : parcours comité d'achat
com = chain(['Économie','Exécution','Preuve','Adoption','Décision'], cls='teal',
    caps=['coût rendu + marge comparables','OTIF + intégrité produit','données d’impact traçables + wording approuvé','charge interne + satisfaction mesurées','étendre ou ajuster selon volume et valeur'])
shot('d05_comite', com)

# 8 — 05 : carte d'influence
inf = '''<div class="col" style="gap:16px">
<div class="row" style="gap:180px"><div class="chip outline">Direction</div><div class="chip outline">RSE / marketing</div></div>
<div class="row" style="gap:26px"><div class="chip outline">Export</div>
<div class="chip" style="background:var(--orange);font-size:19px;padding:18px 30px">FLUX CLIENT &amp; DÉCISION</div>
<div class="chip outline">Finance / achats</div></div>
<div class="row" style="gap:180px"><div class="chip outline">ADV / logistique</div><div class="chip outline">Importateur US</div></div></div>'''
shot('d08_influence', inf, width=1100)

# 9 — 05 : cycle de vie
cyc = chain(['Prospect','Adhérent','Actif','Fidélisé'], cls='teal')
cyc += '''<div class="row" style="margin-top:10px;gap:10px"><div style="width:340px"></div>
<div class="col"><div style="color:var(--orange);font-size:26px;font-weight:700">↓</div>
<div class="cap" style="max-width:260px;margin-top:2px">9 mois sans expédition</div>
<div class="chip" style="background:var(--red);margin-top:8px">Dormant</div>
<div style="color:var(--orange);font-size:24px;font-weight:700;margin-top:6px">→</div>
<div class="chip o" style="margin-top:6px">Réactivation<br><span style="font-weight:400;font-size:16px">mails auto #70/#71 + appel</span></div></div>
<div style="width:340px"></div></div>'''
shot('d05_cycle', cyc, width=1100)

# 10 — 06 : B2B2C
b2b = """<div class="row" style="align-items:stretch">
<div class="card" style="width:380px;background:var(--dark);border-color:var(--dark)"><div class="t" style="color:#fff;border-color:var(--orange)">PLANET AURA</div>
<div style="color:#EAF3F5;font-size:17.5px;line-height:1.55">Le commissionnaire : organise et garantit le transport de A à Z</div></div>
<div class="arr" style="align-self:center">→</div>
<div class="card" style="width:400px"><div class="t">NOTRE CLIENT PRO <span style="font-weight:400;color:var(--gray)">(l'adhérent)</span></div>
<div style="font-size:17.5px;line-height:1.55">Domaine, maison, caviste, négociant, wine tour…</div></div>
<div class="arr" style="align-self:center">→</div>
<div class="card" style="width:380px"><div class="t" style="color:var(--orange);border-color:var(--orange)">LE DESTINATAIRE</div>
<div style="font-size:17.5px;line-height:1.55">Le client final qui reçoit ses bouteilles, où qu'il soit</div></div></div>"""
shot('d06_b2b2c', b2b)

# 11 — 07 : pipeline 7 étapes
pip = chain(['LEAD','QUALIFIÉ','RDV / DÉMO','PROPOSITION','ADHÉSION<br>SIGNÉE','ACTIVÉ<br><span style="font-weight:400;font-size:15px">(1er envoi)</span>','RÉCURRENT'], cls='teal', num=True)
shot('d07_pipeline', pip)

# 12 — 07 : funnel chiffré
steps = [('300','comptes ciblés'),('150','engagés'),('60','MQL'),('30','SQL'),('20','propositions'),('10','clients')]
fn = '<div class="col" style="gap:8px">'
wmax = 1050
for i,(n,lab) in enumerate(steps):
    w = int(wmax * (0.38 + 0.62 * (len(steps)-1-i)/(len(steps)-1)))
    col = 'var(--teal)' if i < len(steps)-1 else 'var(--orange)'
    fn += f'''<div style="width:{w}px;background:{col};border-radius:8px;color:#fff;display:flex;align-items:center;justify-content:center;gap:12px;padding:11px 0">
    <span style="font-size:22px;font-weight:800">{n}</span><span style="font-size:17px">{lab}</span></div>'''
fn += '</div>'
shot('d07_funnel', fn, width=1150)

# 13 — 10 : mapping 2×2
mp = '''<div style="display:grid;grid-template-columns:230px 1fr 1fr;grid-template-rows:60px 1fr 1fr;gap:0;width:1240px">
<div></div><div style="text-align:center;font-weight:800;letter-spacing:.1em;color:var(--gray);font-size:17px;padding-bottom:10px">GÉNÉRALISTE</div>
<div style="text-align:center;font-weight:800;letter-spacing:.1em;color:var(--teal);font-size:17px;padding-bottom:10px">SPÉCIALISTE VIN</div>
<div style="display:flex;align-items:center;font-weight:800;color:var(--gray);font-size:16.5px;line-height:1.3">OFFRE INTÉGRÉE<br>&amp; BAS-CARBONE</div>
<div class="card" style="border-radius:14px 0 0 0;margin:0;min-height:150px"><div style="font-weight:700;color:var(--navy);margin-bottom:6px">Pionniers de la voile</div><div style="font-size:16.5px;line-height:1.5">TOWT, Grain de Sail<br><span style="color:var(--gray)">(pas spécialistes du vin bout en bout)</span></div></div>
<div class="card" style="border-radius:0 14px 0 0;margin:0;background:var(--dark);border-color:var(--dark)"><div style="font-weight:800;color:#fff;margin-bottom:6px">PLANET AURA</div><div style="font-size:16.5px;line-height:1.5;color:#EAF3F5">Spécialiste vin + intégré<br>+ VELA + filiale US</div></div>
<div style="display:flex;align-items:center;font-weight:800;color:var(--gray);font-size:16.5px">OFFRE STANDARD</div>
<div class="card" style="border-radius:0 0 0 14px;margin:0"><div style="font-weight:700;color:var(--navy);margin-bottom:6px">Généralistes &amp; multi-spécialistes</div><div style="font-size:16.5px;line-height:1.5">UPS, FedEx, DHL, Geodis, CMA CGM</div></div>
<div class="card" style="border-radius:0 0 14px 0;margin:0"><div style="font-weight:700;color:var(--navy);margin-bottom:6px">Spécialistes viticoles</div><div style="font-size:16.5px;line-height:1.5">Viticolis, Vinotrans, Dartess, Eureka Logistique</div></div></div>'''
shot('d10_mapping', mp, width=1300)

# 14 — 13 : parcours sinistre
sin = chain(['Signalement<br><span style="font-weight:400;font-size:15px">≤ 48 h, photos</span>','Dossier S_xxxx<br><span style="font-weight:400;font-size:15px">analyse PA</span>','Recours<br>transporteur','Assurance<br><span style="font-weight:400;font-size:15px">Coste Fermon</span>','Décision client<br><span style="font-weight:400;font-size:15px">remplacement / substitution / remboursement</span>','Clôture'], cls='teal', num=True)
shot('d13_sinistre', sin)

# 15 — 14 : chaîne données RGPD
dat = chain(['SOURCES','HUBSPOT','EXÉCUTION','PILOTAGE'], cls='teal',
    caps=['données entrantes','système de vérité : comptes, deals, consentements','Brevo, Planet’Connect','dashboards'])
shot('d14_data', dat, width=1100)

# 16 — 15 : funnel commercial
f15 = chain(['Leads','Qualifiés','RDV tenus','Propositions','Signatures','Activés','Récurrents'], cls='teal')
shot('d15_funnel', f15)

print('done', len(glob.glob(f'{OUT}/*.png')), 'diagrams')
