# Guide de soutenance v5 du 26/10/2026, diapos lisibles en 3 s (HTML imprimé en PDF A4) : essentiel, cas fil rouge,
# grille de conformité, script minuté, transitions, chiffres et définitions, questions du jury, limites, autoévaluation,
# check-lists. Les phrases citées (transitions, plan de coupe) et les renvois aux secours sont contrôlés contre les notes
# du deck à chaque génération : toute incohérence s'affiche en « ATTENTION ».
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

# ---------- contrôles guide / notes ----------
WPM = 130  # même rythme que build.py
NOTE = {sid: slide_info(sid)[2] for sid in main}
NUM = {sid: k for k, sid in enumerate(main, 1)}
CHECK = []  # incohérences relevées, affichées à la fin de la génération
norm = lambda t: re.sub(r'\s+', ' ', t).strip()


def said(sid):
    # texte dit : sans les indications de régie entre parenthèses
    return norm(re.sub(r'\([^)]*\)', ' ', NOTE[sid]))


def secs(phrase):
    # durée d'une phrase au rythme du script (même décompte des mots que build.py)
    return round(len(re.findall(r"[\wÀ-ÿ’'-]+", phrase)) / WPM * 60)

TITLES = {'cover': 'Couverture', 'accroche': 'Accroche : une scène type', 'conclusion': 'Synthèse, ouverture et retour à Houston'}
PART = {'cover': 'Comprendre', 'accroche': 'Comprendre', 'sommaire': 'Comprendre', 'marche': 'Comprendre', 'entreprise': 'Comprendre', 'offre': 'Comprendre',
        'diagnostic': 'Comprendre', 'icp': 'Cibler · partie 8', 'personas': 'Cibler · partie 9', 'solutions': 'Vendre · partie 10', 'processus': 'Vendre · partie 11',
        'prospecter': 'Vendre · partie 11', 'spin': 'Vendre · partie 11', 'proposer': 'Vendre · partie 11', 'activer': 'Activer · partie 11',
        'ressources': 'Piloter · partie 12', 'salesops': 'Piloter · partie 13', 'onboarding': 'Piloter · partie 13', 'kpi': 'Piloter · partie 14',
        'conclusion': 'Synthèse et ouverture'}
# « À montrer » : uniquement ce qui est à l'écran en v5, dans l'ordre des indications (Montrer …) des notes.
SHOW = {
    'cover': 'Rien : laisser la couverture deux secondes, regarder chaque membre du jury, sourire, puis lancer la scène.',
    'accroche': 'Laisser parler les 2 bouteilles pleines sur 24 ; finir sur la question, en bas à gauche.',
    'sommaire': 'Balayer les cinq étapes de haut en bas, puis, à droite, le renvoi « → la problématique » (énoncée diapo 7) et les trois enjeux ; pointer le bandeau « cas fil rouge », puis la légende des étiquettes.',
    'marche': 'Les trois chiffres de gauche à droite (deux reculs en orange, une opportunité en sarcelle), puis le bandeau sombre : cinq contraintes, de la douane à l’emballage.',
    'entreprise': 'Le ×4,7, puis la barre 2025, en foncé ; ensuite le bandeau sombre « Qui vend » : Adam, le seul commercial dédié, arrivé fin 2025 ; enfin la photo de l’équipe, à droite.',
    'offre': 'Les barres du transport par bouteille, puis la dorée : 24 btl, 15 € ; ensuite le bloc sombre « On se débrouille », la ligne surlignée « Spécialistes vin » (nos vrais duels) et « Notre place ».',
    'diagnostic': 'La carte « Fragilités » (448 / 710, activation jamais mesurée), puis le bandeau sombre : lire la problématique lentement, une seule fois ; finir sur les trois pastilles numérotées.',
    'icp': '« Ma recommandation » : 60 % de l’effort sur les caveaux ; puis, à droite, les trois barres 45 → 60 → 85 : les parties hachurées sont les preuves apportées ensuite.',
    'personas': 'Les trois cartes de gauche à droite (Décide, Utilise, Paie) : la ligne « Craint », puis la citation qui y répond ; enfin le bandeau du bas : 70 · 47 · 15, constaté, 5/5 confirmés.',
    'solutions': 'Suivre la chaîne de gauche à droite, de 24 → 2 jusqu’à la preuve ; s’arrêter sur le pavé sombre « Solution » ; finir sur le bandeau « Nous refusons ».',
    'processus': 'Le rond n° 6 (Activé, sous « Ligne d’arrivée ») et sa fiche : qui, délai, outil ; puis le bandeau Constat → Ma décision → Ce que l’on mesure.',
    'prospecter': 'Les trois gestes à gauche (préparer, viser, cadencer), puis la question du script d’appel, en grand ; enfin la phrase de l’e-mail, en dessous.',
    'spin': 'Descendre l’entonnoir S, P, I, N, une question complète par famille ; s’arrêter sur la bande dorée I (12 bouteilles réduites à 2) ; finir sur le bandeau « Reformuler », au bas de l’entonnoir.',
    'proposer': 'La case encadrée de la grille officielle (24 bouteilles = 360 €), puis « 15 € » à droite ; ensuite « C’est cher » et ses quatre temps ; enfin le bloc « Simulation ».',
    'activer': 'La frise de J0 jusqu’au drapeau « ligne d’arrivée » (premier envoi, le couple texan suivi), puis le pointillé vers le point d’étape à J+30 ; enfin le bandeau Constat → Ma décision → Ce que l’on mesure.',
    'ressources': 'À gauche, les trois pages réelles « Déjà livré » ; puis les trois cartes de gauche à droite : l’ordre, et 800 € sur 3 000 € ; enfin le bandeau du bas.',
    'salesops': 'HubSpot au centre, avec à gauche les quatre outils existants ; puis la flèche orange vers Brevo (câblage à déployer) et le dictionnaire CRM (ma contribution) ; finir sur le bandeau : règles communes proposées, pipeline complet chaque lundi.',
    'onboarding': 'L’escalier J+30, J+60, J+90, une preuve par marche ; puis le drapeau S8 sur la deuxième marche : premier adhérent signé et activé.',
    'kpi': 'À gauche le constaté (la capture réelle, puis ~145) ; à droite la grande carte Activation J+30 et son action, puis l’étiquette « Domaine activé » ; enfin « point zéro, 24/09/2026 » en haut à gauche, et le bandeau du bas.',
    'conclusion': 'Les 24 bouteilles pleines, puis les trois enjeux de gauche à droite ; finir en regardant le jury, sans regarder l’écran.',
}
# Renvois aux secours : tous ceux que nomment les notes, plus ceux où est passé le détail retiré de l'écran en v5.
SEC = {'marche': 'B10 · B7 · B8', 'entreprise': 'B9', 'offre': 'B7 · B3', 'diagnostic': 'B8 · B6', 'icp': 'B2 · B16 · B6',
       'personas': 'B1', 'solutions': 'B3 · B11 · B14 · B4', 'processus': 'B17 · B2 · B6', 'prospecter': 'B4 · B12', 'spin': 'B4',
       'proposer': 'B7 · B14', 'activer': 'B11 · B16', 'ressources': 'B13', 'salesops': 'B12 · B17 · B14 · B9', 'onboarding': 'B15',
       'kpi': 'B6 · B11 · B16', 'conclusion': 'B15 · B7 · B10 · B8 · B5'}
