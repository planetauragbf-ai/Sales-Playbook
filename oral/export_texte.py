# Export du texte visible et des notes de chaque diapo (ordre de deck.json), pour relecture.
import json, os, re, sys, html
S = os.path.dirname(os.path.abspath(__file__))
deck = sys.argv[1] if len(sys.argv) > 1 else 'deck5'
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(S, 'texte_export.md')
order = json.load(open(os.path.join(S, deck, 'project', 'deck.json')))['order']
lines = ['# Deck v5, texte visible et notes (export pour relecture)', '']
for n, sid in enumerate(order, 1):
    h = open(os.path.join(S, deck, 'project', 'slides', f'{sid}.html'), encoding='utf-8').read()
    m = re.search(r'<aside[^>]*>(.*?)</aside>', h, re.S)
    notes = html.unescape(re.sub(r'<[^>]+>', '\n', m.group(1))) if m else ''
    body = h[:m.start()] + h[m.end():] if m else h
    body = re.sub(r'<(style|script|svg)[^>]*>.*?</\1>', ' ', body, flags=re.S)
    txt = html.unescape(re.sub(r'<[^>]+>', ' | ', body))
    txt = re.sub(r'\s*\|\s*(\|\s*)+', ' | ', txt); txt = re.sub(r'\s+', ' ', txt).strip(' |')
    notes = re.sub(r'\n{3,}', '\n\n', notes).strip()
    lines += [f'## {n}. {sid}', '### Écran', txt, '### Notes', notes, '']
open(out, 'w', encoding='utf-8').write('\n'.join(lines)); print(out, len(order), 'diapos')
