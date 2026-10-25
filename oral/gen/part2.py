# Diapos 6 à 11 : offre, concurrence, enjeux et problématique, ICP, personas, solutions (v2, après revue)
from kit import *


def chip(text, bg='#FFFFFF', fg=ENCRE, border=FILET):
    return (f'<p style="font-size:24px;line-height:1.3;color:{fg};background:{bg};border:1px solid {border};'
            f'border-radius:12px;padding:10px 16px;white-space:nowrap">{text}</p>')


def offre():
    data = [('1-3 btl', 105, '≥ 35 €'), ('6 btl', 140, '23,3 €'), ('12 btl', 210, '17,5 €'),
            ('24 btl', 360, '15 €'), ('36 btl', 510, '14,2 €')]
    cols = []
    for lab, v, pb in data:
        h = round(v / 510 * 230)
        hi = lab == '24 btl'
        fill = OR if hi else '#B9D6DD'
        vc = ORF if hi else PETROLE
        extra = (f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{ORF};white-space:nowrap">Houston</p>'
                 if hi else '')
        cols.append(f'''<div style="width:150px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:6px">
{extra}{num(f'{v} €', 36, vc, 600, 'white-space:nowrap')}
<div style="width:130px;height:{h}px;background:{fill};border-radius:6px 6px 0px 0px"></div></div>''')
    labs = ''.join(f'<div style="width:150px;display:flex;flex-direction:column;align-items:center;gap:2px">'
                   f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{ORF if l == "24 btl" else GRIS}">{l}</p>'
                   f'<p style="font-size:24px;color:{ORF if l == "24 btl" else GRISD}">{pb}/btl</p></div>' for l, _, pb in data)
    left = f'''<div style="width:960px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:20px">{label('Produit phare · USA groupage DDP', SARCF)}{pill('GRILLE 2026')}</div>
<div style="height:320px;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:2px solid {FILET}">{''.join(cols)}</div>
<div style="display:flex;justify-content:space-between">{labs}</div>
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.35;color:{GRIS}">Transport HT, ~21 jours estimés hors douane · <b>+ taxes estimées par le simulateur, réglées d'avance</b> (+ 17 € de dossier DDP)</p>
</div>'''
    tri = f'''<div style="position:relative;width:640px;height:400px">
<svg style="position:absolute;left:0px;top:0px" width="640" height="400" viewBox="0 0 640 400"><defs><marker id="h" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="{SARC}"/></marker></defs>
<path d="M 140 290 L 216 112" fill="none" stroke="{SARC}" stroke-width="4" marker-end="url(#h)"/>
<path d="M 424 108 L 497 278" fill="none" stroke="{SARC}" stroke-width="4" marker-end="url(#h)"/>
<path d="M 358 345 L 290 345" fill="none" stroke="{SARC}" stroke-width="4" marker-end="url(#h)"/></svg>
<div style="position:absolute;left:170px;top:0px;width:300px;height:100px;background:{NUIT};border-radius:14px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:2px"><p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF">L’ADHÉRENT</p><p style="font-size:24px;color:{BRUME}">domaine, cave, maison</p></div>
<div style="position:absolute;left:0px;top:290px;width:280px;height:110px;background:#FFFFFF;border:2px solid {OR};border-radius:14px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:2px"><p style="font-family:{L};font-size:24px;font-weight:600;color:{ORF}">SON CLIENT FINAL</p><p style="font-size:24px;color:{GRIS}">le visiteur étranger</p></div>
<div style="position:absolute;left:360px;top:290px;width:280px;height:110px;background:{SARCF};border-radius:14px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:2px"><p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF">PLANET AURA</p><p style="font-size:24px;color:#DDEFF3">livre en DDP</p></div>
<p style="position:absolute;left:0px;top:140px;width:170px;font-size:24px;line-height:1.3;color:{ENCRE}"><b>1.</b> paie vin + transport</p>
<p style="position:absolute;left:470px;top:140px;width:170px;font-size:24px;line-height:1.3;color:{ENCRE}"><b>2.</b> nous règle par SEPA</p>
</div>'''
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:20px">
{label('Un modèle B2B2C', SARCF)}
{tri}
<p style="font-size:24px;color:{ENCRE};text-align:center"><b>3.</b> taxes estimées et réglées d’avance : pas de douane à gérer</p>
</div>'''
    chips = (f'<div style="display:flex;gap:12px">{chip("France &amp; UE dès 15 €")}{chip("Spiritueux USA, nouveauté 2026")}'
             f'{chip("Sans abonnement ni minimum")}{chip("Assurance en option : 3 %")}</div>')
    inner = f'''{header("Analyser · L'offre", 'Le client final paie, l’adhérent vend plus', SARCF)}
