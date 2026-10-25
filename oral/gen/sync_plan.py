# Recopie le minutage calculé par build.py dans plan-oral.md (colonne « Fin visée » et ligne de synthèse).
import os, re, subprocess, sys

ORAL = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
out = subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), 'build.py')], capture_output=True, text=True,
                     env={**os.environ}).stdout
rows = re.findall(r'^(\w+)\s+\d+ mots\s+(\d+:\d\d)\s+→ (\d+:\d\d)$', out, re.M)
ends = [e for _, _, e in rows]
total = re.search(r'TOTAL (\d+) mots, (\d+:\d\d)', out)


def sec(t):
    m, s = t.split(':')
    return int(m) * 60 + int(s)


def mmss(s):
    return f'{s // 60}:{s % 60:02d}'


ids = [r[0] for r in rows]
intro = sec(ends[ids.index('enjeux')])
core = sec(ends[ids.index('kpi')]) - intro
tail = sec(ends[-1]) - sec(ends[ids.index('kpi')])
p = os.path.join(ORAL, 'plan-oral.md')
s = open(p).read()
s = re.sub(r'Minutage des notes à 130 mots/minute.*?\n',
           f'Minutage des notes à 130 mots/minute, 2 s par changement de diapo : {total.group(2)} de texte ({total.group(1)} mots), '
           f'soit 20 min avec les silences. Introduction et diagnostic = {mmss(intro)} ; parties 8 à 14 = {mmss(core)} ; '
           f'synthèse, ouverture et clôture = {mmss(tail)}.\n', s, count=1)
lines = s.split('\n')
k = 0
for i, line in enumerate(lines):
    m = re.match(r'^\| (\d+) \| (.*) \| (\d+:\d\d) \|$', line)
    if m and k < len(ends):
        lines[i] = f'| {m.group(1)} | {m.group(2)} | {ends[int(m.group(1)) - 1]} |'
        k += 1
open(p, 'w').write('\n'.join(lines))
print('plan-oral.md :', total.group(2), 'intro', mmss(intro), 'coeur', mmss(core), 'fin', mmss(tail), f'({k} lignes)')
