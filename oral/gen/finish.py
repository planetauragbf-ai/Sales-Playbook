# Passe finale idempotente : espaces insécables (typographie française) + minutage cumulé des notes.
import os, re, json
ROOT = os.path.join(os.path.dirname(__file__), '..', 'deck', 'project')
NB = ' '
WPM = 140          # débit oral visé
TRANSITION = 2     # secondes par changement de diapo
MONTHS = r'(?:janv|févr|mars|avr|mai|juin|juil|août|sept|oct|nov|déc|Janv|Févr|Mars|Avr|Mai|Juin|Juil|Août|Sept|Oct|Nov|Déc)\.?'

def typo(t):
    t = re.sub(r'[  ]([:;!?»%€])', NB + r'\1', t)
    t = re.sub(r'«[  ]', '«' + NB, t)
    for _ in range(2):
        t = re.sub(r'(\d)[  ](\d{3})(?!\d)', r'\1' + NB + r'\2', t)
    t = re.sub(r'(\d)[  ](h|min|j|ans|mois|k€|M€|Md€|Mhl|pt|jours|semaines|bouteilles)(?![\wÀ-ÿ])', r'\1' + NB + r'\2', t)
    t = re.sub(r'(&lt;|&gt;|[≥≤~≈×+−]) (\d)', r'\1' + NB + r'\2', t)
    t = re.sub(r'\b(annexe|Annexe|diapo|T[1-4]|S[1-4]) ([A-Z0-9])', r'\1' + NB + r'\2', t)
    t = re.sub(r'\b(' + MONTHS + r') (\d{4})', r'\1' + NB + r'\2', t)
    return t

def fmt(sec):
    sec = int(round(sec))
    return f'{sec // 60}:{sec % 60:02d}'

def spoken_words(aside):
    a = re.sub(r'^\[[^\]]*\]\s*', '', aside.strip())
    paras = [p for p in a.split('\n') if p.strip() and not p.strip().startswith('(')]
    txt = re.sub(r'\([^)]*\)', '', ' '.join(paras))
    return len(re.findall(r"[\wÀ-ÿ’'%€,\.\- ]+", txt.replace(NB, ' ')))

deck = json.load(open(os.path.join(ROOT, 'deck.json')))
t = 0.0
rows = []
for sid in deck['order']:
    p = os.path.join(ROOT, 'slides', f'{sid}.html')
    s = open(p).read()
    s = ''.join(part if part.startswith('<') else typo(part) for part in re.split(r'(<[^>]+>)', s))
    m = re.search(r'<aside>(.*?)</aside>', s, re.S)
    if m and not sid.startswith('b'):
        n = spoken_words(m.group(1))
        start, t = t, t + n / WPM * 60 + TRANSITION
        body = re.sub(r'^\[[^\]]*\]\s*', '', m.group(1).strip())
        s = s.replace(m.group(1), f'[{fmt(start)} → {fmt(t)}] ' + body)
        rows.append((sid, n, fmt(start), fmt(t)))
    open(p, 'w').write(s)
for r in rows:
    print(f'{r[0]:12s} {r[1]:4d} mots  {r[2]:>5s} → {r[3]:>5s}')
print('total', fmt(t))
