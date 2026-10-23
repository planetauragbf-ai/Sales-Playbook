# Réécrit les notes orales (texte dit + indications entre parenthèses) des 19 diapos principales.
# Les indications de régie existantes sont conservées sauf si NOTES fournit les siennes.
import os, re
D = os.path.join(os.path.dirname(__file__), '..', 'deck', 'project', 'slides')

NOTES = {
'cover': ("""Bonjour à toutes et à tous. Je suis Emma Soares Britschgy, en alternance chez Planet Aura, à Castres, comme chargée de projets et développement. Je vais vous présenter le Sales Playbook que j’ai construit pour notre équipe commerciale.""", None),
'accroche': ("""« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. » (Silence d’une seconde.)

Cette phrase, nos commerciaux l’entendent chaque saison dans les caveaux. 22 bouteilles de vente perdue : pas à cause du prix, pas à cause du vin, à cause d’une valise.

C’est pour cela que Planet Aura existe. Notre pourquoi : lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu’il soit.

Et c’est pour cela que j’ai écrit ce playbook : pour que chaque commercial sache transformer ce couple de Houston en client livré, et ce caveau en adhérent fidèle.""",
"(Énergie : c’est le moment le plus important des 20 minutes. Regarder chaque membre du jury. Anecdote = vécu terrain, ne pas la présenter comme une donnée du dossier.)"),
'sommaire': ("""Mon parcours suit celui d’un commercial, en quatre temps : analyser le marché et l’entreprise, cibler les bons comptes et les bons décideurs, vendre, du premier appel au premier envoi, puis piloter, avec des outils et des indicateurs. Je conclurai par une synthèse et une ouverture.""",
"(15 secondes, pas plus : le jury lit le sommaire, ne pas le réciter.)"),
'marche': ("""Le marché, en trois constats. Un : le monde boit moins, 214 millions d’hectolitres en 2024, le plus bas niveau depuis 1961 selon l’OIV. Deux : l’export se complique ; en 2025, les exportations vers les États-Unis ont reculé de 21 %, et ils restent pourtant le premier marché, avec des droits de 15 %. Trois, notre gisement : 5,4 millions d’œnotouristes étrangers par an, 207 euros dépensés par visite, dont 60 % en vin.

Pour Planet Aura, 64,5 % des envois partent aux États-Unis : c’est un risque, mais aussi une chance, car plus les règles se durcissent, plus un spécialiste devient précieux. La preuve : en 2025, quand l’export reculait de 7,9 %, notre chiffre d’affaires progressait de 11,6 %.""", None),
'enjeux': ("""Et la croissance continue : déjà plus 18,7 % cette année à fin septembre, environ 145 nouveaux adhérents en douze mois pour 120 visés. Mais elle s’est construite au bouche-à-oreille : un premier commercial dédié arrivé fin 2025, un CRM historisé depuis 2025 seulement, et un seul pays qui pèse 64,5 % des envois.

D’où ma problématique : comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente reproductible et mesurable, pour recruter, activer et fidéliser nos adhérents ?

Ma réponse : un Sales Playbook, le référentiel de l’équipe de vente, qui sert aussi à intégrer tout nouveau commercial.""", None),
'entreprise': ("""Planet Aura est née d’un vide : en 2019, le pionnier IziWine ferme du jour au lendemain ; deux anciens, Floriane et Brice, créent Planet Aura à Castres.

Nous ne sommes pas transporteur mais commissionnaire de transport : nous choisissons le bon schéma, UPS, FedEx ou notre groupage, et nous répondons du résultat de bout en bout. Notre filiale de New York, licenciée importateur et grossiste, permet de livrer un Américain taxes payées.

En chiffres : 1,15 million d’euros de chiffre d’affaires en 2025, multiplié par 4,7 depuis 2021, 6 643 expéditions en douze mois, 262 adhérents, et une équipe de 13 personnes en quatre pôles.""", None),
'offre': ("""Notre client, c’est le caveau ; celui qui reçoit le colis, c’est son visiteur étranger. L’offre se vend en trois temps.

La porte d’entrée : la France et l’Europe, sans douane, dès 15 euros. Le produit phare : le groupage vers les États-Unis, taxes payées d’avance ; pour 12 bouteilles vers le Texas, 210 euros de transport, environ 270 euros tout compris, réglés à la commande. Enfin, ce qui fidélise : les cartons homologués, le certificat Champagne géré pour 15 euros, et une assurance en option jusqu’à 20 000 euros, souscrite pour neuf envois sur dix. Le tout sans abonnement ni minimum.""", None),
'concurrence': ("""Notre premier concurrent, c’est le statu quo : le caveau qui laisse repartir son client avec deux bouteilles au lieu de vingt-quatre.

Ensuite, quatre familles. Les expressistes, UPS, FedEx, DHL, sont nos sous-traitants. Les grands généralistes visent les gros volumes. Notre vraie famille, ce sont les spécialistes du vin, comme Dartess ou Viticolis ; peu cumulent un statut de commissionnaire, une filiale licenciée aux États-Unis et leur propre plateforme. Les pionniers de la voile, comme VELA, seraient plutôt des partenaires.

Nous ne sommes pas les moins chers ; nous sommes plus complets et plus sûrs sur le petit, précieux et compliqué. On ne vend pas contre les autres : on vend contre le risque.""", None),
'icp': ("""Pour définir nos cibles, je suis partie de nos dix meilleurs clients réels sur douze mois. Leurs noms restent confidentiels, mais leur profil parle : aucun n’est un « gros » au sens classique ; ce sont des lieux où des étrangers goûtent un vin et veulent le ramener.

J’en ai tiré cinq critères, dans l’ordre : le volume de clientèle étrangère, une bouteille à plus de 12 euros, un responsable caveau ou un e-shop, les destinations, États-Unis en tête, et la saisonnalité.

Ils donnent cinq ICP et une répartition de l’effort : 60 % sur les domaines avec caveau, notre cœur de cible, puis la Champagne, les cavistes, l’œnotourisme et les salons. Les distilleries sont en test depuis notre offre spiritueux 2026.

Pour classer un compte de la même façon, un score express sur 20 au téléphone, puis la grille PA-FIT sur 100, la seule saisie au CRM. Un petit domaine peut être P1 ; un gros négociant peut rester P2 : l’adéquation prime sur la taille.""", None),
'personas': ("""L’ICP dit quelle entreprise viser ; le persona, à qui je parle. Dans un même domaine, le vigneron décide, la responsable caveau utilise l’outil, et le touriste américain paie le transport. Au vigneron, je parle simplicité ; au caveau, rapidité au comptoir ; au caviste, trésorerie ; à la maison de Champagne, image et conformité.

En octobre, je les ai confrontés à nos données réelles : 70 contacts professionnels, 47 réponses à nos trois enquêtes et 15 avis Google.

Les cinq tiennent, avec des corrections : le caviste n’est pas seulement urbain, il est aussi touristique ou en ligne ; dans une grande maison, le quotidien passe par l’ADV. Et un angle mort : une dizaine de contacts sont des assistants ADV ou des comptables, qui utilisent la plateforme tous les jours. Ils entrent désormais dans le comité d’achat.""", None),
'solutions': ("""Pour chaque cible, trois questions : quelle douleur, quelle solution, quelle preuve ?

Pour le domaine avec caveau, la douleur, c’est la vente perdue, notre couple de Houston : le simulateur donne le prix en vingt secondes et le groupage part taxes payées. Pour la maison de Champagne, c’est le certificat CIVC : un original oublié, et le colis reste en douane ; nous le gérons à chaque envoi hors Union européenne. Le caviste raisonne trésorerie : son client paie le transport avec son vin, en trois minutes de saisie. Et la distillerie n’avait aucune solution : depuis 2026, nous expédions des spiritueux aux particuliers américains.

Enfin, le playbook dit quand refuser : vente 100 % B2B, crédit fournisseur, délais garantis. Le dire d’emblée protège la relation et notre marge.""",
"(Œnotourisme si on le demande : notre premier client est une agence de wine tours. Délais : toujours estimatifs, jamais garantis.)"),
'processus': ("""Avant ce playbook, chacun vendait à sa façon. J’ai découpé la vente en sept étapes, avec une règle : une étape n’existe que si sa preuve est dans le CRM.

Et la vente ne s’arrête pas à la signature : un adhérent qui n’expédie jamais ne rapporte rien. Le commercial reste responsable jusqu’au premier envoi, sous trente jours : c’est notre vraie ligne d’arrivée.

Notre premier argument, c’est la vitesse : rappel sous 24 heures, proposition moins de 24 heures après le rendez-vous. Le cycle va d’une à trois semaines pour un dossier standard, à six à douze semaines pour une maison de Champagne : des durées observées, que nous recalculerons sur 90 jours de CRM.

Pour la prospection : huit touches en dix-huit jours pour les comptes structurés, une cadence plus courte, terrain d’abord, pour les caveaux. Dès que le prospect répond, l’automatisation s’arrête.

Le recrutement fonctionne déjà : environ 145 adhérents signés en douze mois, pour 120 visés.""", None),
'spin': ("""Le cœur du rendez-vous, c’est le tunnel SPIN de Neil Rackham, avec une règle : diagnostiquer avant de démontrer.

La découverte dure 35 minutes, en six séquences ; le plus long bloc, douze minutes, porte sur un flux réel du prospect, pas sur notre présentation.

Prenons un vigneron avec caveau. Une seule question de situation : comment organisez-vous vos envois quand un visiteur étranger veut plus que sa valise ? Deux de problème : combien de fois par semaine un client repart-il avec moins que ce qu’il voulait ? Deux d’implication : sur une saison, combien de ventes de douze bouteilles tombent à deux, et que représente ce manque ? Une de bénéfice : livrés chez eux, que deviendrait votre panier moyen ?

À ce moment-là, ce n’est plus moi qui chiffre la perte : c’est lui. Je reformule avec ses mots, il valide, et cette phrase ouvre ma proposition. On ne sort jamais sans une action, un responsable et une date.""",
"(N = Need-payoff, « bénéfice attendu ». Le RDV complet dure 45 min, dont ces 35 de découverte. En pleine saison, au téléphone : 2 questions en 45 s. Version Champagne : diapo de secours B4.)"),
'objections': ("""Une objection n’est pas un refus, c’est une demande d’information. Nous la traitons en quatre temps : accueillir, clarifier, prouver avec une seule preuve, vérifier.

Le playbook en traite vingt-six ; ces cinq-là s’apprennent par cœur. Le prix d’abord : 43 % de nos clients le jugent moyennement compétitif, donc on ne le défend pas, on le ramène à la bouteille : environ 17,50 euros de transport par bouteille livrée aux États-Unis, payés par le client final. La casse : une assurance en option, choisie pour près de neuf envois sur dix.

Mais ce qui fait signer, c’est le ROI. Trente visiteurs étrangers par semaine, un sur trois, 300 euros, vingt semaines : 60 000 euros de ventes potentielles. Même à 25 %, il reste 15 000 euros, pour 110 euros de cartons. Ce calcul se fait à voix haute, avec les chiffres du prospect : un ROI qu’il a construit lui-même ne se conteste pas.""",
"(60 000 € = ventes de vin du domaine, pas CA Planet Aura : un exemple à refaire avec ses chiffres. Détail du prix rendu : diapo de secours B7.)"),
'ressources': ("""Nos prospects posent toujours trois questions : combien ça coûte, et si ça casse, est-ce que ça marche ? Pour chacune, le commercial a quelque chose à montrer : le simulateur sur ses vins, le carton homologué posé sur la table, la fiche Google à 4,8 sur 5.

J’ai recensé dix-sept ressources : treize existent et sont utilisées, dont une fiche par concurrent. Quatre manquent : les one-pagers par ICP, les études de cas, la vidéo démo et le webinaire.

Chaque chantier a une date, un responsable, un temps, un budget et un critère de passage. Exemple : deux salons pour 1 000 euros, à condition d’obtenir huit rendez-vous qualifiés par salon ; sinon, on ne recommence pas. Au total, 3 000 euros de dépenses externes ; le vrai coût, c’est notre temps, réservé dans le planning.""",
"(Le jour J, dire où en sont les chantiers de septembre et d’octobre : fait, en cours ou décalé. Vidéo démo et études de cas : hors budget, après validation, et accord écrit des adhérents cités.)"),
'salesops': ("""Le cahier des charges demande les Sales Ops réellement en place. Les outils existent : HubSpot, Planet’Connect et ses tableaux de bord, Google Workspace, la signature électronique. Le playbook ajoute des règles.

La première : une donnée, un propriétaire, une décision. HubSpot est la source de vérité ; Brevo s’y alimente, jamais l’inverse, ce qui protège aussi nos consentements RGPD. Le câblage est prévu en novembre ; d’ici là, les relances sont créées à la main.

Planet’Connect exécute : commandes, suivi, factures, une trentaine d’emails automatiques. Ses tableaux de bord fournissent tous les chiffres que je vous présente.

Pour intégrer un commercial : certifié à J+30, autonome à J+60, il pilote à J+90. Et le CRM tient grâce aux rituels : chaque lundi, on mesure la complétude des opportunités ; sous 95 %, le dossier sort du forecast.""",
"(Score d’hygiène et rituels : recommandations « à ratifier en revue d’équipe », ne pas dire « mis en place ». Pas d’outil de BI dédié : ce sont les tableaux de bord natifs. Sales Navigator : selon dotation, non acquis.)"),
'kpi': ("""Un directeur commercial, comme un jury, pose toujours la même question : ce chiffre, il est mesuré ou espéré ? Chaque indicateur du playbook porte donc un statut, une formule, une fréquence, un responsable et une action.

Constaté : environ 145 adhérents signés en douze mois pour 120 visés, et 1,45 % de commandes annulées pour moins de 2 % visés.

Baseline : 6 643 expéditions, dont 64,5 % vers les États-Unis. C’est le point zéro qui rendra l’avant/après mesurable, notamment notre diversification.

Objectif, présenté comme tel : 70 % des nouveaux adhérents activés sous 30 jours. Notre CRM n’historise que depuis 2025 : on mesure donc 90 jours sans maquiller, puis on fixe les cibles par segment.

Le suivi : une revue mensuelle de 45 minutes sur une page, qui commence par la qualité de la donnée et se termine par une décision.""",
"(Toujours « signés », jamais « actifs ». Les 145 précèdent la version finale du playbook : performance de l’équipe que le playbook rend reproductible. 227 « récents » n’est PAS le KPI actifs. Satisfaction 4,65/5 sur 23 réponses. Tableau complet : diapo B6.)"),
'synthese': ("""En résumé : Planet Aura grandissait vite, mais son savoir commercial vivait dans quelques têtes, avec des chiffres qui variaient d’un support à l’autre. Le playbook apporte une source unique et un chemin commun : cibler, vendre, outiller, piloter. Il répond à nos enjeux : croître sans dépendre d’un seul pays, et prouver notre valeur quand le marché se durcit.

Le fil rouge tient en une phrase : le prospect n’achète pas un transport, il cherche à réduire son risque.""",
"(Jamais « le playbook a produit » : il rend reproductible. Ce que j’ai produit : la consolidation des chiffres, l’étude des personas, la rédaction et les règles ; Planet’Connect et les procédures existaient.)"),
'ouverture': ("""Trois difficultés ont fait les règles du playbook : des chiffres divergents, d’où une source unique ; des projets qui bougent, toujours au conditionnel ; et l’envie de tout dire, d’où les annexes.

La suite est au calendrier : une version enrichie en novembre, une première lecture avant/après fin décembre, et une version 2027 nourrie de vrais entretiens clients.

Je reviens à ce couple de Houston. Aujourd’hui, un caveau formé avec ce playbook lui répond en trente secondes : 24 bouteilles, 360 euros de transport, les taxes calculées d’avance, livrées en trois semaines environ. Ils repartent les mains libres.

Merci. Je suis prête pour vos questions.""",
"(Taxes DDP, dossier 17 € et assurance en option en sus des 360 €. Délai estimatif, jamais garanti. Dire si la version de novembre est sortie, selon la date du jury.)"),
}

for sid, (spoken, cue) in NOTES.items():
    p = os.path.join(D, f'{sid}.html')
    s = open(p).read()
    old = re.search(r'<aside>(.*?)</aside>', s, re.S).group(1)
    if cue is None:
        cues = [l for l in old.split('\n') if l.strip().startswith('(')]
        cue = '\n'.join(cues)
    new = '[⏱] ' + spoken.strip() + ('\n\n' + cue if cue else '')
    s = s.replace(old, new)
    open(p, 'w').write(s)
print('notes ok')