for sid in main:
    if sid not in SHOW:
        CHECK.append(f'« À montrer » manquant : {sid}')
    for b in sorted(set(re.findall(r'\b(B\d+)\b', NOTE[sid]))):
        if b not in SEC.get(sid, '').split(' · '):
            CHECK.append(f'renvoi {b} de la note « {sid} » absent de SEC')
for sid, v in SEC.items():
    for b in v.split(' · '):
        if b.lower() not in backs:
            CHECK.append(f'secours inexistante dans SEC[{sid}] : {b}')

# Minutage et mots visibles recalculés sur les notes actuelles et le deck (autoeval.py) : un deck plus ancien que les notes
# (build.py non relancé) ou une diapo trop chargée s'affichent en « ATTENTION ».
os.environ['DECK_DIR'] = DECK
import autoeval as AE
for sid in main:
    if AE.ENDS.get(sid) != end(sid):
        CHECK.append(f'deck périmé : « {sid} » finit à {end(sid)} dans le deck, à {AE.ENDS.get(sid)} d’après les notes actuelles (relancer build.py)')
        break
for sid in main[2:]:
    if sid not in AE.GAP and AE.VIS[sid] > 95:
        CHECK.append(f'« {sid} » : {AE.VIS[sid]} mots visibles (95 au plus, hors écarts assumés)')
for sid in backs:
    if AE.VIS[sid] > 130:
        CHECK.append(f'« {sid} » : {AE.VIS[sid]} mots visibles (130 au plus sur une secours)')

# Typographie française du texte d'écran : aucune espace sécable avant : ; ? ! % » ni après «.
TYPO = []
for sid in deck['order']:
    s = re.sub(r'<aside>.*?</aside>|<style.*?</style>', '', open(os.path.join(SL, f'{sid}.html')).read(), flags=re.S)
    t = html.unescape(re.sub(r'<[^>]+>', '', s))
    for m in re.finditer(r'\S ([:;?!%»])|« ', t):
        TYPO.append(sid.upper() if sid in backs else f'diapo {NUM[sid]}')
        CHECK.append(f'espace sécable dans « {sid} » : « {t[max(0, m.start() - 25):m.end() + 15]} »')
