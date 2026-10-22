#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
NAVY='#1B3A4B'; TEAL='#1B7F8C'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'; LIGHT='#E8F1F4'; GRAY='#5A6B75'

# ---------- 4. Matrice SWOT ----------
def swot_cell(title, items, bg, accent, icon):
    lis=''.join(f'<li style="font-size:16.5px;line-height:1.42;margin-bottom:6px;padding-left:18px;position:relative"><span style="position:absolute;left:0;color:{accent};font-weight:800">•</span>{i}</li>' for i in items)
    return f'''<div style="background:{bg};border:2px solid {accent};border-radius:13px;padding:16px 18px">
      <div style="font-size:17px;font-weight:800;letter-spacing:.1em;color:{accent};margin-bottom:10px">{icon} {title}</div>
      <ul style="list-style:none;color:#2B3A42">{lis}</ul></div>'''
html=f'''<div class="kicker">MATRICE SWOT PLANET AURA - 2026</div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;width:1180px;margin:0 auto">
{swot_cell("FORCES",["Commissionnaire : obligation de résultat de bout en bout","Spécialisation vins, champagnes & spiritueux (casse, valeur, accises)","Filiale US licenciée TTB : maîtrise du three-tier","Plateforme propriétaire Planet'Connect + dashboards","Assurance ad valorem intégrée ; option décarbonée VELA"],"#EFF7F4",GREEN,"S")}
{swot_cell("FAIBLESSES",["Notoriété limitée face aux réseaux franchisés","Structure PME : capacité commerciale/marketing à renforcer","Dépendance à des partenaires (transporteurs, fiscalistes, IT)","Forte concentration sur quelques grands comptes"],"#FDF1EC",ORANGE,"W")}
{swot_cell("OPPORTUNITÉS",["Vente directe : petits envois à forte valeur en croissance","Diversification destinations (Canada, Asie hors Chine, Amérique latine)","Demande RSE croissante : fret décarboné VELA","Vivier de vignerons indépendants ; événementiel premium"],"#EEF4F7",TEAL,"O")}
{swot_cell("MENACES",["Droits de douane US, antidumping Chine, volatilité accises","Recul structurel de la consommation de vin","Pression tarifaire des généralistes et franchises","Hausse des coûts logistiques et de l'énergie"],"#F9EDEC",RED,"T")}
</div>'''
shot('d01_swot', html, width=1280)

# ---------- 5. Golden Circle ----------
# Canevas réduit (~820 px CSS affiché à 390 px) : polices >= 23 px, cercle compact,
# WHY à côté du cercle, HOW / WHAT en seconde rangée (mêmes textes, mêmes couleurs).
gc_css='''<style>
.gc .card{padding:12px 17px}
.gc .card .t{font-size:23px;margin-bottom:6px;padding-bottom:5px}
.gc .card li{font-size:23px;line-height:1.28;margin-bottom:4px;padding-left:20px}
</style>'''
html=gc_css+f'''<div class="gc" style="width:810px;margin:0 auto">
<div class="kicker" style="font-size:23px;line-height:1.25;margin-bottom:8px">LE GOLDEN CIRCLE PLANET AURA - COMMENCER PAR LE POURQUOI</div>
<div class="row" style="gap:14px;align-items:center;justify-content:center">
<svg width="304" height="304" font-family="DejaVu Sans,Arial" style="flex:none">
  <circle cx="152" cy="152" r="146" fill="{LIGHT}" stroke="{TEAL}" stroke-width="2"/>
  <circle cx="152" cy="152" r="109" fill="#BFDDE2" stroke="{TEAL}" stroke-width="2"/>
  <circle cx="152" cy="152" r="72" fill="{DARK}"/>
  <text x="152" y="141" text-anchor="middle" font-size="27" font-weight="800" fill="#fff">WHY</text>
  <text x="152" y="166" text-anchor="middle" font-size="23" fill="#F4C9A8">la raison</text>
  <text x="152" y="190" text-anchor="middle" font-size="23" fill="#F4C9A8">d'être</text>
  <text x="152" y="71" text-anchor="middle" font-size="23" font-weight="800" fill="{DARK}">HOW</text>
  <text x="152" y="34" text-anchor="middle" font-size="23" font-weight="800" fill="{TEAL}">WHAT</text>
</svg>
<div class="card" style="flex:1;border-left:6px solid {DARK}"><div class="t" style="border-color:{DARK}">WHY - POURQUOI</div>
  <div style="font-size:23px;line-height:1.38">Lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu'il soit dans le monde. <b>« Un grand vin mérite un grand voyage. »</b></div></div>
</div>
<div class="row" style="gap:14px;align-items:stretch;margin-top:10px">
<div class="card" style="flex:1;border-left:6px solid {TEAL}"><div class="t">HOW - COMMENT</div>
  <ul><li>Commissionnaire à <b>obligation de résultat</b>, un interlocuteur responsable</li>
  <li>Conformité douane & accises, assurance, aléas gérés proactivement</li>
  <li>Traçabilité numérique via <b>Planet'Connect</b></li></ul></div>
<div class="card" style="flex:1;border-left:6px solid {ORANGE}"><div class="t" style="border-color:{ORANGE}">WHAT - QUOI</div>
  <ul><li>Expédition internationale B2C de vins, champagnes & spiritueux</li>
  <li>~50 destinations en grille, jusqu'à 130 pays sur étude</li>
  <li>USA DDP, stockage & picking, emballage, suivi, SAV - option VELA</li></ul></div>
</div></div>'''
shot('d06_why', html, width=1420)

