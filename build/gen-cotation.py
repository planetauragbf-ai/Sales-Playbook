#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
steps = [("Le client demande un prix","domaine, caviste ou particulier - mail, téléphone ou formulaire du site"),
         ("On récupère les informations","enlèvement, destination, colisage, valeur, incoterm, dates"),
         ("On vérifie les questions clés","pays ouvert ? accises ? documents ? emballage homologué ?"),
         ("On demande un prix transport","transporteurs / partenaires - comparaison des options"),
         ("On envoie le devis au client","devis écrit, périmètre précis, validité datée")]
h = '<div class="kicker">TRAITER UNE DEMANDE DE COTATION - LE PROCESS OFFICIEL 2026</div><div class="row" style="align-items:flex-start">'
for i,(t,c) in enumerate(steps):
    if i: h += '<div class="arr" style="margin-top:56px">→</div>'
    h += f'<div class="col" style="width:230px"><div class="num">{i+1}</div><div class="chip teal" style="margin-top:10px;white-space:normal;width:100%;font-size:19px">{t}</div><div class="cap" style="max-width:220px">{c}</div></div>'
h += '</div>'
shot('d07_cotation', h)
