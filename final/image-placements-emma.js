// Placements d'images du document final (clé = id d'unité) - photos réelles + schémas codés charte uniquement.
module.exports = {
  '01': [
    { after: '^Saisonnalité : planifier', img: 'pics/dash_ship_evo.png', w: 398, caption: 'Shippings par mois, sept. 2025 - sept. 2026 (dashboard logistique Planet’Connect)' },
    { after: '^Géographies prioritaires', pair: [
      { img: 'pics/carte_vignobles.png', w: 235, caption: 'Les régions viticoles - terrains de prospection prioritaires' },
      { img: 'pics/worldmap2.png', w: 285, caption: 'Les destinations desservies dans le monde' },
    ] },
    { after: '^Destinations demandées', img: 'pics/dash_pays.png', w: 320, caption: 'Répartition réelle des shippings par pays sur 12 mois : USA 64,5 %, France 18,6 %' },
  ],
  '02': [
    { after: '^Carte d’identité|^Carte d.identité', img: 'pics/site_castres.png', w: 400, caption: 'Le site Planet Aura à Castres (Tarn) - bureaux et entrepôt en propre' },
    { after: '^La filiale américaine', img: 'pics/ny_site.png', w: 282, caption: 'Planet Aura Inc. - 95 Inip Dr, Inwood (New York)' },
    { after: '^Chiffres clés et trajectoire', img: 'pics/dash_histo_ca.png', w: 406, caption: 'Historique du CA mensuel 2021-2026 (dashboard gestion Planet’Connect, 24/09/2026)' },
    { after: '^Analyse SWOT', img: 'diagrams/d01_swot.png', w: 520, caption: 'La matrice SWOT Planet Aura 2026' },
  ],
  '03': [
    { after: '^L’équipe : quatre pôles|^L.équipe : quatre pôles', img: 'pics/team2.png', w: 430, caption: 'L’équipe Planet Aura' },
  ],
  '04': [
    { after: '^Vue d’ensemble du catalogue|^Vue d.ensemble du catalogue', img: 'pics/vela_boat.png', w: 320, caption: 'Le voilier-cargo VELA - option de transport bas-carbone (conditionnelle, voir « Offres en développement »)' },
    { after: '^Stockage, cartonnage', img: 'pics/entrepot.png', w: 330, caption: 'L’entrepôt de Castres : stockage et picking en propre' },
    { after: '^USA Groupage DDP', img: 'diagrams/d04_usabars.png', w: 430, caption: 'Grille USA groupage 2026 : le coût par bouteille passe de 105 € à 14,2 € avec le colisage' },
    { after: '^Planet’Connect : la plateforme|^Planet.Connect : la plateforme', img: 'pics/pc_sim_usa.png', w: 396, caption: 'Simulation réelle États-Unis dans Planet’Connect : transport, assurance, taxes DDP' },
  ],
  '05': [
    { after: 'familles d’acteurs|familles d.acteurs|carte des intervenants', img: 'diagrams/d10_carte.png', w: 406, caption: 'La carte des intervenants du secteur - chiffre d’affaires × spécialisation/diversification de l’offre' },
    { after: '^Concurrents directs à la loupe', img: 'diagrams/d10_radar7p.png', w: 406, caption: 'Le face-à-face des spécialistes : analyse 7P, scores internes 0-5 (octobre 2026)' },
  ],
  '06': [
    { after: '^Le profil de client idéal', img: 'pics/carte_adherents.png', w: 356, caption: 'La carte des adhérents en France (Planet’Connect)' },
    { after: '^Les dix clients de référence', img: 'pics/dash_repartitions.png', w: 406, caption: 'Répartition du portefeuille par région et par catégorie (dashboard commercial, 24/09/2026)' },
    { after: '^Gérer le portefeuille', img: 'pics/dash_prospects.png', w: 406, caption: 'La photographie du portefeuille : 448 prospects, 227 adhérents récents, 35 dormants' },
  ],
  '09': [
    { after: '^L’entonnoir d’acquisition|^L.entonnoir', img: 'pics/dash_nouveaux.png', w: 360, caption: 'Nouveaux adhérents par mois et cumul 12 mois (~145, au-dessus de l\u2019objectif de 10/mois) - dashboard commercial' },
  ],
  '13': [
    { after: '^Commencer par le pourquoi', img: 'diagrams/d06_why.png', w: 390, caption: 'Le Golden Circle Planet Aura : WHY, HOW, WHAT' },
  ],
  '15': [
    { after: 'Planet’Connect|Planet.Connect|outils de la fonction', img: 'pics/pc_shippings.png', w: 398, caption: 'La liste « Vos shippings » et leurs statuts dans Planet’Connect (capture réelle)' },
    { after: 'mails automatiques|Sales Operations|rituels', img: 'pics/mails_admin2026.png', w: 400, caption: 'Les 30 mails automatiques Planet’Connect : déclencheurs et cascades, par famille' },
  ],
  '16': [
    { after: 'sinistre', img: 'diagrams/d13_arbre.png', w: 436, caption: 'Sinistres : l’arbre décisionnel officiel 2026 - RXP ou remboursement' },
  ],
  '17': [
    { after: 'tableau de bord|dashboards|Indicateurs', img: 'pics/dash_gestion.png', w: 410, caption: 'Le dashboard gestion réel : CA, CA vins expédiés, shippings, bouteilles (janv.-sept. 2026)' },
  ],
};