<div style="flex:1;display:flex;gap:64px">{left}{right}</div>
{chips}
{footer(6, 'Analyser')}'''
    return 'offre', inner, dict(gap=28)


def concurrence():
    def fam(x, y, w, h, title, names, note=None, style='', tcol=GRIS):
        n = f'<p style="font-size:24px;font-style:italic;color:{GRISD}">{note}</p>' if note else ''
        return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;border-radius:16px;padding:14px 20px;'
                f'display:flex;flex-direction:column;gap:4px;{style}">{label(title, tcol, ls=2)}'
                f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}">{names}</p>{n}</div>')
    carte = f'''<div style="position:relative;width:1000px;height:620px">
<svg style="position:absolute;left:0px;top:0px" width="1000" height="620" viewBox="0 0 1000 620"><defs><marker id="a" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="{GRISD}"/></marker></defs>
<path d="M 70 540 L 70 14" stroke="{GRISD}" stroke-width="3" fill="none" marker-end="url(#a)"/>
<path d="M 70 540 L 984 540" stroke="{GRISD}" stroke-width="3" fill="none" marker-end="url(#a)"/></svg>
{fam(724, 10, 266, 176, 'Généralistes', 'Hillebrand Gori<br>Kuehne+Nagel<br>DB Schenker', None, f'background:#E9EFF1;border:1px solid {FILET}')}
{fam(400, 150, 300, 160, 'Expressistes', 'FedEx · UPS · DHL', 'aussi nos sous-traitants', f'background:#E9EFF1;border:1px solid {FILET}')}
{fam(400, 334, 300, 180, 'Voile-cargo', 'VELA · TOWT · Grain de Sail', 'partenaires potentiels', f'border:2px dashed {GRISD}')}
<div style="position:absolute;left:90px;top:284px;width:290px;height:232px;border-radius:16px;padding:14px 20px;display:flex;flex-direction:column;gap:8px;background:#E2F0F3;border:2px solid {SARC}">{label('Spécialistes vin', SARCF, ls=2)}<p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF;background:{NUIT};border-radius:8px;padding:4px 12px;align-self:flex-start">Planet Aura</p><p style="font-size:24px;line-height:1.3;color:{ENCRE}">Dartess · Viticolis · Vinotrans · Eureka · MBE</p></div>
<p style="position:absolute;left:0px;top:0px;width:60px;font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">CA +</p>
<p style="position:absolute;left:84px;top:550px;width:300px;font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">Spécialisé vin</p>
<p style="position:absolute;left:740px;top:550px;width:240px;text-align:right;font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">Diversifié</p>
<p style="position:absolute;left:84px;top:588px;width:900px;font-size:24px;color:{GRISD}">Quatre familles, sources publiques (oct. 2026)</p>
</div>'''
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<div style="border:3px dashed {ORANGE};border-radius:20px;padding:14px 24px;display:flex;flex-direction:column;gap:4px">
{label('Concurrent n° 1, hors carte', ORANGE, ls=2)}
<p style="font-family:{T};font-size:38px;font-weight:700;color:{ENCRE}">Le statu quo</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS}">« Débrouillez-vous », la valise, La Poste</p>
</div>
<div style="background:{NUIT};border-radius:20px;padding:20px 24px;display:flex;flex-direction:column;gap:10px">
{label('Notre case', BLEU, ls=2)}
<p style="font-family:{T};font-size:28px;font-weight:700;line-height:1.2;color:#FFFFFF">Spécialiste du vin, <span style="color:{CHAMP}">intégré de bout en bout</span></p>
<div style="display:flex;align-items:center;gap:14px"><x-icon name="Verified" style="color:{CHAMP};width:36px;height:36px"></x-icon><p style="font-size:24px;color:{BRUME}">Obligation de résultat (CGS art. 2)</p></div>
<div style="display:flex;align-items:center;gap:14px"><x-icon name="Globe" style="color:{CHAMP};width:36px;height:36px"></x-icon><p style="font-size:24px;color:{BRUME}">Filiale licenciée à New York</p></div>
<div style="display:flex;align-items:center;gap:14px"><x-icon name="Settings" style="color:{CHAMP};width:36px;height:36px"></x-icon><p style="font-size:24px;color:{BRUME}">Plateforme Planet'Connect + API</p></div>
<p style="font-size:24px;line-height:1.3;color:{CHAMP};border-top:1px solid #2E5867;padding-top:10px"><b>Cap :</b> capitaliser sur ce trio, diversifier sans sacrifier les USA</p>
</div>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b>Prix :</b> 10 répondants sur 23 le jugent « moyennement compétitif », autant le jugent compétitif (2024).</p>
</div>'''
    inner = f'''{header('Analyser · La concurrence', 'Notre premier concurrent : « on se débrouille »', SARCF)}
<div style="flex:1;display:flex;gap:56px">{carte}{right}</div>
{footer(7, 'Analyser')}'''
    return 'concurrence', inner, dict(gap=36)


