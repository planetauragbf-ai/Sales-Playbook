# Réécrit dans plan-oral.md la section « Plan de la présentation » (minutage calculé par build.py) et la section
# « Règles de conception du support » (règles de la v5 : des diapos lisibles en 3 secondes).
# usage : cd gen5 && DECK_DIR=deck5 python3 sync_plan.py
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORAL = os.path.abspath(os.path.join(HERE, '..'))
out = subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], capture_output=True, text=True, env={**os.environ}).stdout
rows = re.findall(r'^(\w+)\s+\d+ mots\s+(\d+:\d\d)\s+→ (\d+:\d\d)$', out, re.M)
END = {sid: e for sid, _, e in rows}
total = re.search(r'TOTAL (\d+) mots, (\d+:\d\d)', out)

VERSION = 'version 5 du 26/10/2026'
# (id, diapo, une idée forte) : ce que la diapo v5 montre (message et point focal) ; le reste est dit ou en secours.
PLAN = [
    ('cover', 'Couverture', 'Sales Playbook Planet Aura : de la première accroche au premier envoi ; Emma, Euridis, tutrice'),
    ('accroche', 'Accroche (Start with why)', 'Houston, scène type entendue sur le terrain : 2 bouteilles sur 24 ; notre pourquoi'),
    ('sommaire', 'Sommaire', 'Cinq étapes titrées par leur idée, la problématique et les trois enjeux en regard ; le cas fil rouge (parcours type) ; la légende des étiquettes'),
    ('marche', 'Le marché (MON ANALYSE)', 'L’export se complique : c’est notre métier. Trois chiffres en grand (OIV, FEVS, Atout France) ; cinq contraintes pour expédier chez un particulier américain'),
    ('entreprise', 'L’entreprise (EXISTANT)', 'Une croissance portée par le bouche-à-oreille : CA ×4,7 (constaté) ; 262 adhérents, part USA ; qui vend, qui décide (organigramme complet en B9)'),
    ('offre', 'L’offre et la concurrence', 'Nous vendons de la sécurité : groupage USA DDP, 15 € de transport par bouteille à 24 bouteilles (grille 2026) ; « on se débrouille », concurrent n° 1 ; notre place'),
    ('diagnostic', 'Diagnostic et problématique (MON ANALYSE)', 'Forces et fragilités constatées ; la problématique en bandeau ; trois enjeux numérotés (SWOT complet en B8)'),
    ('icp', 'Partie 8 · ICP (cas : qualifier)', 'Le score juge la preuve, pas la taille : cinq critères ICP ; 60 % de l’effort sur les caveaux (objectif) ; PA-FIT 45 → 60 → 85 (illustratif, barème en B2)'),
    ('personas', 'Partie 9 · Personas', 'Trois cartes : qui décide, utilise, paie ; sa crainte et le discours qui y répond, en grand ; confrontés au réel : 70 / 47 / 15, 5/5 confirmés (détail en B1)'),
    ('solutions', 'Partie 10 · Problèmes et solutions', 'Une chaîne Problème → Besoin → Solution → Bénéfice → Preuve pour le domaine ; champagne et caviste, dits ; ce que nous refusons'),
    ('processus', 'Partie 11 · Processus', 'Sept étapes, une preuve pour passer chacune ; ligne d’arrivée à l’étape 6, le premier envoi ; durées de cycle, dites ; constat → décision → mesure (détail par étape en B17)'),
    ('prospecter', 'Partie 11 · Prospecter (cas)', 'L’appel ne vend pas, il obtient la démo : préparer, viser, cadencer ; la question clé du script d’appel en grand ; l’e-mail en une phrase'),
    ('spin', 'Partie 11 · Tunnels SPIN (cas : découvrir)', 'Le tunnel du vigneron : les quatre questions S, P, I, N en entier, l’implication en avant ; la reformulation à trous ; tunnel 2 en B4'),
    ('proposer', 'Partie 11 · Proposer (cas)', '15 € de transport par bouteille, payés par son client : grille officielle 2026, 24 bouteilles = 360 € HT ; « C’est cher » en quatre temps ; simulation de 40 000 € de ventes potentiellement perdues'),
    ('activer', 'Partie 11 · Activer (cas)', 'La vente finit au premier envoi : J0 → J+30, signature, bienvenue, formation, premier envoi, point d’étape ; constat → décision → mesure (≥ 70 % à J+30)'),
    ('ressources', 'Partie 12 · Ressources', 'Déjà livré (trois pages réelles), puis trois chantiers d’abord, datés, attribués, chiffrés : 800 € sur 3 000 € ; critères et suite en B13'),
    ('salesops', 'Partie 13 · Sales Ops', 'Une donnée, un propriétaire, une décision : HubSpot source de vérité, quatre outils existants, Brevo à câbler, dictionnaire CRM ; règles marketing-ventes et rituels, dits'),
    ('onboarding', 'Partie 13 · Onboarding 30-60-90', 'Opérationnel en 90 jours : l’escalier J+30 certifié, J+60 autonome, J+90 pilote, une preuve par palier ; ligne d’arrivée en S8 ; qui forme, dit'),
    ('kpi', 'Partie 14 · Indicateurs (cas : suivre)', 'Mesuré ou espéré : ~145 signés (constaté, point zéro) ; Activation J+30 ≥ 70 % avec source, fréquence, responsable, action ; revue mensuelle (détail en B6)'),
    ('conclusion', 'Synthèse, ouverture, retour à Houston', '« Ils repartent les mains libres » : les 24 bouteilles pleines ; ma réponse enjeu par enjeu ; bénéfice visé, limite, ouverture'),
]
# (n°, sujet, sert à répondre à) : titres des diapos de secours v5 et questions de jury.md (« Répond à »).
BACK = [('B1', 'Personas : cinq sur cinq confirmés par nos données', 'Personas réels ou intuition ? Représentativité de l’étude'),
        ('B2', 'Priorisation : une seule grille fait foi (PA-FIT, 8 critères)', '« Usine à gaz » ; ICP contre taille'),
        ('B3', 'Concurrence : reconnaître, recentrer, questionner', 'UPS, Viticolis, Dartess, DHL, « on gère tout en interne » ; sans dénigrer'),
        ('B4', 'SPIN sur le terrain, tunnel 2', '« Quel vigneron accorde 45 min en saison ? » ; la maison de champagne'),
        ('B5', 'Transparence IA', 'Usage de l’IA, part personnelle du travail'),
        ('B6', 'Indicateurs : fréquence, cible, action', 'Origine et suivi des cibles ; les autres KPI'),
        ('B7', 'Prix rendu, sans maquillage', '« C’est trop cher » ; assurance en option, délai estimé'),
        ('B8', 'Stratégie : SWOT complet et horizons', 'Opportunités et menaces ; dépendance USA'),
        ('B9', 'Organigramme complet', 'Qui fait quoi ; place d’Emma'),
        ('B10', 'Carte des États-Unis 2026', 'Où livre-t-on ? POA'),
        ('B11', 'Procédure sinistre 2026', '« Qui paie quand ça casse ? »'),
        ('B12', 'Cadence 8 touches / 18 jours', 'Prospection, câblage Brevo-HubSpot'),
        ('B13', 'Feuille de route détaillée', 'Ressources chiffrées, critères de passage'),
        ('B14', 'Top 5 des objections', 'Jeux de rôle, objections'),
        ('B15', 'Existant → apport → statut', 'Valeur ajoutée personnelle'),
        ('B16', 'Le cas fil rouge, étape par étape', '« Ce cas est-il réel ? »'),
        ('B17', 'Processus : qui, preuve, délai, outil', '« Quel délai, qui, quel outil à l’étape 2 ? »')]
