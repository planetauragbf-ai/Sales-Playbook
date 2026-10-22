#!/usr/bin/env python3
# Visuels concurrence + matrices (charte Planet Aura) : HTML/SVG -> PNG
import math
exec(open('gen-diagrams.py').read().split("def chain(")[0])

NAVY='#1B3A4B'; TEAL='#1B7F8C'; DARK='#12414A'; ORANGE='#E87722'; RED='#C0392B'; GREEN='#2E8B57'; LIGHT='#E8F1F4'; GRAY='#5A6B75'

def radar_svg(axes, series, vmax, size=760, rings=None, label_fs=19, pad=330,
              W=None, H=None, label_rf=1.14, ring_fs=14, sub_fs=None, paren_sub=False):
    # Les nouveaux paramètres gardent par défaut l'ancien comportement (d10_porter inchangé).
    cx=cy=size/2+0; R=size/2-20
    if W is None: W=size+2*pad
    if H is None: H=size+90
    cxx=W/2; cyy=H/2+10
    if sub_fs is None: sub_fs=label_fs-4
    lh = label_fs+4 if paren_sub else label_fs+2
    n=len(axes)
    def pt(i,v):
        a=-math.pi/2 + i*2*math.pi/n
        return (cxx + math.cos(a)*R*v/vmax, cyy + math.sin(a)*R*v/vmax)
    s=f'<svg width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" font-family="DejaVu Sans,Arial">'
    rings = rings or list(range(1,vmax+1))
    for r in rings:
        ring=' '.join(f'{pt(i,r)[0]:.1f},{pt(i,r)[1]:.1f}' for i in range(n))
        s+=f'<polygon points="{ring}" fill="none" stroke="#D8E4E9" stroke-width="1.3" stroke-dasharray="4 4"/>'
        s+=f'<text x="{cxx+6}" y="{cyy - R*r/vmax - 4}" font-size="{ring_fs}" fill="{GRAY}">{r}</text>'
    for i,ax in enumerate(axes):
        x,y=pt(i,vmax)
        s+=f'<line x1="{cxx}" y1="{cyy}" x2="{x:.1f}" y2="{y:.1f}" stroke="#C9D8DE" stroke-width="1.3"/>'
        lx,ly=pt(i,vmax*label_rf)
        anchor='middle'
        if lx>cxx+R*0.35: anchor='start'
        if lx<cxx-R*0.35: anchor='end'
        if paren_sub and anchor=='middle' and ly<cyy: ly-=20  # écarte le libellé du sommet des graduations
        lines=ax.split('\n')
        for j,ln in enumerate(lines):
            is_sub = ln.startswith('(') if paren_sub else j>0
            w='400' if is_sub else '700'; fs=sub_fs if is_sub else label_fs
            col=GRAY if is_sub else NAVY
            s+=f'<text x="{lx:.1f}" y="{ly+j*lh-(len(lines)-1)*(label_fs/2):.1f}" font-size="{fs}" font-weight="{w}" fill="{col}" text-anchor="{anchor}">{ln}</text>'
    for name,vals,color,fill,wd in series:
        poly=' '.join(f'{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}' for i,v in enumerate(vals))
        s+=f'<polygon points="{poly}" fill="{color}" fill-opacity="{fill}" stroke="{color}" stroke-width="{wd}" stroke-linejoin="round"/>'
        for i,v in enumerate(vals):
            x,y=pt(i,v); s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 if wd>2 else 3}" fill="{color}"/>'
    s+='</svg>'
    return s

def legend(items, fs=17, gap=26, wrap=False):
    fw=';flex-wrap:wrap;row-gap:10px' if wrap else ''
    sw,sh=(26,5) if fs==17 else (int(fs*1.4),6)
    h=f'<div class="row" style="gap:{gap}px;margin-top:4px;justify-content:center{fw}">'
    for name,color,strong in items:
        w='800' if strong else '600'
        h+=f'<div class="row" style="gap:8px"><span style="display:inline-block;width:{sw}px;height:{sh}px;border-radius:3px;background:{color}"></span><span style="font-size:{fs}px;font-weight:{w};color:{NAVY}">{name}</span></div>'
    return h+'</div>'

# ---------- 1. Radar 7P ----------
AX7=['Spécialisation vin\n(Produit)','Initiative\nbas-carbone\n(Preuves physiques)','Conseil\npersonnalisé\n(Personnel)','Couverture\ninternationale\n(Distribution)','Rapidité de\nlivraison\n(Processus)','Compétitivité\nprix perçue\n(Prix)','Visibilité RSE\n(Communication)']
S7=[('Vinotrans',[3,1,2,3,3,4,2],NAVY,0,1.8),
    ('Dartess',[4,2,3,4,2,2,3],RED,0,1.8),
    ('Viticolis',[4,1,2,2,3,3,2],TEAL,0,1.8),
    ('Eureka Logistique',[3,3,3,3,2,2,3],GREEN,0,1.8),
    ('Planet Aura',[5,5,4,3,3,2,4],ORANGE,0.20,3.2)]
html='<style>body{width:960px}</style>'
html+='<div class="kicker" style="font-size:26px;letter-spacing:.06em;line-height:1.35;max-width:850px;margin:0 auto 14px">LE FACE-À-FACE DES SPÉCIALISTES - ANALYSE 7P (SCORES INTERNES 0-5)</div>'
html+='<div style="text-align:center">'+radar_svg(AX7,S7,5,size=440,label_fs=27,W=900,H=560,label_rf=1.12,ring_fs=26,sub_fs=26,paren_sub=True)+'</div>'
html+=legend([('Planet Aura',ORANGE,True),('Viticolis',TEAL,False),('Vinotrans',NAVY,False),('Dartess',RED,False),('Eureka Logistique',GREEN,False)], fs=26, gap=22, wrap=True)
shot('d10_radar7p', html, width=960)

# ---------- 2. Radar Porter ----------
AXP=['Menace des\nnouveaux entrants','Pouvoir des\nfournisseurs','Pouvoir des\nclients','Menace des\nsubstituts','Intensité\nconcurrentielle']
SP=[('Pression sur le secteur',[2,2.5,2.5,1.5,3],NAVY,0.10,2.2),
    ('Exposition résiduelle Planet Aura',[1,1.5,2,1,2],ORANGE,0.25,3.2)]
html='<div class="kicker">LES 5 FORCES DE PORTER - PRESSION DU SECTEUR VS EXPOSITION PLANET AURA (0-3)</div>'
html+='<div style="text-align:center">'+radar_svg(AXP,SP,3,size=640,label_fs=20)+'</div>'
html+=legend([('Pression sur le secteur',NAVY,False),('Exposition résiduelle Planet Aura (après parades)',ORANGE,True)])
shot('d10_porter', html, width=1360)
