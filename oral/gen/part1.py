# Diapos 1 à 5 : couverture, accroche, sommaire, marché, entreprise (v2, après revue)
from kit import *

LOGO_MARK_W = '/_blob/8b40700e136fb4e2e66480f214bc3ee5'
LOGO_EURIDIS = '/_blob/ef3824102959481bdc56ec96f10cd910'
WORLDMAP = '/_blob/3b72dc2bb8ee61fc949e4287dc8c5fe1'
TEAM = '/_blob/e380ba79515a0a279a48e9fa24da0591'


def cover():
    inner = f'''<img src="{WORLDMAP}" alt="" style="position:absolute;left:1340px;top:470px;width:560px;height:370px;object-fit:contain;opacity:0.32">
<div style="flex:1;display:flex;align-items:center;gap:88px">
<img src="{LOGO_MARK_W}" alt="Logo Planet Aura : une bouteille et un avion" style="width:330px;height:440px;object-fit:contain">
<div style="display:flex;flex-direction:column;gap:28px;width:1100px">
{eyebrow('Un grand vin mérite un grand voyage', CHAMP)}
<h1 style="font-family:{T};font-size:120px;font-weight:700;line-height:1.02;letter-spacing:-1px;color:#FFFFFF">Sales Playbook<br><span style="color:{CHAMP}">Planet Aura</span></h1>
<p style="font-family:{T};font-style:italic;font-size:44px;line-height:1.2;color:{BLEU}">De la première accroche au premier envoi</p>
</div>
</div>
<div style="display:flex;align-items:flex-end;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;gap:6px">
<p style="font-size:32px;font-weight:600;color:#FFFFFF">Emma Soares Britschgy</p>
<p style="font-size:24px;color:{BRUME}">Chargée de projets &amp; développement · Mastère Marketing &amp; Digital Business, promotion 547 (2024-2027)</p>
<p style="font-size:24px;color:{BRUME}">Tutrice : Floriane Février · Suivi académique : Thibaut du Cleuziou</p>
<p style="font-size:24px;color:#8FB0BA">Document confidentiel : diffusion interne Planet Aura et jury Euridis</p>
</div>
<div style="background:#FFFFFF;border-radius:14px;padding:16px 24px"><img src="{LOGO_EURIDIS}" alt="Euridis Business School" style="width:300px;height:56px;object-fit:contain"></div>
</div>'''
    return 'cover', inner, dict(bg=NUIT, color='#FFFFFF', pad='112px 128px 96px', gap=24,
                                 sect="Accroche, sommaire et parcours : pourquoi un Sales Playbook pour Planet Aura")


def accroche():
    inner = f'''{eyebrow("Ce qu'on entend au caveau", BLEU)}
<p style="font-family:{T};font-style:italic;font-size:60px;line-height:1.22;color:{CLAIR};width:1560px">« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. »</p>
<div style="flex:1"></div>
<div style="display:flex;flex-direction:column;gap:14px">
{bottles(2)}
<div style="display:flex;gap:24px;align-items:flex-start">
<div style="width:116px;border-top:3px solid {CHAMP};padding-top:8px;display:flex;justify-content:center">{num('2', 56, CHAMP)}</div>
<div style="flex:1;border-top:3px solid #3F6B78;padding-top:8px;display:flex;justify-content:center;align-items:baseline;gap:18px">{num('22', 56, BLEU)}<p style="font-size:30px;color:{BRUME}">bouteilles jamais vendues</p></div>
</div>
</div>
<div style="flex:1"></div>
<div style="display:flex;align-items:flex-end;gap:64px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
{label('La question qui bloque la vente', '#8FB0BA')}
<p style="font-family:{T};font-size:52px;line-height:1.15;color:{CHAMP}">« Et comment je fais pour le rapporter chez moi ? »</p>
</div>
<div style="width:600px;border-left:4px solid {SARC};padding:6px 0px 6px 28px;display:flex;flex-direction:column;gap:8px">
{label('Notre pourquoi', '#8FB0BA')}
<p style="font-size:28px;line-height:1.35;color:{BRUME}">Lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu'il soit.</p>
</div>
</div>'''
    return 'accroche', inner, dict(bg=NUIT, color=CLAIR, pad='112px 128px 104px', gap=24)


