// Placements d'images du document final (clé = id d'unité) - photos réelles + schémas codés charte uniquement.
module.exports = {
  '01': [
    { after: '^Saisonnalité : planifier', img: 'pics/dash_ship_evo.png', w: 398, caption: 'Shippings par mois, sept. 2025 - sept. 2026 (dashboard logistique Planet’Connect)' },
    { after: '^Géographies prioritaires', img: 'pics/carte_vignobles.png', w: 310, caption: 'Les régions viticoles - nos terrains de prospection prioritaires' },
    { after: '^Destinations demandées', img: 'pics/worldmap2.png', w: 400, caption: 'Les destinations desservies dans le monde' },
    { after: '^Destinations demandées', img: 'pics/dash_pays.png', w: 282, caption: 'Répartition réelle des shippings par pays sur 12 mois : USA 64,5 %, France 18,6 %' },
  ],
  '02': [
    { after: '^Carte d’identité|^Carte d.identité', img: 'pics/site_castres.png', w: 400, caption: 'Le site Planet Aura à Castres (Tarn) - bureaux et entrepôt en propre' },
    { after: '^La filiale américaine', img: 'pics/ny_site.png', w: 282, caption: 'Planet Aura Inc. - 95 Inip Dr, Inwood (New York)' },
    { after: '^Chiffres clés et trajectoire', img: 'pics/dash_histo_ca.png', w: 406, caption: 'Historique du CA mensuel 2021-2026 (dashboard gestion Planet’Connect, 24/09/2026)' },
    { after: '^Analyse SWOT', img: 'diagrams/d01_swot.png', w: 436, caption: 'La matrice SWOT Planet Aura 2026' },
  ],
  '03': [
    { after: '^L’équipe : quatre pôles|^L.équipe : quatre pôles', img: 'pics/team2.png', w: 430, caption: 'L’équipe Planet Aura' },
  ],
  '04': [
    { after: '^Vue d’ensemble du catalogue|^Vue d.ensemble du catalogue', img: 'pics/vela_boat.png', w: 340, caption: 'Le voilier-cargo VELA - notre option de transport bas-carbone (conditionnelle, chap. 04)' },
    { after: '^Stockage, cartonnage', img: 'pics/entrepot.png', w: 380, caption: 'L’entrepôt de Castres : stockage et picking en propre' },
    { after: '^USA Groupage DDP', img: 'diagrams/d04_usabars.png', w: 436, caption: 'Grille USA groupage 2026 : le coût par bouteille passe de 105 € à 14,2 € avec le colisage' },
    { after: '^Planet’Connect : la plateforme|^Planet.Connect : la plateforme', img: 'pics/pc_sim_usa.png', w: 382, caption: 'Simulation réelle États-Unis dans Planet’Connect : transport, assurance, taxes DDP' },
  ],
  '05': [
    { after: 'familles d’acteurs|familles d.acteurs|carte des intervenants', img: 'diagrams/d10_carte.png', w: 406, caption: 'La carte des intervenants du secteur - chiffre d’affaires × spécialisation/diversification de l’offre' },
    { after: '^Concurrents directs à la loupe', img: 'diagrams/d10_radar7p.png', w: 406, caption: 'Le face-à-face des spécialistes : analyse 7P, scores internes 0-5 (octobre 2026)' },
  ],
  '06': [
    { after: '^Le profil de client idéal', img: 'pics/carte_adherents.png', w: 330, caption: 'La carte des adhérents en France (Planet’Connect)' },
    { after: '^Les dix clients de référence', img: 'pics/dash_repartitions.png', w: 406, caption: 'Répartition du portefeuille par région et par catégorie (dashboard commercial, 24/09/2026)' },
    { after: '^Gérer le portefeuille', img: 'pics/dash_prospects.png', w: 406, caption: 'La photographie du portefeuille : 448 prospects, 227 adhérents récents, 35 dormants' },
  ],
  '09': [
    { after: '^L’entonnoir d’acquisition|^L.entonnoir', img: 'pics/dash_nouveaux.png', w: 390, caption: 'Nouveaux adhérents par mois et cumul 12 mois (~145) - dashboard commercial' },
  ],
  '13': [
    { after: '^Commencer par le pourquoi', img: 'diagrams/d06_why.png', w: 390, caption: 'Le Golden Circle Planet Aura : WHY, HOW, WHAT' },
  ],
  '15': [
    { after: 'Planet’Connect|Planet.Connect|outils de la fonction', img: 'pics/pc_shippings.png', w: 398, caption: 'La liste « Vos shippings » et leurs statuts dans Planet’Connect (capture réelle)' },
    { after: 'mails automatiques|Sales Operations|rituels', img: 'pics/mails_cascade.png', w: 350, caption: 'Les mails automatiques Planet’Connect : déclencheurs et cascades (vue admin)' },
  ],
  '16': [
    { after: 'sinistre', img: 'diagrams/d13_arbre.png', w: 436, caption: 'Sinistres : l’arbre décisionnel officiel 2026 - RXP ou remboursement' },
  ],
  '17': [
    { after: 'tableau de bord|dashboards|Indicateurs', img: 'pics/dash_gestion.png', w: 406, caption: 'Le dashboard gestion réel : CA, CA vins expédiés, shippings, bouteilles (janv.-sept. 2026)' },
  ],
};

