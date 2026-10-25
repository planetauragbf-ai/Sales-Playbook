# Génère le guide de soutenance (HTML imprimé en PDF A4) à partir des diapos, de leurs notes et de la banque de questions.
import os, re, json, html, base64, io
from PIL import Image

ORAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
DECK = os.environ.get('DECK_DIR', 'deck')
RENDU = os.environ.get('RENDU_DIR', 'rendu')
SL = os.path.join(ORAL, DECK, 'project', 'slides')
OUT = os.path.join(ORAL, 'guide')
deck = json.load(open(os.path.join(ORAL, DECK, 'project', 'deck.json')))
E = html.escape

def thumb(sid, w=560):
    im = Image.open(os.path.join(ORAL, RENDU, f'{sid}.png')).convert('RGB')
    im = im.resize((w, int(w * 1080 / 1920)), Image.LANCZOS)
    b = io.BytesIO(); im.save(b, 'JPEG', quality=82)
    return 'data:image/jpeg;base64,' + base64.b64encode(b.getvalue()).decode()

def slide_info(sid):
    s = open(os.path.join(SL, f'{sid}.html')).read()
    aside = re.search(r'<aside>(.*?)</aside>', s, re.S).group(1).strip()
    body = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
    h = re.search(r'<h2[^>]*>(.*?)</h2>', body, re.S)
    title = re.sub(r'<[^>]+>', '', h.group(1)) if h else None
    m = re.match(r'\[([^\]]*)\]\s*', aside)
    timing = m.group(1) if m else ''
    aside = aside[m.end():] if m else aside
    return title, timing, aside

TITLES = {'cover': 'Couverture', 'accroche': 'Accroche : le couple de Houston', 'sommaire': 'Sommaire', 'cloture': 'Clôture : retour au caveau'}

# ---------- banque de questions : mise à jour après les corrections du dossier ----------
J = open(os.path.join(ORAL, 'jury.md')).read()
FIX = []  # jury.md est désormais corrigé à la source (refonte du 25/10/2026)
for a, b in FIX:
    if a not in J:
        raise SystemExit('FIX introuvable : ' + a[:70])
    J = J.replace(a, b)
J = J.replace('une filiale licenciée à New York', 'une filiale à New York titulaire des licences américaines')
J = re.sub(r'content-emma/(\d\d)\.md', r'chap. \1', J)
J = re.sub(r'content-emma/([A-Z])\.md', r'annexe \1', J)
J = J.replace('content-emma/avant.md', 'avant-propos').replace('fiches-emma.js', 'annexe A')
J = J.replace(' ; plan-oral.md (grille : cas SPB existant sans objet)', '')

def parse_qs(block):
    qs = []
    for m in re.finditer(r'^### (\d+)\. (.*?)\s*_\((.*?)\)_\s*\n(.*?)(?=^### |\Z)', block, re.S | re.M):
        n, q, prob, body = m.groups()
        fields = dict(re.findall(r'^- (Pourquoi|Réponse|Preuve|Diapo de secours|Piège) : (.*)$', body, re.M))
        qs.append((n, q, prob, fields))
    return qs

top = parse_qs(J.split('# Questions pièges')[0])
traps = parse_qs(J.split('# Questions pièges')[1].split('# Diapos de secours')[0])
auto = J.split('# Autoévaluation')[1]
assert len(top) == 20 and len(traps) == 5, (len(top), len(traps))

def qa_card(prefix, n, q, prob, f):
    pc = {'très probable': '#722F45', 'probable': '#8A6A33', 'possible': '#20768B'}.get(prob, '#20768B')
    rows = ''.join(f'<div class="qf"><p class="ql">{E(k)}</p><p class="qv">{E(f[k])}</p></div>' for k in ['Pourquoi', 'Réponse', 'Preuve', 'Diapo de secours', 'Piège'] if k in f)
    return f'''<div class="qa"><div class="qh"><p class="qn">{prefix}{n}</p><p class="qq">{E(q)}</p><p class="qp" style="color:{pc};border-color:{pc}">{E(prob)}</p></div>{rows}</div>'''