TYPO = sorted(set(TYPO))

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
traps = parse_qs(J.split('# Questions pièges')[1].split('# Questions difficiles')[0])
HARDB = J.split('# Questions difficiles')[1].split('# Questions sur le cas')[0]
hard = parse_qs(HARDB)
SHORT = re.search(r'^> Réponse courte, à savoir par cœur : (.*)$', HARDB, re.M).group(1)
cas = parse_qs(J.split('# Questions sur le cas')[1].split('# Diapos de secours')[0])
JB = J.split('# Diapos de secours')[1].split('# Autoévaluation')[0]
REPOND = dict(re.findall(r'^### (B\d+) — .*?\n.*?- Répond à : (.*?)$', JB, re.S | re.M))
for sid in backs:
    if sid.upper() not in REPOND:
        CHECK.append(f'« Répond à » manquant pour {sid.upper()}')
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
<p class="sub">Sales Playbook Planet Aura · version 5 : des diapos lisibles en 3 secondes</p>
<p class="who">Emma Soares Britschgy · version du 26 octobre 2026</p>
<div class="cbox"><p><b>Ce que contient ce guide</b></p><p>1. L’essentiel en une page · 2. Le cas fil rouge et les dix gestes du commercial · 3. La grille de conformité · 4. Le script minuté, diapo par diapo · 5. Les transitions, les messages clés, les passages à tester · 6. Chiffres et définitions · 7. Les questions du jury · 8. Les diapos de secours · 9. Limites et réserves · 10. Avant / après : ce qui a changé et pourquoi · 11. L’autoévaluation et l’évaluation critique · 12. Les check-lists</p></div>
<p class="conf">Document de travail personnel : ne pas remettre au jury, ne pas diffuser.</p>
</section>''')

tot = end('conclusion')
# Plan de coupe : à chaque point de passage, des phrases des notes v5 (mot pour mot), sur des diapos encore à venir.
# Jamais la seule trace orale d'un contenu retiré de l'écran en v5 (mesure de l'ICP, autres cibles de la partie 10,
# règles marketing-ventes) : on coupe des justifications ou ce que l'écran affiche déjà.
CUTS = [('icp', 'Diapo 8 · ICP', [
            ('solutions', 'Promettre ce qu’on ne peut pas tenir, c’est perdre le client au premier incident.', ', le bandeau « Nous refusons » reste à l’écran'),
            ('prospecter', 'Et l’e‑mail tient en une phrase : le frein n’est pas le prix, c’est la valise.', ', la phrase est à l’écran'),
            ('onboarding', 'Le jalon qui compte arrive à la huitième semaine : son premier adhérent signé et activé, notre ligne d’arrivée.', ', le drapeau S8 l’affiche')], ''),
        ('spin', 'Diapo 13 · SPIN', [
            ('spin', 'C’est là que le vigneron peut découvrir qu’il n’avait jamais fait le calcul.', ''),
            ('proposer', 'La proposition part sous vingt-quatre heures, avec deux créneaux de formation et une décision datée.', ', délai en B17'),
            ('activer', 'Ensuite, un point d’étape à trente jours.', ', il est à l’écran'),
            ('salesops', 'Concrètement, le commercial y gagne une seule fiche à jour et un pipeline fiable chaque lundi.', ', le bandeau affiche « Pipeline complet ≥ 95 % chaque lundi »'),
            ('onboarding', 'Chacun forme sur son terrain : Adam en binôme, Vincent et Frantz à l’entrepôt, Floriane certifie, moi au simulateur.', '')], ''),
        ('kpi', 'Diapo 19 · Indicateurs', [
            ('kpi', 'Par exemple, si moins de la moitié des signés expédient sous trente jours, on revoit l’onboarding.', ', la grande carte l’affiche')],
         ' ; diapo 20 : ne rien couper')]


def cut_row(cp, label, cuts, tail):
    items, total = [], 0
    for sid, phrase, why in cuts:
        if norm(phrase) not in norm(NOTE[sid]):
            CHECK.append(f'phrase à couper absente de la note « {sid} » : {phrase}')
        if NUM[sid] < NUM[cp]:
            CHECK.append(f'coupe sur une diapo déjà passée au point « {label} » : {sid}')
        s = secs(phrase)
        total += s
        items.append(f'diapo {NUM[sid]} : sauter « {phrase} » (−{s} s{why})')
    txt = ' ; '.join(items) + tail
    txt = txt[0].upper() + txt[1:] + f'. Gain ≈ {total} s.'
    return f'<tr><td>{E(label)}</td><td><b>{start(cp)}</b></td><td>{E(txt)}</td></tr>'


CUTROWS = ''.join(cut_row(*c) for c in CUTS)
# Phrases à savoir mot pour mot (sauf la première, citée telle qu'à l'écran) : présentes dans le texte dit des notes.
for p in ['Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente reproductible et mesurable, pour recruter, activer et fidéliser nos adhérents ?',
          'Un point n’est accordé qu’avec sa preuve.', 'La vente finit au premier envoi, pas à la signature.',
          'Vingt-quatre bouteilles, trois cent soixante euros de transport et dix-sept euros de dossier, les taxes estimées et réglées d’avance, l’assurance en option, une livraison estimée à environ un mois. Ils repartent les mains libres.',
          'Le prospect n’achète pas seulement du transport : il cherche à réduire son risque.']:
    if norm(p).lower() not in ' '.join(said(s) for s in main).lower():
        CHECK.append(f'phrase à savoir absente des notes : {p}')
H.append(f'''<section><p class="ey">1 · L’ESSENTIEL EN UNE PAGE</p><h2>Vingt minutes pour montrer une méthode au travail, pas pour réciter un dossier</h2>
<div class="g3">
<div class="k"><p class="kn">18-19 min</p><p>visées, 20 au maximum. Le script est calé sur {tot} à 130 mots/minute ; la marge sert aux silences et aux regards.</p></div>
<div class="k"><p class="kn">{len(main)} + {len(backs)}</p><p>{len(main)} diapos présentées, lisibles en 3 secondes, puis {len(backs)} diapos de secours après « Merci », pour les questions.</p></div>
<div class="k"><p class="kn">15 min</p><p>de questions : le jury n’a pas lu le playbook ; il juge la communication et le traitement des objections.</p></div>
</div>
<h3>Le découpage, conforme au cahier des charges</h3>
<table class="t"><tr><th>Partie</th><th>Diapos</th><th>Fin visée</th><th>Cahier des charges</th></tr>
<tr><td><b>Introduction et diagnostic</b></td><td>1 à 7</td><td>{end('diagnostic')}</td><td>3 à 5 min</td></tr>
<tr><td><b>Parties 8 à 14, avec le cas fil rouge</b></td><td>8 à 19</td><td>{end('kpi')}</td><td>environ 15 min</td></tr>
<tr><td><b>Synthèse et ouverture</b></td><td>20</td><td>{end('conclusion')}</td><td>environ 1 min</td></tr></table>
<h3>Trois points de passage au chronomètre</h3>
<table class="t"><tr><th>À l’écran</th><th>Heure visée</th><th>Si je suis en retard</th></tr>
{CUTROWS}</table>
<p class="lead">Le minutage est théorique (130 mots par minute, plus 2 s par changement de diapo ; introduction jusqu’à {end('diagnostic')}, fin à {tot}) : il ne prouve pas la durée réelle. Les gains des coupes sont estimés au même rythme. Seules trois répétitions chronométrées à voix haute le confirmeront.</p>
<h3>Six phrases à savoir mot pour mot</h3>
<ol class="ph">
<li>« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. »</li>
<li>« Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente reproductible et mesurable, pour recruter, activer et fidéliser nos adhérents ? »</li>
<li>« Un point n’est accordé qu’avec sa preuve. »</li>
<li>« La vente finit au premier envoi, pas à la signature. »</li>
<li>« Vingt-quatre bouteilles, trois cent soixante euros de transport et dix-sept euros de dossier, les taxes estimées et réglées d’avance, l’assurance en option, une livraison estimée à environ un mois. Ils repartent les mains libres. »</li>
<li>« Le prospect n’achète pas seulement du transport : il cherche à réduire son risque. »</li>
</ol>
<div class="warn"><p class="wl">CE QUE JE NE DIS JAMAIS</p>
<p>Que le cas est une vente réelle, ou qu’un compte du top 10 suit cette trajectoire · « souvent » à propos de la scène de Houston · la capture USA du dossier (grille 2025) · un nom ou un CA de client · « assurance incluse », « tout compris », « garanti » · « 210 € » ou « 360 € » comme prix complet (c’est le transport) · « la valeur résiste » (l’OIV dit l’inverse pour 2025) · « 145 adhérents actifs » (ce sont des signés) · « j’ai interviewé » (échanges écrits) · un objectif présenté comme un résultat · les projets au présent · un taux de droits US de mémoire · les 40 000 € comme un gain (c’est une simulation) · « les seuls », « les premiers », « uniques », « exclusifs » pour parler de Planet Aura.</p></div>
</section>''')

# ---------- le cas en une page ----------
# En v5, « à l'écran » = visible sur la diapo ; « dit » = passé à l'oral (notes) ; Bn = passé en secours.
GESTES = [('1 · Qualifier un prospect', '8', 'cinq critères et score PA-FIT 45 → 60 → 85 à l’écran ; « un point par preuve », dit'),
          ('2 · Choisir son interlocuteur', '9 · 12', 'le vigneron décide, la responsable caveau utilise, le client final paie ; à chacun sa crainte et son discours'),
          ('3 · Préparer sa prospection', '12', 'site, e-shop, avis, prix, saisonnalité ; cadence de terrain J1, J+4, J+10, visite'),
          ('4 · Conduire l’entretien SPIN', '13', 'une question complète par famille (S, P, I, N) ; le rôle de chacune, dit'),
          ('5 · Identifier les besoins', '13', 'la reformulation à trous, validée par le prospect'),
          ('6 · Présenter une solution adaptée', '10 · 14', 'problème → besoin → solution → bénéfice → preuve ; la grille officielle 2026'),
          ('7 · Traiter les objections', '14 (+ B14)', '« c’est cher » en quatre temps, une seule preuve'),
          ('8 · Accompagner l’adhésion', '15', 'signature en ligne, SEPA, cartons ; formation caveau à J+5 ; le premier lot de cartons, dit'),
          ('9 · Déclencher le premier envoi', '15', 'le premier envoi suivi (le couple texan) ; la ligne d’arrivée'),
          ('10 · Suivre les résultats', '19', 'l’étiquette « Domaine activé », KPI, point zéro, revue mensuelle ; la prochaine action datée dans HubSpot, dite')]
CASE = [('1 · Qualifier', '8 (+ B16)', 'Domaine provençal avec caveau, 20+ étrangers / semaine en saison, panier ~300 €, e-shop, clientèle US majoritaire, tiers B (60-100 envois/an). À l’écran : caveau, clientèle US, 60-100 envois/an ; étrangers par semaine, panier et tiers : secours B16', 'Sourcé (chap. 11)'),
        ('', '', 'Score PA-FIT : 45 au départ (nurture), 60 avec l’échéance (P2 : cadence), 85 avec le décideur et la douleur (P1)', 'Illustratif (barème réel, B2)'),
        ('2 · Prospecter', '12', 'Préparer ; viser le décideur et l’utilisatrice ; cadence J1, J+4, J+10, visite ; script d’appel et e-mail 1 de l’annexe E', 'Règle (chap. 10, 11, annexe E)'),
        ('3 · Découvrir', '13', 'Rendez-vous de 45 min : découverte SPIN des minutes 5 à 20, démo 20-30 (dits ; trame unique au chap. 11) ; tunnel 1 du vigneron, une question par famille ; reformulation à trous ; phrase de bénéfice notée mot pour mot (dite)', 'Règle ; réaction du vigneron illustrative'),
        ('4 · Proposer', '14', 'Grille officielle 2026 (document réel) ; 24 bouteilles = 360 € de transport, 15 €/btl ; objection « c’est cher » en 4 temps ; simulation : 40 000 € de ventes potentiellement perdues', 'Grille 2026 ; simulation'),
        ('5 · Activer', '15 (+ B16)', 'Signature en ligne, SEPA, cartons ; formation J+5 ; premier envoi ; point J+30 ; premier lot de cartons, dit ; score de santé : seulement si on le demande, secours B16', 'Règle (chap. 16)'),
        ('6 · Suivre', '19 (+ B16)', 'À l’écran : l’étiquette « Domaine activé » sur la carte Activation J+30. Dit : le domaine serait activé dans HubSpot, avec une prochaine action datée, l’appel du commercial à J+30. Étapes 6 et 7 du cas : secours B16', 'Illustratif (format sourcé)')]
H.append('<section><p class="ey">2 · LE CAS FIL ROUGE EN UNE PAGE</p><h2>Un parcours type, pas une vente réalisée : savoir dire ce qui est sourcé</h2>'
         '<p class="lead">Source : chapitre 11, « le fil rouge : une vente de bout en bout ». Les prix viennent de la grille 2026, les étapes des règles du playbook. Aucun domaine n’est nommé, aucun chiffre client n’est cité. Un seul panier dans tout l’oral : 24 bouteilles, 360 € de transport. En v5, l’écran ne garde que l’essentiel de chaque étape : le reste est dit ou en secours B16.</p>'
         '<table class="t"><tr><th>Étape</th><th>Diapo</th><th>Ce que montre le cas</th><th>Statut</th></tr>'
         + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in CASE) + '</table>'
         '<h3>Les dix gestes du commercial, et où le jury les voit</h3><table class="t"><tr><th>Geste</th><th>Diapo</th><th>Ce qu’il montre</th></tr>'
         + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in GESTES) + '</table>'
         '<div class="warn"><p class="wl">LA PHRASE DE SÉCURITÉ</p><p>« C’est un parcours type, écrit dans le playbook : les prix sont ceux de notre grille, les situations sont illustratives. Ce qui est réel, ce sont les outils que je vous montre. »</p></div></section>')

# ---------- grille de conformité ----------
GRID = [
    ('Débute par un « grab attention » (Start with why)', 'Animation', '2', 'Houston : 2 bouteilles pleines sur 24, le silence, la question ; « notre pourquoi » à l’écran et dit à voix haute.'),
    ('Présente de manière rythmée et dynamique', 'Animation', 'toutes', f'Une idée par diapo, lisible en 3 secondes : un message (le titre), un point focal ; un cas qui avance ; des transitions annoncées ; {len(main)} diapos en 18-19 min.'),
    ('Bon niveau de langage, vocabulaire métier', 'Animation', 'toutes', 'DDP, PA-FIT, nurture, cadence et SPIN définis à l’oral au premier usage ; three-tier, POA, CIVC et ISTA 3A expliqués à l’écran (diapo 4) ; DA/EMCS et accises, cités à l’écran : définition prête au glossaire du guide.'),
    ('Support graphiquement agréable et dynamique', 'Animation', 'toutes', 'Un point focal par diapo, peu de mots, gros caractères ; document et capture réels (grille officielle 2026, tableau de bord Planet’Connect), photo de l’équipe, pages réelles du playbook, frises, score, escalier, bandeau du cas.'),
    ('Grammaire et orthographe', 'Animation', 'toutes', 'Typographie française (espaces insécables ; '
     + (f'aucune espace sécable avant : ; ? ! % » sur les {len(deck["order"])} diapos, contrôle automatique' if not TYPO
        else f'contrôle automatique sur les {len(deck["order"])} diapos : espace sécable à corriger en {", ".join(TYPO)}')
     + '), relectures croisées, rendu vérifié diapo par diapo ; dernière relecture à voix haute la veille, phrase anglaise de la diapo 9 comprise.'),
    ('Respecte le temps imparti (20 min max)', 'Animation', '—', f'Script à {tot}, introduction jusqu’à {end("diagnostic")} ; trois points de passage ; coupes prévues, chiffrées en secondes.'),
    ('Titres précis et impactants dans le sommaire', 'Argumentation', '3', 'Cinq étapes titrées par leur idée : « La vente finit au premier envoi », « Outiller, former, mesurer » ; à droite, le renvoi « → la problématique » (énoncée diapo 7) et les trois enjeux, reliés aux parties 8 à 14 du cahier des charges ; le contenu de chaque étape (ICP et personas, processus et SPIN, ressources et indicateurs), dit.'),
    ('Introduction qui amène le sujet', 'Argumentation', '2 à 7', 'Scène → marché → entreprise → offre → diagnostic → problématique et trois enjeux.'),
    ('Analyse le marché en lien avec l’entreprise', 'Argumentation', '4 (+ 5)', 'Trois bascules chiffrées et cinq contraintes pour expédier chez un particulier américain : « Pour le vigneron, ce sont des freins. Pour nous, c’est le métier. » Chaque bascule traduite pour nous, à l’oral ; part USA de nos envois (64,5 %) à l’écran, diapo 5.'),
    ('Présente l’entreprise (organigramme, CA, offre, concurrence, cibles)', 'Argumentation', '5 à 7 (+ B9, B8)', 'Photo de l’équipe (13 personnes, filiale comprise) et « qui vend, qui décide », avec les interlocuteurs du commercial, dits (direction, exploitation, administration) ; CA ×4,7, 262 adhérents, marchés (diapo 5) ; offre, concurrence et positionnement « Notre place » (diapo 6) ; forces et fragilités (diapo 7) ; cibles : diapo 8 ; organigramme complet en B9, SWOT complet et horizons stratégiques en B8.'),
    ('Processus de vente et tunnels SPIN', 'Argumentation', '11 à 15 (+ B17, B4)', 'Sept étapes et leur preuve à l’écran ; responsable, délai et outil : à l’écran pour l’étape 6, dits pour le principe, détaillés étape par étape en B17 ; durées de cycle, dites ; prospection ; tunnel SPIN du vigneron, question par question ; second tunnel en B4 ; proposition ; activation.'),
    ('Ressources précises, réalistes, échéancées, chiffrées', 'Argumentation', '16 (+ B13)', 'Ce que j’ai créé (trois pages réelles) ; trois premiers chantiers à l’écran : mois, budget, responsable, temps ; 800 € sur 3 000 € ; 80 h de temps interne, dites ; le principe du critère de passage à l’écran, chaque critère et les six chantiers en B13.'),
    ('Sales Ops mises en place et objectif de chacune', 'Argumentation', '17, 18', 'Six éléments autour de HubSpot, chacun avec son rôle et son statut (existant, à déployer, ma contribution) ; règles communes marketing-ventes et rituels proposés (bandeau ; détail dit) ; onboarding (diapo 18).'),
    ('SPB existant : améliorations justifiées', 'Argumentation', '8, 11, 15-17, 19 (+ B15)', 'Pas de playbook avant : chaque décision est justifiée, par le bandeau Constat → Ma décision → Ce que l’on mesure (diapos 11, 15, 16, 17, 19) ou par « Ma recommandation » (diapo 8) ; existant et apport distingués par les étiquettes.'),
    ('Présente les indicateurs de performance', 'Argumentation', '19 (+ B6)', 'Constaté et objectif côte à côte ; activation à J+30 : source, fréquence, responsable et action à l’écran ; les trois autres : cible à l’écran, le reste en B6 ; revue mensuelle ; un exemple de décision.'),
    ('Synthèse en lien avec les enjeux', 'Argumentation', '20 (+ B15)', 'Réponse enjeu par enjeu, bénéfice visé et limite à l’écran ; apport et difficulté, dits (détail en B15).'),
    ('Ouverture', 'Argumentation', '20 (+ B8)', 'Diversifier (UK, UE dont Scandinavie, Canada, Japon) pour réduire la dépendance aux USA ; lecture fin décembre ; entretiens T1 2027 (dits diapo 9, B1) ; horizons stratégiques du dossier en B8.'),
]
AUDIT = [
    ('Tous les critères de la grille sont couverts', 'Oui : tableau ci-dessus.'),
    ('Découpage temporel conforme', f'Introduction {end("diagnostic")}, parties 8 à 14 jusqu’à {end("kpi")} ({AE.mmss(AE.tosec(end("kpi")) - AE.tosec(end("diagnostic")))} de texte, un peu sous les 15 min indicatives ; les silences s’y ajoutent), synthèse jusqu’à {end("conclusion")}.'),
    ('Temps total ≤ 20 min', f'{tot} de texte, soit 18 à 19 min avec les silences.'),
    ('Temps suffisant pour les parties opérationnelles', 'Douze diapos sur vingt, la majorité du temps.'),
    ('ICP et personas distingués', 'Diapo 8 (l’entreprise), diapo 9 (les personnes) ; la phrase le dit.'),
    ('Tunnels SPIN réellement présentés', 'Diapo 13 : le tunnel du vigneron, question par question ; tunnel 2 et banque des 8 profils en B4.'),
    ('Ressources précises, réalistes, datées, chiffrées', 'Diapo 16 : mois, budget, responsable et temps des trois premiers chantiers ; leurs critères de passage et les six chantiers en B13.'),
    ('Sales Ops expliquées avec leurs objectifs', 'Diapo 17 : rôle et statut de chaque outil ; règles proposées.'),
    ('Indicateurs avec méthode de suivi', 'Diapo 19 : source, fréquence, responsable et action de l’activation à J+30 ; les autres indicateurs en B6 ; revue mensuelle.'),
    ('Marché relié aux enjeux de Planet Aura', 'Diapo 4 : chaque bascule traduite pour nous, à l’oral (un vin qu’on veut protéger ; notre premier marché, près des deux tiers de nos envois, recule ; le caveau devient un canal d’export) ; part USA à l’écran, diapo 5.'),
    ('Organisation, offre, concurrence présentées', 'Diapos 5 et 6 (+ B9, B3, B8).'),
    ('Apport personnel démontré', 'Étiquettes sur chaque diapo opérationnelle ; diapo 20 ; B15.'),
    ('La synthèse répond à la problématique', 'Diapo 20 : « une méthode reproductible et mesurable », enjeu par enjeu.'),
    ('Difficultés et ouverture pertinentes', 'Diapo 20 : la difficulté, dite (des chiffres qui divergeaient → une seule source, datée ; B15) ; l’ouverture à l’écran : diversifier.'),
    ('Chiffres cohérents avec le mémoire', 'Revue factuelle et contre-vérification sur les sources ; un seul panier pour le cas.'),
    ('Diapositives lisibles, variées, professionnelles', f'Lisibles en 3 secondes : un message (le titre), un point focal ; {AE.LO} à {AE.HI} mots visibles par diapo de contenu, sauf deux écarts assumés : personas ({AE.VIS["personas"]}) et SPIN ({AE.VIS["spin"]}, les quatre questions en entier) ; textes ≥ 24 px ; banc de rendu sans débordement ni chevauchement, y compris à texte agrandi.'),
    ('Le discours complète le support sans le lire', 'Ce qui a quitté l’écran est dit (notes) ou en secours, avec le renvoi sous chaque vignette du script ; les notes disent ce que l’écran ne dit pas.'),
    ('Diapositives de secours adaptées', f'{len(backs)} secours, dont B15 (l’apport), B16 (le cas) et B17 (le processus, étape par étape).'),
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
H.append('<section><p class="ey">4 · LE SCRIPT MINUTÉ</p><h2>Ce que je dis, ce que je montre, diapo par diapo</h2><p class="lead">Les mêmes notes figurent en mode présentateur. Elles sont écrites pour l’oral : les apprendre par idées, jamais mot à mot, sauf les six phrases de la page 2. En italique : les rappels de régie, à ne pas dire. En version 5, l’écran ne porte que le message et son point focal : ce qui n’y est plus se dit (notes) ou s’ouvre en secours (renvois sous chaque vignette).</p>' + ''.join(script) + '</section>')

# ---------- transitions et messages ----------
# Transitions : chaque phrase est le début réel (mot pour mot) du texte dit de la diapo suivante ; « … » = suite non citée.
TRANS = [('Couverture → accroche', 'accroche', 'Un couple de Houston voulait vingt-quatre bouteilles. Ils sont repartis avec deux.'),
         ('Accroche → sommaire', 'sommaire', 'Pour la lever, j’ai construit le Sales Playbook de Planet Aura : le référentiel de vente de l’équipe.'),
         ('Sommaire → comprendre', 'marche', 'Première étape : comprendre.'),
         ('Marché → entreprise', 'entreprise', 'Planet Aura est née à Castres en 2019.'),
         ('Entreprise → offre', 'offre', 'Ce que nous vendons tient en un circuit…'),
         ('Offre → diagnostic', 'diagnostic', 'Voici mon diagnostic.'),
         ('Diagnostic → cibler', 'icp', 'Deuxième étape : cibler.'),
         ('ICP → personas', 'personas', 'Mais l’ICP décrit l’entreprise, et une entreprise n’achète pas : ce sont des personnes.'),
         ('Personas → vendre', 'solutions', 'Troisième étape : vendre. Chaque solution répond à un problème, et doit se prouver.'),
         ('Solutions → processus', 'processus', 'Pour aller du premier contact au premier envoi, sept étapes.'),
         ('Processus → cas', 'prospecter', 'Revenons à notre domaine.'),
         ('Prospecter → SPIN', 'spin', 'Le rendez-vous dure quarante-cinq minutes.'),
         ('SPIN → proposer', 'proposer', 'Vient la proposition : au rendez-vous, j’ouvre le simulateur sur ses vins…'),
         ('Proposer → activer', 'activer', 'Quatrième étape : activer, car la vente finit au premier envoi, pas à la signature.'),
         ('Activer → piloter', 'ressources', 'Cinquième étape : piloter, pour transmettre et mesurer.'),
         ('Ressources → Sales Ops', 'salesops', 'Les outils existaient avant le playbook…'),
         ('Sales Ops → onboarding', 'onboarding', 'La transmission, c’est la vraie preuve d’un playbook : il doit permettre à un nouveau commercial de vendre sans moi.'),
         ('Onboarding → indicateurs', 'kpi', 'Enfin, mesurer.'),
         ('Indicateurs → conclusion', 'conclusion', 'Je reviens à ce couple de Houston.')]
for lab, sid, ph in TRANS:
    if not said(sid).startswith(norm(ph.rstrip('…'))):
        CHECK.append(f'transition « {lab} » : ce n’est pas le début de la note « {sid} »')
TEST = [('2', 'La première phrase, puis le silence', 'Tenir une vraie seconde de silence sans regarder l’écran.'),
        ('7', 'La problématique', 'La lire lentement, une seule fois, en regardant le jury.'),
        ('8', '45 → 60 → 85', 'Enchaîner les trois preuves sans hésiter ; montrer les parties hachurées des barres.'),
        ('14', '360 €, 15 €, puis la simulation à 40 000 €', 'Les nombres en lettres prennent du temps ; marquer la pause avant « ce n’est pas une promesse ».'),
        ('16', 'Les trois chantiers, 800 € sur 3 000 €', 'Ne pas lire les cartes : dire l’ordre et sa raison.'),
        ('19', 'Constaté, puis objectif', 'Montrer à gauche, puis à droite ; un seul exemple de décision.'),
        ('20', 'Bénéfices, limite, dernière phrase', 'L’apport, la difficulté et le second bénéfice (un commercial certifié en un mois) ne sont pas à l’écran : les dire sans le chercher ; finir en regardant le jury.')]
# Messages : les titres des diapos v5, à l'écran.
MSG = [('Comprendre', 'L’export se complique : c’est notre métier ; nous vendons de la sécurité, pas du transport ; une croissance réelle, une vente encore informelle.'),
       ('Cibler', 'Le score ne juge pas la taille : il juge la preuve ; un domaine, trois interlocuteurs, trois discours.'),
       ('Vendre', 'Chaque solution répond à un problème, et se prouve ; l’appel ne vend pas : il obtient la démo ; le prospect chiffre lui-même sa perte ; 15 € de transport par bouteille, payés par son client.'),
       ('Activer', 'La vente finit au premier envoi ; le commercial en reste responsable.'),
       ('Piloter', 'Trois chantiers d’abord ; une donnée, un propriétaire, une décision ; opérationnel en 90 jours ; mesuré ou espéré ? Chaque KPI déclenche une action.')]
H.append(f'<section><p class="ey">5 · LES TRANSITIONS ET LES MESSAGES CLÉS</p><h2>Le fil qui relie les {"vingt" if len(main) == 20 else len(main)} diapos</h2>'
         '<p class="lead">Chaque phrase de transition est le début exact de la note de la diapo suivante : la savoir, c’est savoir enchaîner.</p>'
         '<table class="t tr"><tr><th>Passage</th><th>La phrase de transition</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>« {E(c)} »</td></tr>' for a, b, c in TRANS) + '</table>'
         '<h3>Un message à faire retenir par étape</h3><table class="t"><tr><th>Étape</th><th>Message</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in MSG) + '</table>'
         '<h3>Les passages à tester à voix haute</h3><p class="lead">Le minutage du script est théorique. Ces passages, chiffrés ou rythmés, sont ceux qui débordent le plus souvent à l’oral : les chronométrer séparément.</p>'
         '<table class="t"><tr><th>Diapo</th><th>Passage</th><th>Ce qu’il faut vérifier</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in TEST) + '</table></section>')

# ---------- chiffres et définitions ----------
NUMS = [('×4,7', 'CA de 2021 à 2025 (1,15 M€ en 2025, +11,6 %) ; +18,7 % au 24/09/2026', 'Constaté, dashboards 24/09/2026'),
        ('262 · 6 643', 'adhérents · envois sur 12 mois, dont 64,5 % vers les USA et 18,6 % en France', 'Constaté'),
        ('13 · fin 2025', 'personnes, filiale comprise · arrivée d’Adam, le seul commercial dédié', 'Constaté'),
        ('~145', 'adhérents signés en 12 mois (signés, pas actifs ; ne pas les comparer aux « 10 actifs/mois » du chap. 09)', 'Constaté'),
        ('448 / 710', 'prospects non qualifiés sur 710 comptes au CRM', 'Constaté'),
        ('89,8 % · 1,45 %', 'envois assurés (option 3 %, jusqu’à 20 000 €/envoi) · commandes annulées', 'Constaté'),
        ('4,65/5 · 4,8/5', 'satisfaction 2024 (23 réponses) · avis Google (296, sept. 2026)', 'Constaté'),
        ('105 → 510 €', 'groupage USA, 1-3 à 36 bouteilles ; 24 btl = 360 € (15 €/btl) ; + taxes estimées, 17 € de dossier', 'Grille 2026'),
        ('Droits US', 'jamais de taux cité à l’oral ; le dossier indique 15 % d’août 2025 à février 2026, puis 10 % ; vérification externe du 25/10/2026 : sources contradictoires depuis juillet 2026 (10 % ou 15 %) ; le simulateur fait foi', 'Externe, à vérifier la veille'),
        ('208 Mhl · 3,56 €/l', 'consommation mondiale 2025 (−2,7 %) · prix moyen à l’export (OIV)', 'Externe'),
        ('−21 % · 5,4 M', 'exports FR vers les USA en 2025 (FEVS) · œnotouristes étrangers en 2023 (Atout France)', 'Externe'),
        ('70 · 47 · 15', 'contacts, réponses d’enquête, avis : l’étude des personas (oct. 2026)', 'Constaté'),
        ('17 · 800 € / 3 000 € · 80 h', 'ressources (13 validées, 4 à créer : « 4 ressources sur 17 manquent », diapo 16) · budget des trois premiers chantiers / plafond de dépenses externes · temps interne de ces trois chantiers (24 + 36 + 20 h, dit) ; ≈ 200 h pour la feuille de route complète (calcul sur B13)', 'Constaté (répertoire) · objectif (budget, plafond) · calcul'),
        ('1-3 · 4-8 · 6-12 semaines', 'durée de cycle : dossier standard (7 à 21 j, B6) · à froid · maison de champagne ; dits à la diapo 11, médiane réelle après 90 jours', 'Objectif · repères de terrain'),
        ('≥ 70 % · > 60 % · 40–60 %', 'activation à J+30 · adhérents actifs · taux de gain', 'Objectif'),
        ('75 · 55 · 35', 'seuils PA-FIT : priorité active · cadence · nurture', 'Règle'),
        ('40 000 € → 10 000 €', 'ventes potentiellement perdues par le domaine du cas : 20 étrangers/sem. × 1 sur 3 × 300 € × 20 sem. ; si un quart était récupéré, ≈ 10 000 €, pour 110 € de cartons (exemple du playbook : 30 visiteurs → 60 000 €)', 'Simulation, jamais un gain')]
GLOSS = [('Commissionnaire de transport', 'Organise le transport en son nom propre et répond du résultat de bout en bout (obligation de résultat, CGS art. 2).'),
         ('DDP / DAP', 'Taxes payées d’avance par le client (DDP) ou à l’arrivée par le destinataire (DAP).'),
         ('Three-tier system', 'Système américain importateur → grossiste → détaillant ; nos licences couvrent les deux premiers niveaux.'),
         ('POA', 'Procuration de dédouanement exigée aux USA au-delà de 2 100 $ ; formalité normale, jamais à éviter.'),
         ('CIVC', 'Comité Champagne : délivre le certificat d’origine obligatoire hors UE.'),
         ('ISTA 3A', 'Norme de test d’emballage (chute, vibration) de nos cartons.'),
         ('DA / EMCS · accises', 'Documents de circulation et de douane des produits sous accises, édités et gérés par Planet Aura · droits perçus sur l’alcool à l’arrivée ; en DDP, estimés et payés d’avance.'),
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
         + f'<h3>Les {len(hard)} questions difficiles : la méthode et sa preuve</h3><div class="warn"><p class="wl">LA RÉPONSE COURTE, À SAVOIR PAR CŒUR</p><p>{E(SHORT)}</p></div>' + ''.join(qa_card('D', *q) for q in hard)
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
       ('Des durées de cycle à mesurer', 'Une à trois semaines pour un dossier standard (objectif, 7 à 21 j en B6) ; quatre à huit semaines à froid, six à douze en champagne (repères de terrain) : médiane réelle après 90 jours.'),
       ('Un saut de CA non expliqué', 'Le +224 % de 2022 n’est pas documenté : « à confirmer avec la direction ».'),
       ('Une formulation à corriger', 'L’annexe F décrit l’assurance comme incluse dans les frais administratifs ; la pratique est une option à 3 % : à remonter pour la grille 2027.'),
       ('Une dépendance sans cible', 'Part USA 64,5 %, suivie chaque trimestre, sans objectif chiffré de diversification.'),
       ('Des droits US incertains', 'Le dossier indique 10 % depuis février 2026 ; des sources externes récentes divergent (10 % ou 15 %) : ne jamais citer un taux de mémoire, renvoyer au simulateur.')]
H.append('<section><p class="ey">9 · LIMITES ET RÉSERVES</p><h2>Les dire avant qu’on me les oppose</h2><p class="lead">Une limite annoncée avec son plan devient une preuve de lucidité ; découverte par le jury, elle devient une faiblesse.</p>'
         '<table class="t"><tr><th>Limite</th><th>Ce que je dis, et ce qui est prévu</th></tr>' + ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>' for a, b in LIM) + '</table></section>')

selfeval, BILAN = AE.HTML, AE.BILAN
H.append(f'<section><p class="ey">10 · AVANT / APRÈS</p><h2>Ce qui a changé dans la version finale, et pourquoi</h2><p class="lead">La structure, le cas fil rouge, les cinq étapes et les chiffres vérifiés sont conservés. La version 4 a traité la densité de quatre diapos, la justification des décisions, la prudence sur les chiffres, la fluidité du script et la préparation aux questions difficiles. La version 5, du 26 octobre 2026, rend chaque diapo lisible en 3 secondes : un message (le titre), un point focal, peu de mots, aucun chevauchement ; le détail retiré de l’écran est passé à l’oral ou en secours, dont une nouvelle B17 (le processus, étape par étape).</p>{BILAN}</section>')
H.append(f'<section><p class="ey">11 · L’AUTOÉVALUATION ET L’ÉVALUATION CRITIQUE</p><h2>Après les questions : un bilan honnête, en deux minutes</h2><p class="lead">Le jury demande souvent une autoévaluation avant le débrief. Deux forces, deux axes de progrès avec leur plan, une phrase de conclusion.</p><div class="g2"><div class="ab"><p class="abl" style="color:#20768B">POINTS FORTS</p>{forts}</div><div class="ab"><p class="abl" style="color:#722F45">AXES D’AMÉLIORATION</p>{axes}</div></div><div class="concl"><p>{concl}</p></div>{selfeval}</section>')

H.append('''<section><p class="ey">12 · LES CHECK-LISTS</p><h2>Préparer, vérifier, arriver serein</h2>
<div class="g3c">
<div class="ck"><p class="ckl">LA SEMAINE AVANT</p><ul>
<li>Trois répétitions complètes au chronomètre, dont une filmée ; viser 18 à 19 minutes ; noter l’heure réelle aux trois points de passage.</li>
<li>Tester à voix haute les passages chiffrés (diapos 8, 14, 16, 19) : un nombre écrit en lettres se dit plus lentement qu’il ne se lit.</li>
<li>Répéter sur les diapos v5 : ce qui a quitté l’écran doit être dit sans le chercher ; savoir ouvrir chaque secours renvoyée par le script, B17 comprise.</li>
<li>Une répétition des questions avec quelqu’un qui joue le jury, pièges et questions sur le cas compris.</li>
<li>Savoir refaire à voix haute : le score 45 → 60 → 85, la simulation des ventes potentiellement perdues (20 × 1/3 × 300 € × 20 = 40 000 €, jamais un gain), 24 bouteilles = 360 €.</li>
<li>Faire valider par la direction la réponse sur l’assurance (annexe F) et le statut des rituels.</li>
<li>Lire l’annexe W une dernière fois : le discours sur l’IA doit lui correspondre.</li>
<li>Télécharger le deck en PDF et en PPTX ; tester le mode présentateur.</li>
</ul></div>
<div class="ck"><p class="ckl">LA VEILLE</p><ul>
<li>Vérifier au simulateur et auprès de la direction le taux des droits US du jour : les sources externes divergent depuis juillet 2026.</li>
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
for c in CHECK:
    print('ATTENTION', c)
print('guide.html ok', len(main), len(backs), len(top), len(traps), len(cas))
