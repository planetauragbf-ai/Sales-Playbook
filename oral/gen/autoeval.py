# Autoévaluation exigeante (grille Euridis), évaluation critique fond / design, et bilan avant / après v4 → v5
# (version 5 du 26/10/2026 : des diapos lisibles en 3 secondes). Fragments HTML insérés dans le guide (sections 10 et 11).
# Mots visibles v5 : recalculés sur le deck (DECK_DIR, deck5 par défaut), même décompte que le banc render5.js (innerText de la
# diapo, en-tête, bandeau du cas et pied de page compris ; vérifié identique sur les 37 diapos) ; v4 : v5cand/_workflow_result.json.
# Mots dits et minutage : recalculés sur notes_main.py, comme build.py (130 mots/min, +2 s par diapo, parenthèses non dites).
import html, json, os, re
from notes_main import NOTES

E = html.escape
HERE = os.path.dirname(os.path.abspath(__file__))
_D = os.environ.get('DECK_DIR') or ('deck5' if os.path.isdir(os.path.join(HERE, '..', 'deck5')) else 'deck')  # dans le dépôt : oral/deck
DECK = os.path.join(HERE, '..', _D, 'project')
ORDER = json.load(open(os.path.join(DECK, 'deck.json')))['order']
MAIN = [s for s in ORDER if not s.startswith('b')]
BACKS = [s for s in ORDER if s.startswith('b')]
WPM, PAUSE = 130, 2


def spoken(t):
    return len(re.findall(r"[\wÀ-ÿ’'-]+", re.sub(r'\([^)]*\)', ' ', t)))


def mmss(s):
    s = int(round(s))
    return f'{s // 60}:{s % 60:02d}'


def tosec(t):
    m, s = t.split(':')
    return int(m) * 60 + int(s)


def visible(sid):
    s = open(os.path.join(DECK, 'slides', f'{sid}.html')).read()
    s = re.sub(r'<aside>.*?</aside>', '', s, flags=re.S)
    s = re.sub(r'<style.*?</style>', '', s, flags=re.S)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'</?(?:a|b|i|em|strong|span|sup|sub|small|u|s|code|mark|br)\b[^>]*>', '', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    return len([w for w in html.unescape(s).split() if re.search(r'[\wÀ-ÿ€%]', w)])


num = lambda n: f'{n:,}'.replace(',', ' ')
WORDS = sum(spoken(NOTES[s]) for s in MAIN)
ENDS, _t = {}, 0.0
for _s in MAIN:
    _t += spoken(NOTES[_s]) / WPM * 60 + PAUSE
    ENDS[_s] = mmss(_t)
TOTAL, INTRO = ENDS[MAIN[-1]], ENDS['diagnostic']
VIS = {s: visible(s) for s in ORDER}
GAP = ('personas', 'spin')  # écarts assumés : chaque discours face à sa crainte ; les quatre questions SPIN en entier
CONTENT = [s for s in MAIN[2:] if s not in GAP]  # diapos de contenu, 3 à 20
LO, HI = min(VIS[s] for s in CONTENT), max(VIS[s] for s in CONTENT)
B16 = [s for s in BACKS if s != 'b17']
NS = len(ORDER)


def mv(sid, v4):
    # « mots visibles v4 → v5 » d'une diapo
    return f'{v4} → {VIS[sid]}' + (' (écart assumé)' if sid in GAP else '')


