# 15 — KPIs & PILOTAGE COMMERCIAL

*Ce qu'on mesure, comment on le pilote, et les rituels qui font progresser.*

---

## 15.1 Les indicateurs North Star

| Niveau | Indicateur | Définition | Cible indicative |
|---|---|---|---|
| Entreprise | **Envois expédiés / mois** | Volume total réseau | Croissance YoY |
| Entreprise | **CA services** (transport + DDP + assurance + options + stockage) | Facturation PA | Croissance YoY |
| Commercial | **Adhérents ACTIFS** (≥ 1 envoi sur 90 j glissants) | La vraie mesure — pas les signatures | > 60 % du parc signé |
| Commercial | **Nouveaux adhérents activés** (1er envoi < 30 j) | Signature → activation | ≥ 70 % des signés |

## 15.2 Le funnel et ses taux (à suivre hebdo)

```
Leads → Qualifiés → RDV tenus → Propositions → Signatures → Activés → Récurrents
```

| Conversion | Cible | Alerte si |
|---|---|---|
| Lead → Qualifié | 40-60 % | < 30 % (mauvais sourcing) |
| Qualifié → RDV tenu | 50-70 % | No-shows > 20 % |
| RDV → Proposition | 70 %+ | Sinon : problème de découverte |
| Proposition → Signature | 40-60 % (mix sources) | < 30 % : revoir closing/objections |
| Signature → Activé < 30 j | ≥ 70 % | < 50 % : onboarding défaillant |
| Activé → Récurrent (≥ 3 envois/trim.) | ≥ 60 % | — |

**SLA non négociables** : lead inbound rappelé **< 24 h** ; contact salon traité < 48 h (email) et < 7 j (téléphone) ; proposition envoyée < 24 h après RDV.

## 15.3 Indicateurs d'activité (inputs) par commercial

| Activité | Cible hebdo (hors saison) | Cible saison |
|---|---|---|
| Appels de prospection aboutis | 25 | 10 |
| Emails personnalisés | 25 | 10 |
| RDV démo (visio/terrain) | 4-6 | 2-3 |
| Visites adhérents (tiers A/B) | 2 | 4-5 |
| Formations caveau | — | 2-3 (mai-juin) |
| Recommandations demandées | 3 | 5 |

## 15.4 Indicateurs de qualité de portefeuille

- **Mix par tiers** : ≥ 50 % du CA sur tiers A ; pas plus de 20 % du CA sur un seul adhérent.
- **Mix destinations** : suivre la part USA (sensibilité douanière) vs UE/UK/CH (récurrence simple) — un portefeuille 100 % USA est fragile, un portefeuille sans USA sous-exploite le panier.
- **Health score** (chap. 12.5) : < 15 % de comptes rouges.
- **Churn annuel** (non-renouvellement documentation) : < 15 % en nombre, < 8 % en valeur.
- **NPS adhérents** (enquête annuelle au renouvellement) : > 50.

## 15.5 Les formules exactes : 10 KPI, leur fréquence et leur piège

Un KPI sans formule partagée finit toujours en débat d'interprétation. Chaque indicateur ci-dessous a une formule unique, une fréquence de lecture et le piège classique qui fausse la mesure.

| KPI | Formule | Fréquence | Piège à éviter |
|---|---|---|---|
| Taux de contact | Comptes avec interaction / comptes contactés | Hebdo | Compter les ouvertures d'email comme des réponses |
| Taux de RDV | RDV tenus / comptes contactés | Hebdo | Mélanger RDV réservés et RDV tenus |
| MQL → SQL | SQL acceptés / MQL transmis | Mensuel | Changer la définition selon la source |
| Win rate | Opportunités gagnées / opportunités clôturées | Mensuel | Inclure des dossiers encore ouverts |
| Cycle médian | Médiane (date de closing − date de qualification) | Mensuel | Utiliser la moyenne seule |
| Panier moyen | CA signé / clients gagnés | Mensuel | Confondre signé et facturé |
| Marge contributive | CA − coûts variables directs | Par dossier | Appliquer un coefficient comme si c'était une marge nette |
| OTIF | Livraisons complètes à l'heure / livraisons | Mensuel | Définition de « l'heure » non convenue avec le client |
| Quote SLA | Devis émis dans le SLA / devis complets | Hebdo | Démarrer le chrono avant que le dossier soit complet |
| Hygiène forecast | Opportunités complètes / opportunités ouvertes | Hebdo | Conserver des opportunités zombies |

> ⚠️ **POINT DE VIGILANCE —** Un coût multiplié par 1,30 n'est pas une « marge nette ». La marge contributive se calcule dossier par dossier : CA moins coûts variables directs. C'est elle qui pilote les décisions de prix, de mix ou de disqualification.

> **REPÈRE — BASELINE D'ABORD.** Pendant les 90 premiers jours, on mesure sans maquiller. On fixe ensuite les cibles par segment et par offre, à partir des médianes réellement observées. Toute cible communiquée à l'extérieur doit préciser sa période, son périmètre, sa source et son propriétaire.

## 15.6 Prévision (forecast) simple et honnête

Méthode par engagement, pas par intuition :