module.exports['avantpre2'] = [
  { after: 'certitudes de Floriane', img: 'pics/bitmoji_floriane.png', w: 54, caption: '' },
  { after: 'Mot d’accueil|Mot d.accueil', img: 'pics/bitmoji_duo.png', w: 128, caption: '' },
];
// Annexe A - fiches ICP & personas : composées nativement (fiches-emma.js), plus d'images
// Annexes documentaires : un document = une annexe
module.exports['F'] = [];
for (let i = 1; i <= 5; i++) module.exports['F'].push({ after: '^Le document officiel', img: `annexes/grille_ship-${i}.png`, w: 520, caption: i === 5 ? 'Grille tarifaire shipping 2026 - document officiel (5 pages)' : '' });
module.exports['G'] = [];
for (let i = 1; i <= 3; i++) module.exports['G'].push({ after: '^Le document officiel', img: `annexes/grille_stock-${i}.png`, w: 505, caption: i === 3 ? 'Grille tarifaire stockage & picking 2026 - document officiel (3 pages)' : '' });
module.exports['H'] = [
  { after: '^Le formulaire officiel vierge', img: 'annexes/orderform-1.png', w: 425, caption: 'Order Form 2026 - formulaire officiel vierge' },
];
module.exports['I'] = [
  { after: '^Le document officiel', img: 'annexes/sepa-2.png', w: 440, caption: 'Mandat de pr\u00e9l\u00e8vement SEPA - formulaire officiel vierge' },
];
module.exports['O'] = [
  { after: '^Couverture et sommaire', img: 'annexes/pconnect_cover-01.png', w: 330, caption: '' },
  { after: '^Couverture et sommaire', img: 'annexes/pconnect_sommaire-02.png', w: 500, caption: "Mode d'emploi Planet'Connect - couverture et sommaire (37 pages)" },
];
module.exports['Q'] = [
  { after: '^Le modèle officiel 2026', img: 'annexes/shipform-1.png', w: 400, caption: 'Formulaire de shipping par email - onglet FORMULAIRE' },
];
module.exports['S'] = [
  { after: '^La face extérieure$|^La face extérieure', img: 'pics/flyer1.png', w: 460, caption: 'Flyer de prospection - face extérieure' },
];
module.exports['L'] = [
  { after: '^Les cartes officielles', img: 'pics/usmap_groupage2026.png', w: 540, caption: 'États-Unis, carte 2026 - couverture groupage vin : ouvert / fermé / certains codes postaux (Vermont : prestataire interne après regroupement)' },
  { after: '^Les cartes officielles', img: 'pics/usmap_statuts2026.png', w: 540, caption: 'États-Unis, carte 2026 - la référence des statuts par État : groupage et envoi direct' },
  { after: '^Les cartes officielles', img: 'pics/norway_zones2026.png', w: 470, caption: 'Norvège, carte 2026 - Zone 1 : Nord, Zone 2 : Sud' },
];
// Annexe R - organigramme
module.exports['T'] = [
  { after: '^L\u2019organigramme Planet Aura 2026|^L.organigramme Planet Aura 2026', img: 'diagrams/d03_org.png', w: 520, caption: 'L\u2019organigramme Planet Aura 2026 - direction, p\u00f4les et filiale am\u00e9ricaine' },
];
module.exports['10'] = (module.exports['10'] || []).concat([
  { after: '^Diagramme de la séquence', img: 'diagrams/d10_sequence.png', w: 500, caption: 'Le diagramme de la séquence de prospection automatisée : 8 touches sur 18 jours et ses embranchements' },
]);
// chap. 00 - le cycle de vente en cartes (design maquette)
module.exports['00'] = [
  { after: '^Notre métier en une image', img: 'diagrams/d00_metier.png', w: 520, caption: 'Notre métier en une image : cinq étapes, un seul responsable de bout en bout' },
];

