# Autoévaluation exigeante (grille Euridis), évaluation critique fond / design, et bilan avant / après de la version 4.
# Fragments HTML insérés dans le guide (sections 10 et 11).
import html

E = html.escape
ANIM = [
    ('Grab attention (Start with why)', '1 / 1', 'Houston : une scène, un silence, une question, puis « notre raison d’être ».',
     'Scène type entendue sur le terrain, pas un cas daté : un jury peut la trouver construite.', 'Le dire d’emblée, sans s’en excuser : « une scène type ».'),
    ('Rythme et dynamisme', '0,75 / 1', 'Un cas qui avance de diapo en diapo, des transitions annoncées, des pauses marquées.',
     'Le rythme réel n’a pas été éprouvé ; la diapo 14 reste la plus dense.', 'Trois répétitions chronométrées ; une seule zone montrée par diapo (voir « À montrer »).'),
    ('Langage et vocabulaire métier', '1 / 1', 'DDP, groupage, CAVE, PA-FIT, nurture, SPIN, Planet’Connect, Brevo : définis au premier usage.',
     'Beaucoup de sigles en peu de temps.', 'Une demi-phrase de définition, jamais plus.'),
    ('Support graphique', '1 / 1', 'Diapos 9, 10, 13 et 16 refondues ; document et capture réels ; parcours, chaînes, bandeaux de décision ; contrastes vérifiés.',
     'Une seule photo réelle.', 'Assumé : la preuve vient des documents réels ; ne rien ajouter sans photo vérifiée.'),
    ('Grammaire et orthographe', '1 / 1', 'Typographie française, relectures croisées, rendu vérifié diapo par diapo.',
     'Une coquille reste possible sur 36 diapos.', 'Dernière relecture à voix haute la veille.'),
    ('Respect du temps (20 min max)', '0,75 / 1', 'Script à 18:35, introduction à 4:52 ; trois points de passage ; plan de coupe d’environ 45 s, toujours sur les diapos à venir.',
     'Minutage théorique : la durée réelle reste à prouver.', 'Noter l’heure réelle aux trois points de passage, à chaque répétition.'),
]
ARG = [
    ('Titres du sommaire', 'Maîtrisé', 'Cinq étapes titrées par leur idée, reliées aux trois enjeux et aux parties du cahier des charges.', '—', '—'),
    ('Introduction qui amène le sujet', 'Maîtrisé', 'Scène → marché → entreprise → offre → diagnostic → problématique, en moins de 5 min.', '—', '—'),
    ('Marché relié à l’entreprise', 'Maîtrisé', 'Trois chiffres sourcés, cinq contraintes traduites en métier.',
     'Droits US : sources externes contradictoires depuis juillet 2026.', 'Renvoyer au simulateur ; ne jamais citer un taux de mémoire.'),
    ('Entreprise : organigramme, CA, offre, concurrence, cibles', 'Maîtrisé', 'Équipe, « qui vend, qui décide », CA ×4,7, circuit de vente, coût par bouteille, statu quo et quatre familles.',
     'Organigramme complet et fiches concurrents en secours (B9, B3).', 'Les ouvrir dès qu’une question l’appelle.'),
    ('Processus de vente et tunnels SPIN', 'Maîtrisé', 'Sept étapes (responsable, preuve, délai, outil), durées de cycle, dix gestes démontrés sur le cas, tunnel du vigneron en action.',
     'Durées de cycle : objectifs et repères terrain, non mesurés.', 'Le dire, avec la date de première mesure.'),
    ('Ressources précises, réalistes, échéancées, chiffrées', 'Maîtrisé', 'Ce que j’ai créé, distingué de ce qui reste à déployer ; trois premiers chantiers datés, attribués, chiffrés ; six en B13.',
     'État réel des chantiers de septembre-octobre à confirmer.', 'Vérifier la veille et le dire tel quel.'),
    ('Sales Ops et objectif de chacune', 'En cours → maîtrisé', 'Six outils et leur statut ; ce que le commercial y gagne ; alignement marketing-ventes ; intégration 30-60-90.',
     'Rituels et dictionnaire proposés, pas ratifiés.', 'Faire confirmer le statut par la direction.'),
    ('Indicateurs de performance', 'En cours → maîtrisé', 'Constaté / objectif ; source, fréquence, responsable, action ; point zéro ; revue mensuelle.',
     'Aucune valeur mesurée sur le funnel ; la décision citée est une règle conditionnelle.', 'Réponse courte prête : la méthode, pas encore la preuve.'),
    ('Améliorations et justifications', 'Maîtrisé', 'Cinq bandeaux Constat → Ma décision → Ce que l’on mesure relient chaque recommandation à un problème et à un bénéfice mesurable.', '—', '—'),
    ('Synthèse en lien avec les enjeux', 'Maîtrisé', 'Réponse enjeu par enjeu, apport, bénéfices visés, difficulté, limites.', '—', '—'),
    ('Ouverture', 'Maîtrisé', 'Diversification hors USA, lecture fin décembre, entretiens au T1 2027.', 'Sans objectif chiffré de diversification.', 'Dire qu’il sera fixé après la première lecture.'),
]
CRIT = [
    ('Fond', '18,5 / 20', 'Sources primaires et statuts partout ; un cas cohérent de bout en bout ; chaque décision reliée à un constat et à une mesure ; contribution personnelle lisible.',
     'Aucun résultat mesuré du playbook ; cas illustratif ; rituels non ratifiés ; droits US incertains à la date de l’oral.'),
    ('Design', '17,5 / 20', 'Identité homogène ; diapos denses refondues ; documents réels ; compositions variées (chaînes, parcours, cartes, bandeaux) ; aucun débordement.',
     'Les diapos 8, 17 et 19 restent riches ; une seule photo réelle.'),
]
AVANT_APRES = [
    ('9 · Personas', 'Trois cartes de neuf lignes et un pavé sombre d’étude', 'Trois colonnes : rôle, ce qui juge et inquiète, la citation en grand, ce que je montre ; l’étude en un bandeau', 'Voir en trois secondes qui décide, qui utilise, qui paie, et le discours adapté'),
    ('10 · Problèmes et solutions', 'Une matrice de quinze cellules', 'Une chaîne Problème → Besoin → Solution → Bénéfice → Preuve pour le domaine du cas ; champagne et caviste en deux lignes', 'Une idée, le cas au premier plan'),
    ('13 · SPIN', 'Le second tunnel en pavé sombre, concurrent du premier', 'Le tunnel du vigneron en pleine largeur, avec le rôle de chaque famille ; le second tunnel en B4, mot pour mot', 'Démontrer une méthode, pas deux'),
    ('16 · Ressources', 'Quatre vignettes et un Gantt de six lignes', 'Ce que j’ai créé, puis trois premiers chantiers : mois, responsable, temps, budget, critère ; les six en B13', 'Distinguer immédiatement l’apport et ce qui reste à faire'),
    ('11, 15, 16, 17, 19', 'Des encadrés de décision isolés', 'Un bandeau commun : Constat → Ma décision → Ce que l’on mesure (diapo 8 : encadré « Ma recommandation » et sa mesure)', 'Relier chaque recommandation à un problème et à un bénéfice mesurable'),
    ('12 · Prospecter', 'Des questions-réponses en texte', 'Trois gestes : préparer, viser les deux interlocuteurs, cadencer', 'Rendre visible l’étape « préparer »'),
    ('14 · Proposer', '« Un quart récupéré : 10 000 € »', '« Simulation » : 40 000 € de ventes potentiellement perdues ; « si un quart était récupéré » ; jamais un gain garanti', 'Ne rien promettre'),
    ('4 · Marché', '« 10 % depuis févr. 2026 »', '« Droits volatils depuis 2025 ; taux du jour au simulateur »', 'Sources externes contradictoires depuis juillet 2026'),
    ('Script oral', '2 345 mots, 18:42 ; quelques lectures d’écran', '2 330 mots, 18:35 ; décisions à la première personne, pauses, définitions, plan de coupe', 'Compléter l’écran au lieu de le lire'),
    ('Questions du jury', '35 questions', '41 questions, dont six sur la méthode et sa preuve, et une réponse courte à savoir par cœur', 'Séparer la méthode de la preuve de son efficacité'),
]