# ---------- script minuté ----------
main = [s for s in deck['order'] if not s.startswith('b')]
backs = [s for s in deck['order'] if s.startswith('b')]
script = []
for k, sid in enumerate(main, 1):
    title, timing, aside = slide_info(sid)
    title = TITLES.get(sid, title)
    paras = [p.strip() for p in aside.split('\n') if p.strip()]
    spoken = ''.join(f'<p class="cue">{E(p)}</p>' if p.startswith('(') else f'<p>{E(p)}</p>' for p in paras)
    script.append(f'''<div class="sl"><div class="slh"><p class="sn">{k}</p><p class="st">{E(title)}</p><p class="stime">{E(timing)}</p></div>
<div class="slb"><img src="{thumb(sid)}" alt=""><div class="say">{spoken}</div></div></div>''')

backup_rows = []
JB = J.split('# Diapos de secours')[1].split('# Autoévaluation')[0]
REPOND = dict(re.findall(r'^### (B\d+) — .*?\n.*?- Répond à : (.*?)$', JB, re.S | re.M))
for sid in backs:
    title, _, aside = slide_info(sid)
    b = sid.upper()
    backup_rows.append(f'<tr><td class="bn">{b}</td><td><b>{E(title)}</b></td><td>{E(REPOND.get(b, ""))}</td></tr>')

def md_list(sec):
    items = re.findall(r'^- (.*)$', sec, re.M)
    return '<ul>' + ''.join(f'<li>{E(i)}</li>' for i in items) + '</ul>'
forts = md_list(auto.split('**Points forts**')[1].split("**Axes d'amélioration**")[0])
axes = md_list(auto.split("**Axes d'amélioration**")[1].split('**Conclusion**')[0])
axes = axes.replace(" Quelques incohérences de version repérées après livraison (calendrier de la feuille de route, poids des ICP, renvois du sommaire) seront corrigées dans la version de novembre.", " Quelques incohérences de version (calendrier de la feuille de route, poids des ICP, renvois du sommaire) ont été repérées et corrigées avant l&#x27;oral.")
concl = E(auto.split('**Conclusion** :')[1].strip())

def start_of(sid):
    return slide_info(sid)[1].split('→')[0].strip()
def end_of(sid):
    return slide_info(sid)[1].split('→')[1].strip()
T_ICP, T_SPIN, T_SYN, T_END = start_of('icp'), start_of('spin'), start_of('synthese'), end_of('cloture')
N_MAIN, N_BACK = len(main), len(backs)

CSS = open(os.path.join(os.path.dirname(__file__), 'guide.css')).read()
H = []
H.append(f'''<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Guide de soutenance</title><style>{CSS}</style></head><body>
<section class="cover">
<p class="ey">SOUTENANCE ORALE · BLOC 2 · EURIDIS</p>
<h1>Guide de soutenance</h1>
<p class="sub">Sales Playbook Planet Aura</p>
<p class="who">Emma Soares Britschgy · version du 25 octobre 2026</p>
<div class="cbox"><p><b>Ce que contient ce guide</b></p><p>1. L’essentiel en une page · 2. La grille, diapo par diapo · 3. Le script minuté · 4. Les questions du jury et leurs réponses · 5. Les diapos de secours · 6. L’auto-évaluation · 7. Les check-lists de préparation</p></div>
<p class="conf">Document de travail personnel : ne pas remettre au jury, ne pas diffuser.</p>
</section>''')