module.exports['avantpre'] = [
  { after: 'certitudes de Floriane', img: 'pics/bitmoji_trio.png', w: 300, caption: '' },
  { after: 'Mot d’accueil|Mot d.accueil', img: 'pics/bitmoji_duo.png', w: 250, caption: '' },
];
// Annexe H - fiches maquettées (pages extraites du PPTX officiel)
module.exports['H'] = [
  { after: '^ICP 1', img: 'fiches/fiche-02.png', w: 520, caption: '' },
  { after: '^ICP 2', img: 'fiches/fiche-01.png', w: 520, caption: '' },
  { after: '^ICP 3', img: 'fiches/fiche-04.png', w: 520, caption: '' },
  { after: '^ICP 4', img: 'fiches/fiche-03.png', w: 520, caption: '' },
  { after: '^ICP 5', img: 'fiches/fiche-06.png', w: 520, caption: '' },
  { after: '^Persona A', img: 'fiches/fiche-05.png', w: 520, caption: '' },
  { after: '^Persona B', img: 'fiches/fiche-07.png', w: 520, caption: '' },
  { after: '^Persona C', img: 'fiches/fiche-08.png', w: 520, caption: '' },
  { after: '^Persona D', img: 'fiches/fiche-10.png', w: 520, caption: '' },
  { after: '^Persona E', img: 'fiches/fiche-09.png', w: 520, caption: '' },
];
// Annexe I - documents officiels entiers
module.exports['I'] = [];
for (let i = 1; i <= 5; i++) module.exports['I'].push({ after: '^Grille tarifaire shipping', img: `annexes/grille_ship-${i}.png`, w: 520, caption: i === 5 ? 'Grille tarifaire shipping 2026 - document officiel (5 pages)' : '' });
for (let i = 1; i <= 3; i++) module.exports['I'].push({ after: '^Grille tarifaire stockage', img: `annexes/grille_stock-${i}.png`, w: 520, caption: i === 3 ? 'Grille tarifaire stockage & picking 2026 - document officiel (3 pages)' : '' });
module.exports['I'].push(
  { after: '^Order Form 2026', img: 'annexes/orderform-1.png', w: 505, caption: 'Order Form 2026 - formulaire officiel vierge' },
  { after: '^Mandat SEPA', img: 'annexes/sepa-1.png', w: 505, caption: '' },
  { after: '^Mandat SEPA', img: 'annexes/sepa-2.png', w: 505, caption: 'Mandat SEPA - document officiel (2 pages)' },
  { after: '^Mode d\u2019emploi Planet|^Mode d.emploi Planet', img: 'annexes/pconnect_cover-01.png', w: 330, caption: '' },
  { after: '^Mode d\u2019emploi Planet|^Mode d.emploi Planet', img: 'annexes/pconnect_sommaire-02.png', w: 500, caption: 'Mode d\u2019emploi Planet\u2019Connect - couverture et sommaire (37 pages)' },
  { after: '^Formulaire de shipping', img: 'annexes/shipform-1.png', w: 400, caption: 'Formulaire de shipping par email - onglet FORMULAIRE' },
  { after: '^Flyer de prospection', img: 'pics/flyer1.png', w: 460, caption: 'Flyer de prospection - face extérieure' },
  { after: '^Cartes de zones', img: 'pics/usmap1.png', w: 520, caption: 'États-Unis - couverture groupage vin (ouvert / codes postaux limités / fermé)' },
  { after: '^Cartes de zones', img: 'pics/usmap3.png', w: 520, caption: 'États-Unis - carte de référence des statuts par État' },
  { after: '^Cartes de zones', img: 'pics/norway2.png', w: 420, caption: 'Norvège - les deux zones tarifaires (lire Sud/Nord, jamais le numéro)' }
);
module.exports['10'] = (module.exports['10'] || []).concat([
  { after: '^Diagramme de la séquence', img: 'diagrams/d10_sequence.png', w: 500, caption: 'Le diagramme de la séquence de prospection automatisée : 8 touches sur 18 jours et ses embranchements' },
]);
