#!/usr/bin/env python3
exec(open('gen-diagrams.py').read().split("def chain(")[0])
TABS=[('tab-p1','PARTIE 1 · ANALYSER','2D92A8','FFFFFF'),
      ('tab-p2','PARTIE 2 · CIBLER','722F45','FFFFFF'),
      ('tab-p3','PARTIE 3 · VENDRE','C6A15B','FFFFFF'),
      ('tab-p4','PARTIE 4 · PILOTER','12475B','FFFFFF'),
      ('tab-ann','ANNEXES','F66803','FFFFFF')]
import subprocess
from PIL import Image
for name,label,bg,fg in TABS:
    html=f'''<!doctype html><html><head><meta charset="utf-8"><style>
    @font-face {{ font-family:'Poppins'; src: local('Poppins'); }}
    body{{margin:0;padding:0}}
    .tab{{writing-mode:vertical-rl;background:#{bg};color:#{fg};font-family:Poppins,Arial;font-weight:700;
         font-size:13px;letter-spacing:2.5px;width:34px;height:300px;display:flex;align-items:center;justify-content:center}}
    </style></head><body><div class="tab">{label}</div></body></html>'''
    p=f'{HTML}/{name}.html'; open(p,'w').write(html)
    png=f'{OUT}/{name}.png'
    subprocess.run([CHROME,'--headless','--no-sandbox','--disable-gpu','--hide-scrollbars',
                    f'--screenshot={png}','--window-size=34,300','--force-device-scale-factor=3',f'file://{p}'],check=True,capture_output=True)
    im=Image.open(png).convert('RGB'); im=im.crop((0,0,102,900)); im.save(png); print(name, im.size)
