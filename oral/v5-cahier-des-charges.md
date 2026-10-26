# Refonte v5 : des diapos lisibles en 3 secondes

## Contexte
Soutenance orale Euridis d'Emma Soares Britschgy (chargée de projets et de développement, Planet Aura) : le « Sales Playbook » de Planet Aura (commissionnaire de transport de vin, groupage DDP vers les USA). Deck de 20 diapos principales (oral de 18 à 19 min) et 16 diapos de secours (B1 à B16), au format « Slides » (sous-ensemble CSS fermé). Un cas fil rouge (un domaine provençal avec caveau, parcours TYPE, illustratif) traverse les diapos 8 à 19.

Retour de l'utilisatrice sur la v4 : « certaines slides sont chargées, compliquées à comprendre à l'œil, et des textes se chevauchent ». Mesure : 140 à 220 mots visibles par diapo de contenu ; à texte agrandi de 10 %, 33 diapos sur 36 débordent (aucune marge) ; des chiffres en grand touchent leur légende.

## Objectif
Chaque diapo se comprend en 3 secondes : UN message (le titre), UN point focal visuel (schéma, chiffre, document réel, parcours), peu de mots, gros caractères, de l'air. Le détail passe à l'oral (notes) ou dans une diapo de secours. Zéro chevauchement, et une vraie marge de sécurité.

