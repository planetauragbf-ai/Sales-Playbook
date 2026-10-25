# Génère ecole/anonymisation.json (édition école : données clients anonymisées)
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
T = []
def r(f, old, new, count=1): T.append({"file": f, "old": old, "new": new, "count": count})

# (1) Top 10 nominatif du chap. 06 -> Compte 1 ... Compte 10 (segment/région conservés)
r("06.md", "Top 10 réel sur 12 mois glissants (dashboard commercial, 24/09/2026)", "Top 10 anonymisé sur 12 mois glissants (dashboard, 24/09/2026)")
r("06.md", "| Planet Provence | Wine tours de domaines provençaux |", "| Compte 1 | Wine tours de domaines provençaux |")
r("06.md", "| Château de Pommard | Maison, œnotourisme international |", "| Compte 2 | Maison, œnotourisme international |")
r("06.md", "| Les Caves Ambacia | Cave touristique (Amboise) |", "| Compte 3 | Cave touristique (Loire) |")
r("06.md", "| O Chateau | Expériences vin, Paris |", "| Compte 4 | Expériences vin, Paris |")
r("06.md", "| Champagne La Maison Penet | Maison de champagne |", "| Compte 5 | Maison de champagne |")
r("06.md", "| Château La Coste | Domaine provençal art & vin |", "| Compte 6 | Domaine provençal à caveau |")
r("06.md", "| Les Caves du Louvre | Cave touristique, Paris |", "| Compte 7 | Cave touristique, Paris |")
r("06.md", "| Domaine de la Citadelle | Domaine du Luberon |", "| Compte 8 | Domaine du Luberon |")
r("06.md", "| Break Events - GL events | Événementiel / salons |", "| Compte 9 | Événementiel / salons |")
r("06.md", "| Maison Ogier | Maison rhodanienne |", "| Compte 10 | Maison rhodanienne |")
# chap. 08 : rang d'adhérents nommés
r("08.md", "preuve : Les Caves du Louvre, O Château, Caves Ambacia", "preuve : trois caves du top 10 (chap. 06)")
r("08.md", "preuve : Planet Provence (n° 1 du top 10), Break Events", "preuve : deux comptes du top 10 (chap. 06)")
# fiches natives de l'annexe A (exemples du réseau rattachés au top 10)
r("fiches-emma.js", "Château de Pommard, Château La Coste, Domaine de la Citadelle, Maison Ogier", "Comptes 2, 6, 8 et 10 du top 10 (chap. 06)")
r("fiches-emma.js", "Champagne La Maison Penet (top 5), Champagne Pol Couronne", "Compte 5 du top 10 (chap. 06) et d'autres maisons du réseau")
r("fiches-emma.js", "Les Caves Ambacia, O Chateau, Les Caves du Louvre (trois comptes du top 10)", "Comptes 3, 4 et 7 (trois comptes du top 10, chap. 06)")
r("fiches-emma.js", "Planet Provence (n° 1 du top 10 : 483 envois), Break Events – GL events", "Compte 1 (n° 1 du top 10 : 483 envois), compte 9 (événementiel)")
r("fiches-emma.js", "Planet Provence, premier compte du réseau, né d'un wine tour", "Une agence de wine tours dans le top 10 du réseau")
r("fiches-emma.js", "Les Caves du Louvre, O Chateau, Caves Ambacia dans le top 10", "Trois caves touristiques dans le top 10")
# annexe C : adhérent nommé avec un chiffre
r("C.md", "chez un caviste adhérent (La Maison du Vouvray)", "chez un caviste adhérent")

# (2) Certificat CIVC réel de l'annexe N -> image caviardée + phrase adaptée
r("N.md", "ici un exemplaire réel émis pour un envoi vers la Corée du Sud (usage strictement interne : références réelles d'un adhérent et de son destinataire).",
  "ici un exemplaire réel émis pour un envoi vers la Corée du Sud, caviardé pour l'édition école : noms, adresses, références et signature masqués.")
r("04.md", "Un exemplaire réel du certificat est reproduit en annexe N.", "Un exemplaire réel caviardé du certificat est reproduit en annexe N.")
r("X.md", "les documents officiels sont reproduits tels quels, jamais altérés.", "les documents officiels sont reproduits tels quels, sans autre altération que le caviardage de l'édition école.")