// schémas complémentaires (escalade, trame SPIN, pyramide de preuve)
module.exports['03'] = (module.exports['03'] || []).concat([
  { after: '^Les règles de fonctionnement', img: 'diagrams/d03_escalade.png', w: 520, caption: 'Le circuit d\u2019escalade : ce que chacun d\u00e9cide, et quand passer la main' },
]);
// chap. 12 : schéma de la trame de 35 minutes retiré (trame unique de 45 min au chap. 11)

module.exports['C'] = (module.exports['C'] || []).concat([
  { after: '^La hi\u00e9rarchie de preuve', img: 'diagrams/d14_preuve.png', w: 440, caption: 'La hi\u00e9rarchie de preuve : citer le niveau le plus haut disponible' },
]);

// Annexes P (Planet'Stock), T (POA Canada), U (certificat CIVC)
module.exports['R'] = [
  { after: '^Le picking par scan group\u00e9', img: 'annexes/planetstock-1.png', w: 505, caption: 'Planet\u2019Stock - pr\u00e9paration d\u2019un picking par scan group\u00e9 (capture r\u00e9elle)' },
  { after: '^La connexion', img: 'annexes/planetstock-2.png', w: 250, caption: 'Planet\u2019Stock - \u00e9cran de connexion' },
];
module.exports['M'] = [
  { after: '^La page \u00e0 compl\u00e9ter', img: 'annexes/poa-2.png', w: 425, caption: 'POA Canada - la page \u00e0 compl\u00e9ter du General Agency Agreement (FedEx)' },
];
module.exports['N'] = [
  { after: 'Certificat de Champagne : un exemplaire', img: 'annexes/civc-1.png', w: 385, caption: 'Certificat de Champagne (CIVC) - exemplaire r\u00e9el' },
];

// Annexe N - manuel utilisateur : couverture et sommaire (extraits du document officiel)
module.exports['P'] = [
  { after: '^Couverture et sommaire', img: 'annexes/manuel-cover.png', w: 330, caption: '' },
  { after: '^Couverture et sommaire', img: 'annexes/manuel-sommaire.png', w: 330, caption: 'Manuel utilisateur 2026 - couverture et sommaire (9 sections)' },
];

// Annexe X - sources de la recherche : captures datées des tableaux de bord (sans donnée nominative)
module.exports['X'] = [
  { after: '^Assurance ad valorem souscrite', img: 'pics/dash_assurance.png', w: 260, caption: 'Assurance ad valorem souscrite sur 12 mois glissants : 89,8 % des expéditions (dashboard Planet\u2019Connect, 24/09/2026)' },
  { after: '^CA, shippings et bouteilles', img: 'pics/dash_ca_graph.png', w: 470, caption: 'CA, shippings et bouteilles par mois, janvier-septembre 2026 (dashboard gestion Planet\u2019Connect, 24/09/2026)' },
];

// Annexe J - CGS 2026 : texte intégral (document officiel, 10 pages)
module.exports['J'] = (module.exports['J'] || []);
module.exports['J'].push({ after: '^Les CGS 2026, texte intégral', img: 'annexes/cgs-1.png', w: 520, caption: 'CGS 2026, première page - texte intégral : lien en annexe V et documentation 2026 sur Planet’Connect' });
