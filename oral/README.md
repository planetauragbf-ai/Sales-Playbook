# Soutenance orale - Sales Playbook Planet Aura

Sources du support de soutenance (artefact Slides, 19 diapos + 7 diapos de secours) et du guide de soutenance.

- `deck/project/` : `deck.json` (ordre, sections) et une page HTML par diapo ; les notes orales minutées sont dans `<aside>`.
- `gen/backups.py` : diapos de secours B1-B7.
- `gen/notes.py`, `gen/notes2.py` : script oral ; `gen/fix2.py` : corrections après vérification des faits.
- `gen/finish.py` : espaces insécables et minutage cumulé (140 mots/min, 2 s par transition). À relancer après toute modification.
- `gen/guide.py` + `gen/guide.css` + `gen/pdf.js` : guide de soutenance (HTML puis PDF A4).
- `render.js` : banc de rendu local (Chromium) qui signale les débordements.
- `plan-oral.md`, `faits.md`, `jury.md` : consignes, fiches de faits vérifiés par diapo, banque de questions du jury.

Usage interne Planet Aura : aucun nom de client, aucune donnée personnelle de client final.
