#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
steps = [("Le client demande un prix","domaine, caviste ou particulier - mail, téléphone ou formulaire du site"),
         ("On récupère les informations","enlèvement, destination, colisage, valeur, incoterm, dates"),
         ("On vérifie les questions clés","pays ouvert ? accises ? documents ? emballage homologué ?"),
         ("On demande un prix transport","transporteurs / partenaires - comparaison des options"),
         ("On envoie le devis au client","devis écrit, périmètre précis, validité datée")]
# Canevas 1210 px CSS affiché à 500 px : police mini 26 px -> >= 8 pt affichés (10,7 x 1210/500 = 25,9).
# Largeurs par colonne mesurées (DejaVu 26 px) pour 3 lignes par chip et des légendes compactes.
colw = [200, 210, 222, 232, 212]
capw = [230, 220, 230, 232, 230]
h = '''<style>
body{width:1210px;padding:16px}
.fx07c .kicker{font-size:26px;letter-spacing:.09em;margin-bottom:6px;line-height:1}
.fx07c .chip{font-size:26px;line-height:1.1;padding:7px 9px;white-space:normal;width:100%}
.fx07c .numin{display:inline-flex;width:31px;height:31px;border-radius:50%;background:var(--orange);color:#fff;font-weight:700;font-size:26px;align-items:center;justify-content:center;margin-right:7px;vertical-align:-7px}
.fx07c .cap{font-size:26px;line-height:1.1;margin-top:5px;max-width:none}
.fx07c .arr{font-size:26px;width:24px;padding:0;display:flex;justify-content:center;margin-top:36px}
</style><div class="fx07c"><div class="kicker">TRAITER UNE DEMANDE DE COTATION - LE PROCESS OFFICIEL 2026</div><div class="row" style="align-items:flex-start">'''
for i,(t,c) in enumerate(steps):
    if i: h += '<div class="arr">→</div>'
    h += (f'<div class="col" style="width:{colw[i]}px">'
          f'<div class="chip teal"><span class="numin">{i+1}</span>{t}</div>'
          f'<div class="cap" style="width:{capw[i]}px">{c}</div></div>')
h += '</div></div>'
shot('d07_cotation', h, width=1210)
