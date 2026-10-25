# Diapos 1 à 7 : couverture, accroche, sommaire, marché et transport, Planet Aura, offre et positionnement, diagnostic
from kit import *

LOGO_MARK_W = '/_blob/8b40700e136fb4e2e66480f214bc3ee5'
LOGO_EURIDIS = '/_blob/ef3824102959481bdc56ec96f10cd910'
WORLDMAP = '/_blob/3b72dc2bb8ee61fc949e4287dc8c5fe1'
TEAM2 = '/_blob/613739a0dffd307c954794c05fc65d3c'

SECT_INTRO = "Comprendre : accroche, marché, entreprise, offre et diagnostic"


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
    return 'cover', inner, dict(bg=NUIT, color='#FFFFFF', pad='112px 128px 96px', gap=24, sect=SECT_INTRO)


def accroche():
    inner = f'''{eyebrow("Une scène type, entendue sur le terrain", BLEU)}
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
        ('01', 'Comprendre', SARCF, 'Pourquoi des ventes se perdent au comptoir', 'Marché · entreprise · offre · diagnostic', 'contexte et diagnostic', '→ la problématique'),
        ('02', 'Cibler', BORD, 'Viser les domaines qui reçoivent le monde', 'ICP · qualification · personas', 'parties 8 et 9', 'enjeu : recruter'),
        ('03', 'Vendre', ORF, 'De la première accroche à la signature', 'Solutions · processus · SPIN · proposition', 'parties 10 et 11', 'enjeu : recruter'),
        ('04', 'Activer', SARC, 'La vente finit au premier envoi', 'Activation · suivi du compte', 'partie 11', 'enjeu : activer, fidéliser'),
        ('05', 'Piloter', PETROLE, 'Outiller, former, mesurer', 'Ressources · Sales Ops · onboarding · KPI', 'parties 12 à 14', 'enjeu : transmettre, mesurer'),
    ]
    blocks = []
    for n, name, c, title, sub, cdc, enj in cols:
        blocks.append(f'''<div style="flex:1;display:flex;flex-direction:column;gap:8px">
{num(n, 72, c)}
<div style="height:10px;background:{c};border-radius:5px"></div>
{label(name, c, ls=3)}
<p style="font-family:{T};font-size:34px;font-weight:700;line-height:1.15;color:{ENCRE}">{title}</p>
<p style="font-size:24px;line-height:1.35;color:{GRIS}">{sub}</p>
<div style="flex:1"></div>
<p style="font-size:24px;color:{GRISD}">{cdc}</p>
<p style="height:60px;font-size:24px;font-weight:700;line-height:1.25;color:{TXT.get(c, c)}">{enj}</p>
</div>''')
    legend = ''.join(ctag(k) for k in CTAG)
    case = (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-left:8px solid {ORF};border-radius:14px;padding:14px 24px;display:flex;align-items:center;gap:22px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{ORF};white-space:nowrap">CAS FIL ROUGE</p>'
            f'<p style="font-size:26px;line-height:1.3;color:{ENCRE}">Un domaine provençal avec caveau, suivi de la qualification au premier envoi. '
            f'<b>Parcours type</b> du playbook : prix de la grille 2026, profil et situations illustratifs.</p></div>')
    inner = f'''{header3('Le parcours', 'Cinq étapes, du comptoir au pilotage', SARCF)}
<div style="display:flex;gap:36px">{''.join(blocks)}</div>
<div style="flex:1"></div>
{case}
<div style="display:flex;align-items:center;gap:12px">{label('Lecture', GRISD, ls=2)}<div style="width:8px"></div>{legend}</div>
{footer(3)}'''
    return 'sommaire', inner, dict(gap=20)


def marche():
    def big(lbl, value, unit, cap, src):
        u = f'<p style="font-family:{L};font-size:36px;font-weight:600;color:{PETROLE}">{unit}</p>' if unit else ''
        return f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px">
{label(lbl, SARCF)}
<div style="display:flex;align-items:baseline;gap:10px">{num(value, 80, PETROLE)}{u}</div>
<p style="font-size:26px;line-height:1.3;color:{GRIS}">{cap}</p>
<p style="font-size:24px;color:{GRISD}">{src}</p>
</div>'''
    top = (f'<div style="display:flex;gap:56px">'
           f'{big("On boit moins", "208", "Mhl", "de vin consommés dans le monde en 2025 (−2,7 %) ; le vin qui voyage reste cher : 3,56 €/l à l’export", "OIV, mai 2026")}'
           f'{big("Le premier marché vacille", "−21 %", "", "d’exports français de vins et spiritueux vers les USA en 2025 : droits de douane et change", "FEVS, févr. 2026")}'
           f'{big("Le client vient à nous", "5,4 M", "", "œnotouristes étrangers dans nos vignobles (2023) : le caveau devient un canal d’export", "Atout France")}'
           f'</div>')
    cons = [('Droits de douane', 'volatils depuis 2025 ; taux du jour au simulateur'),
            ('Three-tier system', 'importateur licencié obligatoire'),
            ('Procuration (POA)', 'au-delà de 2 100 $ de valeur déclarée'),
            ('Documents', 'DA/EMCS, accises, certificat CIVC'),
            ('Emballage', 'carton homologué ISTA 3A')]
    boxes = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:8px;padding:0px 18px;border-left:3px solid {SARC}">
