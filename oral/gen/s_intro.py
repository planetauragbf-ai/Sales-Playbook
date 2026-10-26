# Diapos 1 à 7 : couverture, accroche, sommaire, marché et transport, Planet Aura, offre et positionnement, diagnostic
from kit import *

LOGO_MARK_W = '/_blob/8b40700e136fb4e2e66480f214bc3ee5'
LOGO_EURIDIS = '/_blob/ef3824102959481bdc56ec96f10cd910'
WORLDMAP = '/_blob/3b72dc2bb8ee61fc949e4287dc8c5fe1'
TEAM2 = '/_blob/613739a0dffd307c954794c05fc65d3c'

SECT_INTRO = "Comprendre : accroche, marché, entreprise, offre et diagnostic"


def cover():
    # v5 : composition et texte inchangés. Seuls changements :
    # - carte du monde (décor) décalée à droite et réduite (1340→1440 px, 560×370 → 460×304) : elle ne passe plus
    #   sous la fin de la signature ni sous la ligne « Chargée de projets… », même à texte +10 % ;
    # - « 2024‑2027 » avec un trait d'union insécable : la date ne se coupe jamais en fin de ligne.
    inner = f'''<img src="{WORLDMAP}" alt="" style="position:absolute;left:1440px;top:470px;width:460px;height:304px;object-fit:contain;opacity:0.32">
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
<p style="font-size:24px;color:{BRUME}">Chargée de projets &amp; développement · Mastère Marketing &amp; Digital Business, promotion 547 (2024‑2027)</p>
<p style="font-size:24px;color:{BRUME}">Tutrice : Floriane Février · Suivi académique : Thibaut du Cleuziou</p>
<p style="font-size:24px;color:#8FB0BA">Document confidentiel : diffusion interne Planet Aura et jury Euridis</p>
</div>
<div style="background:#FFFFFF;border-radius:14px;padding:16px 24px"><img src="{LOGO_EURIDIS}" alt="Euridis Business School" style="width:300px;height:56px;object-fit:contain"></div>
</div>'''
    return 'cover', inner, dict(bg=NUIT, color='#FFFFFF', pad='112px 128px 96px', gap=24, sect=SECT_INTRO)


def accroche():
    # v5 : composition et texte inchangés (la diapo passe déjà le banc). Seul changement :
    # « les ramener » lié par une espace insécable : si la citation passe sur trois lignes (moteur réel plus large),
    # la dernière ligne porte deux mots, jamais « ramener. » seul. De même, « où qu'il soit » est lié par des espaces
    # insécables : la locution ne se coupe jamais entre deux lignes.
    inner = f'''{eyebrow("Une scène type, entendue sur le terrain", BLEU)}
<p style="font-family:{T};font-style:italic;font-size:60px;line-height:1.22;color:{CLAIR};width:1560px">« Un couple de Houston voulait 24 bouteilles. Ils sont repartis avec 2 : ils ne savaient pas comment les ramener. »</p>
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
<p style="font-size:28px;line-height:1.35;color:{BRUME}">Lever la dernière barrière entre un vin précieux et celui qui doit le recevoir, où qu'il soit.</p>
</div>
</div>'''
    return 'accroche', inner, dict(bg=NUIT, color=CLAIR, pad='112px 128px 104px', gap=24)