def table(rows, head, bold=2):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{"<b>" + E(c) + "</b>" if j < bold else E(c)}</td>' for j, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<table class="t"><tr>{th}</tr>{tr}</table>'


BILAN = table(AVANT_APRES, ['Diapo ou livrable', 'Avant (v3)', 'Après (v4)', 'Pourquoi'], bold=1)

HTML = f'''<h3>Ma note, critère par critère : exigeante, pour savoir où travailler</h3>
<div class="g3"><div class="k"><p class="score">5,5 / 6</p><p>Animation : support refondu ; rythme et temps encore à éprouver à voix haute.</p></div>
<div class="k"><p class="score">13 / 14</p><p>Argumentation : décisions justifiées et mesurables ; il manque encore une mesure réelle du playbook.</p></div>
<div class="k"><p class="score">≈ 18,5 / 20</p><p>Estimation avant répétition. Le 19-20 dépend du temps tenu et des réponses sur la preuve d’efficacité.</p></div></div>
<h3>Animation, sur 6</h3>
{table(ANIM, ['Critère', 'Ma note', 'Justification', 'Faiblesse restante', 'Correction'])}
<h3>Argumentation et analyse, sur 14</h3>
<p class="lead">« SPB existant » est sans objet : Planet Aura n’avait pas de playbook ; le critère est couvert par la justification des améliorations. La note sur 14 est estimée globalement.</p>
{table(ARG, ['Critère', 'Niveau', 'Justification', 'Faiblesse restante', 'Correction'])}
<h3>Évaluation critique finale : le fond et le design, notés séparément</h3>
{table(CRIT, ['Dimension', 'Note estimée', 'Ce qui la porte', 'Ce qui la retient'])}
<div class="warn"><p class="wl">CE QUI FERAIT PERDRE DES POINTS LE JOUR J</p><p>Dépasser 20 minutes · lire les diapos · laisser croire que le cas est une vente réelle · présenter un objectif ou une simulation comme un résultat · répondre « assurance incluse » · citer un client ou un taux de droits de mémoire.</p></div>'''

if __name__ == '__main__':
    print(HTML)