<p style="font-family:{L};font-size:26px;font-weight:600;color:#FFFFFF">{a}</p>
<p style="font-size:24px;line-height:1.3;color:{BRUME}">{b}</p></div>''' for a, b in cons)
    band = f'''<div style="background:{NUIT};border-radius:20px;padding:24px 30px;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:baseline;gap:18px">{label("Expédier une caisse chez un particulier américain", CHAMP, ls=2)}</div>
<div style="display:flex;gap:6px">{boxes}</div>
<p style="font-family:{T};font-style:italic;font-size:32px;color:{CHAMP}">Chaque contrainte freine le vigneron… et fonde notre métier.</p>
</div>'''
    inner = f'''{header3('Comprendre · Le marché', 'Un marché qui se durcit, un transport qui se complique', SARCF, tags=['MON ANALYSE'])}
{top}
<div style="flex:1"></div>
{band}
{footer(4, 'Comprendre')}'''
    return 'marche', inner, dict(gap=30)


def entreprise():
    data = [('2021', 246637, '247 k€'), ('2022', 800065, '800 k€'), ('2023', 910505, '911 k€'),
            ('2024', 1029570, '1,03 M€'), ('2025', 1148961, '1,15 M€')]
    H = 150.0
    bars = ''
    for y, v, lab in data:
        h = round(v / 1148961 * H)
        fill = PETROLE if y == '2025' else SARC
        bars += (f'<div style="width:96px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px">'
                 f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{ENCRE};white-space:nowrap">{lab}</p>'
                 f'<div style="width:70px;height:{h}px;background:{fill};border-radius:6px 6px 0px 0px"></div>'
                 f'<p style="font-family:{L};font-size:24px;color:{GRIS}">{y}</p></div>')
    ca = f'''<div style="width:520px;display:flex;flex-direction:column;gap:6px">
<div style="display:flex;align-items:baseline;gap:14px">{num('×4,7', 60, ORF)}<p style="font-size:24px;color:{GRIS}">CA de 2021 à 2025</p></div>
<div style="display:flex;align-items:flex-end;gap:8px">{bars}</div>
<p style="font-size:24px;line-height:1.35;color:{ENCRE}">2025 : <b>+11,6 %</b>, à contre-courant<br>2026 : <b>+18,7 %</b> au 24/09</p>
</div>'''
    mk = f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px;justify-content:flex-end">
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b>262 adhérents</b> · <b>6 643 envois</b> sur 12 mois, vers :</p>
<div style="display:flex;height:46px;border-radius:8px;overflow:hidden">
<div style="flex:64.5;background:{PETROLE};display:flex;align-items:center;padding:0px 12px"><p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF">USA 64,5 %</p></div>
<div style="flex:18.6;background:{SARC}"></div><div style="flex:16.9;background:{BRUME}"></div></div>
<p style="font-size:24px;color:{GRIS}"><b><span style="color:{SARCF}">France 18,6 %</span></b> · autres 16,9 %</p>
<p style="font-size:24px;color:{GRISD}">Planet’Connect, 24/09/2026</p>
</div>'''
    who = [('Direction', 'Floriane, Brice', 'remises, comptes stratégiques', PETROLE),
           ('Commercial', 'Adam', 'le seul dédié, depuis fin 2025', ORF),
           ('Projets, développement', 'Emma', 'partenariats, logiciel, playbook', BORD),
           ('Filiale de New York', 'Alessandro', 'relais du marché américain', SARCF),
           ('Exploitation, admin.', '8 personnes', 'cotations hors grille, SEPA', GRISD)]
    hi = lambda a: a == 'Commercial'
    rows = ''.join(f'''<div style="display:flex;align-items:baseline;gap:12px;border-bottom:1px solid {FILET};padding:4px {'10px' if hi(a) else '0px'};{'background:#FBF3E2;border-left:6px solid ' + ORF if hi(a) else ''}">
<p style="width:{300 if hi(a) else 310}px;font-family:{L};font-size:24px;font-weight:600;color:{c};white-space:nowrap">{a}</p>
<p style="width:190px;font-size:24px;font-weight:700;color:{ENCRE};white-space:nowrap">{n}</p>
<p style="flex:1;font-size:24px;color:{ENCRE if hi(a) else GRIS};font-weight:{700 if hi(a) else 400};white-space:nowrap">{d}</p></div>''' for a, n, d, c in who)
    left = f'''<div style="width:620px;display:flex;flex-direction:column;gap:10px">
<img src="{TEAM2}" alt="L’équipe Planet Aura en 2026, treize personnes, filiale de New York comprise" style="width:620px;height:414px;object-fit:cover;border-radius:16px">
<p style="font-size:24px;color:{GRISD}">L’équipe 2026 : treize personnes, New York compris</p>
<p style="font-size:26px;line-height:1.35;color:{ENCRE}">Née à Castres en 2019. <b>Commissionnaire de transport</b> : nous choisissons les transporteurs et répondons du résultat, de bout en bout.</p>
</div>'''
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:22px">
<div style="display:flex;gap:40px">{ca}{mk}</div>
<div style="display:flex;flex-direction:column">{label('Qui vend, qui décide', SARCF, ls=2)}{rows}</div>
</div>'''
    inner = f'''{header3("Comprendre · L'entreprise", 'Planet Aura : une croissance portée par le bouche-à-oreille', SARCF, tags=['EXISTANT'])}