H.append(f'''<section><p class="ey">1 · L’ESSENTIEL EN UNE PAGE</p><h2>Vingt minutes pour montrer une méthode, pas pour réciter un dossier</h2>
<div class="g3">
<div class="k"><p class="kn">20 min</p><p>maximum, viser 18. Le script est calé sur {T_END} à 130 mots/minute : la marge sert aux silences et aux regards.</p></div>
<div class="k"><p class="kn">{N_MAIN} + {N_BACK}</p><p>diapos présentées, plus {N_BACK} diapos de secours après « Merci », pour les questions.</p></div>
<div class="k"><p class="kn">15 min</p><p>de questions. Le jury n’a pas lu le playbook : il juge la communication et le traitement des objections.</p></div>
</div>
<h3>Trois points de passage au chronomètre</h3>
<table class="t"><tr><th>À l’écran</th><th>Heure visée</th><th>Si je suis en retard</th></tr>
<tr><td>Diapo 9 · ICP</td><td><b>{T_ICP}</b></td><td>Raccourcir la concurrence : le statu quo, le trio, le prix assumé.</td></tr>
<tr><td>Diapo 13 · SPIN</td><td><b>{T_SPIN}</b></td><td>Sur la diapo 12, garder la ligne d’arrivée et la vitesse ; sauter la durée du cycle et les cadences.</td></tr>
<tr><td>Diapo 18 · Synthèse</td><td><b>{T_SYN}</b></td><td>Synthèse en deux phrases et mon apport, puis directement Houston et « Merci ».</td></tr></table>
<h3>Six phrases à savoir mot pour mot</h3>
<ol class="ph">
<li>« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. »</li>
<li>« Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente reproductible et mesurable, pour recruter, activer et fidéliser nos adhérents ? »</li>
<li>« La vente finit au premier envoi, pas à la signature. »</li>
<li>« Diagnostiquer avant de démontrer : c’est le prospect qui chiffre sa perte. »</li>
<li>« Le prospect n’achète pas un transport : il cherche à réduire son risque. »</li>
<li>« Vingt-quatre bouteilles, 360 euros de transport, les taxes estimées et réglées d’avance, une livraison en trois semaines environ. Ils repartent les mains libres. »</li>
</ol>
<div class="warn"><p class="wl">CE QUE JE NE DIS JAMAIS</p>
<p>Un nom de client ou un CA par client (top 10 anonymisé) · la part du CA faite par les comptes A · « assurance incluse » ou « risque zéro » (option à 3 %, souscrite sur 89,8 % des envois) · « transporteur » (commissionnaire de transport) · « 145 adhérents actifs » (signés) · un objectif présenté comme un résultat · VELA, Gant Blanc, Planet’Stock, entrepôt agréé ou annexe Champagne au présent · « j’ai interviewé 70 clients » (échanges écrits réels, entretiens prévus au T1 2027) · un taux de droits US cité de mémoire · « 207 € par visiteur » (c’est par réservation, 2,9 adultes en moyenne) · un taux de marge · « premier », « unique », « exclusif ».</p></div>
</section>''')