def sommaire():
    # Un seul point focal : le parcours en cinq stations (numéro, étape, idée-titre), relié aux trois enjeux.
    steps = [('01', 'Comprendre', SARCF, 'Pourquoi des ventes se perdent au comptoir'),
             ('02', 'Cibler', BORD, 'Viser les domaines qui reçoivent le monde'),
             ('03', 'Vendre', ORF, 'De la première accroche à la signature'),
             ('04', 'Activer', SARC, 'La vente finit au premier envoi'),
             ('05', 'Piloter', PETROLE, 'Outiller, former, mesurer')]
    rail = '#C9D8DD'

    def _sommaire_enjeu(txt, parts, c, part='full'):
        # accolade : un trait de couleur, l'enjeu, les parties du cahier des charges.
        # « Recruter » couvre deux lignes (Cibler, Vendre) : deux cellules jointives (haut / bas) au lieu
        # d'une cellule fusionnée, pour que chaque ligne de la grille ait ses 4 cellules (ordre source sûr).
        pad = {'full': '8px 0px', 'top': '8px 0px 0px 0px', 'bottom': '0px 0px 8px 0px'}[part]
        just = {'full': 'center', 'top': 'end', 'bottom': 'start'}[part]  # valeurs de la grammaire Slides
        t = f'<p style="font-size:28px;font-weight:700;line-height:1.2;color:{TXT.get(c, c)}">{txt}</p>'
        s = f'<p style="font-size:24px;line-height:1.2;color:{GRISD}">{parts}</p>'
        body = {'full': t + s, 'top': t, 'bottom': s}[part]
        inpad = {'full': '0px 0px 0px 20px', 'top': '0px 0px 1px 20px', 'bottom': '1px 0px 0px 20px'}[part]
        return (f'<div style="display:flex;padding:{pad}">'
                f'<div style="flex:1;border-left:6px solid {c};padding:{inpad};display:flex;flex-direction:column;justify-content:{just};gap:2px">'
                f'{body}</div></div>')

    # ligne 01, colonne de droite : « → la problématique », alignée sur l'idée-titre de l'étape 01
    prob = (f'<div style="display:flex;align-items:center;gap:12px;padding:10px 0px 10px 26px">{arrow(34, 20, SARCF, 3)}'
            f'<p style="font-size:26px;font-weight:600;line-height:1.2;color:{SARCF}">la problématique</p></div>')
    # ligne intercalaire (entre 01 et 02) : le rail continue, et l'intitulé « Trois enjeux » coiffe la colonne des accolades
    gap_row = (f'<div style="display:flex;flex-direction:column;align-items:center"><div style="flex:1;width:4px;background:{rail}"></div></div>'
               f'<div></div><div></div>'
               f'<div style="display:flex;align-items:flex-end;padding:0px 0px 6px 26px">'
               f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;line-height:1.2;text-transform:uppercase;color:{GRISD}">Trois enjeux</p></div>')
    right = {0: prob,
             1: _sommaire_enjeu('Recruter', 'parties 8 à 11', BORD, part='top'),
             2: _sommaire_enjeu('Recruter', 'parties 8 à 11', BORD, part='bottom'),
             3: _sommaire_enjeu('Activer, fidéliser', 'partie 11', SARC),
             4: _sommaire_enjeu('Transmettre, mesurer', 'parties 12 à 14', PETROLE)}
    cells = ''
    for i, (n, name, c, title) in enumerate(steps):
        top = 'transparent' if i == 0 else rail
        bot = 'transparent' if i == len(steps) - 1 else rail
        cells += (f'<div style="display:flex;flex-direction:column;align-items:center">'
                  f'<div style="flex:1;width:4px;background:{top}"></div>'
                  f'<div style="width:56px;min-height:56px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none">'
                  f'<p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{n}</p></div>'
                  f'<div style="flex:1;width:4px;background:{bot}"></div></div>'
                  f'<div style="display:flex;align-items:center">{label(name, c, size=28, ls=3)}</div>'
                  f'<div style="display:flex;align-items:center;padding:18px 0px">'
                  f'<p style="font-family:{T};font-size:36px;font-weight:700;line-height:1.2;color:{ENCRE}">{title}</p></div>'
                  f'{right[i]}' + (gap_row if i == 0 else ''))
    path = (f'<div style="display:grid;grid-template-columns:56px auto auto 1fr;gap:0px 36px">'
            f'{cells}</div>')
    case = (f'<div style="{CASE_BOX};border-radius:14px;padding:12px 24px;display:flex;align-items:center;gap:24px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{ORF};white-space:nowrap">CAS FIL ROUGE</p>'
            f'<p style="font-family:{T};font-size:30px;font-weight:700;line-height:1.25;color:{ENCRE}">Un domaine provençal avec caveau</p>'
            f'<div style="flex:1"></div>{pill("ILLUSTRATIF", "align-self:center", label="PARCOURS TYPE")}</div>')
    legend = ''.join(ctag(k, 'align-self:center') for k in CTAG)
    inner = f'''{header3('Sommaire', 'Cinq étapes, du comptoir au pilotage', SARCF)}
{path}
<div style="flex:1"></div>
{case}
<div style="display:flex;align-items:center;gap:12px">{label('Étiquettes', GRISD, ls=2)}<div style="width:8px"></div>{legend}</div>
{footer(3)}'''
    return 'sommaire', inner, dict(gap=20)


def marche():
    # Message : l'export se complique, et c'est notre métier.
    # Point focal : trois grands chiffres, trois bascules (deux reculs en orange, une opportunité en sarcelle) ;
    # en bas, le bandeau sombre des cinq contraintes.
    NB = ' '

    def col(lbl, lc, value, cap, src):
        return f'''<div style="flex:1;display:flex;flex-direction:column;gap:8px;border-top:6px solid {lc};padding-top:16px">
<p style="font-family:{L};font-size:30px;font-weight:600;line-height:1.3;color:{TXT.get(lc, lc)}">{lbl}</p>
<div style="display:flex;align-items:baseline">{num(value, 104, PETROLE, extra='line-height:1.3')}</div>
<div style="display:flex;flex-direction:column;gap:4px">
<p style="font-size:24px;line-height:1.3;color:{ENCRE}">{cap}</p>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">{src}</p>
</div>
</div>'''
    c1 = col('Le monde boit moins', ORANGE, '−2,7 %', '208 Mhl consommés en 2025', 'OIV, mai 2026')
    # −21 % : des exports en VALEUR (FEVS), ni la consommation ni les volumes : la légende le dit.
    c2 = col('Le premier marché vacille', ORANGE, '−21 %',
             f'valeur des vins et spiritueux français exportés aux{NB}USA,{NB}2025', 'FEVS, févr. 2026')
    c3 = col('Le client vient à nous', SARCF, '5,4 M', 'œnotouristes étrangers en 2023', 'Atout France')
    top = f'<div style="display:flex;gap:64px">{c1}{c2}{c3}</div>'
    # (intitulé, explication, largeur relative) : la case Documents est un peu plus large pour tenir en deux lignes, même en stress
    cons = [('Douane', f'droits volatils depuis{NB}2025', 1),
            ('Three-tier', 'importateur licencié obligatoire', 1),
            ('POA', f'procuration au‑delà de{NB}2 100 $', 1),
            ('Documents', f'DA/EMCS, accises, certificat{NB}Champagne{NB}(CIVC)', 1.3),
            ('Emballage', 'carton homologué ISTA 3A', 1)]
    boxes = ''.join(f'''<div style="flex:{w};display:flex;flex-direction:column;gap:8px;padding:0px 0px 0px 18px;border-left:3px solid {SARC}">
<p style="font-family:{L};font-size:28px;font-weight:600;line-height:1.2;color:#FFFFFF">{a}</p>
<p style="font-size:24px;line-height:1.3;color:{BRUME}">{b}</p></div>''' for a, b, w in cons)
    band = f'''<div style="background:{NUIT};border-radius:18px;padding:24px 28px 28px 28px;display:flex;flex-direction:column;gap:18px">
{label("Expédier chez un particulier américain", CHAMP, ls=2)}
<div style="display:flex;gap:16px">{boxes}</div>
</div>'''
    inner = f'''{header3('Comprendre · Le marché', 'L’export se complique : c’est notre métier', SARCF, tags=['MON ANALYSE'])}
<div style="flex:1"></div>
{top}
<div style="flex:1"></div>
{band}
<div style="height:74px;flex:none"></div>
{footer(4, 'Comprendre')}'''
    # marge basse : 64 px de padding + 74 px d'entretoise + 22 px d'écart = les 160 px habituels (bas du corps à 920 px),
    # comme offre, processus, kpi… : le pied de page reste dans la limite du banc, même en stress.
    return 'marche', inner, dict(gap=22, pad='128px 128px 64px')


def entreprise():
    # Message : une croissance ×4,7, portée par le bouche-à-oreille (un seul commercial dédié, arrivé fin 2025).
    # Point focal : ×4,7 et les barres du CA, la barre 2025 en foncé ; en bas, le bandeau « qui vend, qui décide ».
    data = [('2021', 246637, '247 k€'), ('2022', 800065, '800 k€'), ('2023', 910505, '911 k€'),
            ('2024', 1029570, '1,03 M€'), ('2025', 1148961, '1,15 M€')]
    H = 240.0
    cols, years = '', ''
    for y, v, lab in data:
        last = y == '2025'
        h = round(v / 1148961 * H)
        cols += (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:6px">'
                 f'<p style="font-family:{L};font-size:{30 if last else 26}px;font-weight:{700 if last else 600};line-height:1.2;'
                 f'color:{PETROLE if last else GRIS};white-space:nowrap">{lab}</p>'
                 f'<div style="width:96px;height:{h}px;background:{PETROLE if last else BLEU};border-radius:8px 8px 0px 0px"></div></div>')
        years += (f'<p style="flex:1;text-align:center;font-family:{L};font-size:24px;font-weight:{700 if last else 500};'
                  f'line-height:1.3;color:{PETROLE if last else GRISD}">{y}</p>')
    chart = f'''<div style="flex:1;display:flex;flex-direction:column;gap:6px">
<div style="display:flex;align-items:flex-end;gap:8px;border-bottom:2px solid {FILET}">{cols}</div>
<div style="display:flex;gap:8px">{years}</div>
</div>'''
    big = f'''<div style="width:300px;display:flex;flex-direction:column;gap:10px">
{num('×4,7', 120, ORF)}
<p style="font-size:28px;line-height:1.3;color:{ENCRE}">CA de 2021 à 2025</p>
{pill('CONSTATÉ')}
</div>'''
    mk = f'''<div style="display:flex;flex-direction:column;gap:10px">
<div style="display:flex;align-items:baseline;justify-content:space-between;gap:24px">
<p style="font-size:26px;line-height:1.3;color:{ENCRE}"><b>262 adhérents</b> · <b>6 643 envois</b> en 12 mois</p>
<p style="font-size:24px;line-height:1.3;color:{GRISD};white-space:nowrap">Planet’Connect, 24/09/2026</p></div>
<div style="display:flex;gap:4px;height:30px"><div style="flex:64.5;background:{PETROLE}"></div><div style="flex:18.6;background:{SARC}"></div><div style="flex:16.9;background:{BRUME}"></div></div>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{PETROLE}">USA 64,5 %</span></b> · <b><span style="color:{SARCF}">France 18,6 %</span></b> · autres 16,9 %</p>
</div>'''
    left = f'''<div style="flex:1;display:flex;flex-direction:column;gap:30px">
<div style="display:flex;align-items:flex-end;gap:40px">{big}{chart}</div>
{mk}
</div>'''
    right = f'''<div style="width:600px;display:flex;flex-direction:column;gap:10px">
<img src="{TEAM2}" alt="L’équipe Planet Aura en 2026, treize personnes, filiale de New York comprise" style="width:600px;height:400px;object-fit:cover;border-radius:16px">
<p style="font-size:24px;line-height:1.3;color:{GRISD}">L’équipe 2026 : 13 personnes, filiale comprise</p>
</div>'''
    row = lambda lab, lc, txt, size, tc: (f'<div style="display:flex;align-items:baseline;gap:24px">'
                                          f'<p style="width:230px;font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{lc};white-space:nowrap">{lab}</p>'
                                          f'<p style="flex:1;font-size:{size}px;line-height:1.3;color:{tc}">{txt}</p></div>')
    band = f'''<div style="background:{NUIT};border-radius:18px;padding:18px 32px;display:flex;flex-direction:column;gap:10px">
{row('QUI VEND', CHAMP, f'<b><span style="color:{CHAMP}">Adam</span></b> : le seul commercial dédié, <b>arrivé fin 2025</b>', 32, '#FFFFFF')}
{row('QUI DÉCIDE', BLEU, 'La direction, Floriane et Brice : remises, comptes stratégiques', 26, BRUME)}
</div>'''
    inner = f'''{header3('Comprendre · Planet Aura', 'Une croissance portée par le bouche-à-oreille', SARCF, tags=['EXISTANT'])}
<div style="flex:1;display:flex;gap:56px;align-items:flex-start">{left}{right}</div>
{band}
<div style="height:72px;flex:none"></div>
{footer(5, 'Comprendre')}'''
    return 'entreprise', inner, dict(gap=24, pad='128px 128px 64px')


def offre():
    # Message : nous vendons de la sécurité, pas du transport.
    # Point focal : les barres du transport par bouteille (grille 2026) ; la dorée = 24 bouteilles à 15 €.
    # Second temps : le bloc sombre « On se débrouille », trois familles de concurrents, notre place.
    grid = [('1–3', '≥ 35 €', 35.0), ('6', '23,3 €', 23.3), ('12', '17,5 €', 17.5), ('24', '15 €', 15.0), ('36', '14,2 €', 14.2)]
    H = 370
    bars, axis = '', ''
    for n, pb, v in grid:
        hi = n == '24'
        top = (num(pb, 72, ORF) if hi else
               f'<p style="font-family:{L};font-size:34px;font-weight:700;line-height:1.2;color:{PETROLE};white-space:nowrap">{pb}</p>')
        bars += (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:10px">'
                 f'{top}<div style="width:112px;height:{round(v / 35 * H)}px;background:{ORF if hi else BLEU};border-radius:8px 8px 0px 0px"></div></div>')
        axis += (f'<div style="flex:1;display:flex;justify-content:center">'
                 f'<p style="font-family:{L};font-size:30px;font-weight:{700 if hi else 600};color:{ORF if hi else ENCRE};white-space:nowrap">{n} btl</p></div>')
    left = f'''<div style="width:860px;display:flex;flex-direction:column;gap:12px">
<p style="font-family:{L};font-size:32px;font-weight:600;line-height:1.3;color:{PETROLE}">Groupage USA en DDP : taxes réglées d’avance</p>
<div style="flex:1"></div>
<div style="display:flex;align-items:flex-end;gap:12px;border-bottom:3px solid {FILET}">{bars}</div>
<div style="display:flex;gap:12px">{axis}</div>
<div style="display:flex;align-items:center;gap:16px">{pill('GRILLE 2026', 'align-self:center')}<p style="font-size:24px;line-height:1.3;color:{GRISD}">Transport HT <b>par bouteille</b> · + taxes estimées</p></div>
</div>'''
    fam = [('Expressistes', 'FedEx · UPS · DHL', 'aussi nos sous-traitants', False),
           ('Généralistes', 'Hillebrand Gori · Kuehne+Nagel', '', False),
           ('Spécialistes vin', 'Dartess · Viticolis · Vinotrans…', 'nos vrais duels', True)]
    rows = ''
    for a, b, c, hi in fam:
        q = f'<p style="font-size:24px;line-height:1.25;color:{GRIS}">{c}</p>' if c else ''
        st = f'background:#FBF3E2;border-left:6px solid {ORF};padding:14px 0px 14px 14px' if hi else 'padding:14px 0px'
        rows += (f'<div style="display:flex;gap:{10 if hi else 16}px;align-items:baseline;border-bottom:1px solid {FILET};{st}">'
                 f'<p style="width:{226 if hi else 240}px;font-family:{L};font-size:26px;font-weight:600;color:{ORF if hi else PETROLE};flex:none">{a}</p>'
                 f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:26px;font-weight:700;line-height:1.25;color:{ENCRE}">{b}</p>{q}</div></div>')
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:20px">
<div style="background:{NUIT};border-radius:18px;padding:20px 28px 22px;display:flex;flex-direction:column;gap:8px">
{label('Concurrent n° 1', CHAMP, ls=2)}
<p style="font-family:{T};font-size:44px;font-weight:700;line-height:1.15;color:#FFFFFF">« On se débrouille »</p>
<p style="font-size:28px;line-height:1.3;color:{BRUME}">la valise, La Poste</p>
</div>
<div style="display:flex;flex-direction:column">{rows}</div>
<div style="flex:1"></div>
<div style="border-left:6px solid {ORF};padding:6px 0px 6px 14px"><p style="font-size:30px;line-height:1.3;color:{ENCRE}"><b>Notre place</b> : spécialiste du vin <b>et</b>\u00a0intégré</p></div>
</div>'''
    inner = f'''{header3("Comprendre · Offre et positionnement", 'Nous vendons de la sécurité, pas du transport', SARCF, tags=['EXISTANT', 'MON ANALYSE'])}
<div style="flex:1;display:flex;gap:64px">{left}{right}</div>
<div style="height:60px;flex:none"></div>
{footer(6, 'Comprendre')}'''
    # marge basse : 64 px de padding + 60 px d'entretoise + 36 px d'écart = les 160 px habituels (bas du corps à 920 px)
    return 'offre', inner, dict(gap=36, pad='128px 128px 64px')


def diagnostic():
    # Message : une croissance réelle, une vente encore informelle : d'où la problématique.
    # Point focal : la problématique, en grand sur le bandeau sombre, et ses trois enjeux.
    # Le diagnostic se réduit à deux cartes (forces, fragilités) ; le SWOT complet est en secours B8.
    def card(lab, c, bg, items, w):
        li = ''.join(f'<p style="font-size:28px;line-height:1.3;color:{ENCRE}">{i}</p>' for i in items)
        size = f'width:{w}px' if w else 'flex:1'
        return (f'<div style="{size};background:{bg};border-left:8px solid {c};border-radius:16px;padding:18px 28px 20px 28px;'
                f'display:flex;flex-direction:column;gap:8px">'
                f'<div style="display:flex;align-items:center;justify-content:space-between;gap:16px">{label(lab, c, size=26, ls=3)}'
                f'{pill("CONSTATÉ", extra="align-self:center")}</div>{li}</div>')
    diag = (f'<div style="display:flex;gap:28px;align-items:stretch">'
            f'{card("Forces", SARCF, "#E8F3F5", ["Le trio : statut, filiale, plateforme", "CA <b>×4,7</b> en quatre ans"], 660)}'
            f'{card("Fragilités", BORD, "#F6EAEE", ["<b>448 / 710</b> prospects non qualifiés", "Activation <b>jamais mesurée</b>", "<b>Aucun référentiel</b> commun"], None)}'
            f'</div>')
    # pastilles claires (CHAMP) : lisibles sur le fond NUIT, quel que soit le numéro
    enj = ''.join(f'''<div style="display:flex;align-items:center;gap:14px"><div style="width:48px;height:48px;border-radius:50%;background:{CHAMP};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:26px;font-weight:700;color:{NUIT}">{i}</p></div>
<p style="font-family:{T};font-size:32px;font-weight:700;line-height:1.2;color:#FFFFFF">{t}</p></div>''' for i, t in [(1, 'Recruter les bons comptes'), (2, 'Activer et fidéliser'), (3, 'Transmettre et mesurer')])
    band = f'''<div style="background:{NUIT};border-radius:20px;padding:30px 44px 34px 44px;display:flex;flex-direction:column;gap:16px">
{label('Problématique', CHAMP, size=26, ls=3)}
<p style="font-family:{T};font-size:44px;font-weight:700;line-height:1.25;color:#FFFFFF">Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente <span style="color:{CHAMP}">reproductible et mesurable</span>, pour recruter, activer et fidéliser nos adhérents ?</p>
<div style="height:2px;background:#2E5866"></div>
<div style="display:flex;align-items:center;justify-content:space-between;gap:40px">{enj}</div>
</div>'''
    sp = '<div style="flex:1;min-height:24px"></div>'
    inner = f'''{header3('Comprendre · Diagnostic', 'Une croissance réelle, une vente encore informelle', SARCF, tags=['MON ANALYSE'])}
{sp}
{diag}
{sp}
{band}
<div style="flex:1"></div>
{footer(7, 'Comprendre')}'''
    return 'diagnostic', inner, dict(gap=0)
