# Intègre les diapos candidates v5 (v5cand/<id>.py) et leurs notes (v5cand/<id>_notes.txt) dans gen5.
# usage : python3 integrate_v5.py id1 id2 …   (sans argument : tous les candidats présents)
import glob, os, re, shutil, sys

S = os.path.dirname(os.path.abspath(__file__))
G = os.path.join(S, 'gen5')
C = os.path.join(S, 'v5cand')
MOD = {}
for f, names in [('s_intro.py', ['cover', 'accroche', 'sommaire', 'marche', 'entreprise', 'offre', 'diagnostic']),
                 ('s_vendre.py', ['icp', 'personas', 'solutions', 'processus', 'prospecter', 'spin', 'proposer', 'activer']),
                 ('s_piloter.py', ['ressources', 'salesops', 'onboarding', 'kpi', 'conclusion']),
                 ('backups.py', [f'b{i}' for i in range(1, 18)])]:
    for n in names:
        MOD[n] = f


def replace_fn(path, name, new_src):
    """Remplace la fonction (bornes données par l'AST : robuste aux f-strings multilignes)."""
    import ast
    s = open(path, encoding='utf-8').read()
    nodes = [n for n in ast.parse(s).body if isinstance(n, ast.FunctionDef) and n.name == name]
    assert len(nodes) == 1, (path, name)
    lines = s.split('\n')
    a, b = nodes[0].lineno - 1, nodes[0].end_lineno
    lines[a:b] = new_src.strip('\n').split('\n')
    open(path, 'w', encoding='utf-8').write('\n'.join(lines))


def replace_note(path, sid, text):
    s = open(path, encoding='utf-8').read()
    pat = re.compile(rf"^'{sid}': \"\"\".*?\"\"\",", re.S | re.M)
    assert len(pat.findall(s)) == 1, (path, sid)
    assert '"""' not in text, sid
    s = pat.sub(lambda m: f"'{sid}': \"\"\"{text.strip()}\"\"\",", s)
    open(path, 'w', encoding='utf-8').write(s)


def main(ids):
    bak = os.path.join(S, 'gen5_avant_integration')
    if not os.path.exists(bak):
        shutil.copytree(G, bak)
    if not ids:
        ids = sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(C, '*.py')) if not os.path.basename(p).startswith('_'))
    for sid in ids:
        cand = os.path.join(C, f'{sid}.py')
        if os.path.exists(cand):
            src = open(cand, encoding='utf-8').read()
            assert re.search(rf'^def {sid}\(', src, re.M), sid
            path = os.path.join(G, MOD[sid])
            cur = open(path, encoding='utf-8').read()
            if re.search(rf'^def {sid}\(', cur, re.M):
                replace_fn(path, sid, src)
            else:  # nouvelle diapo de secours : avant la liste ALL, puis ajoutée à ALL
                cur = cur.replace('\nALL = [', '\n' + src.strip('\n') + '\n\n\nALL = [', 1)
                cur = re.sub(r'^(ALL = \[.*?)\]', lambda m: m.group(1) + f', {sid}]', cur, count=1, flags=re.M)
                open(path, 'w', encoding='utf-8').write(cur)
            print('diapo', sid, '→', MOD[sid])
        nt = os.path.join(C, f'{sid}_notes.txt')
        if os.path.exists(nt):
            path = os.path.join(G, 'notes_main.py' if MOD[sid] != 'backups.py' else 'notes.py')
            body = open(path, encoding='utf-8').read()
            if re.search(rf"^'{sid}': \"\"\"", body, re.M):
                replace_note(path, sid, open(nt, encoding='utf-8').read())
            else:  # nouvelle note : ajoutée en fin de dictionnaire
                txt = open(nt, encoding='utf-8').read().strip()
                i = body.rstrip().rfind('}')
                body = body[:i].rstrip() + f"\n\n'{sid}': \"\"\"{txt}\"\"\",\n" + body[i:]
                open(path, 'w', encoding='utf-8').write(body)
            print('note ', sid, '→', os.path.basename(path))


if __name__ == '__main__':
    main(sys.argv[1:])
