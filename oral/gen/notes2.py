# Deuxième passe sur les notes orales, après la vérification des faits et la relecture de la grille.
import os, re
D = os.path.join(os.path.dirname(__file__), '..', 'deck', 'project', 'slides')

NOTES = {
'cover': ("""Bonjour à toutes et à tous.""",
"(Sourire, une seconde de silence, puis passer tout de suite à l’accroche : je me présente juste après la citation.)"),
'accroche': ("""« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. » (Silence d’une seconde.)

Cette scène, nos adhérents nous la racontent chaque saison. 22 bouteilles jamais vendues : pas à cause du prix, pas à cause du vin, à cause d’une valise.

Je suis Emma Soares Britschgy, chargée de projets et de développement en alternance chez Planet Aura, à Castres. Notre métier : expédier le vin des domaines jusque chez leurs clients, partout dans le monde. Notre pourquoi : lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu’il soit.

Et c’est pour cela que j’ai écrit ce Sales Playbook : pour que chaque commercial sache transformer ce couple de Houston en client livré, et ce caveau en adhérent fidèle.""",
"(Énergie : c’est le moment le plus important des 20 minutes. Regarder chaque membre du jury. La scène est une situation type que racontent nos adhérents, pas une statistique.)"),
'marche': ("""Le marché, en trois constats. Un : le monde boit moins, 214 millions d’hectolitres en 2024, le plus bas niveau depuis 1961 selon l’OIV. Deux : l’export se complique ; en 2025, les exportations françaises vers les États-Unis ont reculé de 21 %, et les États-Unis restent pourtant le premier marché, avec des droits de 15 %. Trois, notre gisement : 5,4 millions d’œnotouristes étrangers en France en 2023, et 207 euros de retombées par visite, dont 60 % en vin.

Pour Planet Aura, 64,5 % des envois partent aux États-Unis : c’est un risque, mais aussi une chance, car plus les règles se durcissent, plus un spécialiste devient précieux. La preuve : en 2025, quand les exportations françaises de vins et spiritueux reculaient de 7,9 %, notre chiffre d’affaires progressait de 11,6 %.""", None),
'entreprise': ("""Planet Aura est née d’un vide : en 2019, le pionnier IziWine ferme ; deux de ses anciens, Floriane et Brice, créent Planet Aura à Castres.

Nous ne sommes pas transporteur mais commissionnaire de transport : nous choisissons le bon schéma, UPS, FedEx ou notre groupage, et nous répondons du résultat de bout en bout, jusqu’aux États-Unis grâce à notre filiale de New York.

En chiffres : 1,15 million d’euros de chiffre d’affaires en 2025, multiplié par 4,7 depuis 2021, 6 643 expéditions en douze mois, 262 adhérents, et une équipe de 13 personnes en quatre pôles.""",
"(Ne jamais dire « transporteur ». ×4,7 = de 2021 à 2025. Les 227 ont expédié dans les 9 derniers mois : ce n’est pas le KPI « actifs ». Le dossier écrit dit « une dizaine de personnes » : 13 en comptant la filiale.)"),
'offre': ("""Notre client, c’est le caveau ; celui qui reçoit le colis, c’est son visiteur étranger. L’offre se vend en trois temps.

La porte d’entrée : la France et l’Europe, sans douane, dès 15 euros. Le produit phare : le groupage vers les États-Unis, taxes payées d’avance ; pour 12 bouteilles vers le Texas, 210 euros de transport, et environ 270 euros avec les taxes estimées, le dossier et l’assurance en option, réglés à la commande. Enfin, ce qui fidélise : les cartons homologués, le certificat CIVC géré pour 15 euros, et une assurance en option jusqu’à 20 000 euros, souscrite pour neuf envois sur dix. Le tout sans abonnement ni minimum.""", None),
'concurrence': ("""Notre premier concurrent, c’est le statu quo : le caveau qui laisse repartir son client avec deux bouteilles au lieu de vingt-quatre.

Ensuite, quatre familles. Les expressistes, UPS, FedEx, DHL, sont nos sous-traitants. Les grands généralistes visent les volumes contractuels. Les pionniers de la voile, comme VELA, seraient plutôt des partenaires. Notre vraie famille, ce sont les spécialistes du vin : peu cumulent un statut de commissionnaire, une filiale agréée aux États-Unis et leur propre plateforme.

Nous ne sommes ni les moins chers ni les plus gros : nous sommes plus complets et plus sûrs sur le petit, précieux et compliqué. On ne vend pas contre les autres : on vend contre le risque.""", None),
'processus': ("""Avant ce playbook, chacun vendait à sa façon. J’ai découpé la vente en sept étapes, avec une règle : une étape n’existe que si sa preuve est dans le CRM.

Et la vente ne s’arrête pas à la signature : un adhérent qui n’expédie jamais ne rapporte rien. Le commercial reste responsable jusqu’au premier envoi, sous trente jours : c’est notre vraie ligne d’arrivée.

Notre premier argument, c’est la vitesse : rappel sous 24 heures, proposition moins de 24 heures après le rendez-vous. Le cycle visé est d’une à trois semaines pour un dossier standard ; pour une maison de Champagne, on observe six à douze semaines. Nous recalculerons ces durées sur 90 jours de CRM.

Pour la prospection : huit touches en dix-huit jours pour les comptes structurés, une cadence plus courte, terrain d’abord, pour les caveaux. Dès que le prospect répond, la cadence s’arrête.

Le recrutement fonctionne déjà, avant même le playbook : environ 145 adhérents signés en douze mois, pour 120 visés.""",
"(« Signés », jamais « actifs ». Le câblage Brevo + HubSpot est prévu en novembre : d’ici là, tâches créées à la main.)"),
'spin': ("""Le cœur du rendez-vous, c’est le tunnel SPIN de Neil Rackham, avec une règle : diagnostiquer avant de démontrer.

Le rendez-vous suit une trame de 35 minutes ; le plus long bloc, douze minutes, porte sur un flux réel du prospect, pas sur notre présentation.

Prenons un vigneron avec caveau. Une seule question de situation : comment organisez-vous vos envois quand un visiteur étranger veut plus que sa valise ? Deux de problème : combien de fois par semaine un client repart-il avec moins que ce qu’il voulait ? Deux d’implication : sur une saison, combien de ventes de douze bouteilles tombent à deux, et que représente ce manque ? Une de bénéfice : livrés chez eux, que deviendrait votre panier moyen ?

À ce moment-là, ce n’est plus moi qui chiffre la perte : c’est lui. Je reformule avec ses mots, il valide, et cette phrase ouvre ma proposition.

Le tunnel change avec le persona. Pour une maison de Champagne, l’implication devient : que coûte un colis immobilisé en douane à l’image de la maison ? Chaque persona a sa version, en annexe E. Et on ne sort jamais sans une action, un responsable et une date.""",
"(N = Need-payoff, « bénéfice attendu ». Le RDV complet dure 45 min, dont cette trame de 35. Version Champagne complète : diapo de secours B4.)"),
'objections': ("""Une objection n’est pas un refus, c’est une demande d’information. Nous la traitons en quatre temps : accueillir, clarifier, prouver avec une seule preuve, vérifier.

Le playbook en traite vingt-six ; ces cinq-là s’apprennent par cœur. Le prix d’abord. 43 % de nos clients le jugent moyennement compétitif. Alors on ne le défend pas : on le ramène à la bouteille. Environ 17,50 euros de transport par bouteille livrée aux États-Unis, et c’est le client final qui les paie. La casse ensuite : une assurance en option, choisie pour près de neuf envois sur dix.

Mais ce qui fait signer, c’est le ROI. Trente visiteurs étrangers par semaine, un sur trois, 300 euros, vingt semaines : 60 000 euros de ventes potentielles. Si 25 % seulement se concrétisent, il reste 15 000 euros, pour 110 euros de cartons. Ce calcul se fait à voix haute, avec les chiffres du prospect : un ROI qu’il a construit lui-même ne se conteste pas.""", None),
'ressources': ("""Nos prospects posent toujours trois questions. Combien ça coûte ? Et si ça casse ? Est-ce que ça marche vraiment ? Pour chacune, le commercial a quelque chose à montrer : le simulateur sur ses vins, le carton homologué posé sur la table, la fiche Google à 4,8 sur 5.

J’ai recensé dix-sept ressources : treize existent et sont utilisées. Quatre manquent : des fiches d’une page par ICP, les études de cas, la vidéo démo et le webinaire. S’y ajoutent les fiches de comparaison face à chaque concurrent.

Chaque chantier a une date, un responsable, un temps, un budget et un critère de passage. Exemple : deux salons pour 1 000 euros, à condition d’obtenir huit rendez-vous qualifiés par salon ; sinon, on ne recommence pas. Au total, environ 200 heures de temps interne et 3 000 euros de dépenses externes.""", None),
'salesops': ("""Le cahier des charges demande les Sales Ops réellement en place. Les outils existent : HubSpot, Planet’Connect et ses tableaux de bord, Google Workspace, la signature électronique. Le playbook ajoute des règles.

La première : une donnée, un propriétaire, une décision. HubSpot est la source de vérité ; Brevo s’y alimente, jamais l’inverse, ce qui protège aussi nos consentements RGPD. Le câblage est prévu en novembre ; d’ici là, les relances sont créées à la main.

Planet’Connect exécute : commandes, suivi, factures, une trentaine d’e-mails automatiques. Ses tableaux de bord fournissent tous nos chiffres d’activité.

Un nouveau commercial est certifié à J+30, autonome à J+60, et pilote son activité à J+90. Et pour que le CRM tienne, je propose un rituel : chaque lundi, on mesurerait la complétude des opportunités ; sous 95 %, le dossier sortirait du prévisionnel.""",
"(Score de complétude et rituels : recommandations « à ratifier en revue d’équipe », ne pas dire « mis en place ». Pas d’outil de BI dédié : ce sont les tableaux de bord natifs. Sales Navigator : selon dotation, non acquis.)"),
'kpi': ("""Un directeur commercial, comme un jury, pose toujours la même question : ce chiffre, il est mesuré ou espéré ? Chaque indicateur du playbook porte donc un statut, une formule, une fréquence, un responsable et une action.

Constaté : environ 145 adhérents signés en douze mois pour 120 visés, et 1,45 % de commandes annulées pour moins de 2 % visés.

Le point zéro ensuite : 6 643 expéditions, dont 64,5 % vers les États-Unis. C’est la base qui rendra l’avant/après mesurable, notamment notre diversification.

Objectif enfin, présenté comme tel : 70 % des nouveaux adhérents activés sous 30 jours. Notre CRM n’historise que depuis 2025 : on mesure donc 90 jours sans maquiller, puis on fixe les cibles par segment.

Le suivi : les tableaux de bord HubSpot et Planet’Connect, et une revue mensuelle de 45 minutes avec la direction, sur une page. Elle commence par la qualité de la donnée et se termine par une décision.""", None),
'synthese': ("""En résumé, je reviens à ma problématique : recruter, activer, fidéliser. Pour recruter, des cibles et un score au lieu de 448 prospects non qualifiés. Pour activer, une vente qui ne se termine qu’au premier envoi. Pour fidéliser, un suivi par tier et le réveil des dormants. Et pour durer : une méthode transmissible, une source unique pour les chiffres, et notre dépendance aux États-Unis suivie chaque trimestre.

Le fil rouge tient en une phrase : le prospect n’achète pas un transport, il cherche à réduire son risque.""", None),
'ouverture': ("""Trois difficultés ont fait les règles du playbook : des chiffres divergents, d’où une source unique ; des projets qui bougent, toujours au conditionnel ; et l’envie de tout dire, d’où les annexes.

La suite est datée : une version enrichie en novembre, une première lecture avant/après fin décembre, des entretiens clients au premier trimestre 2027. Et demain, le même cadre pourra accompagner notre diversification vers le Royaume-Uni, l’Europe et le Japon.

Je reviens à ce couple de Houston. Aujourd’hui, un caveau formé avec ce playbook lui répond en vingt secondes : 24 bouteilles, 360 euros de transport, les taxes estimées et payées d’avance, livrées en trois semaines environ. Ils repartent les mains libres.

Merci. Je suis prête pour vos questions.""", None),
}

for sid, (spoken, cue) in NOTES.items():
    p = os.path.join(D, f'{sid}.html')
    s = open(p).read()
    old = re.search(r'<aside>(.*?)</aside>', s, re.S).group(1)
    if cue is None:
        cue = '\n'.join(l for l in old.split('\n') if l.strip().startswith('('))
    s = s.replace(old, '[⏱] ' + spoken.strip() + ('\n\n' + cue if cue else ''))
    open(p, 'w').write(s)
print('notes2 ok')
