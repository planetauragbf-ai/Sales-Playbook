# Corrections visibles issues de la vérification des faits et de la relecture (langue, grille).
# Les espaces insécables sont retirées avant remplacement ; finish.py les remet ensuite.
import os, re
D = os.path.join(os.path.dirname(__file__), '..', 'deck', 'project', 'slides')
P = "font-family:'Poppins', Arial, sans-serif"

def card(color, tc, title, names, line):
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;background:#FFFFFF;border-top:8px solid {color};border-radius:12px;padding:16px 20px">'
            f'<p style="{P};font-size:24px;font-weight:600;line-height:1.2;color:{tc}">{title}</p>'
            f'<p style="font-size:24px;line-height:1.3;font-weight:600;color:#14303B">{names}</p>'
            f'<p style="font-size:24px;line-height:1.3;color:#3E5058">{line}</p></div>')

CARTE = ('<div style="width:1090px;display:flex;flex-direction:column;gap:12px">'
 f'<div style="display:flex;justify-content:space-between;align-items:center"><p style="{P};font-size:24px;font-weight:600;letter-spacing:3px;color:#20768B">← OFFRE SPÉCIALISÉE</p><p style="{P};font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">OFFRE DIVERSIFIÉE →</p></div>'
 '<div style="display:flex;gap:12px">'
 + card('#2D92A8', '#20768B', 'Spécialistes du vin · notre famille', 'Planet Aura, Dartess, Viticolis, Vinotrans', 'Le duel direct : proximité, expertise')
 + card('#C6A15B', '#8A6A33', 'Pionniers de la voile', 'VELA, TOWT, Grain de Sail', 'Partenaires potentiels, plus que concurrents')
 + '</div><div style="display:flex;gap:12px">'
 + card('#12475B', '#12475B', 'Expressistes', 'FedEx, UPS, DHL', 'Nos sous-traitants ; l’alcool aux particuliers reste leur angle mort')
 + card('#722F45', '#722F45', 'Généralistes', 'Hillebrand Gori, Kuehne+Nagel, DB Schenker', 'Taillés pour les volumes contractuels, pas pour le colis')
 + '</div></div>')

