#!/usr/bin/env python3
import importlib.util, sys
spec = importlib.util.spec_from_file_location('gd', 'gen-diagrams.py')
# reuse CSS + shot only: re-exec header manually
exec(open('gen-diagrams.py').read().split("def chain(")[0])

html = '''
<div class="kicker">SINISTRE - L'ARBRE DÉCISIONNEL (PROCÉDURE 2026)</div>
<div class="col" style="gap:14px">
  <div class="chip" style="font-size:22px">Mail sinistre envoyé - le client choisit la solution</div>
  <div class="arr" style="transform:rotate(90deg)">→</div>
  <div class="row" style="gap:56px;align-items:flex-start">
    <div class="col" style="gap:12px;width:610px">
      <div class="chip teal" style="width:100%">RXP (réexpédition)</div>
      <div class="chip outline" style="width:100%">Le domaine a-t-il encore les bouteilles ?</div>
      <div class="row" style="gap:22px;align-items:flex-start;width:100%">
        <div class="col" style="gap:10px;flex:1">
          <div class="pill" style="background:var(--green)">OUI</div>
          <div class="card" style="width:100%"><ul>
            <li>Enlèvement planifié avec le domaine</li>
            <li>RXP suivie jusqu'à la livraison</li>
            <li>Client + domaine informés à chaque étape</li>
          </ul></div>
        </div>
        <div class="col" style="gap:10px;flex:1">
          <div class="pill" style="background:var(--red)">NON</div>
          <div class="card" style="width:100%"><ul>
            <li>Remplacement équivalent proposé (validé avec le domaine)</li>
            <li>Accepté → enlèvement + réexpédition</li>
            <li>Refusé → bascule en remboursement</li>
          </ul></div>
        </div>
      </div>
      <div class="cap" style="max-width:100%">Facture domaine → Planet Aura : <b>bouteilles uniquement</b> (sans transport ni taxes)</div>
    </div>
    <div class="col" style="gap:12px;width:520px">
      <div class="chip o" style="width:100%">REMBOURSEMENT</div>
      <div class="card" style="width:100%"><ul>
        <li>Vérification des éléments du dossier (valeur déclarée, preuves)</li>
        <li>Instruction avec l'assureur (courtier en copie de tout)</li>
        <li>Client et domaine informés de la décision</li>
      </ul></div>
      <div class="cap" style="max-width:100%">Facture domaine → Planet Aura : <b>bouteilles + transport + taxes</b></div>
    </div>
  </div>
</div>
'''
shot('d13_arbre', html)
