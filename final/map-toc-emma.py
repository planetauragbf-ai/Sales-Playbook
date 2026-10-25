#!/usr/bin/env python3
import json, re, subprocess, sys, unicodedata
PDF = 'Planet_Aura_Sales_Playbook_FINAL_2026.pdf'
subprocess.run(['pdftotext','-layout',PDF,'toc-emma.txt'],check=True)
pages=open('toc-emma.txt',encoding='utf-8').read().split('\f')
def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]','',s.lower())
np_=[norm(p) for p in pages]
start=next(i for i,p in enumerate(np_) if 'modedemploiduplaybook' in p)
reg=json.load(open('toc-map-emma.json'))
out={}; ptr=start; missed=[]
# passe 1 : niveaux 1 (monotone, en sautant les pages d'ouverture de partie)
l1=[h for h in reg if h['level']==1]
for h in l1:
    t=norm(h['text']); found=None
    for i in range(ptr,len(np_)):
        if t in np_[i] and 'danscettepartie' not in np_[i]:
            found=i; break
    if found is None: missed.append(h['text']); continue
    out[h['key']]=found+1; ptr=found
# bornes de chapitre
bounds={}
l1p=[(h['id'],out.get(h['key'])) for h in l1 if out.get(h['key'])]
for k,(uid,p) in enumerate(l1p):
    nxt=l1p[k+1][1] if k+1<len(l1p) else len(np_)+1
    bounds[uid]=(p,nxt)
# passe 2 : niveaux 2 = DERNIERE occurrence dans la plage du chapitre (évite le sous-sommaire)
for h in reg:
    if h['level']!=2: continue
    t=norm(h['text']); lo,hi=bounds.get(h['id'],(start+1,len(np_)))
    cand=[i for i in range(lo-1,min(hi-1,len(np_))) if t in np_[i]]
    out[h['key']]=(max(cand)+1) if cand else lo
# folio affiché : la numérotation démarre à 1 après le sommaire,
# et les pages d'ouverture de partie ne comptent pas dans la numérotation
part_first=['01','06','09','14','A']
openers=sorted(out[h['key']]-1 for h in l1 if h['id'] in part_first and out.get(h['key']))
def folio(p):
    return p - start - sum(1 for o in openers if o <= p)
part_starts={}
for h in l1:
    if h['id'] in part_first and out.get(h['key']):
        part_starts[h['id']]=folio(out[h['key']]-1)
out={k:folio(v) for k,v in out.items()}
json.dump(out,open('toc-pages-emma.json','w'))
json.dump(part_starts,open('part-starts-emma.json','w'))
print('mapped',len(out),'/',len(reg),'(L1',len(l1),') offset',start,'openers',openers,'starts',part_starts)
for m2 in missed: print('MISS',m2)
