# Banc d'essai d'UNE diapo candidate, sans toucher aux modules partagés.
# usage : python3 try_slide.py <id> <candidat.py> [--notes notes.txt] [--out DOSSIER]
# Le candidat définit la fonction de la diapo (même nom que l'id : icp, b4…) ; il est exécuté dans
# l'espace de noms du module d'origine (kit et aides du module disponibles).
# Sortie : rendu normal + rendu « stress » (textes +10 %), mots visibles, delta de mots dits.
import argparse, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORAL = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import kit, s_intro, s_vendre, s_piloter, backups  # noqa: E402
from notes import NOTES, BACKUP_NOTES  # noqa: E402

MOD = {}
for m, names in [(s_intro, ['cover', 'accroche', 'sommaire', 'marche', 'entreprise', 'offre', 'diagnostic']),
                 (s_vendre, ['icp', 'personas', 'solutions', 'processus', 'prospecter', 'spin', 'proposer', 'activer']),
                 (s_piloter, ['ressources', 'salesops', 'onboarding', 'kpi', 'conclusion']),
                 (backups, [f'b{i}' for i in range(1, 17)])]:
    for n in names:
        MOD[n] = m


def spoken(text):
    t = re.sub(r'\([^)]*\)', ' ', text)
    return len(re.findall(r"[\wÀ-ÿ’'-]+", t))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('sid')
    ap.add_argument('cand')
    ap.add_argument('--notes')
    ap.add_argument('--out')
    a = ap.parse_args()
    mod = MOD[a.sid]
    ns = dict(vars(mod))
    exec(compile(open(a.cand, encoding='utf-8').read(), a.cand, 'exec'), ns)
    sid, inner, kw = ns[a.sid]()
    assert sid == a.sid, f'la fonction renvoie l’id {sid}, attendu {a.sid}'
    kw.pop('sect', None)
    old_note = NOTES.get(sid, BACKUP_NOTES.get(sid, ''))
    note = open(a.notes, encoding='utf-8').read().strip() if a.notes else old_note
    out = a.out or os.path.join(ORAL, 'sandbox', sid)
    os.makedirs(os.path.join(out, 'slides'), exist_ok=True)
    open(os.path.join(out, 'slides', f'{sid}.html'), 'w', encoding='utf-8').write(kit.section(sid, inner, note, **kw))
    env = dict(os.environ)
    env['NODE_PATH'] = subprocess.run(['npm', 'root', '-g'], capture_output=True, text=True).stdout.strip()
    bad = False
    for stress in ['1', '1.10']:
        env['STRESS'] = stress
        r = subprocess.run(['node', os.path.join(ORAL, 'render5.js'), os.path.join(out, 'slides'), out, sid],
                           capture_output=True, text=True, env=env, timeout=300)
        txt = (r.stdout + r.stderr).strip()
        print(f'--- rendu {"normal" if stress == "1" else "stress +10 %"}')
        print(txt)
        if stress == '1':
            bad |= any(k in txt for k in ['CHEVAUCHEMENT', 'DÉBORDE', 'FLUX', 'MARGE', 'MOT TROP', 'HORS CADRE'])
        else:
            bad |= any(k in txt for k in ['CHEVAUCHEMENT', 'FLUX', 'MARGE', 'MOT TROP', 'HORS CADRE'])
    print(f'--- notes : {spoken(note)} mots dits (actuel {spoken(old_note)}, delta {spoken(note) - spoken(old_note):+d})')
    print(f'--- images : {out}/{sid}.png  et  {out}/{sid}_stress.png')
    print('RÉSULTAT :', 'À CORRIGER' if bad else 'OK')


if __name__ == '__main__':
    main()
