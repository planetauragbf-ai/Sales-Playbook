# Autoévaluation exigeante, critère par critère de la grille Euridis (fragment HTML inséré dans le guide, section 10).
import html, os

E = html.escape
ANIM = [
    ('Grab attention (Start with why)', '1 / 1', 'Houston : une scène, un silence, une question, puis « notre pourquoi ».',
     'Scène type racontée par les adhérents, pas un cas daté : un jury peut la trouver construite.', 'Le dire d’emblée (« une scène que nos adhérents nous racontent »), sans s’en excuser.'),
    ('Rythme et dynamisme', '0,75 / 1', 'Un cas qui avance de diapo en diapo, une transition par étape, vingt diapos en 18-19 min.',
     'Les diapos 14 (proposer) et 19 (indicateurs) sont denses : risque de ralentir ou de lire.', 'Une seule zone montrée par diapo (voir « À montrer ») ; répéter ces deux diapos à voix haute.'),
    ('Langage et vocabulaire métier', '1 / 1', 'DDP, POA, CIVC, three-tier, ISTA 3A, PA-FIT, SPIN, cadence, activation.',
     'Trop de sigles d’affilée sur la diapo du marché.', 'Définir chaque sigle au premier usage, en une demi-phrase.'),
    ('Support graphique', '0,75 / 1', 'Captures réelles, pages réelles, frises, score, compositions variées, une idée par diapo.',
     'Peu de photos (une seule, l’équipe) ; quelques diapos restent riches en texte à 24 px.', 'Assumé : la preuve vient des captures ; ne rien ajouter sans photo réelle.'),
    ('Grammaire et orthographe', '1 / 1', 'Typographie française, relectures indépendantes, vérification diapo par diapo.',
     'Une coquille reste toujours possible sur 36 diapos.', 'Dernière relecture à voix haute la veille.'),
    ('Respect du temps (20 min max)', '0,75 / 1', 'Script à 18:40 ; trois points de passage ; coupes prévues.',
     'Le script n’a pas encore été dit en conditions réelles : le vrai temps reste inconnu.', 'Trois répétitions chronométrées, dont une filmée ; noter l’heure réelle aux trois points de passage.'),
]
ARG = [
    ('Titres du sommaire', 'Maîtrisé', 'Cinq étapes titrées par leur idée, reliées aux trois enjeux.', '—', '—'),
    ('Introduction qui amène le sujet', 'Maîtrisé', 'Scène → marché → entreprise → offre → diagnostic → problématique, en 4:52.', '—', '—'),
    ('Marché relié à l’entreprise', 'Maîtrisé', 'Trois chiffres sourcés, cinq contraintes traduites en métier.',
     'Une seule diapo : pas de taille de marché du transport de vin.', 'Réponse prête (Q et B10) ; ne pas l’inventer.'),
    ('Entreprise : organigramme, CA, offre, concurrence, cibles', 'Maîtrisé', 'Équipe, « qui vend, qui décide », CA ×4,7, marchés, grille, statu quo et quatre familles.',
     'Organigramme complet et fiches concurrents seulement en secours (B9, B3).', 'Proposer B9 ou B3 dès qu’une question l’appelle.'),
    ('Processus de vente et tunnels SPIN', 'Maîtrisé', 'Sept étapes avec responsable, preuve, délai et outil ; prospection, SPIN, proposition et activation sur le cas.',
     'Durées de cycle : objectifs et hypothèse terrain, non mesurées.', 'Le dire, avec la date de première mesure.'),
    ('Ressources précises, réalistes, échéancées, chiffrées', 'Maîtrisé', 'Pages réelles ; six chantiers avec responsable, temps, budget, critère ; 3 000 €.',
     '≈ 200 h est mon calcul ; état des chantiers de septembre-octobre à confirmer.', 'Vérifier l’état réel la veille et le dire tel quel.'),
    ('Sales Ops et objectif de chacune', 'En cours → maîtrisé', 'Six outils, statut de chacun, alignement marketing-ventes, onboarding 30-60-90.',
     'Rituels et règles proposés, pas ratifiés ; pas de « marketing » nommé dans l’organigramme.', 'Faire confirmer par la direction le statut des rituels ; question C5 prête sur l’alignement.'),
    ('Indicateurs de performance', 'En cours → maîtrisé', 'Constaté / objectif ; source, fréquence, responsable, action ; revue mensuelle.',
     'Aucune valeur mesurée sur le funnel ; l’exemple de décision est une règle conditionnelle.', 'L’assumer : point zéro posé, première lecture fin décembre.'),
    ('Synthèse en lien avec les enjeux', 'Maîtrisé', 'Réponse enjeu par enjeu, apport, bénéfices attendus, limites.', '—', '—'),
    ('Ouverture', 'Maîtrisé', 'Diversification hors USA, lecture fin décembre, entretiens T1 2027.', 'Ouverture prudente, sans objectif chiffré de diversification.', 'Ne pas inventer de cible : dire qu’elle sera fixée après la première lecture.'),
]


def table(rows, head):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''.join('<tr>' + ''.join(f'<td>{"<b>" + E(c) + "</b>" if j < 2 else E(c)}</td>' for j, c in enumerate(r)) + '</tr>' for r in rows)
    return f'<table class="t"><tr>{th}</tr>{tr}</table>'


HTML = f'''<h3>Ma note, critère par critère : exigeante, pour savoir où travailler</h3>
<div class="g3"><div class="k"><p class="score">5,25 / 6</p><p>Animation : solide sur le fond, deux risques de rythme et un temps encore non éprouvé.</p></div>
<div class="k"><p class="score">12,5 / 14</p><p>Argumentation : les parties 8 à 14 sont démontrées ; Sales Ops et KPI restent des propositions et des objectifs.</p></div>
<div class="k"><p class="score">≈ 17,5 / 20</p><p>Estimation avant répétition. Les 18-20 dépendent de trois choses : le temps tenu, la fluidité sur les diapos denses, les réponses aux questions sur le cas.</p></div></div>
<h3>Animation, sur 6</h3>
{table(ANIM, ['Critère', 'Ma note', 'Justification', 'Faiblesse restante', 'Correction'])}
<h3>Argumentation et analyse, sur 14</h3>
<p class="lead">« SPB existant » est sans objet : Planet Aura n’avait pas de playbook. La note sur 14 est estimée globalement, à partir de ces dix critères.</p>
{table(ARG, ['Critère', 'Niveau', 'Justification', 'Faiblesse restante', 'Correction'])}
<div class="warn"><p class="wl">CE QUI FERAIT PERDRE DES POINTS LE JOUR J</p><p>Dépasser 20 minutes · lire les diapos denses · laisser croire que le cas est une vente réelle · présenter un objectif comme un résultat · répondre « assurance incluse » · citer un client.</p></div>'''

if __name__ == '__main__':
    print(HTML)
