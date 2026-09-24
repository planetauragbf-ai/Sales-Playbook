// Placements d'images par chapitre : { 'fichier.md': [{after: regex ligne de titre, img, w(px), caption}] }
// Photos : uniquement de VRAIES photos (issues des supports Planet Aura) — aucun visuel généré par IA.
module.exports = {
  '00-resume-executif.md': [
    { after: '^Qui sommes-nous', img: 'pics/hq.png', w: 430, caption: 'Le site Planet Aura à Castres (Tarn)' },
  ],
  '01-entreprise.md': [
    { after: 'La filiale américaine', img: 'pics/ny_site.png', w: 360, caption: 'Le site de Planet Aura Inc. — 95 Inip Dr, Inwood (New York)' },
    { after: '^1\\.5 Vos interlocuteurs', img: 'pics/team.png', w: 460, caption: 'L’équipe Planet Aura' },
  ],
  '02-marche.md': [
    { after: '^2\\.10 Destinations demandées', img: 'pics/worldmap.png', w: 440, caption: 'Les destinations desservies par Planet Aura' },
  ],
  '03-offres-services.md': [
    { after: '^3\\.4 USA Groupage', img: 'pics/usmap1.png', w: 470, caption: 'Couverture des États-Unis — groupage vin (ouvert / codes postaux limités / fermé)' },
    { after: 'Le simulateur, l’outil de vente|^3\\.13 Planet\'Connect', img: 'pics/simulator.png', w: 470, caption: 'Le simulateur d’expédition Planet’Connect' },
  ],
  '04-tarifs.md': [
    { after: '^4\\.5 USA — Direct', img: 'pics/usmap2.png', w: 470, caption: 'États desservis en direct' },
  ],
  '12-onboarding-retention.md': [
    { after: '^12\\.1 Le parcours', img: 'pics/photo_cover.png', w: 260, caption: 'Chaque colis remis au transporteur engage la promesse Planet Aura' },
  ],
  '14-conformite-reglementation.md': [
    { after: '^Lire les cartes de zones USA', img: 'pics/usmap3.png', w: 470, caption: 'Carte de référence des statuts par État (vin) — vérifier État ET code postal' },
    { after: 'Norvège', img: 'pics/norway.png', w: 380, caption: 'Norvège — les deux zones tarifaires' },
  ],
};
// Annexes documentaires (chapitre 17)
module.exports['17-annexes-documentaires.md'] = [
  { after: '^17\\.6 Annexe A10', img: 'pics/sim_devis.png', w: 470, caption: 'Simulateur Planet’Connect — devis DDP (taxes prépayées)' },
  { after: '^17\\.7 Annexe A13', img: 'pics/mails_auto2.png', w: 380, caption: 'Aperçu de la bibliothèque de mails automatiques Planet’Connect' },
  { after: '^17\\.8 Annexe A14', img: 'pics/flyer1.png', w: 440, caption: 'Flyer de prospection — face extérieure' },
];

// Documents officiels intégraux (chapitre 17.9-17.12)
const annexPages = [];
for (let i = 1; i <= 5; i++) annexPages.push({ after: '^17\\.9 Annexe A2', img: `annexes/grille_ship-${i}.png`, w: 470, caption: i === 5 ? 'Grille tarifaire shipping 2026 — document officiel (5 pages)' : '' });
for (let i = 1; i <= 3; i++) annexPages.push({ after: '^17\\.10 Annexe A4', img: `annexes/grille_stock-${i}.png`, w: 470, caption: i === 3 ? 'Grille tarifaire stockage & picking 2026 — document officiel (3 pages)' : '' });
annexPages.push({ after: '^17\\.11 Annexe A6', img: 'annexes/orderform-1.png', w: 470, caption: 'Order Form 2026 — formulaire officiel vierge' });
for (let i = 1; i <= 2; i++) annexPages.push({ after: '^17\\.12 Annexe A7', img: `annexes/sepa-${i}.png`, w: 470, caption: i === 2 ? 'Formulaire de mandat SEPA — document officiel (2 pages)' : '' });
module.exports['17-annexes-documentaires.md'].push(...annexPages);
// A9 / A8 (17.13-17.14)
module.exports['17-annexes-documentaires.md'].push(
  { after: '^17\\.13 Annexe A9', img: 'annexes/pconnect_cover-01.png', w: 300, caption: '' },
  { after: '^17\\.13 Annexe A9', img: 'annexes/pconnect_sommaire-02.png', w: 430, caption: 'Mode d’emploi Planet’Connect — couverture et sommaire (37 pages)' },
  { after: '^17\\.14 Annexe A8', img: 'annexes/shipform-1.png', w: 340, caption: 'Formulaire de shipping par email — onglet FORMULAIRE (modèle officiel 2026)' }
);
// Captures réelles Planet'Connect (mode d'emploi officiel)
module.exports['12-onboarding-retention.md'].push(
  { after: '^12\\.9 Prise en main', img: 'pics/pc_login.png', w: 430, caption: 'L’écran de connexion Planet’Connect (app.planet-aura.com)' }
);
module.exports['03-offres-services.md'].push(
  { after: 'Créer un shipping : les 6 champs', img: 'pics/pc_edition.png', w: 470, caption: 'Édition d’un shipping dans Planet’Connect (capture réelle)' },
  { after: 'Les statuts de suivi', img: 'pics/pc_shippings.png', w: 470, caption: 'La liste « Vos shippings » et leurs statuts (capture réelle)' }
);
module.exports['04-tarifs.md'].push(
  { after: '^4\\.11 Exemples de paniers', img: 'pics/pc_sim_usa.png', w: 440, caption: 'Simulation réelle États-Unis dans Planet’Connect : transport, assurance, taxes DDP' }
);
module.exports['07-processus-vente.md'] = module.exports['07-processus-vente.md'] || [];
module.exports['07-processus-vente.md'].push(
  { after: 'handoff commercial', img: 'pics/pc_enlevements.png', w: 440, caption: 'Les lieux d’enlèvement de l’adhérent, gérés dans Planet’Connect' }
);