# Règles de conception de la v5 (cahier des charges de la refonte : v5cand/BRIEF.md).
RULES = [
    'Lisible en 3 secondes : le titre dit le message ; un seul point focal (schéma, chiffre, document réel, parcours) ; trois zones au plus, plus le bandeau d’argument.',
    'Peu de mots : 70 à 90 mots visibles visés par diapo principale, 95 au plus ; 130 au plus sur une secours. Deux écarts assumés : SPIN (139 mots, les quatre questions en entier) et personas (114, chaque discours face à la crainte qu’il lève).',
    'Gros caractères : messages clés de 28 à 36 px, jamais moins de 24 px ; chiffres clés en grand, jamais collés à leur légende.',
    'Aucun critère de la grille n’est retiré pour alléger : ce qui quitte l’écran est dit (notes) ou placé dans une diapo de secours.',
    'Zéro chevauchement, avec une marge : chaque diapo passe le banc de rendu (vraies polices) en rendu normal et en rendu stress, textes agrandis de 10 %.',
    'Statut affiché à côté de chaque chiffre discutable : CONSTATÉ, OBJECTIF, SIMULATION, GRILLE 2026, ILLUSTRATIF (dont « parcours type » et « points illustratifs »), RÈGLE.',
    'Contribution marquée par étiquette : EXISTANT, MON ANALYSE, MA CONTRIBUTION, À DÉPLOYER, À MESURER.',
    'Argument des décisions (diapos 11, 15, 16, 17, 19) : Constat → Ma décision → Ce que l’on mesure, dix mots au plus par case.',
    'Visuels : photo réelle de l’équipe (avec accord), documents et captures réels (grille officielle 2026, tableau de bord Planet’Connect), pages réelles du playbook ; aucune image générée par IA.',
    'Les notes du mode présentateur disent ce que l’écran ne montre pas ; les indications entre parenthèses ne se disent pas.',
]


