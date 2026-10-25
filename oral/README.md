# Soutenance orale - Sales Playbook Planet Aura

Sources du support de soutenance (artefact Slides, 20 diapos + 15 diapos de secours) et du guide de soutenance. Version refondue du 25/10/2026 : une idée forte par diapo, chiffres à statut (constaté, objectif, hypothèse, point zéro, projet), contribution personnelle marquée (MON ANALYSE, MON ÉTUDE, MON OUTIL, MES PROPOSITIONS).

- `deck/project/` : `deck.json` (ordre, sections) et une page HTML par diapo ; les notes orales minutées sont dans `<aside>`.
- `gen/build.py` : régénère `deck/project/` à partir des scripts ci-dessous et affiche le minutage (130 mots/min, 2 s par transition ; le texte entre parenthèses n'est pas compté). À relancer après toute modification.
  - `gen/kit.py` : palette, typographie (espaces insécables), composants (en-têtes, pastilles de statut, bouteilles, flèches).
  - `gen/part1.py`, `gen/part2.py`, `gen/part3.py` : les 20 diapos principales ; `gen/backups.py` : diapos de secours B1-B15.
  - `gen/notes.py` : script oral de chaque diapo et notes des diapos de secours.
- `gen/guide.py` + `gen/guide.css` + `gen/pdf.js` : guide de soutenance (HTML puis PDF A4) ; il lit `deck/` et les rendus PNG (`rendu/`, variable `RENDU_DIR`).
- `render.js` : banc de rendu local (Chromium) qui signale les débordements ; les images sources se placent dans `img/` (non versionné, correspondance dans `assets-map.md`).
- `plan-oral.md`, `faits.md`, `jury.md` : consignes et plan minuté, fiches de faits vérifiés, banque de questions du jury.

Usage interne Planet Aura : aucun nom de client, aucune donnée personnelle de client final.