# (3) Avis Google : aucun nom de personne -> descripteurs de rôle
r("C.md", "| Sara Croche · déc. 2024 |", "| Professionnelle, cliente depuis 3 ans · déc. 2024 |")
r("C.md", "| Valérie Mingot, Maison du Vouvray · déc. 2020 |", "| Adhérent historique · déc. 2020 |")
r("C.md", "| Manon Lafont · août 2022 |", "| Professionnelle, domaine provençal · août 2022 |")
r("C.md", "| Naima Mazirh · mai 2022 |", "| Professionnelle de la filière · mai 2022 |")
r("C.md", "| Michel Bruneau · janv. 2023 |", "| Apporteur d'affaires, client USA · janv. 2023 |")
r("C.md", "| Arthus et Jean · avr. 2025 |", "| Professionnels, clients depuis 2 ans · avr. 2025 |")
r("C.md", "| Charles-Alexandre de Kuyper · nov. 2023 |", "| Client, Local Guide · nov. 2023 |")
r("C.md", "| Filaquier · août 2020 |", "| Professionnel, envois USA · août 2020 |")

# (4) Annexe A : verbatims attribués à des domaines nommés -> descripteurs de segment
r("A.md", "« gros point fort » (Cave Henri IV)", "« gros point fort » (un vigneron adhérent)")
r("A.md", "sur les casses (Vignobles Jade)", "sur les casses (un autre vigneron)")
r("A.md", "(La Cavale, Domaine de Marie)", "(deux domaines à caveau)")
r("A.md", "(Famille Gonnet)", "(un domaine familial)", 2)
r("A.md", "(La Maison du Vouvray, caviste)", "(un caviste adhérent)")
r("A.md", "(« Corée & Taïwan » - Clos Fleurus)", "(« Corée & Taïwan » - un domaine exportateur)")
r("A.md", "(Wineriz - Domaine la Barroche)", "(Wineriz - un domaine e-commerçant)")
r("A.md", "le groupage dégressif (Dalmeran)", "le groupage dégressif (un domaine du réseau)")
r("A.md", "« le client ne comprend pas les suppléments » (La Barroche)", "« le client ne comprend pas les suppléments » (le même domaine e-commerçant)")
r("A.md", "juin 2019 » (Maison du Vouvray).", "juin 2019 » (un adhérent historique).")
r("A.md", "envois BtoC à l'étranger » (Domaine de Fontenille).", "envois BtoC à l'étranger » (un domaine provençal).")

# (5) Légende de l'image du certificat CIVC (annexe N)
r("image-placements-emma.js", "Certificat de Champagne (CIVC) - exemplaire réel", "Certificat de Champagne (CIVC) - exemplaire réel, caviardé pour l’édition école")

# (6) Ré-identification par recoupement (vérification du 25/10/2026) :
# compte 1 <-> récit fondateur, compte 9 <-> organisateurs nommés, compte 3 <-> Amboise
r("02.md", "Planet Provence (wine tours dirigés par Brice) devient le premier client.", "Le premier client vient du réseau des fondateurs.")
r("fiches-emma.js", "Le premier compte du réseau est né d'un wine tour", "Un des gros comptes du réseau vient du wine tour")
r("fiches-emma.js", "organisateurs de salons (GL events, Aux Vignobles !, Break Events)", "organisateurs de salons et de foires aux vins")
r("06.md", "axe organisateurs (GL events, Aux Vignobles !, Break Events)", "axe organisateurs de salons et de foires aux vins")
r("04.md", "stockage tampon (GL events, Aux Vignobles !, Break Events…)", "stockage tampon (organisateurs de salons, Aux Vignobles !…)")
r("A.md", "caves touristiques (Amboise, caveaux de châteaux)", "caves touristiques (Val de Loire, caveaux de châteaux)")
r("A.md", "Le directeur d'une cave touristique de la Loire enchaîne", "Le directeur d'une cave touristique enchaîne")

IMAGES = [
    {"asset": "annexes/civc-1.png", "redacted": "ecole/civc-1.png"},
    {"asset": "pics/flyer1.png", "redacted": "ecole/flyer1.png"},
    {"asset": "annexes/planetstock-1.png", "redacted": "ecole/planetstock-1.png"},
    {"asset": "pics/dash_repartitions.png", "redacted": "ecole/dash_repartitions.png"},
]
out = {"text": T, "images": IMAGES, "cover_note": "ÉDITION ÉCOLE · DONNÉES CLIENTS ANONYMISÉES"}
with open(os.path.join(HERE, "anonymisation.json"), "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print(len(T), "remplacements,", len(IMAGES), "images")
