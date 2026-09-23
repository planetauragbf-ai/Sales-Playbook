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