R = {
'sommaire': [
 ("Quatre étapes pour transformer un visiteur étranger en client livré", "Quatre étapes pour transformer un caveau en adhérent fidèle"),
 ("Cinq profils, cinq décideurs, validés sur le terrain", "Cinq profils, cinq décideurs, confrontés au réel"),
],
'marche': [
 ("vers les USA en 2025, qui restent le 1er marché", "vers les USA en 2025, qui restent le premier marché"),
 ("Droits de douane US : 15 % en vigueur", "Droits de douane américains : 15 % en vigueur"),
 (", à contre-courant d’un marché à −7,9 %", ", à contre-courant des exports français de vins et spiritueux (−7,9 %)"),
],
'entreprise': [
 ("Brice de Montplanet", "Brice de Monplanet"),
 ("adhérents, 227 actifs sur 9 mois", "adhérents, dont 227 ayant expédié en 9 mois"),
],
'offre': [
 ("48 h en France, 3 à 4 jours en UE", "48 h en France, 3 à 5 jours dans l’UE"),
 (">110 €<", ">110 € HT<"),
 ("certificat Champagne : 15 € HT", "certificat CIVC : 15 € HT"),
],
'concurrence': [
 ("Filiale licenciée TTB à New York", "Filiale à New York, titulaire des licences TTB"),
],
'icp': [],
'personas': [
 ("« Si je bafouille sur un prix pour Boston, la vente est perdue. »", "« Si je bafouille, la vente est perdue, et l’avis Google aussi. »"),
 ("7 contacts · élargi", "7 contacts · confirmé, élargi"),
],
'solutions': [
 ("Simulateur au comptoir, order form, groupage USA en DDP", "Simulateur au comptoir, bon de commande, groupage USA en DDP"),
 ("210 € pour 12 bouteilles, taxes payées d’avance", "210 € de transport pour 12 bouteilles, taxes estimées et payées d’avance"),
 ("Partenariat de recommandation, logistique événementielle", "Partenariat de recommandation"),
 ("Aucun prestataire B2C vers les USA", "Presque aucune solution B2C vers les USA"),
 (">SAVOIR DIRE NON<", ">CE QUE NOUS REFUSONS<"),
],
'processus': [
 ("1er envoi sous 30 jours", "premier envoi sous 30 jours"),
 ("Toute réponse arrête l’automatisation", "Toute réponse arrête la cadence"),
 ("nouveaux adhérents signés en 12 mois, pour 120 visés", "nouveaux adhérents signés en 12 mois pour 120 visés, constaté au 24/09/2026"),
],
'spin': [],
'objections': [],
'ressources': [
 ("One-pager par ICP, landing page", "Fiche par ICP, page web dédiée"),
 ("13 validées et utilisées (dont une battle card par concurrent) · 4 à créer : one-pagers ICP, études de cas, vidéo démo, webinaire",
  "13 validées et utilisées · 4 à créer : fiches par ICP, études de cas, vidéo démo, webinaire · plus une fiche de comparaison par concurrent"),
],
'salesops': [
 ("Les séquences email de prospection", "Les séquences d’e-mails de prospection"),
 ("Certifié J+30, autonome J+60, pilote J+90", "Certifié J+30, autonome J+60, pilote de son activité J+90"),
 ("~30 emails automatiques", "≈ 30 e-mails automatiques"),
 ("Re-signature chaque année en mars-avril", "Signature renouvelée chaque année en mars-avril"),
 ("10 min/jour · 45 min/semaine · 45 min/mois · 90 min/trimestre", "10 min/jour · 45 + 30 min/semaine · 45 min/mois · 90 min/trimestre"),
 ("Hygiène CRM ≥ 95 % chaque lundi", "Complétude du CRM ≥ 95 % chaque lundi"),
],
'kpi': [
 (">BASELINE<", ">POINT ZÉRO<"),
 ("des envois vers les USA : diversifier vers UK, UE, Japon", "des envois vers les USA : diversifier vers Royaume-Uni, UE, Japon"),
 ("des signés activés à J+30, alerte sous 50 %", "des nouveaux adhérents activés à J+30 (alerte sous 50 %)"),
 ("d’adhérents actifs : 1 envoi sur 90 jours", "d’adhérents actifs : au moins 1 envoi en 90 jours"),
 ("de win rate sur les affaires clôturées", "de taux de transformation des affaires clôturées"),
 ("Revue mensuelle de 45 min sur une page · forecast pondéré 20 / 60 / 80 % · première lecture avant/après fin décembre 2026",
  "Tableaux de bord HubSpot et Planet’Connect · revue mensuelle de 45 min avec la direction · prévisionnel pondéré 20 / 60 / 80 % · première lecture fin décembre 2026"),
],
'ouverture': [
 ("Tout dire, rester lisible → <b style=\"color:#F4F8F9\">le réemployable en annexes</b>", "Tout dire, rester lisible → <b style=\"color:#F4F8F9\">les outils réutilisables en annexe</b>"),
 ("· entretiens clients, études de cas, version mobile</p>", "· entretiens clients, études de cas autorisées</p>\n<p style=\"font-size:24px;line-height:1.35;color:#D7E5EA\"><b style=\"color:#F4F8F9\">Ensuite</b> · le même cadre pour diversifier : Royaume-Uni, UE, Japon</p>"),
 ("taxes calculées d’avance, livrées en trois semaines environ. »", "taxes estimées et payées d’avance, livrées en trois semaines environ. »"),
],
}
CDC = {'icp': '8', 'personas': '9', 'solutions': '10', 'processus': '11', 'spin': '11', 'objections': '11', 'ressources': '12', 'salesops': '13', 'kpi': '14'}

