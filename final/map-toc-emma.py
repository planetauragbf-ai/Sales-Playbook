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
for h in reg:
    t=norm(h['text'])
    found=None
    for i in range(ptr,len(np_)):
        if t in np_[i] and 'danscettepartie' not in np_[i]:
            found=i; break
    if found is None: missed.append(h['text']); continue
    out[h['key']]=found+1
    ptr=found
json.dump(out,open('toc-pages-emma.json','w'))
print('mapped',len(out),'/',len(reg),'start',start+1)
for m in missed: print('MISS',m)
