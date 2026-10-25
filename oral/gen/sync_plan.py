# Réécrit dans plan-oral.md la section « Plan de la présentation » à partir du minutage calculé par build.py.
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORAL = os.path.abspath(os.path.join(HERE, '..'))
out = subprocess.run([sys.executable, os.path.join(HERE, 'build.py')], capture_output=True, text=True, env={**os.environ}).stdout
rows = re.findall(r'^(\w+)\s+\d+ mots\s+(\d+:\d\d)\s+→ (\d+:\d\d)$', out, re.M)
END = {sid: e for sid, _, e in rows}
total = re.search(r'TOTAL (\d+) mots, (\d+:\d\d)', out)

PLAN = [
    ('cover', 'Couverture', 'Sales Playbook Planet Aura, Emma, Euridis, tutrice'),
    ('accroche', 'Accroche (Start with why)', 'Houston, scène type racontée par les adhérents : 2 bouteilles sur 24 ; notre pourquoi'),
    ('sommaire', 'Sommaire', 'Cinq étapes titrées par leur idée, reliées aux enjeux ; le cas fil rouge annoncé ; la légende des étiquettes'),
    ('marche', 'Le marché (MON ANALYSE)', 'Trois chiffres (OIV, FEVS, Atout France) ; cinq contraintes pour une caisse vers les USA : notre métier'),
    ('entreprise', 'L’entreprise (EXISTANT)', 'Commissionnaire né en 2019 ; CA ×4,7 ; marchés ; qui vend, qui décide'),
    ('offre', 'L’offre et la concurrence', 'Nous vendons de la sécurité ; grille USA ; le statu quo comme concurrent n° 1 ; notre case'),
    ('diagnostic', 'Diagnostic et problématique (MON ANALYSE)', 'SWOT en quatre quadrants ; problématique ; trois enjeux'),
    ('icp', 'Partie 8 · ICP (cas : qualifier)', 'Du top 10 anonymisé au score : PA-FIT du domaine, 45 au départ, 85 après preuve (illustratif)'),
    ('personas', 'Partie 9 · Personas', 'Décideur, utilisateur, payeur : ce qu’ils veulent, craignent, ce que je leur dis ; étude 70 / 47 / 15'),
    ('solutions', 'Partie 10 · Enjeux et solutions', 'Problème → besoin → solution → bénéfice → preuve, pour trois cibles ; ce que nous refusons'),
    ('processus', 'Partie 11 · Processus', 'Sept étapes : responsable, preuve, délai, outil ; durées de cycle ; la vente finit au premier envoi'),
    ('prospecter', 'Partie 11 · Prospecter (cas)', 'Qui, par quel canal, quand ; cadence caveau ; extraits réels du script d’appel et de l’e-mail 1'),
    ('spin', 'Partie 11 · Tunnels SPIN (cas : découvrir)', 'Trame de 35 min ; tunnel 1 en action, tunnel 2 en regard ; la reformulation'),
    ('proposer', 'Partie 11 · Proposer (cas)', 'Capture réelle du simulateur ; 24 bouteilles = 360 € ; objection en 4 temps ; ROI de l’exemple'),
    ('activer', 'Partie 11 · Activer (cas)', 'J0 → J+30 : signature, formation, premier envoi, point ; score de santé ; activation ≥ 70 %'),
    ('ressources', 'Partie 12 · Ressources', 'Pages réelles du playbook ; une preuve par doute ; six chantiers datés, chiffrés, attribués (3 000 €)'),
    ('salesops', 'Partie 13 · Sales Ops', 'HubSpot au centre, six outils et leur statut ; alignement marketing-ventes ; rituels proposés'),
    ('onboarding', 'Partie 13 · Onboarding 30-60-90', 'Annexe U ; l’escalier J+30 / J+60 / J+90 ; jalons S1, S4, S8 ; qui forme'),
    ('kpi', 'Partie 14 · Indicateurs (cas : suivre)', 'Constaté / objectif ; quatre KPI avec source, fréquence, responsable, action ; la revue mensuelle'),
    ('conclusion', 'Synthèse, ouverture, retour à Houston', 'Réponse à la problématique, apport, bénéfices, limites, ouverture ; « Ils repartent les mains libres »'),
]
BACK = [('B1', 'Personas confrontés au réel', 'Représentativité de l’étude'), ('B2', 'Priorisation : une seule grille fait foi', '« Usine à gaz »'),
        ('B3', 'Fiches de comparaison concurrents', 'UPS, DHL, Viticolis, Dartess'), ('B4', 'SPIN sur le terrain', '« Quel vigneron accorde 35 min en saison ? »'),
        ('B5', 'Transparence IA', 'Usage de l’IA'), ('B6', 'Tableau des KPI', 'Origine et suivi des cibles'), ('B7', 'Prix rendu Texas', '« C’est trop cher »'),
        ('B8', 'SWOT et horizons', 'Stratégie, dépendance USA'), ('B9', 'Organigramme complet', 'Organisation'), ('B10', 'Carte des États-Unis 2026', 'Où livre-t-on ?'),
        ('B11', 'Sinistre', '« Qui paie quand ça casse ? »'), ('B12', 'Cadence 8 touches / 18 jours', 'Prospection, câblage Brevo-HubSpot'),
        ('B13', 'Feuille de route détaillée', 'Ressources chiffrées'), ('B14', 'Top 5 des objections', 'Jeux de rôle, objections'),
        ('B15', 'Existant → apport → statut', 'Valeur ajoutée personnelle'), ('B16', 'Le cas fil rouge, étape par étape', '« Ce cas est-il réel ? »')]


