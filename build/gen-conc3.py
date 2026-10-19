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
{swot_cell("OPPORTUNITÉS",["Vente directe : petits envois à forte valeur en croissance","Diversification destinations (Canada, Asie hors Chine)","Demande RSE croissante : fret décarboné VELA","Vivier de vignerons indépendants ; événementiel premium"],"#EEF4F7",TEAL,"O")}
{swot_cell("MENACES",["Droits de douane US, volatilité réglementaire (accises)","Recul structurel de la consommation de vin","Pression tarifaire des généralistes et franchises","Hausse des coûts logistiques et de l'énergie"],"#F9EDEC",RED,"T")}
</div>'''
shot('d01_swot', html, width=1280)

# ---------- 5. Golden Circle ----------
html=f'''<div class="kicker">LE GOLDEN CIRCLE PLANET AURA - COMMENCER PAR LE POURQUOI</div>
<div class="row" style="gap:40px;align-items:center;justify-content:center">
<svg width="520" height="520" font-family="DejaVu Sans,Arial">
  <circle cx="260" cy="260" r="248" fill="{LIGHT}" stroke="{TEAL}" stroke-width="2"/>
  <circle cx="260" cy="260" r="168" fill="#BFDDE2" stroke="{TEAL}" stroke-width="2"/>
  <circle cx="260" cy="260" r="88" fill="{DARK}"/>
  <text x="260" y="252" text-anchor="middle" font-size="30" font-weight="800" fill="#fff">WHY</text>
  <text x="260" y="278" text-anchor="middle" font-size="14.5" fill="#F4C9A8">la raison d'être</text>
  <text x="260" y="140" text-anchor="middle" font-size="26" font-weight="800" fill="{DARK}">HOW</text>
  <text x="260" y="48" text-anchor="middle" font-size="26" font-weight="800" fill="{TEAL}">WHAT</text>
</svg>
<div class="col" style="gap:14px;width:600px;align-items:stretch">
  <div class="card" style="border-left:6px solid {DARK}"><div class="t" style="border-color:{DARK}">WHY - POURQUOI</div>
    <div style="font-size:17.5px;line-height:1.5">Lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu'il soit dans le monde. <b>« Un grand vin mérite un grand voyage. »</b></div></div>
  <div class="card" style="border-left:6px solid {TEAL}"><div class="t">HOW - COMMENT</div>
    <ul><li>Commissionnaire à <b>obligation de résultat</b>, un interlocuteur responsable</li>
    <li>Conformité douane & accises, assurance, aléas gérés proactivement</li>
    <li>Traçabilité numérique via <b>Planet'Connect</b></li></ul></div>
  <div class="card" style="border-left:6px solid {ORANGE}"><div class="t" style="border-color:{ORANGE}">WHAT - QUOI</div>
    <ul><li>Expédition internationale B2C de vins, champagnes & spiritueux</li>
    <li>~50 destinations en grille, jusqu'à 130 pays sur étude</li>
    <li>USA DDP, stockage & picking, emballage, suivi, SAV - option VELA</li></ul></div>
</div></div>'''
shot('d06_why', html, width=1300)

# ---------- 6. Barres grille USA groupage ----------
vals=[(1,105),(2,105),(3,105),(6,140),(12,210),(18,285),(24,360),(30,435),(36,510)]
maxv=510; bw=92; gap=26; H=430; base=360
bars=''
for i,(bt,p) in enumerate(vals):
    h=int(p/maxv*(H-130)); x=40+i*(bw+gap)
    per=p/bt
    perl=f'{per:.0f}' if per==int(per) else f'{per:.1f}'.replace('.',',')
    bars+=f'<rect x="{x}" y="{base-h}" width="{bw}" height="{h}" rx="7" fill="{"#E87722" if bt==12 else TEAL}"/>'
    bars+=f'<text x="{x+bw/2}" y="{base-h-12}" text-anchor="middle" font-size="19" font-weight="800" fill="{NAVY}">{p} €</text>'
    bars+=f'<text x="{x+bw/2}" y="{base+24}" text-anchor="middle" font-size="17.5" font-weight="700" fill="{NAVY}">{bt} bt</text>'
    bars+=f'<text x="{x+bw/2}" y="{base+47}" text-anchor="middle" font-size="14.5" fill="{GRAY}">{perl} €/bt</text>'
html=f'''<div class="kicker">USA GROUPAGE DDP - GRILLE 2026 : LE COÛT PAR BOUTEILLE S'EFFONDRE AVEC LE COLISAGE</div>
<svg width="1120" height="{H}" font-family="DejaVu Sans,Arial">{bars}
<line x1="30" y1="{base}" x2="1105" y2="{base}" stroke="{NAVY}" stroke-width="2"/></svg>
<div style="text-align:center;font-size:16px;color:{GRAY};margin-top:2px">De 105 € la bouteille seule à <b style="color:{ORANGE}">14,2 € par bouteille</b> sur un envoi de 36 - l'argument qui fait grossir les paniers (délai estimatif 21 j, taxes DDP en sus).</div>'''
shot('d04_usabars', html, width=1200)
