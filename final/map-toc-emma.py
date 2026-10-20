#!/usr/bin/env python3
import json, re, subprocess, unicodedata
PDF='Planet_Aura_Sales_Playbook_FINAL_2026.pdf'
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
json.dump(out,open('toc-pages-emma.json','w'))
print('mapped',len(out),'/',len(reg),'(L1',len(l1),')')
for m2 in missed: print('MISS',m2)