| Stade | Pondération |
|---|---|
| Proposition envoyée | 20 % |
| Accord verbal / documentation en signature | 60 % |
| Signé non activé | 80 % (valeur année 1 prudente) |
| Activé | Run-rate réel |

**Valeur d'un adhérent (année 1)** : nb d'envois estimés × prestation moyenne (~150-250 € selon mix destinations) + options (CIVC, stockage). Réviser après 90 jours d'historique réel.

### Le test d'arithmétique : auto-contrôle des ordres de grandeur

Avant de présenter un objectif ou un plan chiffré, on vérifie que les chiffres tiennent ensemble. Exemples de contrôles :

| Contrôle | Calcul juste | Erreur classique |
|---|---|---|
| Cartons par palettes | 20 palettes × 20 cartons = 400 cartons | Écrire 600 cartons ou 30 palettes |
| Tonnage | 400 cartons × 18 kg = 7,2 t | Annoncer 20 palettes ET 8 t (incohérent) |
| Chiffre d'affaires | 400 cartons × 238 € = 95 200 € | Annoncer 20 palettes ET 100 k€ (incohérent) |
| Seuil de capacité | 8 t à 18 kg/carton = 445 cartons ≈ 22,25 palettes | Garder le triptyque volume/prix/capacité sans le rebaseliner |

> ⚠️ **POINT DE VIGILANCE —** Si un des trois chiffres (volume, prix, capacité) bouge, on rebaseline les deux autres. Un plan dont l'arithmétique ne tombe pas juste perd toute crédibilité en revue de direction — et en face du client.

## 15.7 Rituels d'équipe

### Pas de rituel sans sortie obligatoire

Un rituel qui ne produit rien est une réunion. Chaque rituel de la cadence a une sortie obligatoire — si elle n'est pas produite, le rituel n'a pas eu lieu.

| Rituel | Cadence / durée | Participants | Sortie obligatoire |
|---|---|---|---|
| Signaux chauds | Chaque jour / 10 min | Commercial | Réponse ou tâche datée |
| Pipeline (deals en mouvement, blocages) | Hebdomadaire / 45 min | Direction + commerce | Forecast, blocages, prochaine action datée |
| Commerce-opérations | Hebdomadaire / 30 min | Commerce + ADV/logistique | Faisabilités, risques et SLA |
| Performance (funnel & KPIs) | Mensuel / 60 min | Marketing + ventes + direction | Funnel, marge, sources et tests |
| Revue de comptes (tiers A + rouges) | Mensuel | Commerce + direction | Health scores, plans d'action |
| Voix du client | Mensuel / 30 min | ADV + commerce | Incidents, CSAT, objections et preuves |
| Playbook (retro : wins/pertes, veille concurrence) | Trimestriel / 90 min | Propriétaires de chapitres | Version, décisions et archive |
| Préparation saison / renouvellement | Févr. & mai | Commerce + direction | Campagnes, formations saisonniers, objectifs |

### Ordre du jour de la revue mensuelle de performance (60 minutes)

| Minutes | Contenu |
|---|---|
| 0-10 | Qualité de la donnée et écarts de définition |
| 10-25 | Funnel par source, ICP et séquence |
| 25-40 | Pipeline, win/loss, cycle et marge |
| 40-50 | OTIF, incidents, CSAT et expansion |
| 50-60 | Un test à arrêter, un test à amplifier, un propriétaire et une date |

> 💡 **BONNE PRATIQUE —** La revue mensuelle commence par la qualité de la donnée, pas par les résultats. Si les définitions divergent ou si le CRM est sale, les 50 minutes suivantes ne valent rien. Et elle se termine toujours par une décision : un test qu'on arrête, un test qu'on amplifie, un propriétaire, une date.

## 15.8 Qui décide quoi : la matrice RACI

Cinq décisions reviennent sans cesse et créent des frictions si personne ne sait qui tranche. La matrice ci-dessous fixe les rôles : **R** réalise, **A** décide (accountable), **C** est consulté, **I** est informé.

| Décision | R | A | C | I |
|---|---|---|---|---|
| Ciblage / séquence | Marketing/BD | Direction commerciale | Commercial | ADV |
| Faisabilité / délai | ADV/logistique | Responsable opérations | Commercial | Client |
| Prix / remise | Commercial | Direction | Finance/logistique | ADV |
| Allégation / cas client | Marketing | Direction | RSE/juridique/partenaire | Commerce |
| Passage aux opérations | Commercial + ADV | Responsable opérations | Logistique | Direction |

> 🚫 **INTERDIT —** Accorder une remise ou publier une allégation client (chiffre, nom, promesse carbone) sans le A de la ligne concernée. Un commercial réalise la proposition de prix, la direction la décide.

## 15.9 Hygiène CRM (règles d'or)

1. Tout contact loggé **sous 24 h** (appel, email, visite, salon).
2. Toute opportunité a **une prochaine action datée** — sinon elle est fermée (perdue/nurturing).
3. Champs obligatoires en fermeture : **raison réelle** (prix, délai, statu quo, concurrent [lequel], inertie) — c'est la matière des retros.
4. Les fiches adhérents portent : tiers, health score, contacts caveau À JOUR (les saisonniers changent !), destinations récurrentes, particularités (CIVC, POA fréquents, e-shop connecté).
5. Les leads inbound (formulaire site) sont **routés le jour même** avec horodatage du premier rappel.

