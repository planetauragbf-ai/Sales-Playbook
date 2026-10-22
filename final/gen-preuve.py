#!/usr/bin/env python3
# Hiérarchie de preuve - pyramide 4 niveaux (source : content-emma/F.md)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

LEVELS = [
    ('NIVEAU 1', 'Contrat signé, CRM, finance, preuve opérationnelle',
     'Opposable - utilisable en proposition et en engagement client', '#12475B', '#fff', 78),
    ('NIVEAU 2', 'Source publique primaire datée (FEVS, OIV, douanes&hellip;)',
     'Argumentaire marché - toujours citer la source et l&rsquo;année', '#20768B', '#fff', 86),
    ('NIVEAU 3', 'Livrable interne documenté (étude, plan, analyse)',
     'Usage interne - à requalifier en niveau 1 ou 2 avant diffusion', '#7FA6B4', '#fff', 93),
    ('NIVEAU 4', 'Hypothèse de travail',
     'Toujours étiquetée comme telle - jamais présentée comme un fait', '#D9E8ED', '#12475B', 100),
]
bars = ''
for tag, name, usage, bg, fg, w in LEVELS:
    sub = fg if fg != '#fff' else '#D7E5EA'
    bars += f'''<div class="bar" style="background:{bg};width:{w}%">
      <div class="tag" style="color:{fg}">{tag}</div>
      <div class="tx"><span class="nm" style="color:{fg}">{name}</span>
      <span class="us" style="color:{sub}">&mdash; {usage}</span></div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:14px 16px 10px;font-family:Inter,Arial,sans-serif;background:#fff;width:896px;box-sizing:border-box}}
h1{{font-size:26px;font-weight:800;color:#12475B;margin:0 0 10px;text-align:center}}
.pyr{{display:flex;flex-direction:column;align-items:center;gap:6px}}
.bar{{display:flex;align-items:center;border-radius:8px;padding:8px 14px;box-sizing:border-box}}
.tag{{font-size:22px;font-weight:800;letter-spacing:1px;white-space:nowrap;margin-right:14px;
     border-right:2px solid rgba(255,255,255,.45);padding-right:12px;align-self:stretch;display:flex;align-items:center}}
.bar:last-child .tag{{border-right-color:rgba(18,71,91,.3)}}
.tx{{flex:1;line-height:1.24}}
.nm{{font-size:22.5px;font-weight:700}}
.us{{font-size:22px;font-weight:400}}
.foot{{font-size:22px;color:#3A4A50;font-style:italic;text-align:center;margin-top:8px}}
</style></head><body>
<h1>La hiérarchie de preuve : que citer en premier</h1>
<div class="pyr">{bars}</div>
<div class="foot">Un chiffre sans niveau de preuve identifié ne sort pas.</div>
</body></html>'''

p = f'{HTML}/d14_preuve.html'
open(p, 'w').write(html)
png = f'{OUT}/d14_preuve.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=900,700', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image, ImageChops
im = Image.open(png).convert('RGB')
bg = Image.new('RGB', im.size, 'white')
bb = ImageChops.difference(im, bg).getbbox()
if bb:
    pad = 8
    bb = (max(0, bb[0]-pad), max(0, bb[1]-pad), min(im.size[0], bb[2]+pad), min(im.size[1], bb[3]+pad))
    im = im.crop(bb)
im.save(png)
print('d14_preuve:', Image.open(png).size)
