# Notes d'oratrice : secours (B1-B16) ; les 20 diapos principales sont dans notes_main.py : ce qui se DIT. L'écran montre, la voix explique et décide.
# Les indications entre parenthèses ne sont pas dites et ne comptent pas dans le minutage.

from notes_main import NOTES  # notes des 20 diapos principales (v4)

BACKUP_NOTES = {
'b1': """Si on me demande si mes personas sont réels : je les ai confrontés en octobre 2026 à 70 contacts professionnels et à 47 réponses de nos trois enquêtes, plus 15 avis. Résultat : cinq profils confirmés, trois ajustements, comme le caviste, qui n'est pas seulement urbain, et un angle mort, l'ADV, les comptables et la logistique, traités par le comité d'achat.

Ma limite, je la dis : ce sont des échanges écrits, pas encore des entretiens dédiés, et les prospects sont sous-représentés. Les entretiens sont prévus au premier trimestre 2027.

(Ne jamais dire « j'ai interviewé 70 clients ». 49 contacts rattachés : 14 + 8 + 7 + 15 + 5. Aucun nom.)""",

'b2': """Si on me dit que c'est une usine à gaz : chaque outil a un rôle différent, et un seul fait foi. CAVE sert à trier, avant d'investir du temps. Le score express sur 20 est un brouillon de terrain. Le PA-FIT sur 100 est la seule grille saisie dans le CRM : c'est lui qui décide de l'entrée en cadence, à partir de 55. Et les tiers A, B, C ne disent pas qui appeler en premier : ils fixent le rythme de suivi.

La règle qui évite l'usine à gaz : un score sans preuve vaut zéro, et le barème sera recalibré après 90 jours.

(Ne jamais citer la part du CA réalisée sur les comptes A.)""",

'b3': """Si on me demande comment je me bats contre UPS ou DHL : on ne dénigre jamais. On reconnaît ce que le concurrent fait bien, on recentre sur ce qui fait mal au prospect, la douane, les taxes, la casse, et on pose une question qui l'amène à le constater lui-même.

Et j'assume nos faiblesses avant qu'on me les oppose : 21 jours en groupage, mais le direct existe en cinq jours environ ; un prix unitaire élevé sur les petites quantités, que je ramène au coût par bouteille ; notre taille, compensée par un statut réglementé et une filiale aux États-Unis.

(Sources publiques datées d'octobre 2026. Le premier adversaire reste le statu quo, sans pourcentage.)""",

'b4': """Si on m'objecte qu'en pleine saison aucun vigneron n'accorde trente-cinq minutes : on prospecte avant les pics, pas pendant. Et au premier appel, on ne déroule pas le tunnel. Chez un vigneron, l'appel dure moins de trois minutes et vise trente minutes de démonstration sur ses vins ; pour un compte structuré, on demande la permission de poser deux questions en quarante-cinq secondes, puis on propose vingt-cinq minutes de cartographie du flux.

Et si vous voulez le second tunnel, celui de la maison de champagne : en situation, je demande ses marchés, ses modes et ses incoterms hors Union européenne ; en problème, où elle perd du temps, certificat CIVC, douane américaine, suivi ; en implication, ce que coûte à son image un colis immobilisé en douane ; et en need-payoff, ce que changerait un plan de flux où le certificat et les taxes sont gérés à chaque envoi.

La banque de questions décline le tunnel par profil : huit lignes, du vigneron à la distillerie.""",

'b5': """Si on me demande ce que l'IA a fait : j'ai utilisé Claude, d'Anthropic, et je l'ai crédité dès l'avant-propos. L'annexe W détaille huit chantiers de forme, avec un prompt représentatif pour chacun.

Je le complète honnêtement : des passes de mise en cohérence ont aussi été faites avec l'IA, chiffres corrigés d'après les sources, règles harmonisées, bibliographie, renvois, chaque correction vérifiée à sa source. Et ce support oral, ses titres, ses visuels et la formulation de mes notes, a été travaillé avec Claude à partir de mon dossier, puis relu.

Le fond vient de sources que je peux citer : la documentation officielle 2026, nos tableaux de bord du 24 septembre, nos trois enquêtes, et vingt-quatre références externes, vérifiées en ligne. Aucune image n'a été générée par IA : les schémas sont codés à partir des données. Et je retourne la question avec le sourire : quel chiffre ou quelle procédure voulez-vous que je vous explique ?""",

'b6': """Si on me demande d'où viennent les cibles : ce sont des objectifs de pilotage, étiquetés comme tels, parce que notre CRM n'historise que depuis 2025. Chaque indicateur a une fréquence, une cible et une action si l'écart se creuse. Là où je n'ai pas de base, j'écris « baseline 90 jours » plutôt que d'inventer un chiffre.

(4,87/5 est une probabilité de recommandation sur 23 réponses, pas un NPS. Les 227 adhérents récents ne sont pas le KPI « actifs ». La marge contributive se suit par dossier, sans valeur affichée.)""",

'b7': """Si on me dit que c'est trop cher : je ramène le prix à ce que paie vraiment le client final. Pour les vingt-quatre bouteilles du cas, le total dépend de la valeur déclarée : le simulateur fait foi. Le playbook détaille un exemple complet : douze bouteilles et 300 euros de vin : 210 euros de transport, une trentaine d'euros de taxes estimées dans l'exemple du playbook, 17 euros de dossier, et, s'il la choisit, l'assurance en option, 3 % du vin et du transport, soit une quinzaine d'euros. Environ 270 euros avec l'option, tout réglé d'avance. Les taxes restent une estimation, révisable selon nos conditions générales. Le transport seul revient à environ 17,50 euros par bouteille ; sur vingt-quatre bouteilles, il tombe à quinze euros.

(Le simulateur fait foi : refaire la simulation la veille ; les taxes dépendent de la valeur déclarée et du taux du jour. Droits US : ne jamais citer un taux, dire « le taux du jour est dans le simulateur » ; sources externes contradictoires depuis juillet 2026. Pas de remise sans contrepartie ni validation de la direction.)""",

'b8': """Si on me demande la stratégie : le SWOT fait ressortir un trio de forces, le statut, la filiale, la plateforme, et une dépendance aux États-Unis. Les priorités en découlent : capitaliser sur le trio, diversifier sans sacrifier le produit phare, vendre la conformité comme un service, prospecter les paniers élevés. À court terme, consolider et activer ; à moyen terme, diversifier destinations et segments ; à long terme, devenir la référence, les projets restant au conditionnel.

(Concentration du CA : jamais de chiffre.)""",

'b9': """L'organigramme complet : direction, commerce et développement, filiale de New York, logistique et administration. Treize personnes nommées, filiale comprise. Un commercial parle directement à la direction, à l'exploitation et à l'administration : c'est pourquoi le playbook propose une matrice de décision, à ratifier.""",

'b10': """Aux États-Unis, la carte 2026 dit où l'on livre en groupage, en direct, ou pas du tout. En groupage, 36 bouteilles au maximum par personne et par envoi ; au-delà de 2 100 dollars, une procuration du destinataire est obligatoire, et on ne cherche jamais à l'éviter.

(POA = power of attorney. La carte officielle fait foi : ne pas citer de liste d'États de mémoire.)""",

'b11': """Si on me demande qui paie quand ça casse : l'assurance est une option, 3 % de la valeur du vin et du transport, jusqu'à 20 000 euros par envoi, choisie sur près de neuf envois sur dix. Le client signale sous 48 heures, avec photos, et choisit entre réexpédition et remboursement. En réexpédition, le domaine nous facture seulement les bouteilles : l'incident devient une seconde vente. Sans l'option, on reste aux conditions de base, pas au régime ad valorem. Et je dis franchement les exclusions : la chaleur, l'oxydation, les bouchons, les étiquettes.

(Si on m'oppose l'annexe F, qui dit les frais administratifs « incluant » l'assurance : la couverture est décrite dans la grille, mais facturée en option à 3 %, proposée à chaque commande, et choisie sur 89,8 % des envois. Formulation à faire valider par Floriane.)""",

'b12': """La cadence complète : huit touches en dix-huit jours, pour une vingtaine de comptes prioritaires en approche individualisée ; la cadence s'ouvre dès 55 points de PA-FIT, et les caveaux ont une cadence plus courte et plus terrain. La règle d'or : toute réponse arrête l'automatisation et crée une tâche humaine. Le câblage Brevo-HubSpot est prévu en novembre ; d'ici là, les mêmes étapes avec des tâches manuelles.

(Huit touches = six contacts actifs : trois e-mails, deux appels, une invitation LinkedIn.)""",

'b13': """La feuille de route détaillée : chaque chantier a une échéance, un responsable, un temps, un budget et un critère de passage. Trois mille euros de dépenses externes au total ; le temps interne n'est pas chiffré en euros, c'est une capacité à réserver.

(Dire l'état réel des chantiers de septembre et d'octobre : fait, en cours ou décalé.)""",

'b14': """Si on me demande les cinq objections à connaître par cœur : le prix, la casse, la chaleur, le statu quo et le temps. Pour chacune, une seule preuve, jamais trois. Le prix se ramène au coût par bouteille et à celui qui paie. La casse, à l'assurance en option, en disant ses limites. La chaleur, au départ différé, en reconnaissant qu'elle n'est pas couverte. Contre le statu quo, je ne demande pas de changer, seulement de comparer sur un envoi. Et le temps, c'est trois minutes de saisie.

(Ce classement vient du terrain ; il sera hiérarchisé sur les motifs de perte du CRM en novembre. Ne jamais dire « tout est assuré ».)""",

'b15': """Si on me demande ce qui vient vraiment de moi : voici ce qui existait, ce que j'ai apporté, et pourquoi. Les outils, les conditions générales, les procédures et la filiale existaient avant le playbook ; à Planet'Connect, j'ai contribué avec Halt Solutions. Mon apport, c'est la méthode qui les relie : une source unique des chiffres, le ciblage, les personas, le processus, l'argumentaire, le parcours d'intégration. Chaque ligne porte son statut : livré, objectif ou proposé à ratifier.

(Ne pas s'attribuer les ~145 signatures, ni Planet'Connect seule : « au développement de laquelle j'ai contribué ».)""",

'b16': """Si on me demande si ce cas est réel : c'est un parcours type, tiré du chapitre 11 du playbook. Les prix viennent de la grille 2026, les étapes des règles du playbook ; les réponses du prospect et les points du score sont illustratifs. Je n'ai pas voulu présenter une vente réelle : aucun domaine n'est nommé, aucun chiffre client n'est cité, parce que notre top 10 reste confidentiel.

Le chapitre 11 dit « en chiffres réels » : ce sont les prix de la grille qui sont réels. Il chiffre douze bouteilles ; j'ai gardé un seul panier, vingt-quatre bouteilles, celui du chapitre 4 et de la fiche du domaine avec caveau.

(Ne jamais dire qu'un compte réel du top 10 suit cette trajectoire : la phrase du chap. 11 n'est pas documentée, à retirer à la prochaine révision.)""",

}
