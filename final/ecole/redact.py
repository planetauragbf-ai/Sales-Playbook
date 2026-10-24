# Caviardage de l'édition école : rectangles noirs opaques aux coordonnées pixel relevées sur chaque image.
from PIL import Image, ImageDraw
A = '/home/user/Sales-Playbook/build/assets/'
BOXES = {
    'annexes/civc-1.png': [
        (816, 114, 1076, 142),   # N° de délivrance
        (850, 239, 1196, 361),   # Expéditeur : raison sociale, adresse, code postal
        (850, 445, 1196, 567),   # Destinataire : organisation, événement, adresse
        (394, 859, 931, 1145),   # Marques et qualités : nom de l'adhérent + cuvées
        (912, 1556, 1197, 1637), # Signature numérique
        (984, 1645, 1240, 1675), # Lien de vérification (référence)
    ],
    'pics/flyer1.png': [
        (377, 481, 523, 496),    # signature d'avis : prénom + établissement + département
        (377, 576, 523, 591),    # signature d'avis : prénom + établissement + département
    ],
    'annexes/planetstock-1.png': [
        # désignations des vins en stock (producteurs, dont noms de personnes) ; REF, couleur,
        # millésime et emplacement restent visibles
        (159, 465, 690, 489), (159, 577, 690, 601), (159, 689, 690, 713),
        (159, 801, 690, 822), (159, 914, 690, 939), (159, 1026, 690, 1047),
    ],
}
def run(only=None):
    for src, boxes in BOXES.items():
        if only and src not in only: continue
        im = Image.open(A + src).convert('RGB')
        d = ImageDraw.Draw(im)
        for b in boxes:
            d.rectangle(b, fill=(0, 0, 0))
        out = A + 'ecole/' + src.split('/')[-1]
        im.save(out, optimize=True)
        print(out, im.size, len(boxes), 'boxes')
if __name__ == '__main__':
    import sys
    run(sys.argv[1:] or None)