def sec(t):
    m, s = t.split(':')
    return int(m) * 60 + int(s)


def mmss(s):
    return f'{s // 60}:{s % 60:02d}'


intro, core_end, fin = sec(END['diagnostic']), sec(END['kpi']), sec(END['conclusion'])
sect = [f'## Plan de la présentation, version 3 du 25/10/2026 : le cas fil rouge (20 diapositives + {len(BACK)} diapos de secours)',
        f'Minutage des notes à 130 mots/minute, 2 s par changement de diapo : {total.group(2)} de texte ({total.group(1)} mots), soit 18 à 19 min avec les silences (20 min au maximum). '
        f'Introduction et diagnostic = {mmss(intro)} ; parties 8 à 14 = {mmss(core_end - intro)} ; synthèse et ouverture = {mmss(fin - core_end)}.',
        '',
        'Fil rouge : un domaine provençal avec caveau et clientèle internationale (chap. 11 du playbook). C’est un parcours type, pas une vente réalisée : prix de la grille 2026, règles du playbook, situations illustratives.',
        '', '| # | Diapo | Une idée forte | Fin visée |', '|---|---|---|---|']
sect += [f'| {k} | {t} | {i} | {END[sid]} |' for k, (sid, t, i) in enumerate(PLAN, 1)]
sect += ['', '| Secours | Sujet | Sert à répondre à |', '|---|---|---|'] + [f'| {a} | {b} | {c} |' for a, b, c in BACK] + ['']
p = os.path.join(ORAL, 'plan-oral.md')
s = open(p).read()
s = re.sub(r'## Plan de la présentation.*?(?=\n## Règles de conception)', '\n'.join(sect), s, count=1, flags=re.S)
s = re.sub(r'- Contribution personnelle marquée : .*', '- Contribution marquée par étiquette : EXISTANT, MON ANALYSE, MA CONTRIBUTION, À DÉPLOYER, À MESURER.', s)
s = re.sub(r'- Statut affiché sur chaque chiffre discutable : .*', '- Statut affiché sur chaque chiffre discutable : CONSTATÉ, OBJECTIF, HYPOTHÈSE, POINT ZÉRO, PROJET, GRILLE 2026, ILLUSTRATIF, RÈGLE.', s)
s = s.replace('- Photos : uniquement des photos réelles du dossier (équipe, couverture) ; aucune image générée par IA.',
              '- Visuels : photos réelles (équipe, avec accord), captures réelles des outils (simulateur, tableau de bord), pages réelles du playbook ; aucune image générée par IA.')
open(p, 'w').write(s)
print('plan-oral.md :', total.group(2), 'intro', mmss(intro), 'coeur', mmss(core_end - intro), 'fin', mmss(fin - core_end))