for sid, pairs in R.items():
    p = os.path.join(D, f'{sid}.html')
    s = open(p).read().replace(' ', ' ')
    for a, b in pairs:
        assert s.count(a) == 1, (sid, a[:60], s.count(a))
        s = s.replace(a, b)
    if sid in CDC:
        m = re.search(r'(letter-spacing:4px;color:#[0-9A-F]{6}">)([^<]+)(</p>)', s)
        if 'PARTIE' not in m.group(2):
            s = s.replace(m.group(0), m.group(1) + m.group(2) + f' · PARTIE {CDC[sid]}' + m.group(3), 1)
    if sid == 'concurrence':
        old = re.search(r'<div style="display:flex;background:#FFFFFF;border-radius:12px;padding:18px">\s*<img[^>]*>\s*</div>', s).group(0)
        s = s.replace(old, CARTE)
    if sid == 'icp':
        s = re.sub(r'sous 55 = nurture', '35 à 54 = nurture', s)
        assert '35 à 54 = nurture' in s
    if sid == 'objections':
        rows = re.findall(r'<div style="display:flex;align-items:center;gap:18px">.*?</div>', s)
        assert len(rows) == 3
        new = [rows[2].replace('de ventes potentielles par an', 'de ventes potentielles par an'),
               rows[1].replace('de ventes par an, même à 25 %', 'si 25 % seulement se concrétisent'),
               rows[0].replace('>110 €<', '>110 € HT<').replace('de cartons : le seul investissement', 'de cartons : le seul investissement')]
        block = ''.join(rows[i] + '\n' for i in range(3))
        assert block in s
        s = s.replace(block, ''.join(r + '\n' for r in new))
    if sid == 'spin':
        band = ('<div style="display:flex;align-items:center;gap:28px;background:#FFFFFF;border-radius:12px;padding:16px 32px">'
                f'<p style="{P};font-size:24px;font-weight:600;letter-spacing:3px;color:#8A6A33;white-space:nowrap">MAISON DE CHAMPAGNE</p>'
                '<p style="font-size:26px;line-height:1.35;font-style:italic;color:#14303B">I : « Que coûte un colis immobilisé en douane à l’image de la maison ? »</p></div>\n')
        anchor = '<div style="display:flex;align-items:center;gap:32px;background:#F8F3E9'
        assert s.count(anchor) == 1
        s = s.replace(anchor, band + anchor)
        s = s.replace('padding:128px 128px 160px;display:flex;flex-direction:column;gap:36px', 'padding:128px 128px 160px;display:flex;flex-direction:column;gap:24px', 1)
    if sid == 'ressources':
        s = s.replace('padding:13px 16px', 'padding:10px 16px')
        last = '<td style="padding:10px 16px">8 RDV qualifiés par salon</td></tr>'
        assert last in s
        s = s.replace(last, last + '\n<tr style="background:#EAF0F4"><td style="padding:10px 16px;font-weight:700;color:#14303B">Total</td><td style="padding:10px 16px"></td><td style="padding:10px 16px;font-weight:700;color:#14303B">≈ 200 h</td><td style="padding:10px 16px;font-weight:700;color:#14303B">3 000 €</td><td style="padding:10px 16px">Pas de critère, pas d’étape suivante</td></tr>')
    if sid == 'salesops':
        s = s.replace('<p style="font-family:\'Poppins\', Arial, sans-serif;font-size:24px;font-weight:600;color:#E8D3A6">NOUVEAU</p>\n<p style="font-size:26px;font-weight:700;color:#F4F8F9">Rituels d’équipe</p>',
                      '<p style="font-family:\'Poppins\', Arial, sans-serif;font-size:24px;font-weight:600;color:#E8D3A6">PROPOSÉ, À RATIFIER</p>\n<p style="font-size:26px;font-weight:700;color:#F4F8F9">Rituels d’équipe</p>')
        assert 'PROPOSÉ, À RATIFIER' in s
    open(p, 'w').write(s)

# synthèse : tableau reconstruit autour de la problématique (recruter, activer, fidéliser)
p = os.path.join(D, 'synthese.html'); s = open(p).read().replace(' ', ' ')
rows = [('Recruter', '448 prospects non qualifiés sur 710 comptes', '5 ICP, 5 personas, un score PA-FIT sur 100'),
        ('Activer', 'Une activation qui n’était pas mesurée', 'Premier envoi sous 30 jours, objectif ≥ 70 %'),
        ('Fidéliser', '35 adhérents dormants à réveiller', 'Un suivi par tier, un e-mail de réactivation'),
        ('Transmettre', 'Un savoir commercial dans quelques têtes', 'Une méthode écrite, transmise en 90 jours'),
        ('Prouver', 'Des chiffres qui varient d’un support à l’autre', 'Une source unique datée, trois statuts'),
        ('Diversifier', '64,5 % des envois vers les USA, marché à −21 % en 2025', 'Une part USA suivie chaque trimestre')]
T = 'padding:13px 22px'
ALT = ' style="background:#F4F8F9"'
tbl = ("<table style=\"font-family:'Inter', Arial, sans-serif;font-size:26px;color:#3E5058;background:#FFFFFF;border-radius:12px\">\n"
       f'<tr style="background:#12475B"><th style="width:18%;{T};color:#FFFFFF;font-weight:600">Enjeu</th><th style="width:40%;{T};color:#FFFFFF;font-weight:600">Avant</th><th style="width:42%;{T};color:#FFFFFF;font-weight:600">Avec le playbook</th></tr>\n'
       + ''.join(f'<tr{ALT if i % 2 else ""}><td style="{T};font-weight:700;color:#14303B">{a}</td><td style="{T}">{b}</td><td style="{T};color:#14303B">{c}</td></tr>\n' for i, (a, b, c) in enumerate(rows))
       + '</table>')
s = re.sub(r'<table.*?</table>', tbl, s, count=1, flags=re.S)
s = s.replace('>SYNTHÈSE<', '>SYNTHÈSE — RETOUR À LA PROBLÉMATIQUE<')
open(p, 'w').write(s)
print('fix2 ok')
