#!/usr/bin/env python3
# Visuels concurrence + matrices (charte Planet Aura) : HTML/SVG -> PNG
import math
exec(open('gen-diagrams.py').read().split("def chain(")[0])

NAVY='#1B3A4B'; TEAL='#1B7F8C'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'; LIGHT='#E8F1F4'; GRAY='#5A6B75'

def radar_svg(axes, series, vmax, size=760, rings=None, label_fs=19, pad=330):
    cx=cy=size/2+0; R=size/2-20
    W=size+2*pad; H=size+90
    cxx=W/2; cyy=H/2+10
    n=len(axes)
    def pt(i,v):
        a=-math.pi/2 + i*2*math.pi/n
        return (cxx + math.cos(a)*R*v/vmax, cyy + math.sin(a)*R*v/vmax)
    s=f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans,Arial">'
    rings = rings or list(range(1,vmax+1))
    for r in rings:
        ring=' '.join(f'{pt(i,r)[0]:.1f},{pt(i,r)[1]:.1f}' for i in range(n))
        s+=f'<polygon points="{ring}" fill="none" stroke="#D8E4E9" stroke-width="1.3" stroke-dasharray="4 4"/>'
        s+=f'<text x="{cxx+6}" y="{cyy - R*r/vmax - 4}" font-size="14" fill="{GRAY}">{r}</text>'
    for i,ax in enumerate(axes):
        x,y=pt(i,vmax)
        s+=f'<line x1="{cxx}" y1="{cyy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#C9D8DE" stroke-width="1.3"/>'
        lx,ly=pt(i,vmax*1.14)
        anchor='middle'
        if lx>cxx+R*0.35: anchor='start'
        if lx<cxx-R*0.35: anchor='end'
        lines=ax.split('\n')
        for j,ln in enumerate(lines):
            w='700' if j==0 else '400'; fs=label_fs if j==0 else label_fs-4
            col=NAVY if j==0 else GRAY
            s+=f'<text x="{lx:.1f}" y="{ly+j*(label_fs+2)-(len(lines)-1)*(label_fs/2):.1f}" font-size="{fs}" font-weight="{w}" fill="{col}" text-anchor="{anchor}">{ln}</text>'
    for name,vals,color,fill,wd in series:
        poly=' '.join(f'{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}' for i,v in enumerate(vals))
        s+=f'<polygon points="{poly}" fill="{color}" fill-opacity="{fill}" stroke="{color}" stroke-width="{wd}" stroke-linejoin="round"/>'
        for i,v in enumerate(vals):
            x,y=pt(i,v); s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 if wd>2 else 3}" fill="{color}"/>'
    s+='</svg>'
    return s

def legend(items):
    h='<div class="row" style="gap:26px;margin-top:4px;justify-content:center">'
    for name,color,strong in items:
        w='800' if strong else '600'
        h+=f'<div class="row" style="gap:8px"><span style="display:inline-block;width:26px;height:5px;border-radius:3px;background:{color}"></span><span style="font-size:17px;font-weight:{w};color:{NAVY}">{name}</span></div>'
    return h+'</div>'

# ---------- 1. Radar 7P ----------
AX7=['Spécialisation vin\n(Produit)','Initiative bas-carbone\n(Preuves physiques)','Conseil personnalisé\n(Personnel)','Couverture internationale\n(Distribution)','Rapidité de livraison\n(Processus)','Compétitivité prix perçue\n(Prix)','Visibilité RSE\n(Communication)']
S7=[('Vinotrans',[3,1,2,3,3,4,2],NAVY,0,1.8),
    ('Dartess',[4,2,3,4,2,2,3],RED,0,1.8),
    ('Viticolis',[4,1,2,2,3,3,2],TEAL,0,1.8),
    ('Eureka Logistique',[3,3,3,3,2,2,3],GREEN,0,1.8),
    ('Planet Aura',[5,5,4,3,3,2,4],ORANGE,0.20,3.2)]
html='<div class="kicker">LE FACE-À-FACE DES SPÉCIALISTES - ANALYSE 7P (SCORES INTERNES 0-5)</div>'
html+='<div style="text-align:center">'+radar_svg(AX7,S7,5)+'</div>'
html+=legend([('Planet Aura',ORANGE,True),('Viticolis',TEAL,False),('Vinotrans',NAVY,False),('Dartess',RED,False),('Eureka Logistique',GREEN,False)])
shot('d10_radar7p', html, width=1460)

# ---------- 2. Radar Porter ----------
AXP=['Menace des\nnouveaux entrants','Pouvoir des\nfournisseurs','Pouvoir des\nclients','Menace des\nsubstituts','Intensité\nconcurrentielle']
SP=[('Pression sur le secteur',[2,2.5,2.5,1.5,3],NAVY,0.10,2.2),
    ('Exposition résiduelle Planet Aura',[1,1.5,2,1,2],ORANGE,0.25,3.2)]
html='<div class="kicker">LES 5 FORCES DE PORTER - PRESSION DU SECTEUR VS EXPOSITION PLANET AURA (0-3)</div>'
html+='<div style="text-align:center">'+radar_svg(AXP,SP,3,size=640,label_fs=20)+'</div>'
html+=legend([('Pression sur le secteur',NAVY,False),('Exposition résiduelle Planet Aura (après parades)',ORANGE,True)])
shot('d10_porter', html, width=1360)
