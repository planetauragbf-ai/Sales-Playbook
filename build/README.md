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