def sec(t):
    m, s = t.split(':')
    return int(m) * 60 + int(s)


def mmss(s):
    return f'{s // 60}:{s % 60:02d}'


def milliers(n):
    return f'{int(n):,}'.replace(',', ' ')


assert len(PLAN) == len(END) and all(sid in END for sid, _, _ in PLAN), 'PLAN et build.py ne décrivent pas les mêmes diapos'
intro, core_end, fin = sec(END['diagnostic']), sec(END['kpi']), sec(END['conclusion'])
sect = [f'## Plan de la présentation, {VERSION} : des diapos lisibles en 3 s, autour du cas fil rouge ({len(PLAN)} diapositives + {len(BACK)} diapos de secours)',
        f'Minutage des notes à 130 mots/minute, 2 s par changement de diapo : {total.group(2)} de texte ({milliers(total.group(1))} mots), soit 18 à 19 min avec les silences (20 min au maximum). '
        f'Introduction et diagnostic = {mmss(intro)} ; parties 8 à 14 = {mmss(core_end - intro)} ; synthèse et ouverture = {mmss(fin - core_end)}. '
        'Minutage théorique : la durée réelle reste à chronométrer à voix haute.',
        '',
        'Version 5 : chaque diapo porte un message (son titre) et un point focal ; le détail passe à l’oral (notes) ou dans une diapo de secours. '
        'Nouvelle diapo de secours B17 : le responsable, la preuve, le délai et l’outil de chacune des sept étapes ; la diapo 11 ne garde que la preuve de chaque étape et la fiche complète de l’étape 6.',
        '',
        'Fil rouge : un domaine provençal avec caveau et clientèle internationale (chap. 11 du playbook). C’est un parcours type, pas une vente réalisée : prix de la grille 2026, règles du playbook, situations illustratives.',
        '', '| # | Diapo | Une idée forte | Fin visée |', '|---|---|---|---|']
sect += [f'| {k} | {t} | {i} | {END[sid]} |' for k, (sid, t, i) in enumerate(PLAN, 1)]
sect += ['', '| Secours | Sujet | Sert à répondre à |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in BACK] + ['']
rules = ['## Règles de conception du support (v5)'] + [f'- {r}' for r in RULES]

p = os.path.join(ORAL, 'plan-oral.md')
s = open(p, encoding='utf-8').read()
s, n1 = re.subn(r'## Plan de la présentation.*?(?=\n## Règles de conception)', lambda m: '\n'.join(sect), s, count=1, flags=re.S)
s, n2 = re.subn(r'## Règles de conception du support.*?(?=\n## |\Z)', lambda m: '\n'.join(rules) + '\n', s, count=1, flags=re.S)
assert n1 == 1 and n2 == 1, 'sections « Plan de la présentation » ou « Règles de conception du support » introuvables'
open(p, 'w', encoding='utf-8').write(s)
print('plan-oral.md :', VERSION, '·', total.group(1), 'mots', total.group(2), '· intro', mmss(intro), '· cœur', mmss(core_end - intro),
      '· fin', mmss(fin - core_end), '·', len(PLAN), 'diapos +', len(BACK), 'secours')