def enjeux():
    def tile(n, c):
        return (f'<div style="flex:1;display:flex;flex-direction:column;gap:2px">{num(n, 48, "#FFFFFF")}'
                f'<p style="font-size:24px;line-height:1.25;color:{BRUME}">{c}</p></div>')

    def frag(t):
        return (f'<div style="display:flex;gap:14px;align-items:flex-start"><div style="width:14px;height:14px;border-radius:50%;'
                f'background:#F0A879;flex:none"></div><p style="font-size:24px;line-height:1.3;color:{CLAIR}">{t}</p></div>')

    def enjeu(icon, t):
        return (f'<div style="display:flex;align-items:center;gap:20px;background:rgba(255,255,255,0.08);border-radius:14px;padding:10px 18px">'
                f'<div style="width:60px;height:60px;border-radius:50%;background:{CHAMP};display:flex;align-items:center;justify-content:center;flex:none">'
                f'<x-icon name="{icon}" style="color:{NUIT};width:34px;height:34px"></x-icon></div>'
                f'<p style="font-family:{T};font-size:32px;font-weight:700;color:#FFFFFF">{t}</p></div>')
    wave = ('<svg width="1000" height="30" viewBox="0 0 1000 30"><path d="M0 15 Q 25 3 50 15 T 100 15 T 150 15 T 200 15 T 250 15 T 300 15 '
            'T 350 15 T 400 15 T 450 15 T 500 15 T 550 15 T 600 15 T 650 15 T 700 15 T 750 15 T 800 15 T 850 15 T 900 15 T 950 15 T 1000 15" '
            f'fill="none" stroke="{BLEU}" stroke-width="3"/></svg>')
    probl = f'''<div style="display:flex;flex-direction:column;gap:8px;border-left:6px solid {CHAMP};padding-left:28px">
{label('Problématique', CHAMP)}
<p style="font-family:{T};font-size:40px;font-weight:700;line-height:1.22;color:#FFFFFF">Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente <span style="color:{CHAMP}">reproductible et mesurable</span>, pour recruter, activer et fidéliser nos adhérents ?</p>
</div>'''
    left = f'''<div style="width:1000px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:24px">{label('Ce qui se voit', BLEU)}</div>
<div style="display:flex;gap:28px">{tile('+18,7 %', 'de CA en 2026, à date')}{tile('~145', 'adhérents signés en 12 mois, pour 120 visés')}{tile('4,65/5', 'de satisfaction (2024, 23 rép.)')}</div>
{wave}
<div style="background:{NUIT};border-radius:18px;padding:18px 26px;display:flex;flex-direction:column;gap:10px">
{label('Sous la surface', '#F0A879')}
<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:10px 28px">
{frag('Une croissance née du bouche-à-oreille')}{frag('1er commercial dédié : fin 2025')}
{frag('448 prospects non qualifiés sur 710 comptes')}{frag('Activation des signés : jamais mesurée')}
{frag('64,5 % des envois vers les USA')}{frag('Pas de référentiel de vente unique')}
</div></div>
</div>'''
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:14px">
{label('Trois enjeux', BLEU)}
{enjeu('Users', 'Recruter les bons comptes')}
{enjeu('PaperPlane', 'Activer et fidéliser')}
{enjeu('Book', 'Transmettre et mesurer')}
</div>'''
    inner = f'''{header('Analyser · Diagnostic', 'Une croissance réelle, une méthode à construire', BLEU, '#FFFFFF')}
{probl}
<div style="flex:1;display:flex;gap:56px">{left}{right}</div>
{footer(8, 'Analyser', dark=True)}'''
    return 'enjeux', inner, dict(bg=PETROLE, color=CLAIR, gap=30)


def icp():
    step = lambda n, t: label(f'{n} · {t}', BORD, ls=2)
    dots_spec = [(OR, 1), (BORD, 4), (SARC, 3), (CHAMP, 1), (GRISD, 1)]
    dots = []
    for c, k in dots_spec:
        for _ in range(k):
            b = f'border:2px solid {ORF};' if c == CHAMP else ''
            dots.append(f'<div style="width:50px;height:50px;border-radius:50%;background:{c};{b}"></div>')
    leg = ''.join(f'<div style="display:flex;align-items:center;gap:10px"><div style="width:18px;height:18px;border-radius:50%;background:{c};flex:none;{"border:2px solid " + ORF if c == CHAMP else ""}"></div><p style="font-size:24px;line-height:1.25;color:{GRIS}">{t}</p></div>'
                  for c, t in [(OR, '1 agence de wine tours (n° 1)'), (BORD, '4 domaines avec œnotourisme'), (SARC, '3 caves touristiques'),
                               (CHAMP, '1 maison de champagne'), (GRISD, '1 organisateur d’événements')])
    s1 = f'''<div style="width:400px;display:flex;flex-direction:column;gap:16px">
{step(1, 'Top 10 réel')}
<div style="display:grid;grid-template-columns:repeat(5, 50px);gap:14px">{''.join(dots)}</div>
<div style="display:flex;flex-direction:column;gap:6px">{leg}</div>
{pill('CONSTATÉ', label='CONSTATÉ · 12 MOIS')}
</div>'''
    crit = ''.join(f'<div style="display:flex;gap:12px;align-items:flex-start"><p style="width:40px;height:40px;border-radius:50%;background:{BORD};color:#FFFFFF;font-family:{L};font-size:24px;font-weight:600;text-align:center;line-height:40px;flex:none">{i}</p><p style="font-size:24px;line-height:1.3;color:{ENCRE}">{t}</p></div>'
                   for i, t in enumerate(['Clientèle étrangère (&gt; 20 / semaine)', 'Bouteille à plus de 12 €',
                                          'Responsable caveau ou e-shop', 'Destinations, USA en tête', 'Saisonnalité'], 1))
    s2 = f'''<div style="width:330px;display:flex;flex-direction:column;gap:16px">
{step(2, '5 critères')}
<div style="display:flex;flex-direction:column;gap:14px">{crit}</div>
<p style="font-size:24px;color:{GRISD}">Hiérarchisés, recalibrés à 90 jours</p>
</div>'''
    eff = [('Domaines avec caveau', 60, BORD), ('Maisons de champagne', 15, '#9C5A70'), ('Œnotourisme et salons', 15, '#9C5A70'), ('Cavistes', 10, '#9C5A70')]
    rows = ''.join(f'<div style="display:flex;flex-direction:column;gap:4px"><p style="font-size:24px;color:{ENCRE}">{t}</p>'
                   f'<div style="display:flex;align-items:center;gap:10px"><div style="width:{round(v / 60 * 250)}px;height:26px;background:{c};border-radius:4px"></div>'
                   f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{BORD}">{v} %</p></div></div>' for t, v, c in eff)
    s3 = f'''<div style="width:350px;display:flex;flex-direction:column;gap:16px">
{step(3, '5 ICP')}
<div style="display:flex;flex-direction:column;gap:12px">{rows}
<div style="border:2px dashed {GRISD};border-radius:10px;padding:6px 12px"><p style="font-size:24px;color:{GRIS}">Distilleries : test 2026, hors répartition</p></div></div>
{pill('OBJECTIF', label="OBJECTIF · EFFORT")}
</div>'''
    zones = [('P1 · priorité', '75-100', 25, PETROLE), ('P2 · à développer', '55-74', 20, SARCF), ('Nurture', '35-54', 20, BLEU), ('Écarter ou veille', '&lt; 35', 35, FILET)]
    gz = ''.join(f'<div style="height:{round(v * 3.1)}px;display:flex;align-items:center;gap:14px"><div style="width:64px;height:{round(v * 3.1) - 4}px;background:{c};border-radius:4px"></div>'
                 f'<div style="display:flex;flex-direction:column"><p style="font-family:{L};font-size:24px;font-weight:600;color:{ENCRE}">{rng}</p><p style="font-size:24px;color:{GRIS}">{t}</p></div></div>'
                 for t, rng, v, c in zones)
    s4 = f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{step(4, 'Score PA-FIT')}
<div style="display:flex;flex-direction:column">{gz}</div>
<p style="font-size:24px;font-weight:700;color:{ENCRE}">Cadence dès 55 points</p>
</div>'''
    arr = f'<div style="padding-top:150px">{arrow(48, 32, BLEU)}</div>'
    dec = (f'<div style="display:flex;align-items:center;gap:20px;background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {BORD};border-radius:12px;padding:12px 22px">'
           f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{BORD};white-space:nowrap">MA DÉCISION</p><p style="font-size:26px;color:{ENCRE}"><b>60 % de l’effort sur les domaines avec caveau</b> : tout notre top 10 accueille des étrangers.</p></div>')
    inner = f'''{header('Cibler · ICP', "L'adéquation prime sur la taille", BORD, tg='MON ANALYSE')}
<div style="flex:1;display:flex;gap:22px">{s1}{arr}{s2}{arr}{s3}{arr}{s4}</div>
{dec}
{footer(9, 'Cibler')}'''
    return 'icp', inner, dict(gap=32, sect="Cibler : ICP, personas, enjeux des cibles et solutions")


def personas():
    def card(letter, name, role, need, ch, c, accent=False):
        bd = f'border:2px solid {OR}' if accent else f'border:1px solid {FILET}'
        return f'''<div style="flex:1;background:#FFFFFF;{bd};border-radius:16px;padding:12px 18px;display:flex;flex-direction:column;gap:4px">
<div style="display:flex;align-items:center;gap:14px"><p style="width:44px;height:44px;border-radius:50%;background:{c};color:#FFFFFF;font-family:{L};font-size:24px;font-weight:700;text-align:center;line-height:44px;flex:none">{letter}</p>
<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{c}">{role}</p></div>
<p style="font-size:26px;font-weight:700;line-height:1.2;color:{ENCRE}">{name}</p>
<p style="font-size:24px;line-height:1.25;color:{GRIS}">{need}</p>
<p style="font-size:24px;font-style:italic;line-height:1.25;color:{c};border-top:1px solid {FILET};padding-top:6px">{ch}</p></div>'''
    left = f'''<div style="width:1110px;display:flex;flex-direction:column;gap:10px">
{label('Au domaine : une même vente, trois rôles', BORD, ls=2)}
<div style="display:flex;gap:16px">
{card('A', 'Le vigneron-propriétaire', 'DÉCIDE', 'Veut : qu’on s’occupe de tout', 'Visite, confrère · « J’ai déjà un compte UPS »', BORD)}
{card('B', 'La responsable caveau', 'UTILISE', 'Veut : un prix en 20 secondes', 'E-mail + démo · « Mon équipe n’est pas à l’aise avec l’informatique »', SARCF)}
{card('E', 'Le client final étranger', 'PAIE', 'Demande : combien, quand, si ça casse ?', 'Au comptoir, via l’adhérent', ORF)}
</div>
{label('Ailleurs : deux autres décideurs', BORD, ls=2)}
<div style="display:flex;gap:16px">
{card('C', 'Le caviste', 'DÉCIDE VITE', 'Veut : rien à avancer, aller vite', 'Boutique, 10 h-12 h · « Mes clients ne paieront jamais ça »', '#9C5A70')}
{card('D', 'Le directeur commercial (maison de champagne)', 'EN COMITÉ', 'Veut : image et conformité', 'LinkedIn + RDV formel · « Nous avons déjà un transitaire »', PETROLE)}
</div>
</div>'''
    fig = lambda n, c: (f'<div style="flex:1;display:flex;flex-direction:column">{num(n, 52, "#FFFFFF")}'
                        f'<p style="font-size:24px;line-height:1.25;color:{BRUME}">{c}</p></div>')
    right = f'''<div style="flex:1;background:{NUIT};border-radius:20px;padding:26px 28px;display:flex;flex-direction:column;gap:16px">
{label('Mon étude · oct. 2026', CHAMP, ls=2)}
<div style="display:flex;gap:12px">{fig('70', 'contacts pro')}{fig('47', 'réponses à 3 enquêtes')}{fig('15', 'avis Google')}</div>
<div style="height:2px;background:#2E5867"></div>
<div style="display:flex;align-items:baseline;gap:14px">{num('5/5', 80, CHAMP)}<p style="font-size:26px;color:#FFFFFF">confirmés</p></div>
<p style="font-size:26px;line-height:1.3;color:{CLAIR}"><b>3 ajustements</b> · <b>1 angle mort :</b> l’ADV, utilisatrice au quotidien</p>
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.3;color:#8FB0BA">Échanges écrits ; entretiens prévus au T1 2027</p>
</div>'''
    inner = f'''{header('Cibler · Personas', 'Qui décide, qui utilise, qui paie', BORD, tg='MON ÉTUDE')}
<div style="flex:1;display:flex;gap:40px">{left}{right}</div>
{footer(10, 'Cibler')}'''
    return 'personas', inner, dict(gap=36)


def solutions():
    rows = [('Domaine avec caveau', 'Ventes perdues avec les étrangers', 'Simulateur au comptoir + groupage DDP', '210 € de transport / 12 btl'),
            ('Maison de champagne', 'Certificat CIVC oublié, colis bloqué', 'Certificat géré à chaque envoi', '15 € HT par envoi'),
            ('Caviste', 'Ni temps, ni trésorerie', 'Order form : le client paie son transport', '3 min de saisie'),
            ('Œnotourisme, salons', "Une fin d'expérience frustrante", 'Partenariat de recommandation', 'n° 1 du top 10'),
            ('Distillerie', 'Aucune solution export B2C', 'Spiritueux USA en DDP (2026)', '6 L par personne')]
    W = [290, 400, 44, 470, 340]
    head = (f'<div style="display:flex;gap:30px;padding:0px 0px 10px;border-bottom:2px solid {FILET}">'
            + ''.join(f'<p style="width:{w}px;font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{GRISD}">{t}</p>'
                      for t, w in zip(['CIBLE', 'DOULEUR', '', 'NOTRE RÉPONSE', 'REPÈRE'], W)) + '</div>')
    body = ''
    for c, d, r, k in rows:
        body += (f'<div style="flex:1;display:flex;gap:30px;align-items:center;border-bottom:1px solid {FILET}">'
                 f'<p style="width:{W[0]}px;font-size:26px;font-weight:700;line-height:1.25;color:{BORD}">{c}</p>'
                 f'<p style="width:{W[1]}px;font-size:26px;line-height:1.3;color:{GRIS}">{d}</p>'
                 f'<div style="width:{W[2]}px">{arrow(44, 26, SARC, 3)}</div>'
                 f'<p style="width:{W[3]}px;font-size:26px;line-height:1.3;color:{ENCRE}">{r}</p>'
                 f'<p style="width:{W[4]}px;font-family:{L};font-size:26px;font-weight:600;line-height:1.2;color:{PETROLE}">{k}</p></div>')
    table = f'<div style="flex:1;display:flex;flex-direction:column">{head}{body}</div>'
    refus = ''.join(f'<p style="font-size:26px;color:{CLAIR};white-space:nowrap"><b><span style="color:#F0A879">×</span></b> {t}</p>'
                    for t in ['Délais garantis', 'Crédit fournisseur', '100 % B2B sans étude', 'Caisses bois en colis', '&gt; 21° hors spiritueux USA'])
    band = f'''<div style="background:{NUIT};border-radius:18px;padding:18px 28px;display:flex;align-items:center;gap:28px">
<div style="display:flex;flex-direction:column;gap:2px;width:250px">{label('Ce que nous refusons', '#F0A879', ls=2)}<p style="font-size:24px;font-style:italic;color:{CHAMP}">à dire d’emblée</p></div>
<div style="flex:1;display:flex;flex-wrap:wrap;gap:10px 34px">{refus}</div></div>'''
    inner = f'''{header('Cibler · Enjeux et solutions', 'À chaque cible, sa douleur et sa réponse', BORD)}
{table}
{band}
{footer(11, 'Cibler')}'''
    return 'solutions', inner, dict(gap=30)
