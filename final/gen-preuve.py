#!/usr/bin/env python3
# Hiérarchie de preuve - pyramide 4 niveaux (source : content-emma/F.md)
exec(open('gen-diagrams.py').read().split("def chain(")[0])
import subprocess

LEVELS = [
    ('NIVEAU 1', 'Contrat signé, CRM, finance, preuve opérationnelle',
     'Opposable - utilisable en proposition et en engagement client', '#12475B', '#fff', 52),
    ('NIVEAU 2', 'Source publique primaire datée (FEVS, OIV, douanes&hellip;)',
     'Argumentaire marché - toujours citer la source et l&rsquo;année', '#20768B', '#fff', 68),
    ('NIVEAU 3', 'Livrable interne documenté (étude, plan, analyse)',
     'Usage interne - à requalifier en niveau 1 ou 2 avant diffusion', '#7FA6B4', '#fff', 84),
    ('NIVEAU 4', 'Hypothèse de travail',
     'Toujours étiquetée comme telle - jamais présentée comme un fait', '#D9E8ED', '#12475B', 100),
]
bars = ''
for tag, name, usage, bg, fg, w in LEVELS:
    sub = fg if fg != '#fff' else '#D7E5EA'
    bars += f'''<div class="bar" style="background:{bg};width:{w}%">
      <div class="tag" style="color:{fg}">{tag}</div>
      <div class="tx"><div class="nm" style="color:{fg}">{name}</div>
      <div class="us" style="color:{sub}">{usage}</div></div>
    </div>'''

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>
body{{margin:0;padding:20px 24px 16px;font-family:Inter,Arial,sans-serif;background:#fff;width:976px;box-sizing:border-box}}
h1{{font-size:21px;font-weight:800;color:#12475B;margin:0 0 16px;text-align:center}}
.pyr{{display:flex;flex-direction:column;align-items:center;gap:6px}}
.bar{{display:flex;align-items:center;border-radius:7px;padding:11px 20px;box-sizing:border-box;min-height:60px}}
.tag{{font-size:13px;font-weight:800;letter-spacing:1.4px;white-space:nowrap;margin-right:18px;
     border-right:2px solid rgba(255,255,255,.45);padding-right:16px;align-self:stretch;display:flex;align-items:center}}
.bar:last-child .tag{{border-right-color:rgba(18,71,91,.3)}}
.tx{{flex:1}}
.nm{{font-size:14.5px;font-weight:700;line-height:1.3}}
.us{{font-size:12px;line-height:1.35;margin-top:3px}}
.foot{{font-size:12px;color:#3A4A50;font-style:italic;text-align:center;margin-top:12px}}
</style></head><body>
<h1>La hiérarchie de preuve : que citer en premier</h1>
<div class="pyr">{bars}</div>
<div class="foot">Un chiffre sans niveau de preuve identifié ne sort pas.</div>
</body></html>'''

p = f'{HTML}/d14_preuve.html'
open(p, 'w').write(html)
png = f'{OUT}/d14_preuve.png'
subprocess.run([CHROME, '--headless', '--no-sandbox', '--disable-gpu', '--hide-scrollbars',
                f'--screenshot={png}', '--window-size=1000,420', '--force-device-scale-factor=2', f'file://{p}'],
               check=True, capture_output=True)
from PIL import Image
im = Image.open(png).convert('RGB')
g = im.convert('L').point(lambda x: 0 if x > 250 else 255)
bb = g.getbbox()
im.crop((0, 0, im.size[0], min(im.size[1], bb[3] + 20))).save(png)
print('d14_preuve:', Image.open(png).size)