<div style="flex:1;display:flex;gap:48px">{left}{right}</div>
{footer(5, 'Comprendre')}'''
    return 'entreprise', inner, dict(gap=30)


def offre():
    # gauche : ce que nous vendons ; droite : où nous nous plaçons
    grid = [('1-3', 105, '≥ 35 €'), ('6', 140, '23,3 €'), ('12', 210, '17,5 €'), ('24', 360, '15 €'), ('36', 510, '14,2 €')]
    gb = ''
    for n, v, pb in grid:
        h = round(float(pb.replace('≥ ', '').replace(' €', '').replace(',', '.')) / 35 * 140)
        hi = n == '24'
        gb += (f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:4px">'
               f'<p style="font-family:{L};font-size:26px;font-weight:700;color:{ORF if hi else PETROLE}">{pb}</p>'
               f'<div style="width:70px;height:{h}px;background:{OR if hi else BLEU};border-radius:6px 6px 0px 0px"></div>'
               f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{ENCRE}">{n} btl</p>'
               f'<p style="font-size:24px;color:{ORF if hi else GRISD}">{v} €</p></div>')
    prom = ''.join(f'<p style="font-size:24px;line-height:1.3;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:999px;padding:6px 16px;white-space:nowrap">{t}</p>'
                   for t in ['Vous vendez plus', 'Vous ne gérez rien', 'Votre risque est maîtrisé'])
    node = lambda t, c: f'<p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF;background:{c};border-radius:10px;padding:6px 14px;white-space:nowrap;flex:none">{t}</p>'
    step = lambda t: f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:2px"><p style="font-size:24px;line-height:1.15;text-align:center;color:{GRIS}">{t}</p>{arrow(90, 22, ORF, 4)}</div>'
    flow = f'''<div style="display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:center;gap:10px">{node('Visiteur', ORF)}{step('vin + transport, au comptoir')}{node('Domaine', BORD)}{step('par SEPA')}{node('Planet Aura', PETROLE)}</div>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}">Et nous livrons le visiteur en <b>DDP</b> : taxes estimées, réglées d’avance.</p></div>'''
    left = f'''<div style="width:800px;display:flex;flex-direction:column;gap:14px">
{label('Ce que nous vendons', SARCF, ls=2)}
{flow}
<div style="display:flex;align-items:center;gap:12px">{pill('GRILLE 2026', label='GRILLE 2026')}<p style="font-size:24px;color:{GRIS}">Produit phare : groupage USA, ~21 jours estimés hors douane</p></div>
<div style="display:flex;align-items:flex-end;height:250px;gap:10px;border-bottom:2px solid {FILET}">{gb}</div>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Transport HT <b>par bouteille</b>, total dessous · + taxes estimées · assurance en option, 3 %</p>
</div>'''
    fam = [('Expressistes', 'FedEx · UPS · DHL', 'puissants, mais l’alcool B2C est leur angle mort ; aussi nos sous-traitants'),
           ('Généralistes', 'Hillebrand Gori · Kuehne+Nagel', 'les gros volumes'),
           ('Spécialistes vin', 'Dartess · Viticolis · Vinotrans…', 'nos vrais duels'),
           ('Voile-cargo', 'VELA · TOWT · Grain de Sail', 'partenaires potentiels')]
    fr_ = ''.join(f'''<div style="display:flex;gap:14px;align-items:baseline;border-bottom:1px solid {FILET};padding:6px 0px">
<p style="width:230px;font-family:{L};font-size:24px;font-weight:600;color:{PETROLE}">{a}</p>
<p style="flex:1;font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{ENCRE}">{b}</span></b> · {c}</p></div>''' for a, b, c in fam)
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:14px">
{label('Où nous nous plaçons', BORD, ls=2)}
<div style="background:{NUIT};border-radius:16px;padding:16px 22px;display:flex;flex-direction:column;gap:6px">
<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{CHAMP}">CONCURRENT N° 1, HORS CARTE</p>
<p style="font-family:{T};font-size:34px;font-weight:700;color:#FFFFFF">« On se débrouille » : la valise, La Poste</p></div>
<div style="display:flex;flex-direction:column">{fr_}</div>
<div style="border-left:6px solid {SARC};padding:4px 0px 4px 18px;display:flex;flex-direction:column;gap:4px">
<p style="font-size:26px;line-height:1.3;color:{ENCRE}"><b>Notre case</b> : spécialiste du vin <b>et</b> intégré : obligation de résultat, filiale licenciée, plateforme.</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS}">Prix : point faible assumé, avis partagé (10 répondants sur 23 « moyennement compétitif », autant « compétitif » ou « très compétitif », 2024).</p></div>
</div>'''
    inner = f'''{header3("Comprendre · Offre et positionnement", 'Nous vendons de la sécurité, pas du transport', SARCF, tags=['EXISTANT', 'MON ANALYSE'])}
