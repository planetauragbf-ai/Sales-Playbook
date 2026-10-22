#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
NAVY='#1B3A4B'; TEAL='#1B7F8C'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'; LIGHT='#E8F1F4'; GRAY='#5A6B75'

# ---------- 3. Carte des intervenants (axe spécialisation -> diversification + badges CA) ----------
# 4e passe : une seule rangée de 4 cartes (H/W <= 0,45), affichage 520 px -> polices >= 25,2 px
F=25.2
def card(title_html, chip_rows, note, accent, badge, badge_bg, w, hl=None):
    rows=''
    for row in chip_rows:
        spans=''.join(
            (f'<span style="display:inline-block;margin:1px;padding:2px 4px;border-radius:8px;background:{ORANGE};color:#fff;font-weight:800;font-size:{F}px;line-height:1.2;border:2px solid {DARK}">{a}</span>'
             if a==hl else
             f'<span style="display:inline-block;margin:1px;padding:2px 4px;border-radius:8px;background:#fff;color:{NAVY};font-weight:400;font-size:{F}px;line-height:1.2;border:1.5px solid #C9D8DE">{a}</span>')
            for a in row)
        rows+=f'<div style="white-space:nowrap;text-align:center;margin:0 -8px">{spans}</div>'
    bdg=f'<span style="display:inline-block;background:{badge_bg};color:#fff;font-weight:800;font-size:{F}px;line-height:1.15;padding:1px 8px;border-radius:7px;margin-right:7px;white-space:nowrap">{badge}</span>'
    return f'''<div style="flex:0 0 auto;width:{w}px;background:#fff;border:2px solid {accent};border-radius:13px;padding:9px 8px;box-shadow:0 2px 6px rgba(18,65,74,.09);display:flex;flex-direction:column">
      <div style="font-size:{F}px;font-weight:800;line-height:1.08;color:{accent};margin:0 -8px 4px;text-align:center;white-space:nowrap">{title_html}</div>
      <div>{rows}</div>
      <div style="font-size:{F}px;color:{GRAY};margin-top:4px;line-height:1.14">{bdg}{note}</div></div>'''

# Ordre le long de l'axe : spécialisation (gauche) -> diversification (droite)
c_special=card("LES FREIGHT<br>FORWARDERS<br>SPÉCIALISÉS VIN",
    [["Planet Aura","Dartess"],["Viticolis","Vinotrans"],["Eureka Logistique","MBE"]],
    "Notre famille : spécialisation forte, proximité, CA plus modeste. C'est ici que se jouent les duels directs.",
    ORANGE,"CA −",GRAY,314,hl="Planet Aura")
c_emerg=card("LES ÉMERGENTS<br>BAS-CARBONE",
    [["VELA","TOWT"],["Grain de Sail"]],
    "Transport maritime à la voile : partenaires ou co-traitants plus que concurrents frontaux - VELA est notre option (chap. 04).",
    GREEN,"CA −",GRAY,280)
c_express=card("LES EXPRESSISTES<br>/ INTÉGRATEURS",
    [["FedEx","UPS","DHL"]],
    "Se diversifient de plus en plus ; puissance mondiale, mais l'alcool B2C reste un angle mort (contrats, douane fine, DDP).",
    NAVY,"CA +",DARK,276)
c_general=card("LES GÉNÉRALISTES «<br>MULTI-SPÉCIALISTES »",
    [["Hillebrand Gori"],["Kuehne+Nagel"],["DB Schenker"],["Dimotrans Group"]],
    "Gros CA, offre très large dont une verticale boissons ; taillés pour les volumes contractuels, pas pour le B2C au colis.",
    RED,"CA +",DARK,324)

W=1206
pill_side=f'background:{TEAL};color:#fff;font-weight:800;font-size:{F}px;line-height:1.12;padding:5px 14px;border-radius:999px;text-align:center;position:relative'
html=f'''<style>body{{width:1226px;padding:12px}}</style>
<div style="width:{W}px;margin:0 auto">
  <div class="kicker" style="font-size:{F}px;letter-spacing:.04em;line-height:1.2;margin-bottom:4px">LA CARTE DES INTERVENANTS DU SECTEUR - CA × SPÉCIALISATION</div>
  <div style="position:relative;display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
    <div style="position:absolute;left:4px;right:4px;top:50%;border-top:2.5px dashed {TEAL}"></div>
    <div style="{pill_side}">SPÉCIALISATION<br>DE L'OFFRE</div>
    <div style="background:{DARK};color:#fff;font-weight:800;font-size:{F}px;padding:7px 16px;border-radius:999px;position:relative">CHIFFRE D'AFFAIRES + / −</div>
    <div style="{pill_side}">DIVERSIFICATION<br>DE L'OFFRE</div>
  </div>
  <div style="display:flex;gap:4px;align-items:stretch">{c_special}{c_emerg}{c_express}{c_general}</div>
</div>'''
shot('d10_carte', html, width=1250)
