# Assemble les rendus PNG du deck (ordre de deck.json) en un PDF de 36 pages, pour relire ou imprimer la présentation.
import json, os, sys
from PIL import Image
S = os.path.dirname(os.path.abspath(__file__))
deck, rendu, out = sys.argv[1], sys.argv[2], sys.argv[3]
order = json.load(open(os.path.join(S, deck, 'project', 'deck.json')))['order']
ims = [Image.open(os.path.join(S, rendu, f'{i}.png')).convert('RGB') for i in order]
ims[0].save(out, save_all=True, append_images=ims[1:], resolution=144, quality=85)
print(out, len(ims), 'pages', os.path.getsize(out) // 1024, 'Ko')
