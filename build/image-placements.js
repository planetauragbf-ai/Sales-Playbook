// Placements d'images par chapitre : { 'fichier.md': [{after: regex ligne de titre, img, w(px), caption}] }
// `after` : regex testée sur le texte des titres ; l'image est insérée juste après le titre correspondant.
module.exports = {
  '00-resume-executif.md': [
    { after: '^Qui sommes-nous', img: 'pics/hq.png', w: 430, caption: 'Le siège Planet Aura à Castres (Tarn)' },
  ],
  '01-entreprise.md': [
    { after: '^1\\.3 Carte d\'identité', img: 'pics/office.png', w: 400, caption: 'Les bureaux Planet Aura — « Wine delivery world wide »' },
    { after: '^1\\.5 Vos interlocuteurs', img: 'pics/team.png', w: 460, caption: 'L’équipe Planet Aura' },
  ],
  '02-marche.md': [
    { after: '^2\\.10 Destinations demandées', img: 'pics/worldmap.png', w: 440, caption: 'Les destinations desservies par Planet Aura' },
  ],
  '03-offres-services.md': [
    { after: '^3\\.4 USA Groupage', img: 'pics/usmap1.png', w: 470, caption: 'Couverture des États-Unis — groupage vin (ouvert / codes postaux limités / fermé)' },
    { after: '^3\\.8 Option VELA', img: 'pics/sailboat.png', w: 360, caption: 'Le voilier-cargo — fret vélique bas-carbone (offre conditionnelle)' },
    { after: '^3\\.9 Stockage', img: 'pics/warehouse.png', w: 420, caption: 'L’entrepôt de stockage Planet Aura' },
    { after: '^3\\.13 Planet\'Connect', img: 'pics/simulator.png', w: 470, caption: 'Le simulateur d’expédition Planet’Connect' },
  ],
  '04-tarifs.md': [
    { after: '^4\\.5 USA — Direct', img: 'pics/usmap2.png', w: 470, caption: 'États desservis en direct' },
  ],
  '05-cibles-personas.md': [
    { after: '^5\\.1 Le profil de client idéal', img: 'pics/illus_people.png', w: 500, caption: '' },
  ],
  '14-conformite-reglementation.md': [
    { after: '^Lire les cartes de zones USA', img: 'pics/usmap3.png', w: 470, caption: 'Carte de référence des statuts par État (vin) — vérifier État ET code postal' },
    { after: 'Norvège', img: 'pics/norway.png', w: 380, caption: 'Norvège — les deux zones tarifaires' },
  ],
};