## 15.10 Tableau de bord mensuel type (une page)

- Envois du mois (vs N-1) & CA services — par région, par destination.
- Nouveaux signés / nouveaux activés / taux d'activation 30 j.
- Parc actif 90 j (vs parc signé) + comptes passés rouge.
- Pipeline pondéré 90 jours vs objectif.
- Top 3 wins (avec raison) / top 3 pertes (avec raison).
- Incidents notables du mois (sinistres majeurs, retards groupage) — pour aligner le discours commercial du mois suivant.

## 15.11 Feuille de route commerciale budgétée (sept. 2026 → 2027)

Le pilotage se traduit en plan d'action daté, budgété et conditionné : chaque chantier a un responsable, un temps alloué, un budget et un critère de passage à l'étape suivante. Pas de critère atteint, pas d'étape suivante.

| Période | Chantier | Responsable | Temps | Budget | Critère de passage |
|---|---|---|---|---|---|
| S1-S2 (sept. 2026) | Nettoyage CRM, listes A/B/C, champs obligatoires | Emma + Adam | 24 h | 0 € | ≥ 95 % des comptes prioritaires exploitables |
| M1 (oct.) | Landing page, one-pager par ICP, FAQ preuves/risques | — | 36 h | 600 € | — |
| M2 (nov.) | 3 séquences Brevo, listes repoussoir, reporting HubSpot | — | 20 h | 200 € | — |
| M2-M8 | Tests LinkedIn sur 3 clusters (100 € puis montée progressive) | — | 3 h/sem | 900 € | Coût par SQL comparé à l'outbound |
| M3 (janv. 2027) | Webinaire export : coût rendu, conformité, preuve responsable | Emma + expert | 20 h | 300 € | 10 inscrits ICP et 3 diagnostics |
| M4-M10 | Deux salons en visiteur, RDV prébookés, suivi sous 48 h | Adam + Emma | 24 h | 1 000 € | 8 RDV qualifiés par événement |
| Après validation | Pilote VELA : dossier pilote, calcul rendu, FAQ carbone, plan de secteurs | — | — | — | Validations préalables obtenues |

> **REPÈRE —** Plafond total : **3 000 € de dépenses externes maximum**. Le temps interne est une capacité à réserver, pas un coût salarial. Sont exclus du plafond : voyages, stands, impressions et développements logiciels.

### Les trois horizons

| Horizon | Priorité |
|---|---|
| 0-90 jours | Assainir la donnée, prouver le message, réactiver les comptes à bon fit |
| 3-12 mois | Industrialiser séquences et cas clients ; pilote VELA seulement après validations |
| 12-36 mois | Comptes récurrents, partenaires internationaux, automatisation rentable |

## 15.12 La stack Sales Ops (vue d'ensemble)

| Domaine | Outil / dispositif | Usage & propriétaire |
|---|---|---|
| CRM | **HubSpot** | Système de vérité (comptes, deals, consentements) — dictionnaire de données et score d'hygiène au chap. 7.15 |
| Marketing automation | **Brevo** | Séquences et campagnes (3 séquences socle en roadmap M1-M2) ; scénarios de nurturing à enrichir |
| Plateforme métier | **Planet'Connect** (+ API) | Commandes, suivi, factures, e-signature, mails automatiques (~30 modèles) — modifications via Emma |
| Collaboration | **Google Workspace** (Drive, Docs/Sheets, Gmail, Meet) + WhatsApp Business | Drive = source unique des documents officiels (dossiers adhérents 2026) ; visio et messagerie |
| Reporting / BI | Dashboards HubSpot + tableau de bord mensuel une page (15.10) | Revue mensuelle de performance ; reporting HubSpot renforcé en roadmap M2 |
| Cycle de contrat (CLM) | Signature électronique Planet'Connect + archivage Drive | Documentation annuelle re-signée chaque année (mars-avril) ; avenants et résiliations : traités par la direction, à formaliser |
| Onboarding & formation | Plan 30-60-90 (chap. 12.8) + rituel playbook trimestriel | Le playbook EST le support de formation ; matrice de compétences à construire (proposition en ouverture, 17.14) |

> ⚠️ **POINT DE VIGILANCE —** Les éléments notés « à confirmer / à construire » (licences Sales Navigator, dashboards avancés, matrice de compétences, process avenants) sont des chantiers Sales Ops, pas des acquis : ne pas les présenter comme existants.

> 📌 **À RETENIR —** Un KPI n'est utile que s'il a une formule partagée, une fréquence de lecture et une décision associée. On mesure d'abord 90 jours sans maquiller (baseline), puis on fixe les cibles par segment. Chaque rituel produit une sortie obligatoire, chaque décision a un responsable (RACI), et chaque chiffre présenté passe le test d'arithmétique. La feuille de route apprend vite avec 3 000 € maximum : pas de critère de passage atteint, pas d'étape suivante.