<div style="flex:1;display:flex;gap:56px">{left}{right}</div>
{footer(6, 'Comprendre')}'''
    return 'offre', inner, dict(gap=30)


def diagnostic():
    def quad(t, c, bg, items):
        li = ''.join(f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}">· {i}</p>' for i in items)
        return (f'<div style="background:{bg};border-top:6px solid {c};border-radius:12px;padding:12px 18px;display:flex;flex-direction:column;gap:4px">'
                f'{label(t, c, ls=2)}{li}</div>')
    sw = f'''<div style="width:900px;display:grid;grid-template-columns:repeat(2, 1fr);gap:14px">
{quad('Forces', SARCF, '#E8F3F5', ['Le trio : statut, filiale, plateforme', 'CA ×4,7 en quatre ans', 'Satisfaction 4,65/5 (2024, 23 rép.)'])}
{quad('Fragilités', BORD, '#F6EAEE', ['1er commercial dédié : fin 2025', '448 / 710 prospects non qualifiés', 'Activation <b>jamais mesurée</b>', '<b>Aucun référentiel</b> commun'])}
{quad('Opportunités', '#3A8A5C', '#EAF4EE', ['Œnotourisme et vente directe', 'Royaume-Uni, Europe, Japon', 'Champagne, spiritueux'])}
{quad('Risques', ORANGE, '#FBEFE8', ['64,5 % des envois vers les USA', 'Droits de douane volatils', 'Recul de la consommation'])}
</div>'''
    enj = ''.join(f'''<div style="display:flex;align-items:center;gap:14px"><div style="width:44px;height:44px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{i}</p></div>
<p style="font-family:{T};font-size:30px;font-weight:700;color:#FFFFFF">{t}</p></div>''' for i, t, c in [(1, 'Recruter les bons comptes', BORD), (2, 'Activer et fidéliser', SARC), (3, 'Transmettre et mesurer', PETROLE)])
    right = f'''<div style="flex:1;background:{NUIT};border-radius:20px;padding:26px 30px;display:flex;flex-direction:column;gap:18px">
{label('Problématique', CHAMP, ls=3)}
<p style="font-family:{T};font-size:36px;font-weight:700;line-height:1.25;color:#FFFFFF">Comment transformer une croissance portée par le bouche-à-oreille en une méthode de vente <span style="color:{CHAMP}">reproductible et mesurable</span>, pour recruter, activer et fidéliser nos adhérents ?</p>
<div style="flex:1"></div>
{label('Trois enjeux', '#8FB0BA', ls=3)}
{enj}
</div>'''
    inner = f'''{header3('Comprendre · Diagnostic', 'Une croissance réelle, une vente encore informelle', SARCF, tags=['MON ANALYSE'])}
<div style="flex:1;display:flex;gap:44px">{sw}{right}</div>
{footer(7, 'Comprendre')}'''
    return 'diagnostic', inner, dict(gap=30)
