#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
NAVY='#1B3A4B'; TEAL='#1B7F8C'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'; LIGHT='#E8F1F4'; GRAY='#5A6B75'

# ---------- 3. Carte des intervenants (quadrant) ----------
def cluster(title, actors, note, accent, hl=None, w=330):
    chips=''.join(
        (f'<span style="display:inline-block;margin:3px;padding:7px 13px;border-radius:8px;background:{ORANGE};color:#fff;font-weight:800;font-size:16.5px;border:2.5px solid {DARK}">{a}</span>'
         if a==hl else
         f'<span style="display:inline-block;margin:3px;padding:7px 13px;border-radius:8px;background:#fff;color:{NAVY};font-weight:600;font-size:16px;border:1.5px solid #C9D8DE">{a}</span>')
        for a in actors)
    return f'''<div style="width:{w}px;background:#fff;border:2px solid {accent};border-radius:13px;padding:12px 14px;box-shadow:0 3px 10px rgba(18,65,74,.09)">
      <div style="font-size:15px;font-weight:800;letter-spacing:.08em;color:{accent};margin-bottom:7px">{title}</div>
      <div style="text-align:center">{chips}</div>
      <div style="font-size:13.5px;color:{GRAY};margin-top:7px;line-height:1.35">{note}</div></div>'''

W,H=1460,880
html=f'''<div class="kicker">LA CARTE DES INTERVENANTS DU SECTEUR - CA × SPÉCIALISATION</div>
<div style="position:relative;width:{W}px;height:{H}px;margin:0 auto">
  <div style="position:absolute;left:{W//2}px;top:40px;bottom:40px;width:0;border-left:2.5px dashed {TEAL}"></div>
  <div style="position:absolute;top:{H//2}px;left:30px;right:30px;height:0;border-top:2.5px dashed {TEAL}"></div>
  <div style="position:absolute;left:50%;top:0;transform:translateX(-50%);background:{DARK};color:#fff;font-weight:800;font-size:17px;padding:7px 18px;border-radius:999px">CHIFFRE D'AFFAIRES +</div>
  <div style="position:absolute;left:50%;bottom:0;transform:translateX(-50%);background:{DARK};color:#fff;font-weight:800;font-size:17px;padding:7px 18px;border-radius:999px">CHIFFRE D'AFFAIRES -</div>
  <div style="position:absolute;left:4px;top:{H//2-30}px;background:{TEAL};color:#fff;font-weight:800;font-size:16px;padding:7px 14px;border-radius:999px">SPÉCIALISATION<br>DE L'OFFRE</div>
  <div style="position:absolute;right:4px;top:{H//2-30}px;background:{TEAL};color:#fff;font-weight:800;font-size:16px;padding:7px 14px;border-radius:999px;text-align:right">DIVERSIFICATION<br>DE L'OFFRE</div>
  <div style="position:absolute;left:{W//2-190}px;top:52px">{cluster("LES EXPRESSISTES / INTÉGRATEURS",["FedEx","UPS","DHL"],"Se diversifient de plus en plus ; puissance mondiale, mais l'alcool B2C reste un angle mort (contrats, douane fine, DDP).",NAVY,w=380)}</div>
  <div style="position:absolute;right:195px;top:{H//2-200}px">{cluster("LES GÉNÉRALISTES « MULTI-SPÉCIALISTES »",["Hillebrand Gori","Kuehne+Nagel","DB Schenker","Dimotrans Group"],"Gros CA, offre très large dont une verticale boissons ; taillés pour les volumes contractuels, pas pour le B2C au colis.",RED,w=360)}</div>
  <div style="position:absolute;left:185px;top:{H//2-120}px">{cluster("LES FREIGHT FORWARDERS SPÉCIALISÉS VIN",["Planet Aura","Dartess","Viticolis","Vinotrans","Eureka Logistique","MBE"],"Notre famille : spécialisation forte, proximité, CA plus modeste. C'est ici que se jouent les duels directs.",ORANGE,hl="Planet Aura",w=420)}</div>
  <div style="position:absolute;left:{W//2-420}px;bottom:46px">{cluster("LES ÉMERGENTS BAS-CARBONE",["VELA","TOWT","Grain de Sail"],"Transport maritime à la voile : partenaires ou co-traitants plus que concurrents frontaux - VELA est notre option (chap. 3.8).",GREEN,w=350)}</div>
</div>'''
shot('d10_carte', html, width=1540)
