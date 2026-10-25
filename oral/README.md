# Soutenance orale - Sales Playbook Planet Aura

Sources du support de soutenance (artefact Slides : 20 diapos + 16 diapos de secours, oral de 20 min, script calé sur 18 min 30) et du guide de soutenance. Version 4 (finale) du 25/10/2026, construite autour d'un cas fil rouge : un domaine provençal avec caveau, suivi de la qualification au suivi dans le CRM. C'est un parcours type (chap. 11 du playbook) : prix de la grille 2026, règles du playbook, situations illustratives ; ce n'est pas une vente réalisée.

Trois repères sur les diapos :
- la contribution, en pastilles arrondies : EXISTANT, MON ANALYSE, MA CONTRIBUTION, À DÉPLOYER, À MESURER ;
- le statut des chiffres, en tampons : CONSTATÉ, OBJECTIF, HYPOTHÈSE, SIMULATION, POINT ZÉRO, PROJET, GRILLE 2026, ILLUSTRATIF, RÈGLE ;
- l'argument de chaque décision, en bandeau : Constat → Ma décision → Ce que l'on mesure.

Contenu du dossier :
- `deck/project/` : `deck.json` (ordre, sections) et une page HTML par diapo ; les notes orales minutées sont dans `<aside>`.
- `gen/build.py` : régénère `deck/project/` et affiche le minutage (130 mots/min, 2 s par transition ; le texte entre parenthèses n'est pas compté). À relancer après toute modification. `gen/sync_plan.py` réécrit le plan minuté de `plan-oral.md`.
  - `gen/kit.py` : palette (contrastes vérifiés pour la projection), typographie (espaces insécables), composants : en-têtes à étiquettes, tampons de statut, bandeau du cas, cadre des captures et documents réels.
  - `gen/s_intro.py` (diapos 1 à 7), `gen/s_vendre.py` (8 à 15), `gen/s_piloter.py` (16 à 20) ; `gen/backups.py` : diapos de secours B1 à B16.
  - `gen/notes_main.py` : script oral des 20 diapos principales ; `gen/notes.py` : notes des diapos de secours.
- `gen/guide.py` + `gen/autoeval.py` + `gen/guide.css` + `gen/pdf.js` : guide de soutenance (HTML puis PDF A4) : essentiel, cas fil rouge et dix gestes du commercial, grille de conformité, script minuté avec ce qu'il faut montrer, transitions et passages à tester, chiffres et définitions, questions du jury, limites, bilan avant / après, autoévaluation et évaluation critique (fond, design), check-lists. Il lit `deck/` et les rendus PNG (`rendu/`, variable `RENDU_DIR`).
- `render.js` : banc de rendu local (Chromium) qui signale les débordements (bas du flux, marge droite, mots trop longs) ; les images sources se placent dans `img/` (non versionné, correspondance dans `assets-map.md`).
- `plan-oral.md`, `faits.md`, `jury.md` : consignes et plan minuté, fiches de faits vérifiés, banque de questions du jury (20 probables, 5 pièges, 6 difficiles sur la méthode et sa preuve, 10 sur le cas) et autoévaluation.

Usage interne Planet Aura et évaluateurs Euridis : aucun nom ni chiffre d'affaires de client, aucune donnée personnelle de client final, aucun identifiant.