// Captures réelles des dashboards admin Planet'Connect (extraction 24/09/2026)
module.exports['01-entreprise.md'].push(
  { after: 'La trajectoire du chiffre d’affaires|La trajectoire du chiffre d.affaires', img: 'pics/dash_histo_ca.png', w: 470, caption: 'Historique du CA mensuel 2021-2026 - dashboard gestion Planet’Connect (24/09/2026)' }
);
module.exports['02-marche.md'].push(
  { after: '^2\\.8 Saisonnalit', img: 'pics/dash_ship_evo.png', w: 470, caption: 'Nombre de shippings par mois (sept. 2025 - sept. 2026) - dashboard logistique Planet’Connect' },
  { after: '^2\\.10 Destinations demand', img: 'pics/dash_pays.png', w: 360, caption: 'Répartition réelle des shippings par pays sur 12 mois : États-Unis 64,5 %, France 18,6 % (dashboard logistique)' }
);
module.exports['03-offres-services.md'].push(
  { after: '^3\\.4 USA Groupage', img: 'pics/dash_usa_etats.png', w: 360, caption: 'Groupage USA - poids réel des États sur 12 mois : Californie, Texas, New York, Floride en tête (dashboard logistique)' }
);
module.exports['05-cibles-personas.md'] = module.exports['05-cibles-personas.md'] || [];
module.exports['05-cibles-personas.md'].push(
  { after: '^5\\.7 Gérer le portefeuille', img: 'pics/dash_prospects.png', w: 470, caption: 'La photographie du portefeuille au 24/09/2026 : 448 prospects, 227 adhérents récents, 35 dormants' },
  { after: '^5\\.7 Gérer le portefeuille', img: 'pics/dash_repartitions.png', w: 470, caption: 'Répartition du portefeuille par région et par catégorie (dashboard commercial Planet’Connect)' }
);
module.exports['13-sav-sinistres.md'] = [
  { after: '^13\\.3 Le circuit officiel', img: 'pics/dash_sinistres.png', w: 470, caption: 'La file des sinistres en cours, suivie en temps réel dans le dashboard logistique Planet’Connect (24/09/2026)' },
  { after: '^13\\.12 Le SAV comme argument', img: 'pics/dash_assurance.png', w: 330, caption: '89,8 % des expéditions des 12 derniers mois sont parties avec l’assurance ad valorem souscrite' }
];
module.exports['15-kpis-pilotage.md'] = module.exports['15-kpis-pilotage.md'] || [];
module.exports['15-kpis-pilotage.md'].push(
  { after: '^15\\.2 Le funnel', img: 'pics/dash_nouveaux.png', w: 470, caption: 'Nouveaux adhérents par mois et cumul sur 12 mois (~145 nouveaux) - dashboard commercial' },
  { after: '^15\\.10 Tableau de bord mensuel', img: 'pics/dash_gestion.png', w: 470, caption: 'Le tableau de bord gestion réel : CA, CA vins expédiés, shippings, bouteilles - janv.-sept. 2026' },
  { after: '^15\\.10 Tableau de bord mensuel', img: 'pics/dash_ca_graph.png', w: 470, caption: 'CA, shippings et bouteilles par mois 2026 (dashboard gestion Planet’Connect)' }
);
