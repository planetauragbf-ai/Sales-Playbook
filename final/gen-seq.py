#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
NAVY='12475B'; TEAL='2D92A8'; ORANGE='F66803'; BORD='722F45'
steps=[('J1','Tâche','Recherche + vue LinkedIn'),('J2','Email 1','Problème + valeur'),('J4','Appel 1','2 questions, 45 s'),
       ('J6','LinkedIn','Invitation contextualisée'),('J8','Email 2','Preuve de méthode'),('J11','Appel 2','+ message vocal'),
       ('J14','Email 3','Break-up : 1 / 2 / 3'),('J18','Sortie','Nurture 45 j ou suppression')]
h='<div class="kicker" style="color:#2D92A8">SÉQUENCE DE PROSPECTION AUTOMATISÉE - BREVO + HUBSPOT (8 TOUCHES / 18 JOURS)</div>'
h+='<div class="row" style="gap:0;margin-top:6px"><div class="chip" style="background:#12475B">Déclencheur : compte P1/P2 qualifié (PA-FIT ≥ 55) ajouté à la liste de cadence</div></div>'
h+='<div class="row" style="margin-top:18px;align-items:flex-start">'
for i,(j,typ,txt) in enumerate(steps):
    if i: h+='<div class="arr" style="margin-top:34px;color:#F66803">→</div>'
    col='#2D92A8' if 'mail' in typ.lower() or 'Email' in typ else ('#F66803' if 'Appel' in typ else ('#722F45' if typ=='Sortie' else '#12475B'))
    h+=f'<div class="col" style="width:150px"><div class="pill" style="background:{col};font-size:15px">{j} · {typ}</div><div class="cap" style="max-width:150px">{txt}</div></div>'
h+='</div>'
h+='''<div class="row" style="gap:16px;margin-top:26px;align-items:stretch">
<div class="card" style="flex:1;border-top:4px solid #2E8B57"><div class="t" style="border-color:#2E8B57">RÉPONSE / RAPPEL</div><ul><li>Cadence stoppée automatiquement</li><li>Tâche « répondre &lt; 4 h » ; qualification CAVE</li></ul></div>
<div class="card" style="flex:1;border-top:4px solid #F66803"><div class="t" style="border-color:#F66803">RDV PRIS</div><ul><li>Cadence stoppée ; opportunité créée (étape 3)</li><li>Préparation RDV (checklist annexe C)</li></ul></div>
<div class="card" style="flex:1;border-top:4px solid #C0392B"><div class="t" style="border-color:#C0392B">OPPOSITION</div><ul><li>Cadence stoppée ; liste repoussoir HubSpot → Brevo</li><li>Motif « opposition » enregistré</li></ul></div>
</div>'''
shot('d10_sequence', h, width=1500)
