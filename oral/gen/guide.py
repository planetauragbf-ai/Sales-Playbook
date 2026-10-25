# Guide de soutenance v3 (HTML imprimé en PDF A4) : essentiel, cas fil rouge, grille de conformité, script minuté,
# transitions, chiffres et définitions, questions du jury, limites, autoévaluation, check-lists.
import os, re, json, html, base64, io
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ORAL = os.path.abspath(os.path.join(HERE, '..'))
DECK = os.environ.get('DECK_DIR', 'deck')
RENDU = os.environ.get('RENDU_DIR', 'rendu')
SL = os.path.join(ORAL, DECK, 'project', 'slides')
OUT = os.path.join(ORAL, 'guide')
deck = json.load(open(os.path.join(ORAL, DECK, 'project', 'deck.json')))
E = html.escape
os.makedirs(OUT, exist_ok=True)


def thumb(sid, w=620):
    im = Image.open(os.path.join(ORAL, RENDU, f'{sid}.png')).convert('RGB')
    im = im.resize((w, int(w * 1080 / 1920)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=84)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()


def slide_info(sid):
    s = open(os.path.join(SL, f'{sid}.html')).read()
    aside = re.search(r'<aside>(.*?)</aside>', s, re.S).group(1).strip()
    body = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
    h = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
    title = html.unescape(re.sub(r'<[^>]+>', '', h.group(1))) if h else None
    m = re.match(r'\[([^\]]*)\]\s*', aside)
    timing = m.group(1) if m else ''
    aside = aside[m.end():] if m else aside
    return title, timing, html.unescape(aside)


main = [s for s in deck['order'] if not s.startswith('b')]
backs = [s for s in deck['order'] if s.startswith('b')]
T = {sid: slide_info(sid)[1] for sid in main}
start = lambda sid: T[sid].split('→')[0].strip()
end = lambda sid: T[sid].split('→')[1].strip()

TITLES = {'cover': 'Couverture', 'accroche': 'Accroche : une scène type', 'conclusion': 'Synthèse, ouverture et retour à Houston'}
PART = {'cover': 'Comprendre', 'accroche': 'Comprendre', 'sommaire': 'Comprendre', 'marche': 'Comprendre', 'entreprise': 'Comprendre', 'offre': 'Comprendre',
        'diagnostic': 'Comprendre', 'icp': 'Cibler · partie 8', 'personas': 'Cibler · partie 9', 'solutions': 'Vendre · partie 10', 'processus': 'Vendre · partie 11',
        'prospecter': 'Vendre · partie 11', 'spin': 'Vendre · partie 11', 'proposer': 'Vendre · partie 11', 'activer': 'Activer · partie 11',
        'ressources': 'Piloter · partie 12', 'salesops': 'Piloter · partie 13', 'onboarding': 'Piloter · partie 13', 'kpi': 'Piloter · partie 14',
        'conclusion': 'Synthèse et ouverture'}
SHOW = {
    'cover': 'Rien : regarder le jury, puis lancer la scène.',
    'accroche': 'Laisser parler les 2 bouteilles pleines sur 24 ; finir sur la question, en bas à gauche.',
    'sommaire': 'Balayer les cinq étapes ; pointer le bandeau « cas fil rouge », puis la légende des étiquettes.',
    'marche': 'Les trois chiffres, puis le bandeau sombre : les cinq contraintes d’une caisse vers les USA.',
    'entreprise': 'La barre 2025 et ×4,7 ; puis la ligne « Commercial · Adam · fin 2025 ».',
    'offre': 'Les barres par bouteille : la dorée, 24 bouteilles à 15 € ; puis le bloc « On se débrouille ».',
    'diagnostic': 'Le quadrant « Fragilités », puis la problématique : la lire lentement, une seule fois.',
    'icp': 'Le score 45, puis la flèche vers 85 : les barres hachurées sont les preuves apportées ensuite.',
    'personas': 'Les trois encadrés « Ce que je lui dis » ; le bloc sombre « Mon étude ».',
    'solutions': 'Suivre la première ligne de gauche à droite, du problème à la preuve.',
    'processus': 'Le bandeau « Mon choix » : la ligne d’arrivée est le premier envoi.',
    'prospecter': 'La question clé du script d’appel, puis l’objet de l’e-mail.',
    'spin': 'Descendre les bulles S, P, I, N ; finir sur le bandeau « Reformuler ».',
    'proposer': 'La grille officielle 2026 : la case encadrée, 24 bouteilles = 360 € ; puis 15 € par bouteille ; le bloc 40 000 €.',
    'activer': 'La frise J0 → J+30 ; puis le bloc « ≥ 70 % ».',
    'ressources': 'Les quatre vignettes de pages réelles ; puis le total 3 000 €.',
    'salesops': 'HubSpot au centre, puis la flèche orange pointillée vers Brevo : à déployer en novembre.',
    'onboarding': 'L’escalier J+30, J+60, J+90 ; puis S8 : premier adhérent activé.',
    'kpi': 'À gauche le constaté (capture réelle), à droite une carte : RDV → proposition.',
    'conclusion': 'Les 24 bouteilles pleines ; finir en regardant le jury, sans regarder l’écran.',
}
SEC = {'marche': 'B10 · B8', 'entreprise': 'B9', 'offre': 'B7 · B3', 'diagnostic': 'B8', 'icp': 'B2 · B16', 'personas': 'B1',
       'solutions': 'B3', 'processus': 'B6 · B12', 'prospecter': 'B4 · B12', 'spin': 'B4', 'proposer': 'B7 · B14', 'activer': 'B11',
       'ressources': 'B13', 'salesops': 'B12 · B9', 'kpi': 'B6', 'conclusion': 'B15 · B5'}

# ---------- banque de questions ----------
J = open(os.path.join(ORAL, 'jury.md')).read()
J = re.sub(r'content-emma/(\d\d)\.md', r'chap. \1', J)
J = re.sub(r'content-emma/([A-Z])\.md', r'annexe \1', J)
J = J.replace('content-emma/avant.md', 'avant-propos').replace('fiches-emma.js', 'annexe A')


def parse_qs(block):
    qs = []
    for m in re.finditer(r'^### (\d+)\. (.*?)\s*_\((.*?)\)_\s*\n(.*?)(?=^### |\Z)', block, re.S | re.M):
        n, q, prob, body = m.groups()
        fields = dict(re.findall(r'^- (Pourquoi|Réponse|Preuve|Diapo de secours|Piège) : (.*)$', body, re.M))
        qs.append((n, q, prob, fields))
    return qs


top = parse_qs(J.split('# Questions pièges')[0])
traps = parse_qs(J.split('# Questions pièges')[1].split('# Questions sur le cas')[0])
cas = parse_qs(J.split('# Questions sur le cas')[1].split('# Diapos de secours')[0])
JB = J.split('# Diapos de secours')[1].split('# Autoévaluation')[0]
REPOND = dict(re.findall(r'^### (B\d+) — .*?\n.*?- Répond à : (.*?)$', JB, re.S | re.M))
auto = J.split('# Autoévaluation')[1]


def qa_card(prefix, n, q, prob, f):
    pc = {'très probable': '#722F45', 'probable': '#8A6A33', 'possible': '#20768B'}.get(prob, '#20768B')
    rows = ''.join(f'<div class="qf"><p class="ql">{E(k)}</p><p class="qv">{E(f[k])}</p></div>' for k in ['Pourquoi', 'Réponse', 'Preuve', 'Diapo de secours', 'Piège'] if k in f)
    return f'<div class="qa"><div class="qh"><p class="qn">{prefix}{n}</p><p class="qq">{E(q)}</p><p class="qp" style="color:{pc};border-color:{pc}">{E(prob)}</p></div>{rows}</div>'


def md_list(sec):
    return '<ul>' + ''.join(f'<li>{E(i)}</li>' for i in re.findall(r'^- (.*)$', sec, re.M)) + '</ul>'


forts = md_list(auto.split('**Points forts**')[1].split("**Axes d'amélioration**")[0])
axes = md_list(auto.split("**Axes d'amélioration**")[1].split('**Conclusion**')[0])
concl = E(auto.split('**Conclusion** :')[1].strip())

CSS = open(os.path.join(ORAL, 'gen', 'guide.css')).read() + '''
.show { background:#FBF4E6; border-left:1.2mm solid #8A6A33; border-radius:1.5mm; padding:1.6mm 3mm; font-size:8.8pt; color:#5A4321; margin-bottom:2mm; }
.show b { color:#8A6A33; }
.secr { font-family:'Poppins', Arial, sans-serif; font-size:8pt; color:#6A7B82; margin-top:1mm; }
.part { font-family:'Poppins', Arial, sans-serif; font-size:7.5pt; font-weight:600; letter-spacing:1.5px; color:#8A6A33; margin:0; }
.st1 { color:#20768B; font-weight:600; } .st2 { color:#12475B; font-weight:600; } .st3 { color:#6A7B82; font-weight:600; }
.ok { color:#20768B; font-weight:700; }
.score { font-family:'Playfair Display', Georgia, serif; font-size:30pt; font-weight:700; color:#12475B; line-height:1; }
.tr td:first-child { white-space:nowrap; }
'''

H = []
H.append(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Guide de soutenance</title><style>{CSS}</style></head><body>
<section class="cover">
<p class="ey">SOUTENANCE ORALE · BLOC 2 · EURIDIS</p>
<h1>Guide de soutenance</h1>
<p class="sub">Sales Playbook Planet Aura · version 3, le cas fil rouge</p>
<p class="who">Emma Soares Britschgy · version du 25 octobre 2026</p>
<div class="cbox"><p><b>Ce que contient ce guide</b></p><p>1. L’essentiel en une page · 2. Le cas fil rouge en une page · 3. La grille de conformité · 4. Le script minuté, diapo par diapo · 5. Les transitions et les messages clés · 6. Chiffres et définitions · 7. Les questions du jury · 8. Les diapos de secours · 9. Limites et réserves · 10. L’autoévaluation · 11. Les check-lists</p></div>
<p class="conf">Document de travail personnel : ne pas remettre au jury, ne pas diffuser.</p>
</section>''')

tot = end('conclusion')
H.append(f'''<section><p class="ey">1 · L’ESSENTIEL EN UNE PAGE</p><h2>Vingt minutes pour montrer une méthode au travail, pas pour réciter un dossier</h2>
<div class="g3">
<div class="k"><p class="kn">18-19 min</p><p>visées, 20 au maximum. Le script est calé sur {tot} à 130 mots/minute ; la marge sert aux silences et aux regards.</p></div>
<div class="k"><p class="kn">{len(main)} + {len(backs)}</p><p>diapos présentées, plus {len(backs)} diapos de secours après « Merci », pour les questions.</p></div>
<div class="k"><p class="kn">15 min</p><p>de questions : le jury n’a pas lu le playbook ; il juge la communication et le traitement des objections.</p></div>
</div>
<h3>Le découpage, conforme au cahier des charges</h3>
<table class="t"><tr><th>Partie</th><th>Diapos</th><th>Fin visée</th><th>Cahier des charges</th></tr>
<tr><td><b>Introduction et diagnostic</b></td><td>1 à 7</td><td>{end('diagnostic')}</td><td>3 à 5 min</td></tr>
<tr><td><b>Parties 8 à 14, avec le cas fil rouge</b></td><td>8 à 19</td><td>{end('kpi')}</td><td>l’essentiel du temps</td></tr>
<tr><td><b>Synthèse et ouverture</b></td><td>20</td><td>{end('conclusion')}</td><td>environ 1 min</td></tr></table>
<h3>Trois points de passage au chronomètre</h3>
<table class="t"><tr><th>À l’écran</th><th>Heure visée</th><th>Si je suis en retard</th></tr>
<tr><td>Diapo 8 · ICP</td><td><b>{start('icp')}</b></td><td>Diapo 6 : garder le triangle et « on se débrouille », sauter la carte des familles.</td></tr>
<tr><td>Diapo 13 · SPIN</td><td><b>{start('spin')}</b></td><td>Diapo 11 : garder la ligne d’arrivée, sauter les durées de cycle.</td></tr>
<tr><td>Diapo 19 · Indicateurs</td><td><b>{start('kpi')}</b></td><td>Une carte, une décision ; puis directement la conclusion.</td></tr></table>
<h3>Six phrases à savoir mot pour mot</h3>
<ol class="ph">
<li>« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. »</li>
<li>« Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente reproductible et mesurable, pour recruter, activer et fidéliser nos adhérents ? »</li>
<li>« Un point n’est accordé qu’avec sa preuve. »</li>
<li>« La vente finit au premier envoi, pas à la signature. »</li>
<li>« Vingt-quatre bouteilles, trois cent soixante euros de transport, les taxes estimées et réglées d’avance, une livraison estimée à trois semaines. Ils repartent les mains libres. »</li>
<li>« Le prospect n’achète pas seulement du transport : il cherche à réduire son risque. »</li>
</ol>
<div class="warn"><p class="wl">CE QUE JE NE DIS JAMAIS</p>
<p>Que le cas est une vente réelle, ou qu’un compte du top 10 suit cette trajectoire · « souvent » à propos de la scène de Houston · la capture USA du dossier (grille 2025) · un nom ou un CA de client · « assurance incluse », « tout compris », « garanti » · « 210 € » ou « 360 € » comme prix complet (c’est le transport) · « la valeur résiste » (l’OIV dit l’inverse pour 2025) · « 145 adhérents actifs » (ce sont des signés) · « j’ai interviewé » (échanges écrits) · un objectif présenté comme un résultat · les projets au présent · un taux de droits US de mémoire · « premier », « unique », « exclusif ».</p></div>
</section>''')

# ---------- le cas en une page ----------
CASE = [('1 · Qualifier', '8', 'Domaine provençal avec caveau, 20+ étrangers / semaine en saison, panier ~300 €, e-shop, clientèle US majoritaire, tiers B (60-100 envois/an)', 'Sourcé (chap. 11)'),
        ('', '', 'Score PA-FIT : 45 au départ (nurture), 85 après preuve de la douleur, de l’échéance et du décideur (P1)', 'Illustratif (barème réel)'),
        ('2 · Prospecter', '12', 'Cadence caveau J1, J+4, J+10, visite ; script d’appel de moins de 3 min ; e-mail 1 de l’annexe E', 'Règle (chap. 10, annexe E)'),
        ('3 · Découvrir', '13', 'Trame de 35 min ; tunnel 1 du vigneron ; reformulation à trous ; phrase de bénéfice notée mot pour mot', 'Règle ; réponses illustratives'),
        ('4 · Proposer', '14', 'Grille officielle 2026 (document réel) ; 24 bouteilles = 360 € de transport, 15 €/btl ; objection « c’est cher » en 4 temps ; ROI : 40 000 € de ventes perdues', 'Grille 2026 ; ROI : calcul illustratif'),
        ('5 · Activer', '15', 'Signature en ligne, SEPA, 1er lot de cartons ; formation J+5 ; premier envoi ; point J+30 ; score de santé', 'Règle (chap. 16)'),
        ('6 · Suivre', '19', 'Étape 6 dans HubSpot, prochaine action datée (verbe, propriétaire, date, résultat) ; KPI d’activation', 'Illustratif (format sourcé)')]
H.append('<section><p class="ey">2 · LE CAS FIL ROUGE EN UNE PAGE</p><h2>Un parcours type, pas une vente réalisée : savoir dire ce qui est sourcé</h2>'
         '<p class="lead">Source : chapitre 11, « le fil rouge : une vente de bout en bout ». Les prix viennent de la grille 2026, les étapes des règles du playbook. Aucun domaine n’est nommé, aucun chiffre client n’est cité. Un seul panier dans tout l’oral : 24 bouteilles, 360 € de transport.</p>'
         '<table class="t"><tr><th>Étape</th><th>Diapo</th><th>Ce que montre le cas</th><th>Statut</th></tr>'
         + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in CASE) + '</table>'
         '<div class="warn"><p class="wl">LA PHRASE DE SÉCURITÉ</p><p>« C’est un parcours type, écrit dans le playbook : les prix sont ceux de notre grille, les situations sont illustratives. Ce qui est réel, ce sont les outils que je vous montre. »</p></div></section>')

# ---------- grille de conformité ----------
GRID = [
    ('Débute par un « grab attention » (Start with why)', 'Animation', '2', 'Houston : 2 bouteilles sur 24, le silence, la question ; le « pourquoi » dit à voix haute.'),
    ('Présente de manière rythmée et dynamique', 'Animation', 'toutes', 'Une idée par diapo, un cas qui avance, des transitions annoncées ; 20 diapos en 18-19 min.'),
    ('Bon niveau de langage, vocabulaire métier', 'Animation', 'toutes', 'DDP, POA, CIVC, three-tier, ISTA 3A, PA-FIT, SPIN, cadence, définis à l’oral au premier usage.'),
    ('Support graphiquement agréable et dynamique', 'Animation', 'toutes', 'Document et capture réels (grille officielle 2026, tableau de bord), pages réelles du playbook, frises, score, bandeau du cas.'),
    ('Grammaire et orthographe', 'Animation', 'toutes', 'Typographie française (espaces insécables), relecture par trois relecteurs indépendants.'),
    ('Respecte le temps imparti (20 min max)', 'Animation', '—', f'Script à {tot} ; trois points de passage ; coupes prévues.'),
    ('Titres précis et impactants dans le sommaire', 'Argumentation', '3', 'Cinq étapes titrées par leur idée : « La vente finit au premier envoi », « Outiller, former, mesurer ».'),
    ('Introduction qui amène le sujet', 'Argumentation', '2 à 7', 'Scène → marché → entreprise → offre → diagnostic → problématique et trois enjeux.'),
    ('Analyse le marché en lien avec l’entreprise', 'Argumentation', '4', 'Trois bascules et cinq contraintes réglementaires : « freins pour le vigneron, notre métier ».'),
    ('Présente l’entreprise (organigramme, CA, offre, concurrence, cibles)', 'Argumentation', '5, 6 (+ B9)', 'Équipe et « qui vend, qui décide », CA ×4,7, marchés, grille, positionnement ; organigramme en B9.'),
    ('Processus de vente et tunnels SPIN', 'Argumentation', '11 à 15', 'Sept étapes (responsable, preuve, délai, outil), prospection, deux tunnels SPIN en action, proposition, activation.'),
    ('Ressources précises, réalistes, échéancées, chiffrées', 'Argumentation', '16 (+ B13)', 'Pages réelles, une preuve par doute, six chantiers : responsable, temps, budget, critère ; 3 000 €.'),
    ('Sales Ops mises en place et objectif de chacune', 'Argumentation', '17, 18', 'Six outils autour de HubSpot, statut de chacun, alignement marketing-ventes, rituels ; onboarding.'),
    ('SPB existant : améliorations justifiées', 'Argumentation', '7, 20 (+ B15)', 'Sans objet : pas de playbook avant ; existant et apport distingués partout (étiquettes, B15).'),
    ('Présente les indicateurs de performance', 'Argumentation', '19 (+ B6)', 'Constaté / objectif ; source, fréquence, responsable, action ; revue mensuelle ; exemple de décision.'),
    ('Synthèse en lien avec les enjeux', 'Argumentation', '20', 'Réponse enjeu par enjeu, apport, bénéfices attendus, difficulté, limites.'),
    ('Ouverture', 'Argumentation', '20', 'Diversifier pour réduire la dépendance aux USA ; lecture fin décembre ; entretiens T1 2027.'),
]
AUDIT = [
    ('Tous les critères de la grille sont couverts', 'Oui : tableau ci-dessus.'),
    ('Découpage temporel conforme', f'Introduction {end("diagnostic")}, parties 8 à 14 jusqu’à {end("kpi")}, synthèse jusqu’à {end("conclusion")}.'),
    ('Temps total ≤ 20 min', f'{tot} de texte, soit 18 à 19 min avec les silences.'),
    ('Temps suffisant pour les parties opérationnelles', 'Douze diapos sur vingt, la majorité du temps.'),
    ('ICP et personas distingués', 'Diapo 8 (l’entreprise), diapo 9 (les personnes) ; la phrase le dit.'),
    ('Tunnels SPIN réellement présentés', 'Diapo 13 : tunnel 1 en action, tunnel 2 en regard ; banque en B4.'),
    ('Ressources précises, réalistes, datées, chiffrées', 'Diapo 16 : responsable, temps, budget, critère pour chaque chantier.'),
    ('Sales Ops expliquées avec leurs objectifs', 'Diapo 17 : rôle et statut de chaque outil ; règles proposées.'),
    ('Indicateurs avec méthode de suivi', 'Diapo 19 : source, fréquence, responsable, action ; revue mensuelle.'),
    ('Marché relié aux enjeux de Planet Aura', 'Diapo 4 : chaque bascule traduite en conséquence.'),
    ('Organisation, offre, concurrence présentées', 'Diapos 5 et 6 (+ B9, B3, B8).'),
    ('Apport personnel démontré', 'Étiquettes sur chaque diapo opérationnelle ; diapo 20 ; B15.'),
    ('La synthèse répond à la problématique', 'Diapo 20 : « une méthode reproductible et mesurable », enjeu par enjeu.'),
    ('Difficultés et ouverture pertinentes', 'Diapo 20 : chiffres divergents → source unique ; diversification.'),
    ('Chiffres cohérents avec le mémoire', 'Revue factuelle et contre-vérification sur les sources ; un seul panier pour le cas.'),
    ('Diapositives lisibles, variées, professionnelles', 'Textes ≥ 24 px, rendu vérifié diapo par diapo, compositions variées.'),
    ('Le discours complète le support sans le lire', 'Notes réécrites pour dire ce que l’écran ne dit pas.'),
    ('Diapositives de secours adaptées', f'{len(backs)} secours, dont B16 (le cas) et B15 (l’apport).'),
]
H.append('<section><p class="ey">3 · LA GRILLE DE CONFORMITÉ</p><h2>Chaque critère officiel a sa diapo et sa preuve</h2><p class="lead">Grille Euridis Bloc 2 : capacités d’animation sur 6 points, d’argumentation et d’analyse sur 14.</p>'
         '<table class="t"><tr><th>Critère officiel</th><th>Bloc</th><th>Diapo</th><th>La preuve apportée</th></tr>'
         + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in GRID) + '</table>'
         '<h3>Le contrôle final demandé, point par point</h3><table class="t"><tr><th>Point de contrôle</th><th>Résultat</th></tr>'
         + ''.join(f'<tr><td><b>{E(a)}</b></td><td><span class="ok">✓</span> {E(b)}</td></tr>' for a, b in AUDIT) + '</table></section>')

# ---------- script minuté ----------
script = []
for k, sid in enumerate(main, 1):
    title, timing, aside = slide_info(sid)
    title = TITLES.get(sid, title)
    paras = [p.strip() for p in aside.split('\n') if p.strip()]
    spoken = ''.join(f'<p class="cue">{E(p)}</p>' if p.startswith('(') else f'<p>{E(p)}</p>' for p in paras)
    sec = f'<p class="secr">Secours utiles : {E(SEC[sid])}</p>' if sid in SEC else ''
    script.append(f'''<div class="sl"><div class="slh"><p class="sn">{k}</p><div style="flex:1"><p class="part">{E(PART[sid].upper())}</p><p class="st">{E(title)}</p></div><p class="stime">{E(timing)}</p></div>
<div class="slb"><div style="width:62mm;flex:none"><img src="{thumb(sid)}" alt="">{sec}</div><div class="say"><p class="show"><b>À montrer</b> · {E(SHOW[sid])}</p>{spoken}</div></div></div>''')
H.append('<section><p class="ey">4 · LE SCRIPT MINUTÉ</p><h2>Ce que je dis, ce que je montre, diapo par diapo</h2><p class="lead">Les mêmes notes figurent en mode présentateur. Elles sont écrites pour l’oral : les apprendre par idées, jamais mot à mot, sauf les six phrases de la page 2. En italique : les rappels de régie, à ne pas dire.</p>' + ''.join(script) + '</section>')

# ---------- transitions et messages ----------
TRANS = [('Accroche → sommaire', '« Pour la lever, j’ai construit le Sales Playbook de Planet Aura… »'),
         ('Sommaire → comprendre', '« Première étape : comprendre. »'),
         ('Diagnostic → cibler', '« Trois enjeux en découlent, et nous allons les suivre sur notre domaine. » → « Deuxième étape : cibler. »'),
         ('Personas → vendre', '« Troisième étape : vendre. Chaque solution doit répondre à un problème, et se prouver. »'),
         ('Processus → cas', '« Revenons à notre domaine. »'),
         ('Proposer → activer', '« Quatrième étape : activer, car la signature n’est pas la fin. »'),
         ('Activer → piloter', '« Cinquième étape : piloter, pour transmettre et mesurer. »'),
         ('Indicateurs → conclusion', '« Je reviens à ce couple de Houston. »')]
MSG = [('Comprendre', 'Le marché complique l’export ; nos clients viennent à nous ; notre vente reposait sur le bouche-à-oreille.'),
       ('Cibler', 'L’adéquation prime sur la taille ; un point n’est accordé qu’avec sa preuve ; on parle au rôle, pas au portrait.'),
       ('Vendre', 'Chaque solution se prouve ; le prospect chiffre lui-même sa perte ; on montre au lieu de dire.'),
       ('Activer', 'La vente finit au premier envoi ; le commercial en reste responsable.'),
       ('Piloter', 'Une donnée, un propriétaire, une décision ; mesuré ou espéré ; une méthode qui se transmet en 90 jours.')]
H.append('<section><p class="ey">5 · LES TRANSITIONS ET LES MESSAGES CLÉS</p><h2>Le fil qui relie les vingt diapos</h2>'
         '<table class="t tr"><tr><th>Passage</th><th>La phrase de transition</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in TRANS) + '</table>'
         '<h3>Un message à faire retenir par étape</h3><table class="t"><tr><th>Étape</th><th>Message</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in MSG) + '</table></section>')

# ---------- chiffres et définitions ----------
NUMS = [('×4,7', 'CA de 2021 à 2025 (1,15 M€ en 2025, +11,6 %) ; +18,7 % à fin sept. 2026', 'Constaté, dashboards 24/09/2026'),
        ('262 · 6 643', 'adhérents · envois sur 12 mois, dont 64,5 % vers les USA et 18,6 % en France', 'Constaté'),
        ('13 · fin 2025', 'personnes, filiale comprise · arrivée d’Adam, premier commercial dédié', 'Constaté'),
        ('~145 / 120', 'adhérents signés en 12 mois, pour 120 visés (signés, pas actifs)', 'Constaté'),
        ('448 / 710', 'prospects non qualifiés sur 710 comptes au CRM', 'Constaté'),
        ('89,8 % · 1,45 %', 'envois assurés (option 3 %, jusqu’à 20 000 €/envoi) · commandes annulées', 'Constaté'),
        ('4,65/5 · 4,8/5', 'satisfaction 2024 (23 réponses) · avis Google (296, sept. 2026)', 'Constaté'),
        ('105 → 510 €', 'groupage USA, 1-3 à 36 bouteilles ; 24 btl = 360 € (15 €/btl) ; + taxes estimées, 17 € de dossier', 'Grille 2026'),
        ('15 % → 10 %', 'droits US : 15 % d’août 2025 à février 2026, 10 % depuis ; le simulateur fait foi', 'Externe'),
        ('208 Mhl · 3,56 €/l', 'consommation mondiale 2025 (−2,7 %) · prix moyen à l’export (OIV)', 'Externe'),
        ('−21 % · 5,4 M', 'exports FR vers les USA en 2025 (FEVS) · œnotouristes étrangers en 2023 (Atout France)', 'Externe'),
        ('70 · 47 · 15', 'contacts, réponses d’enquête, avis : l’étude des personas (oct. 2026)', 'Constaté'),
        ('17 · 3 000 € · ≈ 200 h', 'ressources (13 validées, 4 à créer) · plafond externe · temps interne (calcul)', 'Objectif'),
        ('≥ 70 % · > 60 % · 40-60 %', 'activation à J+30 · adhérents actifs · taux de gain', 'Objectif'),
        ('75 · 55 · 35', 'seuils PA-FIT : priorité active · cadence · nurture', 'Règle'),
        ('40 000 € → 10 000 €', 'ROI du cas : 20 étrangers/sem. × 1 sur 3 × 300 € × 20 sem. ; un quart récupéré, pour 110 € de cartons (exemple du playbook : 30 visiteurs → 60 000 €)', 'Calcul illustratif')]
GLOSS = [('Commissionnaire de transport', 'Organise le transport en son nom propre et répond du résultat de bout en bout (obligation de résultat, CGS art. 2).'),
         ('DDP / DAP', 'Taxes payées d’avance par le client (DDP) ou à l’arrivée par le destinataire (DAP).'),
         ('Three-tier system', 'Système américain importateur → grossiste → détaillant ; nos licences couvrent les deux premiers niveaux.'),
         ('POA', 'Procuration de dédouanement exigée aux USA au-delà de 2 100 $ ; formalité normale, jamais à éviter.'),
         ('CIVC', 'Comité Champagne : délivre le certificat d’origine obligatoire hors UE.'),
         ('ISTA 3A', 'Norme de test d’emballage (chute, vibration) de nos cartons.'),
         ('Adhérent · B2B2C', 'Point de vente qui a signé la documentation annuelle, sans frais ni minimum ; nous servons son client final.'),
         ('ICP · persona', 'Le profil d’entreprise à viser · le portrait type d’une personne qui décide, utilise ou paie.'),
         ('CAVE · PA-FIT', 'Trier (Clientèle, Autorité, Volume, Échéance) · prioriser sur 100 points, un point par preuve.'),
         ('SPIN', 'Situation, Problème, Implication, Need-payoff : le prospect formule lui-même son besoin (Rackham).'),
         ('Cadence · nurture', 'Séquence de relances planifiées · entretien de la relation en attendant un signal d’achat.'),
         ('SLA', 'Délai maximal convenu pour agir : répondre, relancer, transmettre.'),
         ('Activation · actif', 'Premier envoi sous 30 jours après la signature · au moins un envoi sur 90 jours.'),
         ('ADV', 'Administration des ventes : commandes et dossiers après la vente, assurée par l’exploitation.')]
H.append('<section><p class="ey">6 · CHIFFRES ET DÉFINITIONS</p><h2>Les chiffres à connaître, avec leur statut</h2>'
         '<table class="t"><tr><th>Chiffre</th><th>Ce qu’il mesure</th><th>Statut</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in NUMS) + '</table>'
         '<h3>Les définitions à donner au jury, au premier usage</h3><table class="t"><tr><th>Terme</th><th>Définition simple</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in GLOSS) + '</table></section>')

# ---------- questions ----------
H.append('<section><p class="ey">7 · LES QUESTIONS DU JURY</p><h2>Une méthode pour toutes les questions : accueillir, clarifier, prouver, vérifier</h2>'
         '<div class="g4"><div class="m"><p class="mn">1</p><p><b>Accueillir</b> : reconnaître ce qui est juste dans la question.</p></div><div class="m"><p class="mn">2</p><p><b>Clarifier</b> : une question courte pour viser le vrai doute.</p></div><div class="m"><p class="mn">3</p><p><b>Prouver</b> : une seule preuve, chiffrée et sourcée.</p></div><div class="m"><p class="mn">4</p><p><b>Vérifier</b> : « Cela répond-il à votre question ? »</p></div></div>'
         '<p class="lead">C’est la méthode du playbook face aux objections : l’appliquer devant le jury, c’est la démontrer. Si je ne sais pas : « Je ne veux pas vous donner un chiffre approximatif ; je le vérifie et je vous le transmets. »</p>'
         f'<h3>Les {len(top)} questions les plus probables</h3>' + ''.join(qa_card('Q', *q) for q in top)
         + f'<h3>Les {len(traps)} questions pièges</h3>' + ''.join(qa_card('P', *q) for q in traps)
         + f'<h3>Les {len(cas)} questions sur le cas et la démonstration</h3>' + ''.join(qa_card('C', *q) for q in cas) + '</section>')

rows = []
for sid in backs:
    title, _, _ = slide_info(sid)
    b = sid.upper()
    rows.append(f'<tr><td class="bn">{b}</td><td><b>{E(title)}</b></td><td>{E(REPOND.get(b, ""))}</td></tr>')
H.append(f'<section><p class="ey">8 · LES DIAPOS DE SECOURS</p><h2>{len(backs)} diapos après « Merci », à n’ouvrir que si la question l’appelle</h2><p class="lead">Les atteindre par le panneau des diapos (section « Diapositives de secours »). Une réponse sans support convainc souvent davantage : ne pas les montrer par réflexe.</p><table class="t"><tr><th>N°</th><th>Titre</th><th>Répond à</th></tr>' + ''.join(rows) + '</table></section>')

LIM = [('Rien n’est encore mesuré', 'Le CRM n’historise que depuis 2025 : les cibles sont des objectifs de départ ; point zéro au 24/09/2026, première lecture fin décembre 2026.'),
       ('Des personas sur échanges écrits', 'Aucun entretien formel ; prospects sous-représentés (4 réponses) : entretiens prévus au T1 2027.'),
       ('Un parcours d’intégration non testé', 'Livré, mesurable (S1, S4, S8), mais jamais suivi par un recrutement : sa première mesure viendra avec lui.'),
       ('Des règles proposées, pas ratifiées', 'Dictionnaire CRM, score d’hygiène, semaine type, RACI, rituels : à valider en équipe ; câblage Brevo-HubSpot en novembre 2026.'),
       ('Un cas type, pas une vente', 'Situations et points du score illustratifs ; prix et règles sourcés.'),
       ('Des durées de cycle à mesurer', '7 à 21 j (objectif) et 6 à 12 semaines en champagne (hypothèse terrain) : médiane réelle après 90 jours.'),
       ('Un saut de CA non expliqué', 'Le +224 % de 2022 n’est pas documenté : « à confirmer avec la direction ».'),
       ('Une formulation à corriger', 'L’annexe F décrit l’assurance comme incluse dans les frais administratifs ; la pratique est une option à 3 % : à remonter pour la grille 2027.'),
       ('Une dépendance sans cible', 'Part USA 64,5 %, suivie chaque trimestre, sans objectif chiffré de diversification.')]
H.append('<section><p class="ey">9 · LIMITES ET RÉSERVES</p><h2>Les dire avant qu’on me les oppose</h2><p class="lead">Une limite annoncée avec son plan devient une preuve de lucidité ; découverte par le jury, elle devient une faiblesse.</p>'
         '<table class="t"><tr><th>Limite</th><th>Ce que je dis, et ce qui est prévu</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in LIM) + '</table></section>')

from autoeval import HTML as selfeval
H.append(f'<section><p class="ey">10 · L’AUTOÉVALUATION</p><h2>Après les questions : un bilan honnête, en deux minutes</h2><p class="lead">Le jury demande souvent une autoévaluation avant le débrief. Deux forces, deux axes de progrès avec leur plan, une phrase de conclusion.</p><div class="g2"><div class="ab"><p class="abl" style="color:#20768B">POINTS FORTS</p>{forts}</div><div class="ab"><p class="abl" style="color:#722F45">AXES D’AMÉLIORATION</p>{axes}</div></div><div class="concl"><p>{concl}</p></div>{selfeval}</section>')

H.append('''<section><p class="ey">11 · LES CHECK-LISTS</p><h2>Préparer, vérifier, arriver serein</h2>
<div class="g3c">
<div class="ck"><p class="ckl">LA SEMAINE AVANT</p><ul>
<li>Trois répétitions complètes au chronomètre, dont une filmée ; viser 18 à 19 minutes.</li>
<li>Une répétition des questions avec quelqu’un qui joue le jury, pièges et questions sur le cas compris.</li>
<li>Savoir refaire à voix haute : le score 45 → 60 → 85, le ROI (20 × 1/3 × 300 € × 20 = 40 000 €), 24 bouteilles = 360 €.</li>
<li>Faire valider par la direction la réponse sur l’assurance (annexe F) et le statut des rituels.</li>
<li>Lire l’annexe W une dernière fois : le discours sur l’IA doit lui correspondre.</li>
<li>Télécharger le deck en PDF et en PPTX ; tester le mode présentateur.</li>
</ul></div>
<div class="ck"><p class="ckl">LA VEILLE</p><ul>
<li>Vérifier au simulateur le taux des droits US (10 % depuis février 2026).</li>
<li>Relire chaque date future du deck (câblage Brevo et objections en novembre, lecture fin décembre, chantiers de la diapo 16) : passer au présent ou au passé ce qui est échu, avec l’état réel confirmé.</li>
<li>Noter le statut réel des chantiers de septembre et d’octobre.</li>
<li>Savoir si la version de novembre est sortie, selon la date du jury.</li>
<li>Copier le deck sur une clé USB ; l’envoyer par e-mail à soi-même.</li>
<li>Imprimer ce guide ; préparer une fiche avec les trois points de passage.</li>
</ul></div>
<div class="ck"><p class="ckl">LE JOUR J</p><ul>
<li>Le carton ISTA 3A de démonstration, si le format le permet.</li>
<li>Téléphone : simulateur et fiche Google ouverts, en mode avion pendant l’exposé.</li>
<li>Un chronomètre visible ; une bouteille d’eau.</li>
<li>Arriver tôt, tester l’écran et la télécommande.</li>
<li>Première phrase, puis un silence : laisser Houston faire son effet.</li>
</ul></div>
</div>
<div class="warn"><p class="wl">CONFIDENTIALITÉ</p><p>Le playbook est diffusé en interne et aux seuls évaluateurs Euridis, avec l’accord de la direction. À l’oral : aucun nom ni CA de client, aucune donnée personnelle de client final, aucun identifiant, aucun mot de passe, aucun taux de marge.</p></div>
</section>''')
H.append('</body></html>')
doc = '\n'.join(H)
head, body = doc.split('</style>', 1)
body = body.replace('« ', '« ').replace(' »', ' »')
body = re.sub(r' ([:;?!])(?=[\s<])', ' \\1', body)
open(os.path.join(OUT, 'guide.html'), 'w').write(head + '</style>' + body)
print('guide.html ok', len(main), len(backs), len(top), len(traps), len(cas))
