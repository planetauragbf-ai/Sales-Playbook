#!/usr/bin/env python3
import json, re, subprocess, sys, unicodedata
PDF='Planet_Aura_Sales_Playbook_2026.pdf'
subprocess.run(['pdftotext','-layout',PDF,'toc-check.txt'],check=True)
pages=open('toc-check.txt',encoding='utf-8').read().split('\f')
def norm(s):
    s=unicodedata.normalize('NFKD',s)
    s=''.join(c for c in s if not unicodedata.combining(c))
    return re.sub(r'[^a-z0-9]','',s.lower())
npages=[norm(p) for p in pages]
# body starts after the TOC: anchor on README body text
start=next(i for i,p in enumerate(npages) if 'ceplaybookrassemble' in p)
reg=json.load(open('toc-map.json'))
out={}; ptr=start; missed=[]
for h in reg:
    t=norm(h['text'])
    if not t: missed.append(h); continue
    found=None
    for i in range(ptr,len(npages)):
        if t in npages[i]: found=i; break
    if found is None:
        # fallback: search from body start
        for i in range(start,len(npages)):
            if t in npages[i]: found=i; break
    if found is None:
        missed.append(h); continue
    out[h['key']]=found+1
    ptr=found
json.dump(out,open('toc-pages.json','w'))
print('mapped',len(out),'of',len(reg),'start page',start+1)
for m in missed[:10]: print('MISS',m['text'])