def sommaire():
    cols = [
        ('01', 'Analyser', SARCF, SARC, 'Un spécialiste du vin dans un marché qui se durcit', 'Marché · entreprise · offre · concurrence', 'Introduction et diagnostic', 'd’où la problématique'),
        ('02', 'Cibler', BORD, BORD, 'Viser ceux qui reçoivent des étrangers', 'ICP · personas · solutions', 'Parties 8 à 10', 'enjeu : recruter'),
        ('03', 'Vendre', ORF, OR, 'Du premier appel au premier envoi', 'Processus · tunnels SPIN · objections', 'Partie 11', 'enjeu : activer, fidéliser'),
        ('04', 'Piloter', PETROLE, PETROLE, "Outiller l'équipe, mesurer ce qui compte", 'Ressources · Sales Ops · indicateurs', 'Parties 12 à 14', 'enjeu : transmettre, mesurer'),
    ]
    blocks = []
    for n, name, c, road, title, sub, cdc, enj in cols:
        blocks.append(f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{num(n, 84, c)}
<div style="height:10px;background:{road};border-radius:5px"></div>
{label(name, c, ls=4)}
<p style="font-family:{T};font-size:38px;font-weight:700;line-height:1.15;color:{ENCRE}">{title}</p>
<p style="font-size:24px;line-height:1.4;color:{GRIS}">{sub}</p>
<p style="font-size:24px;line-height:1.35;color:{GRISD}">{cdc}<br><b><span style="color:{c}">{enj}</span></b></p>
</div>''')
    blocks.append(f'''<div style="width:300px;display:flex;flex-direction:column;gap:16px">
<div style="height:88px;display:flex;align-items:center">{arrow(120, 64, OR, 6)}</div>
<div style="height:10px;border-top:4px dashed {OR}"></div>
{label('Et après', ORF, ls=4)}
<p style="font-family:{T};font-size:38px;font-weight:700;line-height:1.15;color:{ENCRE}">Ce que le playbook change, et la suite</p>
<p style="font-size:24px;line-height:1.4;color:{GRIS}">Synthèse · ouverture</p>
</div>''')
    defin = (f'<div style="display:flex;align-items:center;gap:18px;border-top:1px solid {FILET};padding-top:18px">'
             f'{label("Sales Playbook", PETROLE, ls=3)}<p style="font-size:26px;color:{GRIS}">le référentiel opérationnel de vente d’une équipe : '
             f'diagnostic, cibles, offres, processus, scripts et indicateurs</p></div>')
    inner = f'''{header('Le parcours', 'Quatre étapes, du caveau au premier envoi', SARCF)}
<div style="flex:1"></div>
<div style="display:flex;gap:40px">{''.join(blocks)}</div>
<div style="flex:1"></div>
{defin}
{footer(3)}'''
    return 'sommaire', inner, dict(gap=24)


C2 = "<b>64,5 % de nos envois</b> partent aux USA : notre risque n° 1. Leur complexité nous protège aussi."


def marche():
    def head(lbl, value, unit, cap):
        u = f'<p style="font-family:{L};font-size:40px;font-weight:600;color:{PETROLE}">{unit}</p>' if unit else ''
        return f'''{label(lbl, SARCF)}
<div style="display:flex;align-items:baseline;gap:12px">{num(value, 88, PETROLE)}{u}</div>
<p style="font-size:28px;line-height:1.3;color:{GRIS}">{cap}</p>'''

    c1 = f'''<div style="display:flex;flex-direction:column;gap:14px">
{head('Moins de volume', '208', 'Mhl', 'de vin consommés dans le monde en 2025 (−2,7 %)')}
<div style="display:flex;flex-direction:column;gap:8px;padding-top:6px">
<div style="display:flex;align-items:center;gap:14px"><p style="width:70px;font-size:24px;color:{GRISD}">2024</p><div style="width:360px;height:26px;background:#B9D6DD;border-radius:4px"></div><p style="font-size:24px;color:{GRIS}">214</p></div>
<div style="display:flex;align-items:center;gap:14px"><p style="width:70px;font-size:24px;color:{GRISD}">2025</p><div style="width:350px;height:26px;background:{SARCF};border-radius:4px"></div><p style="font-size:24px;font-weight:700;color:{PETROLE}">208</p></div>
</div>
<div style="flex:1"></div>
<p style="font-size:24px;color:{GRISD}">OIV, mai 2026</p>
</div>'''
    c2 = f'''<div style="display:flex;flex-direction:column;gap:14px">
{head('Le premier marché vacille', '−21 %', '', 'exports français de vins et spiritueux vers les USA en 2025 (~3 Md€)')}
<div style="position:relative;width:520px;height:82px">
<div style="position:absolute;left:12px;top:15px;width:470px;height:4px;background:#B9D6DD"></div>
<div style="position:absolute;left:4px;top:7px;width:20px;height:20px;border-radius:50%;background:{ORANGE}"></div>
<div style="position:absolute;left:276px;top:7px;width:20px;height:20px;border-radius:50%;background:{SARCF}"></div>
<p style="position:absolute;left:0px;top:36px;width:270px;font-size:24px;color:{GRIS}">Droits US : <b>15 %</b> dès août 2025</p>
<p style="position:absolute;left:272px;top:36px;width:250px;font-size:24px;color:{GRIS}"><b>10 %</b> depuis février 2026</p>
</div>
<div style="flex:1"></div>
<p style="font-size:24px;color:{GRISD}">FEVS, févr. 2026 · Hillebrand Gori, févr. 2026</p>
</div>'''
    c3 = f'''<div style="display:flex;flex-direction:column;gap:14px">
{head('Plus de visiteurs', '5,4 M', '', 'œnotouristes étrangers dans nos vignobles en 2023 (+29 % vs 2016)')}
<div style="display:flex;flex-direction:column;gap:8px;padding-top:6px">
<div style="display:flex;width:500px;height:40px;border-radius:6px;overflow:hidden"><div style="flex:60;background:{BORD};display:flex;align-items:center;padding:0px 14px"><p style="font-size:24px;font-weight:600;color:#FFFFFF">60 % en vin</p></div><div style="flex:40;background:#EADDE2"></div></div>
<p style="font-size:24px;color:{GRIS}">sur 207 € dépensés par réservation au domaine</p>
</div>
<div style="flex:1"></div>
<p style="font-size:24px;color:{GRISD}">Atout France · Winalist, données 2025</p>
</div>'''

    def card(txt):
        return (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-top:6px solid {SARC};border-radius:12px;'
                f'padding:16px 26px;display:flex;flex-direction:column;gap:6px">{label("Pour Planet Aura", SARCF, ls=2)}'
                f'<p style="font-size:28px;line-height:1.3;color:{ENCRE}">{txt}</p></div>')
    inner = f'''{header('Analyser · Le marché', "Le marché se durcit, et c'est notre terrain", SARCF)}
<div style="flex:1;display:grid;grid-template-columns:repeat(3, 1fr);grid-template-rows:1fr auto;gap:22px 56px">
{c1}{c2}{c3}
{card('Moins de volume, une valeur qui résiste : la sécurité se vend')}
{card(C2)}
{card('Le caveau devient un canal international : notre gisement')}
</div>
{footer(4, 'Analyser')}'''
    return 'marche', inner, dict(gap=40, sect="Analyser : le marché, l'entreprise, l'offre, la concurrence et la problématique")


def entreprise():
    data = [('2021', 246637, '247 k€'), ('2022', 800065, '800 k€'), ('2023', 910505, '911 k€'),
            ('2024', 1029570, '1,03 M€'), ('2025', 1148961, '1,15 M€'), ('2026', 991568, '992 k€')]
    H = 270.0
    bars = []
    for y, v, lab in data:
        h = round(v / 1148961 * H)
        cw = 180 if y == '2026' else 112
        if y == '2026':
            fill = f'background:repeating-linear-gradient(45deg, {SARC} 0px, {SARC} 9px, #B9D6DD 9px, #B9D6DD 18px)'
            top = f'<p style="font-size:24px;font-weight:600;line-height:1.2;text-align:center;color:{SARCF}">+18,7 %<br><span style="color:{GRISD}">vs 9 mois 2025</span></p>'
        elif y == '2025':
            fill = f'background:{PETROLE}'
            top = f'<p style="font-size:24px;font-weight:600;color:{SARCF};white-space:nowrap">+11,6 %</p>'
        else:
            fill = f'background:{SARC}'
            top = ''
        bars.append(f'''<div style="width:{cw}px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:6px">
{top}<p style="font-family:{L};font-size:26px;font-weight:600;color:{ENCRE};white-space:nowrap">{lab}</p>
<div style="width:112px;height:{h}px;{fill};border-radius:6px 6px 0px 0px"></div>
</div>''')
    labels = ''.join(f'<p style="width:112px;text-align:center;font-family:{L};font-size:24px;font-weight:600;color:{GRIS}">{y}</p>'
                     for y, _, _ in data[:5])
    labels += f'<p style="width:180px;text-align:center;font-family:{L};font-size:24px;font-weight:600;color:{GRIS};line-height:1.15">2026<br><span style="color:{GRISD}">janv.-sept.</span></p>'
    chart = f'''<div style="width:900px;display:flex;flex-direction:column;gap:10px">
<div style="position:relative;height:430px;display:flex;align-items:flex-end;justify-content:space-between;border-bottom:2px solid {FILET}">
<div style="position:absolute;left:0px;top:0px;width:420px;display:flex;flex-direction:column;gap:10px">
{num('×4,7', 88, ORF)}
<p style="font-size:24px;color:{GRIS}">chiffre d'affaires, de 2021 à 2025</p>
</div>
{''.join(bars)}
</div>
<div style="display:flex;justify-content:space-between">{labels}</div>
<div style="flex:1"></div>
<p style="font-size:26px;line-height:1.35;color:{ENCRE}">2025 : <b>+11,6 %</b>, quand l'export français de vins et spiritueux recule de 7,9 % : <b>à contre-courant</b>.</p>
<p style="font-size:24px;color:{GRISD}">Dashboards Planet'Connect au 24/09/2026 · FEVS, févr. 2026</p>
</div>'''
    pole = lambda t, n, c=SARCF, bd=FILET: (f'<p style="font-size:24px;color:{ENCRE};background:#FFFFFF;border:1px solid {bd};border-radius:999px;'
                                           f'padding:6px 16px;white-space:nowrap"><b><span style="color:{c}">{t}</span></b> · {n}</p>')
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{label('Commissionnaire de transport', SARCF)}
<p style="font-family:{T};font-size:34px;font-weight:700;line-height:1.15;color:{ENCRE}">Une obligation de résultat, de Castres à New York</p>
<p style="font-size:24px;color:{GRIS}"><b>262 adhérents</b> · <b>6 643 envois</b> sur 12 mois · <b>13 personnes</b></p>
<div style="position:relative;width:660px;height:282px;background:#FFFFFF;border-radius:16px;overflow:hidden">
<img src="{TEAM}" alt="L’équipe Planet Aura en 2026 : treize personnes" style="position:absolute;left:0px;top:0px;width:660px;height:282px;object-fit:cover">
<p style="position:absolute;left:418px;top:226px;width:96px;text-align:center;font-family:{L};font-size:24px;font-weight:600;color:#5A4321;background:{CHAMP};border-radius:999px;padding:2px 0px">Emma</p>
</div>
<div style="display:flex;flex-wrap:wrap;gap:10px">
{pole('Commerce &amp; dév.', 'Adam, Emma, Alessandro (NY)', ORF, OR)}
{pole('Direction', 'Floriane, Brice', PETROLE)}{pole('Logistique', '7', SARCF)}{pole('Admin.', '1', SARCF)}
</div>
</div>'''
    inner = f'''{header("Analyser · L'entreprise", 'Une croissance portée par le bouche-à-oreille', SARCF)}
<div style="flex:1;display:flex;gap:64px">{chart}{right}</div>
{footer(5, 'Analyser')}'''
    return 'entreprise', inner, dict(gap=36)