ANIM = [
    ('Grab attention (Start with why)', '1 / 1', 'Houston : une scène, un silence, une question, puis « notre raison d’être » ; écran inchangé, 2 bouteilles pleines sur 24.',
     'Scène type entendue sur le terrain, pas un cas daté : un jury peut la trouver construite.', 'Le dire d’emblée, sans s’en excuser : « une scène type ».'),
    ('Rythme et dynamisme', '0,75 / 1', 'Un point focal par diapo, un geste « Montrer » dans chaque note ; le cas avance de diapo en diapo ; transitions annoncées, pauses marquées.',
     'Rythme jamais éprouvé à voix haute. L’écran en dit moins qu’en v4, la voix porte davantage : risque de lire ses notes.', 'Trois répétitions chronométrées ; notes apprises par idées ; ne regarder l’écran qu’au geste « Montrer ».'),
    ('Langage et vocabulaire métier', '1 / 1', 'DDP, groupage, CAVE, PA-FIT, nurture, SPIN, Planet’Connect, Brevo : définis au premier usage.',
     'Beaucoup de sigles en peu de temps.', 'Une demi-phrase de définition, jamais plus.'),
    ('Support graphique', '1 / 1', f'Refonte v5 : un message et un point focal par diapo ; {LO} à {HI} mots visibles par diapo de contenu, hors SPIN et personas (115 à 222 en v4) ; aucun texte sous 24 px ; aucun signalement au banc, rendu normal et agrandi de 10 %.',
     f'SPIN ({VIS["spin"]} mots) et personas ({VIS["personas"]}) restent au-dessus de la cible ; rendu contrôlé dans Chromium avec les vraies polices, pas encore dans le lecteur Slides ni projeté en salle ; une seule photo réelle.',
     f'Parcourir les {NS} diapos dans le lecteur Slides, puis une fois au vidéoprojecteur, depuis le fond de la salle.'),
    ('Grammaire et orthographe', '1 / 1', 'Typographie française (espaces insécables), relectures croisées, rendu vérifié diapo par diapo, mots isolés en fin de ligne corrigés.',
     f'Une coquille reste possible sur {NS} diapos et {num(WORDS)} mots de notes.', 'Dernière relecture à voix haute la veille, phrase anglaise de la diapo 9 comprise.'),
    ('Respect du temps (20 min max)', '0,75 / 1', f'Script de {num(WORDS)} mots : {TOTAL} à 130 mots/min (+2 s par diapo), introduction à {INTRO} ; trois points de passage ; plan de coupe, toujours sur les diapos à venir.',
     'Minutage théorique : 130 mots/min est une hypothèse de débit, jamais vérifiée à voix haute.', 'Noter l’heure réelle aux trois points de passage, à chaque répétition ; appliquer le plan de coupe dès 30 s de retard.'),
]
ARG = [
    ('Titres du sommaire', 'Maîtrisé', 'Cinq étapes titrées par leur idée ; en v5, le renvoi à la problématique et les trois enjeux en regard, reliés aux parties du cahier des charges.', '—', '—'),
    ('Introduction qui amène le sujet', 'Maîtrisé', f'Scène → marché → entreprise → offre → diagnostic → problématique, en {INTRO} (minutage théorique).', '—', '—'),
    ('Marché relié à l’entreprise', 'Maîtrisé', 'Trois chiffres sourcés, en grand ; cinq contraintes ; un titre-message : « L’export se complique : c’est notre métier ».',
     'Droits US : sources externes contradictoires depuis juillet 2026.', 'Renvoyer au simulateur ; ne jamais citer un taux de mémoire.'),
    ('Entreprise : organigramme, CA, offre, concurrence, cibles', 'Maîtrisé', 'CA ×4,7 constaté, 262 adhérents, part USA, « qui vend, qui décide », photo de l’équipe ; offre et concurrence sur la diapo 6.',
     'À l’écran, l’organigramme se réduit à la photo légendée de l’équipe et à « qui vend, qui décide » : les pôles et les rôles sont en B9, les fiches concurrents en B3.', 'Le dire en une phrase et ouvrir B9 dès qu’une question l’appelle.'),
    ('Processus de vente et tunnels SPIN', 'Maîtrisé', 'Sept étapes et leur preuve, ligne d’arrivée au premier envoi ; responsable, délai, outil étape par étape en B17 ; tunnel du vigneron question par question ; second tunnel en B4.',
     'Durées de cycle : objectifs et repères terrain, non mesurés ; en v5, elles se disent mais ne sont plus à l’écran.', 'Les dire avec leur statut et la date de première mesure ; B6 et B17 si on les demande.'),
    ('Ressources précises, réalistes, échéancées, chiffrées', 'Maîtrisé', 'Ce qui est déjà livré, distingué de ce qui reste à déployer ; trois chantiers datés, attribués, chiffrés (800 € sur 3 000 €) ; critères et suite en B13.',
     'État réel des chantiers de septembre et d’octobre à confirmer ; les chantiers suivants ne sont plus qu’en B13.', 'Vérifier la veille avec la direction et le dire tel quel.'),
    ('Sales Ops et objectif de chacune', 'En cours → maîtrisé', 'HubSpot source de vérité, quatre outils existants, Brevo à câbler, dictionnaire CRM ; règles marketing-ventes et rituels, dits ; intégration 30-60-90.',
     'Rituels et dictionnaire proposés, pas ratifiés ; les quatre règles marketing-ventes ne sont plus visibles.', 'Faire confirmer le statut par la direction ; si on demande les règles : B12 (PA-FIT 55, nurture 45 j) et B17 (rappel du lead entrant < 24 h).'),
    ('Indicateurs de performance', 'En cours → maîtrisé', 'Mesuré ou espéré : ~145 signés constatés, point zéro au 24/09/2026 ; Activation J+30 ≥ 70 % avec source, fréquence, responsable, action ; revue mensuelle ; détail en B6.',
     'Aucun résultat du playbook n’est encore mesuré ; la décision citée est une règle conditionnelle ; première lecture fin décembre.', 'Réponse courte prête : la méthode, pas encore la preuve.'),
    ('Améliorations et justifications', 'Maîtrisé', 'Cinq bandeaux Constat → Ma décision → Ce que l’on mesure (diapos 11, 15, 16, 17, 19), dix mots au plus par case.', '—', '—'),
    ('Synthèse en lien avec les enjeux', 'Maîtrisé', 'Retour à Houston ; réponse enjeu par enjeu ; bénéfice visé, limite ; apport et difficulté dits (détail en B15).', '—', '—'),
    ('Ouverture', 'Maîtrisé', 'Diversifier (UK, UE dont Scandinavie, Canada, Japon), réduire la dépendance aux États-Unis ; première lecture fin décembre.', 'Sans objectif chiffré de diversification.', 'Dire qu’il sera fixé après la première lecture.'),
]
CRIT = [
    ('Fond', '18,5 / 20', 'Aucun critère évalué retiré : ce qui a quitté l’écran est dit, ou placé en secours (B17 ajoutée) ; statuts à côté des chiffres ; un cas cohérent de bout en bout ; chaque décision reliée à un constat et à une mesure ; contribution lisible.',
     'Aucun résultat du playbook n’est encore mesuré ; cas illustratif ; rituels non ratifiés ; droits US incertains à la date de l’oral ; une partie de la preuve n’est plus à l’écran : elle dépend de l’oral et des secours.'),
    ('Design', '18 / 20', f'Un message et un point focal par diapo ; {LO} à {HI} mots par diapo de contenu (hors SPIN et personas) ; aucun texte sous 24 px ; aucun signalement au banc sur les {NS} diapos, en rendu normal comme agrandi de 10 % ; identité homogène, documents réels.',
     'SPIN et personas au-dessus de la cible (assumé) ; rendu pas encore vu dans le lecteur Slides ni projeté ; marge du banc obtenue en partie par des entretoises devant le pied de page ; quelques vides (offre, personas) ; une seule photo réelle.'),
]
# Bilan v4 → v5 : (diapo, mots visibles v4 → v5, à l'écran en v5, passé à l'oral (dit) ou en secours, pourquoi).
AVANT_APRES = [
    ('3 · Sommaire', mv('sommaire', 141), 'Cinq étapes titrées par leur idée ; le renvoi à la problématique et les trois enjeux en regard ; parties du cahier des charges',
     'Dit : le contenu de chaque étape (ICP et personas, processus et SPIN, ressources et indicateurs) ; le cas suivi de la qualification au premier envoi, parcours type. Retiré : les listes de sous-thèmes, qui sont les sur-titres des diapos 4 à 19',
     'Un seul rail à suivre ; les enjeux nommés dès le sommaire'),
    ('4 · Marché', mv('marche', 146), 'Titre-message « L’export se complique : c’est notre métier » ; trois chiffres en grand, source sous chacun ; cinq contraintes',
     'Dit : ce que chaque bascule change pour nous (un vin qu’on veut protéger ; notre premier marché, près des deux tiers de nos envois, recule ; le caveau devient un canal d’export). Réserve non dite : 3,56 €/l. Secours : POA (B10), taux du jour au simulateur (B7)',
     'Trois bascules lues d’un coup d’œil ; un message au lieu de deux'),
    ('5 · Entreprise', mv('entreprise', 136), '×4,7 constaté et les barres du CA ; 262 adhérents, part USA ; qui vend, qui décide ; photo de l’équipe',
     'Dit : Castres 2019, commissionnaire, filiale, +11,6 % en 2025 ; les interlocuteurs du commercial (direction, exploitation, administration). Secours B9 : trois lignes du tableau « qui vend, qui décide » (projets, filiale, exploitation)',
     'Un chiffre héros et la fragilité commerciale, côte à côte'),
    ('6 · Offre', mv('offre', 185), 'Barres du transport par bouteille, 15 € à 24 bouteilles (grille 2026) ; « on se débrouille » ; familles de concurrents ; notre place',
     'Dit : le circuit de vente, le DDP, l’avis partagé sur le prix. Réserve non dite : totaux de la grille, familles, voile-cargo (partenaires potentiels), enquête prix. Secours : B7 (prix rendu, ~21 j), B3',
     'Un graphique comme point focal ; la concurrence en un bloc'),
    ('7 · Diagnostic', mv('diagnostic', 115), 'Forces et fragilités constatées ; la problématique en bandeau ; trois enjeux numérotés',
     'Secours B8 : opportunités et menaces (SWOT complet) ; B6 : satisfaction 4,65/5. Retiré : « 1er commercial dédié », déjà montré diapo 5',
     'La problématique devient le point focal'),
    ('8 · ICP', mv('icp', 222), 'Titre « Le score ne juge pas la taille : il juge la preuve » ; cinq critères ; 60 % sur les caveaux (objectif) ; PA-FIT 45 → 60 → 85 (illustratif)',
     'Dit : le top 10 anonymisé, les cinq ICP, la mesure 40 à 60 %. Secours : barème PA-FIT (B2), profil du domaine (B16). Retiré : la répartition des autres ICP (15 % champagne, 10 % cavistes, 15 % œnotourisme et salons), à dire si on la demande (Q3)',
     'Le score en action, pas un tableau de critères'),
    ('9 · Personas', mv('personas', 203), 'Trois cartes Décide / Utilise / Paie : la crainte et le discours qui y répond ; 70 · 47 · 15, constaté, 5/5 confirmés',
     'Dit : ICP et persona distingués, ce que je montre à chacun, l’angle mort ADV, entretiens au T1 2027. Secours B1 : personas A à E, base de l’étude. Retiré : « jugé sur », canaux (dossier, chap. 07)',
     'Au-dessus de la cible : chaque discours reste face à la crainte qu’il lève'),
    ('10 · Solutions', mv('solutions', 173), 'La chaîne du cas, de 24 → 2 à la preuve ; le pavé « Solution » ; « Nous refusons »',
     'Dit : champagne (certificat géré à chaque envoi), caviste, notre différence. Secours : concurrents (B3), assurance en option (B11, B14) ; le caviste, 2 bouteilles au lieu de 12 : à dire (note de B4). Réserve non dite : le refus des plus de 21°',
     'Une idée, le cas au premier plan'),
    ('11 · Processus', mv('processus', 180), 'Chaîne 1 → 7 ; étape 6 « Activé », ligne d’arrivée, avec sa fiche ; bandeau constat → décision → mesure',
     'Secours B17 (nouvelle) : responsable, preuve, délai, outil des sept étapes. Dit : six portes d’entrée, lead entrant rappelé sous 24 h, durées de cycle avec leur statut (aussi en B6)',
     'Le principe à l’écran, le détail en secours'),
    ('12 · Prospecter', mv('prospecter', 217), 'Préparer, viser, cadencer ; la question clé du script d’appel en grand ; l’e-mail en une phrase',
     'Secours : bloc 10 h-12 h et « avant les pics » (B4), nurture 45 j (B12). Retiré : ouverture et clôture du script, objet de l’e-mail (annexe E du dossier)',
     'Une question qui décroche la démo, lisible de loin'),
    ('13 · SPIN', mv('spin', 212), 'Les quatre questions S, P, I, N en entier, l’implication en avant ; la reformulation à trous',
     'Dit : le rôle de chaque famille, la réaction illustrative du vigneron (« il n’avait jamais fait le calcul »). Secours B4 : tunnel 2. Retiré : trame en six séquences, réponses illustratives (dossier, chap. 12)',
     'Tunnels SPIN impératifs au cahier des charges : les questions restent mot pour mot'),
    ('14 · Proposer', mv('proposer', 178), 'Titre « 15 € de transport par bouteille, payés par son client » ; grille officielle 2026, 24 btl = 360 € HT ; « C’est cher » en quatre temps ; 40 000 € (simulation)',
     'Dit : la formule de la simulation, « s’il en récupérait un quart », la proposition sous 24 h. Secours : ~21 j et 3 % (B7), cinq objections (B14). Retiré : la ligne d’estimation des taxes du document (aucun taux de droits US à l’écran)',
     'Une seule preuve chiffrée ; rien de promis'),
    ('15 · Activer', mv('activer', 168), 'Frise J0 → J+30, un seul accent sur la ligne d’arrivée (premier envoi) ; le couple texan suivi ; bandeau',
     'Dit : cartons, formation du caveau, premier envoi, point d’étape. Réserve non dite : score de santé, casse. Secours : B16 (étapes 5 à 7), B11 (sinistre). Retiré : détails d’exploitation (dossier, chap. 16)',
     'Voir la ligne d’arrivée, pas une liste de tâches'),
    ('16 · Ressources', mv('ressources', 197), 'Trois pages réelles « déjà livré » ; trois chantiers de septembre à novembre, budget, responsable, temps ; titre « 800 € sur 3 000 € »',
     'Dit : l’existant mobilisé (simulateur, carton homologué, avis Google 4,8/5). Secours B13 : critères de passage, chantiers suivants (LinkedIn, webinaire, salons)',
     'Distinguer d’un coup d’œil l’apport et ce qui reste à faire'),
    ('17 · Sales Ops', mv('salesops', 186), 'HubSpot au centre, quatre outils existants, Brevo à déployer, dictionnaire CRM ; bandeau',
     'Dit : contact loggé sous 24 h, quatre règles marketing-ventes, rituels (10 min par jour à 90 par trimestre). Secours : PA-FIT 55 et nurture 45 j (B12), rappel du lead entrant < 24 h (B17), motifs de perte (B14)',
     'Un schéma « source de vérité » au lieu de trois listes'),
    ('18 · Onboarding', mv('onboarding', 153), 'Escalier J+30 certifié, J+60 autonome, J+90 pilote, une preuve par marche ; drapeau S8',
     'Dit : qui forme (Adam, Vincent et Frantz, Floriane, moi), parcours non testé. Secours B15 : annexe U. Retiré : jalons hebdomadaires et contenus des paliers (annexe U)',
     'Une progression visible en un regard'),
    ('19 · Indicateurs', mv('kpi', 179), 'Capture réelle et ~145 signés (constaté, point zéro) ; carte Activation J+30 ≥ 70 % et son action ; trois autres KPI',
     'Dit : annulations 1,45 %, prochaine action du cas (datée dans HubSpot), lecture fin décembre puis chaque trimestre. Secours : fréquences et actions (B6), 89,8 % d’envois assurés (B11, B14), les étapes 6 et 7 du cas (B16) ; l’action datée dans HubSpot est seulement dite',
     'Séparer d’un coup d’œil le mesuré de l’espéré'),
    ('20 · Conclusion', mv('conclusion', 145), 'Les 24 bouteilles pleines, « Ils repartent les mains libres » ; ma réponse enjeu par enjeu ; bénéfice visé, limite, ouverture',
     'Dit : le panier du cas, mon apport, la difficulté, un commercial certifié en un mois. Secours : B15 (apport, difficulté), B7 (prix rendu), B8 (horizons stratégiques). Retiré : « 18 chapitres, 24 annexes »',
     'Finir sur l’image de l’accroche, et sur le jury'),
    (f'Secours B1 à B{len(B16)}', f'14 à 217 → {min(VIS[s] for s in B16)} à {max(VIS[s] for s in B16)}', 'Chaque secours à 130 mots au plus, même système visuel',
     'Détail resté dans les notes de secours et le dossier', 'Lisibles dès qu’une question les ouvre'),
    ('Secours B17 (nouvelle)', f'— → {VIS["b17"]}', 'Les sept étapes : responsable, preuve, délai (objectif), outil ; l’étape 6 surlignée',
     'Reçoit le détail retiré de la diapo 11 ; fiche ajoutée dans la banque de questions', '« Quel délai, qui, quel outil à l’étape 2 ? »'),
    ('Rendu au banc', '—', f'{NS} diapos sans aucun signalement (débordement, chevauchement), rendu normal et agrandi de 10 % (render5.js, vraies polices)',
     '—', 'En v4, des textes se chevauchaient et des grands chiffres touchaient leur légende'),
    ('Script oral', f'2 330 → {num(WORDS)} mots dits', f'{TOTAL} à 130 mots/min (+2 s par diapo), introduction à {INTRO} ; en v4 : 18:35, introduction à 4:52',
     'Ce qui a quitté l’écran se dit sans allonger : ajouts compensés par la coupe des redites et des relectures d’écran',
     'Le temps reste dans la cible ; il reste à le chronométrer à voix haute'),
]


