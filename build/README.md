# Build du document Word

Génère `Planet_Aura_Sales_Playbook_2026.docx` (charte Planet Aura : teal/navy/orange, logo, icônes, photos, encadrés sémantiques) à partir des 18 chapitres markdown du dépôt.

```bash
cd build
npm install docx
node build-docx.js        # produit le .docx dans build/
# PDF : soffice --headless --convert-to pdf Planet_Aura_Sales_Playbook_2026.docx
```

- `image-placements.js` : où insérer chaque photo/carte (regex sur les titres de sections).
- `assets/pics` : logo et visuels extraits des playbooks maquettés internes ; `assets/icons` : icônes de chapitres.
- Encadrés : `> **REPÈRE —**`, `> 💡 **LE CONSEIL DE FLORIANE —**`, `> ⚠️ **POINT DE VIGILANCE —**`, `> 🚫 **INTERDIT —**`, `> ✅ **CE QUI FONCTIONNE —**`, `> 📌 **À RETENIR —**`.

## Sommaire interactif (2 passes)

Le sommaire (liens cliquables + numéros de page exacts) se génère en 2 passes :
1. `node build-docx.js` (le sommaire affiche 0) → convertir en PDF → exécuter le script de mappage (voir `toc-pages.json` : {clé de signet: page}) qui associe chaque titre à sa page réelle en ignorant les pages du sommaire.
2. `node build-docx.js` à nouveau : les numéros exacts sont injectés. La pagination est stable entre les 2 passes (seuls les chiffres changent).
