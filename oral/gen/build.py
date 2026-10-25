# Génère deck/project/slides/*.html et deck.json (soutenance v3, cas fil rouge), avec minutage des notes à 130 mots/min.
import json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
from kit import section
import s_intro
try:
    import s_vendre
except ImportError:
    s_vendre = None
try:
    import s_piloter
except ImportError:
    s_piloter = None
try:
    import backups
except ImportError:
    backups = None
from notes import NOTES, BACKUP_NOTES

ORAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ORAL, os.environ.get('DECK_DIR', 'deck'), 'project')
WPM = 130
PAUSE = 2  # secondes de respiration au changement de diapo

MAIN = []
for mod, names in [(s_intro, ['cover', 'accroche', 'sommaire', 'marche', 'entreprise', 'offre', 'diagnostic']),
                   (s_vendre, ['icp', 'personas', 'solutions', 'processus', 'prospecter', 'spin', 'proposer', 'activer']),
                   (s_piloter, ['ressources', 'salesops', 'onboarding', 'kpi', 'conclusion'])]:
    if mod is None:
        continue
    for n in names:
        if hasattr(mod, n):
            MAIN.append(getattr(mod, n))


def spoken(text):
    # les indications scéniques entre parenthèses ne sont pas dites
    t = re.sub(r'\([^)]*\)', ' ', text)
    return len(re.findall(r"[\wÀ-ÿ’'-]+", t))


def mmss(s):
    s = int(round(s))
    return f'{s // 60}:{s % 60:02d}'


def main():
    os.makedirs(f'{OUT}/slides', exist_ok=True)
    order, sections = [], {}
    t = 0.0
    total_words = 0
    rows = []
    for fn in MAIN:
        sid, inner, kw = fn()
        note = NOTES.get(sid, '(à écrire)')
        w = spoken(note)
        total_words += w
        dur = w / WPM * 60 + PAUSE
        stamp = f'[{mmss(t)} → {mmss(t + dur)}] '
        rows.append((sid, w, mmss(dur), mmss(t + dur)))
        t += dur
        sect = kw.pop('sect', None)
        html = section(sid, inner, stamp + note, sect=sect, **kw)
        open(f'{OUT}/slides/{sid}.html', 'w').write(html)
        order.append(sid)
        if sect:
            sections[f's{len(sections) + 1}'] = {'description': sect, 'start': sid}
    if backups:
        first = True
        for fn in backups.ALL:
            sid, inner, kw = fn()
            kw.pop('sect', None)
            note = BACKUP_NOTES.get(sid, '')
            html = section(sid, inner, note, sect=None, **kw)
            open(f'{OUT}/slides/{sid}.html', 'w').write(html)
            order.append(sid)
            if first:
                sections[f's{len(sections) + 1}'] = {'description': 'Diapositives de secours pour les questions du jury', 'start': sid}
                first = False
    deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-23T09:00:00Z"}, "lists": "css",
            "title": "Soutenance Sales Playbook Planet Aura", "cover": "cover", "order": order, "sections": sections,
            "faces": {"playfair-display": {"family": "Playfair Display", "href": "https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400..800;1,400..700&display=swap"},
                      "inter": {"family": "Inter", "href": "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"},
                      "poppins": {"family": "Poppins", "href": "https://fonts.googleapis.com/css2?family=Poppins:wght@500;600;700&display=swap"}},
            "designSystems": []}
    json.dump(deck, open(f'{OUT}/deck.json', 'w'), ensure_ascii=False)
    for r in rows:
        print(f'{r[0]:12s} {r[1]:4d} mots  {r[2]}  → {r[3]}')
    print(f'TOTAL {total_words} mots, {mmss(t)} à {WPM} mots/min (+{PAUSE} s par diapo)')


if __name__ == '__main__':
    main()