def table(rows, head, bold=2):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{"<b>" + E(c) + "</b>" if j < bold else E(c)}</td>' for j, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<table class="t"><tr>{th}</tr>{tr}</table>'


BILAN = table(AVANT_APRES, ['Diapo ou livrable', 'Mots visibles v4 → v5', 'À l’écran en v5', 'Passé à l’oral (dit) ou en secours', 'Pourquoi'], bold=1)

HTML = f'''<h3>Ma note, critère par critère : exigeante, pour savoir où travailler</h3>
<div class="g3"><div class="k"><p class="score">5,5 / 6</p><p>Animation : support lisible en 3 secondes ; rythme et temps encore à éprouver à voix haute.</p></div>
<div class="k"><p class="score">13 / 14</p><p>Argumentation : décisions justifiées et mesurables ; aucun résultat du playbook n’est encore mesuré.</p></div>
<div class="k"><p class="score">≈ 18,5 / 20</p><p>Estimation avant répétition. Le 19-20 dépend du temps tenu à voix haute et des réponses sur la preuve d’efficacité.</p></div></div>
<h3>Animation, sur 6</h3>
{table(ANIM, ['Critère', 'Ma note', 'Justification', 'Faiblesse restante', 'Correction'])}
<h3>Argumentation et analyse, sur 14</h3>
<p class="lead">« SPB existant » est sans objet : Planet Aura n’avait pas de playbook ; le critère est couvert par la justification des améliorations. La note sur 14 est estimée globalement. En v5, une partie de la preuve est passée de l’écran à l’oral ou en secours : elle ne compte que si je la dis.</p>
{table(ARG, ['Critère', 'Niveau', 'Justification', 'Faiblesse restante', 'Correction'])}
<h3>Évaluation critique finale : le fond et le design, notés séparément</h3>
{table(CRIT, ['Dimension', 'Note estimée', 'Ce qui la porte', 'Ce qui la retient'])}
<div class="warn"><p class="wl">CE QUI FERAIT PERDRE DES POINTS LE JOUR J</p><p>Dépasser 20 minutes · lire les diapos ou ses notes pour compenser un écran plus léger · laisser croire que le cas est une vente réelle · présenter un objectif ou une simulation comme un résultat · répondre « assurance incluse » · citer un client ou un taux de droits de mémoire · ouvrir une diapo de secours par réflexe.</p></div>'''

if __name__ == '__main__':
    print(HTML)
