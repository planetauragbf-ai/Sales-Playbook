#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
NAVY='12475B'; TEAL='2D92A8'; ORANGE='F66803'; BORD='722F45'
steps=[('J1','Tâche','Recherche + vue LinkedIn'),('J2','Email 1','Problème + valeur'),('J4','Appel 1','2 questions, 45 s'),
       ('J6','LinkedIn','Invitation contextualisée'),('J8','Email 2','Preuve de méthode'),('J11','Appel 2','+ message vocal'),
       ('J14','Email 3','Break-up : 1 / 2 / 3'),('J18','Sortie','Nurture 45 j ou suppression')]
# Lisibilité : canevas 1660 px CSS affiché à 500 px dans le document -> plus petite police 35.6 px (≈ 8 pt affiché).
# Les 8 touches passent sur 2 rangées de 4 ; largeurs des 3 cartes calées pour des puces sur 2 lignes max.
h='''<style>
.sq{width:1608px}
.sq .kicker{font-size:35.6px;letter-spacing:.04em;line-height:1.12;margin-bottom:6px}
.sq .chip{font-size:35.6px;white-space:normal;line-height:1.2;padding:7px 4px;width:100%}
.sq .pill{font-size:37px;padding:6px 14px}
.sq .cap{font-size:35.6px;line-height:1.15;margin-top:4px}
.sq .arr{font-size:38px;padding:0 6px}
.sq .card{padding:8px;border-radius:12px}
.sq .card .t{font-size:37px;letter-spacing:.03em;line-height:1.12;padding-bottom:4px;margin-bottom:6px;border-bottom-width:4px}
.sq .card li{font-size:35.6px;line-height:1.16;padding-left:17px;margin-bottom:2px}
.sq .card li:before{left:0}
</style><div class="sq">'''
h+='<div class="kicker" style="color:#2D92A8">SÉQUENCE DE PROSPECTION AUTOMATISÉE - BREVO + HUBSPOT<br>(8 TOUCHES / 18 JOURS)</div>'
h+='<div class="row" style="gap:0"><div class="chip" style="background:#12475B">Déclencheur : compte P1/P2 qualifié (PA-FIT ≥ 55) ajouté à la liste de cadence</div></div>'
for r in range(2):
    h+=f'<div class="row" style="margin-top:{8 if r==0 else 4}px;align-items:flex-start">'
    for i,(j,typ,txt) in enumerate(steps[4*r:4*r+4]):
        if i: h+='<div class="arr" style="margin-top:5px;color:#F66803">→</div>'
        col='#2D92A8' if 'mail' in typ.lower() or 'Email' in typ else ('#F66803' if 'Appel' in typ else ('#722F45' if typ=='Sortie' else '#12475B'))
        h+=f'<div class="col" style="width:352px"><div class="pill" style="background:{col}">{j} · {typ}</div><div class="cap" style="max-width:352px">{txt}</div></div>'
    # flèche de continuité rangée 1 -> rangée 2 (masquée en rangée 2 pour garder l'alignement)
    h+=f'<div class="arr" style="margin-top:5px;color:#F66803;{"" if r==0 else "visibility:hidden"}">↓</div></div>'
h+='''<div class="row" style="gap:10px;margin-top:8px;align-items:stretch">
<div class="card" style="width:494px;border-top:5px solid #2E8B57"><div class="t" style="border-color:#2E8B57">RÉPONSE / RAPPEL</div><ul><li>Cadence stoppée automatiquement</li><li>Tâche « répondre &lt; 4 h » ; qualification CAVE</li></ul></div>
<div class="card" style="width:538px;border-top:5px solid #F66803"><div class="t" style="border-color:#F66803">RDV PRIS</div><ul><li>Cadence stoppée ; opportunité créée (étape 3)</li><li>Préparation RDV (checklist annexe B)</li></ul></div>
<div class="card" style="width:550px;border-top:5px solid #C0392B"><div class="t" style="border-color:#C0392B">OPPOSITION</div><ul><li>Cadence stoppée ; liste repoussoir HubSpot → Brevo</li><li>Motif « opposition » enregistré</li></ul></div>
</div></div>'''
shot('d10_sequence', h, width=1660)