GRID = [
 ('Capter l’attention (Start with why)', 'Animation', '2 · Accroche', 'Houston, 2 bouteilles sur 24, puis un silence ; la question du comptoir devient le fil rouge.'),
 ('Rythme, langage, support, orthographe, temps', 'Animation', 'Toutes', 'Une idée par diapo, chiffres en grand ; vocabulaire métier défini (DDP, CIVC, ADV, cadence) ; 18 minutes.'),
 ('Titres du sommaire impactants', 'Argumentation', '3 · Sommaire', 'Quatre verbes, chacun relié à son enjeu : analyser, cibler, vendre, piloter.'),
 ('Introduction qui amène le sujet', 'Argumentation', '2 à 8', 'Houston → marché → entreprise → offre → concurrence → problématique et trois enjeux.'),
 ('Analyse du marché reliée à l’entreprise', 'Argumentation', '4 · Marché', 'Trois bascules, chacune traduite « Pour Planet Aura » : la sécurité se vend, 64,5 % des envois vers les USA, le caveau comme gisement.'),
 ('Entreprise : organigramme, CA, offre, concurrence, cibles', 'Argumentation', '5, 6, 7 (+ B9)', 'CA ×4,7 et +11,6 % à contre-courant, équipe et pôles, modèle B2B2C et grille, carte des concurrents ; organigramme complet en B9.'),
 ('ICP', 'Argumentation', '9 · ICP', 'Top 10 réel anonymisé → 5 critères → 5 ICP → score PA-FIT ; ma décision : 60 % sur les caveaux.'),
 ('Personas', 'Argumentation', '10 · Personas', 'Qui décide, qui utilise, qui paie ; mon étude d’octobre 2026 (70 contacts, 47 réponses, 15 avis).'),
 ('Problématiques → solutions', 'Argumentation', '11 · Solutions', 'Cible, douleur, réponse, repère chiffré ; et ce que nous refusons d’emblée.'),
 ('Processus de vente et tunnel SPIN', 'Argumentation', '12 · 13 · 14 (+ B4, B12, B14)', 'Sept étapes avec SLA, vente finie au premier envoi, durée du cycle à statut ; deux tunnels SPIN ; objections en 4 temps et ROI.'),
 ('Ressources précises, réalistes, échéancées, chiffrées', 'Argumentation', '15 · Ressources (+ B13)', 'Une preuve par doute ; six chantiers datés, responsables, heures, 3 000 €, critères de passage.'),
 ('Sales Ops : chaque outil et son objectif', 'Argumentation', '16 · Sales Ops', 'Six outils autour de HubSpot, chacun avec son objectif et son statut ; intégration 30-60-90 ; rituels proposés.'),
 ('KPI et méthode de suivi', 'Argumentation', '17 · KPI (+ B6)', 'Constaté / point zéro / objectif ; 90 jours de mesure ; revue mensuelle de 45 min close par une décision.'),
 ('Synthèse reliée aux enjeux', 'Argumentation', '18 · Synthèse (+ B15)', 'Avant / avec le playbook, enjeu par enjeu, avec le pourquoi ; mon apport ; bénéfices attendus.'),
 ('Ouverture', 'Argumentation', '19 · Ouverture', 'Trois difficultés → trois règles ; autocritique ; jalons datés ; projets au conditionnel.'),
 ('Conclusion qui revient à l’accroche', 'Animation', '20 · Clôture', 'Houston, 24 bouteilles, les mains libres ; le fil rouge en dernière phrase.'),
 ('Valeur ajoutée personnelle', 'Transversal', '9, 10, 12-17, 18, B15', 'Étiquettes MON ANALYSE, MON ÉTUDE, MON OUTIL, MES PROPOSITIONS ; « Mon apport » en synthèse.'),
 ('Raisonnement stratégique', 'Transversal', '7, 9, 11, 12, 17', 'Décisions justifiées : le cap, 60 % sur les caveaux, les refus, la ligne d’arrivée, des cibles de départ plutôt que des promesses.'),
]
H.append('<section><p class="ey">2 · LA GRILLE, DIAPO PAR DIAPO</p><h2>Chaque critère noté a sa diapo et sa preuve</h2><p class="lead">Animation sur 6 points, argumentation sur 14. Le critère « playbook existant » est sans objet : Planet Aura n’en avait pas, le dire en une phrase (diapos 8 et 18, détail en B15).</p><table class="t"><tr><th>Critère</th><th>Bloc</th><th>Diapo</th><th>Ce que le jury doit voir ou entendre</th></tr>' +
 ''.join(f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in GRID) + '</table></section>')

H.append('<section><p class="ey">3 · LE SCRIPT MINUTÉ</p><h2>Ce que je dis, diapo par diapo</h2><p class="lead">Les mêmes notes figurent en mode présentateur. Elles sont écrites pour l’oral : les apprendre par blocs d’idées, jamais mot à mot, sauf les six phrases de la page 2. Les indications entre parenthèses sont des rappels de régie, à ne pas dire.</p>' + ''.join(script) + '</section>')

H.append('<section><p class="ey">4 · LES QUESTIONS DU JURY</p><h2>Une méthode pour toutes les questions : accueillir, clarifier, prouver, vérifier</h2>'
 '<div class="g4"><div class="m"><p class="mn">1</p><p><b>Accueillir</b> : remercier, reconnaître ce qui est juste dans la question.</p></div><div class="m"><p class="mn">2</p><p><b>Clarifier</b> : une question courte pour viser le vrai doute.</p></div><div class="m"><p class="mn">3</p><p><b>Prouver</b> : une seule preuve, chiffrée et sourcée.</p></div><div class="m"><p class="mn">4</p><p><b>Vérifier</b> : « Cela répond-il à votre question ? »</p></div></div>'
 '<p class="lead">C’est exactement la méthode du playbook face aux objections : l’appliquer devant le jury, c’est la démontrer. Si je ne sais pas : « Je ne veux pas vous donner un chiffre approximatif ; je le vérifie et je vous le transmets. »</p>'
 '<h3>Les 20 questions les plus probables</h3>' + ''.join(qa_card('Q', *q) for q in top) +
 '<h3>Les 5 questions pièges</h3>' + ''.join(qa_card('P', *q) for q in traps) + '</section>')