## Fichiers (S = /tmp/claude-0/-home-user-Sales-Playbook/937d2675-9cdd-54b9-a3ad-2207ab8c8104/scratchpad/oral)
- Code actuel des diapos : `S/gen5/s_intro.py` (cover…diagnostic), `S/gen5/s_vendre.py` (icp…activer), `S/gen5/s_piloter.py` (ressources…conclusion), `S/gen5/backups.py` (b1…b16). Composants communs : `S/gen5/kit.py` (header3, head_case, case_bar, footer, pill, ctag, num, label, why3, decision, shot, arrow, CASE_BOX, couleurs, fr()). NE MODIFIEZ AUCUN de ces fichiers.
- Notes orales actuelles : `S/gen5/notes_main.py` (20 diapos principales), `S/gen5/notes.py` (BACKUP_NOTES).
- Rendu actuel de chaque diapo : `S/audit5/<id>.png` ; rendu à texte +8 % : `S/audit5/<id>_stress.png` ; rapport : `S/audit5/report_normal.txt`, `S/audit5/report_stress.txt`.
- Texte complet du deck v4 (écran + notes) : `S/refonte3/deck_v4_texte.md`.
- Ce que chaque diapo doit prouver devant le jury : `S/gen5/guide.py`, tables GESTES (l. ~169), CASE (~179), GRID (~195, la grille officielle : critère → diapos → preuve), SHOW (~48, ce qu'on montre), NUMS (~283, statut de chaque chiffre).
- Faits sourcés : `S/faits.md` ; dossier écrit : `/home/user/Sales-Playbook/final/content-emma/*.md`.
- Format Slides (CSS autorisé, rendu réel) : `S/typeref/artifact-type/reference/format.md`, `layout.md`, `styles.md`.
- Images disponibles (aucune nouvelle) : `S/assets-map.md` (ids /_blob/…).

## Banc d'essai (obligatoire)
Écrivez votre diapo candidate dans `S/v5cand/<id>.py` : la fonction complète, même nom que l'id (`def icp():` … `return 'icp', inner, dict(gap=…)`), plus d'éventuelles petites aides À PRÉFIXER par `_<id>_` (aucune collision). Elle est exécutée dans l'espace de noms du module d'origine : kit et aides du module sont disponibles.
Si vous modifiez la note orale de la diapo, écrivez la note COMPLÈTE dans `S/v5cand/<id>_notes.txt`.
Testez :
`cd S/gen5 && python3 try_slide.py <id> ../v5cand/<id>.py [--notes ../v5cand/<id>_notes.txt]`
→ rendu normal + rendu « stress » (tous les textes +10 %), mots visibles, delta de mots dits, chemins des PNG. Ouvrez TOUJOURS le PNG normal avec l'outil Read et regardez-le vraiment (lisibilité, équilibre, chevauchements, mots isolés en fin de ligne). Itérez jusqu'à « RÉSULTAT : OK ».

## Règles de forme (non négociables)
1. Lisible en 3 s : le titre dit le message ; un seul point focal occupe l'essentiel du corps ; au plus 3 zones (+ éventuellement le bandeau d'argument en bas).
2. Mots visibles (compte du banc, en-tête, bandeau du cas et pied de page compris) : diapo principale ≤ 95, cible 70 à 90 ; secours ≤ 130. Cover et accroche ne sont pas concernées.
3. Taille : messages clés 28 à 36 px ; secondaire 24 px minimum (jamais moins) ; chiffres clés en grand (num()).
4. Robustesse : RÉSULTAT OK au banc (rendu normal sans aucun signalement ; rendu stress +10 % sans FLUX DÉPASSE, CHEVAUCHEMENT, MARGE, MOT TROP LONG). Aucun texte épinglé (position:absolute) hormis ce que kit fournit (pied de page, pastilles d'en-tête) ; pas de hauteur fixe sur un bloc qui contient du texte ; `white-space:nowrap` seulement sur des étiquettes courtes ; un grand chiffre (num) jamais collé à sa légende (gap ≥ 6 px).
5. Identité homogène : en-tête `header3(...)` (ou `head_case(header3(...), étape)` sur les diapos du cas), `footer(n, partie)` (ou `bfoot(n)` / `bhead(...)` pour les secours) ; palette et composants du kit ; cartes à coins arrondis 14-18 px ; bandeaux sombres NUIT. Titres sur UNE ligne de préférence (≤ 48 caractères environ à 60 px).
6. Format Slides : CSS du sous-ensemble uniquement (pas de margin, pas de z-index, pas de <style>) ; <svg> sans <text> ; pas d'image générée ; seulement les /_blob existants.

## Règles de fond (non négociables)
1. Ne supprimez jamais un critère évalué pour alléger (voir GRID dans guide.py) : ce qui quitte l'écran doit être (a) déjà dit dans la note, ou (b) ajouté à la note (delta de mots dits ≤ +12 pour la diapo ; idéalement 0 ou négatif), ou (c) présent dans une diapo de secours (nommez-la : « secours B13 »).
2. Aucun chiffre, nom, date ou fait nouveau : réutilisez uniquement ce qui figure déjà à l'écran, dans la note, dans les secours, ou dans faits.md / le dossier. Aucune reformulation qui change un sens ou un statut.
3. Statuts toujours visibles à côté des chiffres : CONSTATÉ, OBJECTIF, HYPOTHÈSE, SIMULATION, ILLUSTRATIF, POINT ZÉRO, GRILLE 2026 (pill()).
4. Grille de lecture des contributions (pastilles d'en-tête EXISTANT / MON ANALYSE / MA CONTRIBUTION / À DÉPLOYER / À MESURER) : gardez celles qui sont vraies pour la diapo (1 à 3).
5. Diapos 11, 15, 16, 17, 19 : gardez l'argument « Constat → Ma décision → Ce que l'on mesure » (why3 ou équivalent), mais court (≤ 10 mots par case).
6. Contraintes permanentes : aucune donnée personnelle de client final ; aucun mot de passe ni identifiant ; top 10 jamais nominatif, pas de CA par client, ne pas citer « comptes A = 76 % du CA » ; pas d'image générée par IA ; projets en développement (VELA, Gant Blanc, Planet'Stock, entrepôt agréé, annexe Champagne) au conditionnel ; assurance = OPTION à 3 % ad valorem (vin + transport), jusqu'à 20 000 €/envoi, souscrite sur 89,8 % des envois, JAMAIS « incluse » ; paiement : mandat SEPA par défaut ; droits de douane US : AUCUN taux cité (« taux du jour au simulateur ») ; le cas est un parcours TYPE (jamais une vente réalisée) ; un seul panier pour le cas : 24 bouteilles, 360 € de transport HT + taxes estimées + 17 € de dossier, assurance en option ; les 40 000 € sont des ventes POTENTIELLEMENT perdues (simulation), jamais un gain ; ~145 = adhérents SIGNÉS en 12 mois (pas actifs, pas attribuables au playbook) ; ne pas nommer Planet Provence ; ne pas citer ~325 €/envoi ni 241 € de médiane ; jamais « la valeur résiste » ; jamais « Un compte du top 10 réel suit exactement cette trajectoire » ; jamais « tout compris » ni « garanti ».
7. La note : ce qui se DIT (les parenthèses sont des indications non dites). Gardez les indications « (Montrer …) » cohérentes avec ce qui est à l'écran ; si un élément montré disparaît, changez l'indication.