# ---------- 6. Barres grille USA groupage ----------
# Canevas réduit (~860 px CSS affiché à 430 px) : polices >= 22 px,
# le €/bt passe sur deux lignes sous chaque barre (mêmes textes, mêmes couleurs).
vals=[(1,105),(2,105),(3,105),(6,140),(12,210),(18,285),(24,360),(30,435),(36,510)]
maxv=510; bw=78; gap=16; base=245
bars=''
for i,(bt,p) in enumerate(vals):
    h=int(p/maxv*210); x=10+i*(bw+gap)
    per=p/bt
    perl=f'{per:.0f}' if per==int(per) else f'{per:.1f}'.replace('.',',')
    bars+=f'<rect x="{x}" y="{base-h}" width="{bw}" height="{h}" rx="7" fill="{"#E87722" if bt==12 else TEAL}"/>'
    bars+=f'<text x="{x+bw/2}" y="{base-h-12}" text-anchor="middle" font-size="23" font-weight="800" fill="{NAVY}">{p} €</text>'
    bars+=f'<text x="{x+bw/2}" y="{base+30}" text-anchor="middle" font-size="22" font-weight="700" fill="{NAVY}">{bt} bt</text>'
    bars+=f'<text x="{x+bw/2}" y="{base+58}" text-anchor="middle" font-size="22" fill="{GRAY}">{perl}</text>'
    bars+=f'<text x="{x+bw/2}" y="{base+81}" text-anchor="middle" font-size="22" fill="{GRAY}">€/bt</text>'
html=f'''<div style="width:860px;margin:0 auto">
<div class="kicker" style="font-size:22px;line-height:1.35;margin-bottom:12px">USA GROUPAGE DDP - GRILLE 2026 : LE COÛT PAR BOUTEILLE S'EFFONDRE AVEC LE COLISAGE</div>
<svg width="850" height="{base+92}" font-family="DejaVu Sans,Arial" style="display:block;margin:0 auto">{bars}
<line x1="2" y1="{base}" x2="848" y2="{base}" stroke="{NAVY}" stroke-width="2"/></svg>
<div style="text-align:center;font-size:22px;line-height:1.4;color:{GRAY};margin-top:8px">De 105 € la bouteille seule à <b style="color:{ORANGE}">14,2 € par bouteille</b> sur un envoi de 36 - l'argument qui fait grossir les paniers (délai estimatif 21 j, taxes DDP en sus).</div></div>'''
shot('d04_usabars', html, width=1420)