H.append('<section><p class="ey">5 · LES DIAPOS DE SECOURS</p><h2>' + f'{N_BACK}' + ' diapos après « Merci », à n’ouvrir que si la question l’appelle</h2><p class="lead">Dans le mode présentation, les atteindre par le panneau des diapos (section « Diapos de secours »). Une réponse sans support convainc souvent davantage : ne pas les montrer par réflexe.</p><table class="t"><tr><th>N°</th><th>Titre</th><th>Répond à</th></tr>' + ''.join(backup_rows) + '</table></section>')

H.append(f'<section><p class="ey">6 · L’AUTO-ÉVALUATION</p><h2>Après les questions : un bilan honnête, en deux minutes</h2><p class="lead">Le jury demande souvent une auto-évaluation avant le débrief. Deux forces, deux axes de progrès avec leur plan, une phrase de conclusion.</p><div class="g2"><div class="ab"><p class="abl" style="color:#20768B">POINTS FORTS</p>{forts}</div><div class="ab"><p class="abl" style="color:#722F45">AXES D’AMÉLIORATION</p>{axes}</div></div><div class="concl"><p>{concl}</p></div></section>')

H.append('''<section><p class="ey">7 · LES CHECK-LISTS</p><h2>Préparer, vérifier, arriver serein</h2>
<div class="g3c">
<div class="ck"><p class="ckl">LA SEMAINE AVANT</p><ul>
<li>Trois répétitions complètes au chronomètre, dont une filmée.</li>
<li>Une répétition des questions avec quelqu’un qui joue le jury, pièges compris.</li>
<li>Savoir refaire à voix haute : le ROI (30 × 1/3 × 300 € × 20 = 60 000 €) et le prix Texas (≈ 270 €).</li>
<li>Relire la grille shipping 2026 et les seuils POA (2 100 $), 36 bouteilles par personne et par envoi.</li>
<li>Lire l’annexe W une dernière fois : mon discours sur l’IA doit lui correspondre exactement.</li>
<li>Télécharger le deck en PDF et en PPTX (menu de l’artefact) ; tester le mode présentateur.</li>
</ul></div>
<div class="ck"><p class="ckl">LA VEILLE</p><ul>
<li>Vérifier dans le simulateur que les droits de douane US sont toujours à 10 % (en vigueur depuis février 2026) ; sinon, adapter les diapos 4 et B7.</li>
<li>Noter le statut réel des chantiers de septembre et d’octobre (fait, en cours, décalé).</li>
<li>Savoir si la version de novembre est sortie selon la date du jury.</li>
<li>Copier le deck sur une clé USB et l’envoyer par email à soi-même.</li>
<li>Imprimer ce guide ; préparer une fiche avec les 3 points de passage.</li>
</ul></div>
<div class="ck"><p class="ckl">LE JOUR J</p><ul>
<li>Le carton ISTA 3A de démonstration, si le format le permet.</li>
<li>Téléphone : simulateur de coûts et fiche Google ouverts, en mode avion pendant l’exposé.</li>
<li>Un chronomètre visible ; une bouteille d’eau.</li>
<li>Arriver tôt, tester l’écran et la télécommande.</li>
<li>Première phrase, puis un silence : laisser Houston faire son effet.</li>
</ul></div>
</div>
<div class="warn"><p class="wl">CONFIDENTIALITÉ</p><p>Le playbook est diffusé en interne et aux seuls évaluateurs Euridis, avec l’accord de la direction. À l’oral : aucun nom ni CA par client, aucune donnée personnelle de client final, aucun identifiant, aucun mot de passe, aucune capture d’administration, aucun taux de marge.</p></div>
</section>''')
H.append('</body></html>')
open(os.path.join(OUT, 'guide.html'), 'w').write('\n'.join(H))
print('guide.html ok')
