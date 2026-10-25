# Diapos 12 à 20 : processus, SPIN, objections, ressources, Sales Ops, KPI, synthèse, ouverture, clôture (v2, après revue)
from kit import *

PHOTO_CARTON = '/_blob/ef0653efdd69aa1019998d62b2c7af5b'
LOGO_MARK_W = '/_blob/8b40700e136fb4e2e66480f214bc3ee5'
LIGHT_BORD = '#D58FA6'   # bordeaux éclairci, lisible sur fond nuit


def processus():
    names = [('Lead', 'rappel &lt; 24 h'), ('Qualifié', '≤ 7 j'), ('RDV · démo', 'CR &lt; 24 h'), ('Proposition', 'sous 24 h'),
             ('Adhésion', 'signature, ≤ 14 j'), ('Activé', '1er envoi ≤ 30 j<br>formation à J+5'), ('Récurrent', '≥ 3 envois / trim.<br>score de santé')]
    cx = [60 + round(i * 1544 / 6) for i in range(7)]
    els = [f'<p style="position:absolute;left:0px;top:0px;width:1300px;font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{BLEU}">LE COMMERCIAL EST RESPONSABLE JUSQU’À L’ACTIVATION</p>',
           f'<div style="position:absolute;left:{cx[0] - 20}px;top:44px;width:{cx[5] - cx[0] + 40}px;height:6px;background:{SARC};border-radius:3px"></div>',
           f'<div style="position:absolute;left:{cx[0] - 20}px;top:44px;width:6px;height:22px;background:{SARC}"></div>',
           f'<div style="position:absolute;left:{cx[5] + 14}px;top:44px;width:6px;height:22px;background:{SARC}"></div>',
           f'<div style="position:absolute;left:{cx[0]}px;top:113px;width:{cx[6] - cx[0]}px;height:6px;background:#2E5867"></div>']
    for i, x in enumerate(cx):
        if i == 5:
            els.append(f'<p style="position:absolute;left:{x - 44}px;top:72px;width:88px;height:88px;border-radius:50%;background:{OR};color:{NUIT};'
                       f'font-family:{L};font-size:38px;font-weight:700;text-align:center;line-height:88px">6</p>')
        else:
            bg = SARCF if i < 5 else '#4A7A88'
            els.append(f'<p style="position:absolute;left:{x - 32}px;top:84px;width:64px;height:64px;border-radius:50%;background:{bg};color:#FFFFFF;'
                       f'font-family:{L};font-size:28px;font-weight:700;text-align:center;line-height:64px">{i + 1}</p>')
    for i, (n, s) in enumerate(names):
        c = CHAMP if i == 5 else '#FFFFFF'
        sc = CHAMP if i == 5 else BRUME
        els.append(f'<p style="position:absolute;left:{cx[i] - 125}px;top:172px;width:250px;text-align:center;font-size:24px;line-height:1.35;color:{sc}">'
                   f'<b><span style="color:{c}">{n}</span></b><br>{s}</p>')
    route = f'<div style="position:relative;width:1664px;height:282px">{"".join(els)}</div>'
    sources = (f'<p style="font-size:24px;color:{BRUME}"><b><span style="color:{CHAMP}">Les prospects arrivent par</span></b> '
               f'formulaires entrants · recommandations · salons · terrain (caveaux) · comptes ciblés, en cadence</p>')

    scale = 500 / 120

    def rng(lbl, a, b, txt, kind, plabel):
        dashed = kind == 'HYPOTHÈSE'
        bar = (f'border:3px dashed {OR};background:rgba(200,164,92,0.15)' if dashed else f'background:{LIGHT_BORD}')
        tc = CHAMP if dashed else LIGHT_BORD
        if dashed:
            tx = (f'<p style="position:absolute;left:{round(a * scale)}px;top:2px;width:{round((b - a) * scale)}px;text-align:center;'
                  f'font-family:{L};font-size:24px;font-weight:600;color:{tc}">{txt}</p>')
        else:
            tx = (f'<p style="position:absolute;left:{round(b * scale) + 12}px;top:2px;width:150px;font-family:{L};font-size:24px;'
                  f'font-weight:600;color:{tc}">{txt}</p>')
        return (f'<div style="display:flex;align-items:center;gap:16px"><p style="width:290px;font-size:24px;color:#FFFFFF">{lbl}</p>'
                f'<div style="position:relative;width:500px;height:40px;background:rgba(255,255,255,0.08);border-radius:6px">'
                f'<div style="position:absolute;left:{round(a * scale)}px;top:6px;width:{round((b - a) * scale)}px;height:28px;border-radius:6px;{bar}"></div>'
                f'{tx}</div>'
                f'{pill(kind, label=plabel)}</div>')
    ticks = ''.join(f'<p style="position:absolute;left:{round(d * scale) - 40}px;top:0px;width:80px;text-align:center;font-size:24px;color:#8FB0BA">{d} j</p>'
                    for d in (30, 60, 90))
    cycle = f'''<div style="width:1060px;display:flex;flex-direction:column;gap:12px">
{label('Durée du cycle de vente', BLEU)}
{rng('Dossier standard', 7, 21, '7-21 j', 'OBJECTIF', 'OBJECTIF')}
{rng('Compte récurrent, offre combinée', 30, 60, '30-60 j', 'OBJECTIF', 'OBJECTIF')}
{rng('Maison de champagne', 42, 84, '6-12 sem.', 'HYPOTHÈSE', 'HYPOTHÈSE · TERRAIN')}
<div style="display:flex;gap:16px"><div style="width:290px"></div><div style="position:relative;width:500px;height:34px">{ticks}</div></div>
</div>'''
    vite = f'''<div style="flex:1;background:rgba(255,255,255,0.06);border-left:6px solid {OR};border-radius:14px;padding:20px 26px;display:flex;flex-direction:column;gap:10px">
{label('La vitesse, premier argument', CHAMP, ls=2)}
<p style="font-family:{T};font-size:30px;font-weight:700;line-height:1.2;color:#FFFFFF">Accusé de réception &lt; 1 h, proposition &lt; 24 h</p>
<p style="font-size:24px;font-style:italic;line-height:1.35;color:{BRUME}">« Un prospect qui a rempli un formulaire compare rarement plus de deux prestataires. »</p>
</div>'''
    inner = f'''{header('Vendre · Processus de vente', 'La vente finit au premier envoi, pas à la signature', OR, '#FFFFFF', tg='MON OUTIL')}
{sources}
{route}
<div style="flex:1;display:flex;gap:44px;align-items:flex-end">{cycle}{vite}</div>
{footer(12, 'Vendre', dark=True)}'''
    return 'processus', inner, dict(bg=NUIT, color=CLAIR, gap=26, sect="Vendre : processus de vente, tunnels SPIN et objections")


def spin():
    segs = [(3, 'Cadrer', '#E3EAEC', GRIS), (5, 'Contexte', '#D3E5EA', GRIS), (12, 'Questions SPIN · 12 min', PETROLE, '#FFFFFF'),
            (5, 'Reformuler', '#D3E5EA', GRIS), (5, 'Besoin → offre', '#D3E5EA', GRIS), (5, 'Décider', '#E3EAEC', GRIS)]
    bar = ''.join(f'<div style="flex:{n};height:56px;background:{bg};display:flex;align-items:center;justify-content:center">'
                  f'<p style="font-size:24px;font-weight:600;color:{fg};white-space:nowrap">{t}</p></div>' for n, t, bg, fg in segs)
    acc, ticks = 0, []
    for n, *_ in [(0,)] + segs:
        acc += n
        x = round(acc / 35 * 1664)
        if acc == 0:
            ticks.append(f'<p style="position:absolute;left:0px;top:0px;width:60px;font-size:24px;color:{GRISD}">0</p>')
        elif acc == 35:
            ticks.append(f'<p style="position:absolute;left:1544px;top:0px;width:120px;text-align:right;font-size:24px;color:{GRISD}">35 min</p>')
        else:
            ticks.append(f'<p style="position:absolute;left:{x - 30}px;top:0px;width:60px;text-align:center;font-size:24px;color:{GRISD}">{acc}</p>')
    timebar = f'''<div style="display:flex;flex-direction:column;gap:6px">
{label('Le rendez-vous de découverte : 35 minutes', SARCF, ls=2)}
<div style="display:flex;border-radius:10px;overflow:hidden;gap:3px">{bar}</div>
<div style="position:relative;width:1664px;height:32px">{''.join(ticks)}</div>
</div>'''
    legend = (f'<p style="font-size:24px;color:{GRIS}"><b><span style="color:{PETROLE}">S</span></b> Situation · '
              f'<b><span style="color:{PETROLE}">P</span></b> Problème · <b><span style="color:{PETROLE}">I</span></b> Implication · '
              f'<b><span style="color:{PETROLE}">N</span></b> Need-payoff, le bénéfice attendu (Neil Rackham) · ici, une question par étape</p>')
    lv = [('S', '#DCECEF', ENCRE, 800), ('P', BLEU, ENCRE, 730), ('I', SARC, '#FFFFFF', 660), ('N', PETROLE, '#FFFFFF', 590)]

    def funnel(title, color, qs):
        rows = ''.join(f'<div style="width:{w}px;height:72px;align-self:center;background:{bg};border-radius:12px;display:flex;align-items:center;gap:16px;padding:0px 22px">'
                       f'<p style="width:36px;font-family:{L};font-size:36px;font-weight:700;color:{fg}">{k}</p>'
                       f'<p style="flex:1;font-size:24px;line-height:1.25;color:{fg}">{q}</p></div>'
                       for (k, bg, fg, w), q in zip(lv, qs))
        return (f'<div style="flex:1;display:flex;flex-direction:column;gap:8px">{label(title, color, ls=2)}'
                f'<div style="display:flex;flex-direction:column;gap:8px">{rows}</div></div>')
    f1 = funnel('Tunnel 1 · Vigneron avec caveau', BORD, [
        'Comment gérez-vous le visiteur qui veut plus que sa valise ?',
        'Combien repartent en achetant moins que voulu ?',
        'Sur une saison, que représente ce manque en CA ?',
        'Livré chez lui, payé au comptoir : quel effet sur votre panier ?'])
    f2 = funnel('Tunnel 2 · Maison de champagne', PETROLE, [
        'Quels marchés et incoterms pour vos particuliers hors UE ?',
        'Où perdez-vous du temps : certificat CIVC, douane, suivi ?',
        "Que coûte un colis bloqué en douane à l'image de la maison ?",
        'Et si certificat et taxes étaient gérés à chaque envoi ?'])
    bottom = f'''<div style="display:flex;align-items:center;gap:22px">
<p style="font-size:24px;color:{GRIS}">En RDV : <b>1 S · 2 P · 2 I · 1 N</b></p>
{arrow(44, 26, OR, 3)}
<p style="flex:1;font-size:24px;font-weight:700;color:{ENCRE}">Sa phrase, notée mot pour mot, ouvre la proposition</p>
{pill('OBJECTIF', label='RDV → PROPOSITION ≥ 70 %')}
</div>'''
    inner = f'''{header('Vendre · Tunnels SPIN', 'Deux tunnels SPIN : le prospect chiffre sa perte', ORF, tg='MON OUTIL')}
{timebar}
{legend}
<div style="display:flex;gap:56px">{f1}{f2}</div>
<div style="flex:1"></div>
{bottom}
{footer(13, 'Vendre')}'''
    return 'spin', inner, dict(gap=20)


def objections():
    steps = [('Accueillir', SARC, '« Vous avez raison d’en parler. »', True),
             ('Clarifier', SARCF, "« Qu'est-ce qui vous fait dire ça ? »", True),
             ('Prouver, une fois', ORF, '12 btl vers les USA : <b>≈ 17,50 € de transport par bouteille</b>, payés par son client', False),
             ('Vérifier', PETROLE, "« Si ce point est réglé, qu'est-ce qui nous empêche de créer votre compte cette semaine ? »", True)]
    boxes = []
    for i, (n, c, txt, it) in enumerate(steps):
        st = 'font-style:italic;' if it else ''
        boxes.append(f'''<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {c};border-radius:14px;padding:16px 22px;display:flex;flex-direction:column;gap:8px">
<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{c}">{i + 1} · {n.upper()}</p>
<p style="font-size:24px;line-height:1.35;color:{ENCRE};{st}">{txt}</p></div>''')
        if i < 3:
            boxes.append(f'<div style="align-self:center">{arrow(36, 26, BLEU, 3)}</div>')
    top = f'''<div style="display:flex;flex-direction:column;gap:12px">
{label("La méthode en quatre temps, appliquée à « c'est cher »", ORF, ls=2)}
<div style="display:flex;gap:12px">{''.join(boxes)}</div></div>'''
    kw = ''.join(f'<p style="font-size:26px;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:999px;padding:6px 20px;white-space:nowrap">{k}</p>'
                 for k in ['Le prix', 'La casse', 'La chaleur', '« On a déjà quelqu’un »', 'Le temps'])
    left = f'''<div style="width:640px;display:flex;flex-direction:column;gap:16px">
{label('La banque', ORF, ls=2)}
<div style="display:flex;align-items:baseline;gap:16px">{num('26', 88, ORF)}<p style="font-size:28px;line-height:1.3;color:{ENCRE}">objections préparées,<br>dont 5 apprises mot pour mot</p></div>
<div style="display:flex;flex-wrap:wrap;gap:10px">{kw}</div>
<p style="font-size:24px;color:{GRISD}">Réponses du top 5 : diapo de secours B14</p>
</div>'''

    def ln(op, txt):
        return (f'<div style="display:flex;align-items:baseline;gap:14px"><p style="width:30px;font-size:30px;font-weight:700;color:{CHAMP}">{op}</p>'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    roi = f'''<div style="flex:1;background:{NUIT};border-radius:20px;padding:22px 28px;display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:center;gap:16px">{label('Le ROI, avec SES chiffres', CHAMP, ls=2)}<div style="flex:1"></div>{pill('HYPOTHÈSE', label='HYPOTHÈSE · EXEMPLE')}</div>
{ln('', '<b>30</b> visiteurs étrangers par semaine en saison')}
{ln('×', '<b>1 sur 3</b> repart frustré, soit 10 ventes perdues')}
{ln('×', '<b>300 €</b> de vin × <b>20</b> semaines')}
<div style="display:flex;align-items:baseline;gap:16px"><p style="width:30px;font-size:30px;font-weight:700;color:{CHAMP}">=</p>{num('60 000 €', 56, CHAMP)}<p style="font-size:24px;line-height:1.25;color:{BRUME}">de ventes de vin potentielles<br>pour le domaine</p></div>
<p style="font-size:24px;line-height:1.35;color:{CLAIR}">Si 1 vente sur 4 est récupérée : <b>15 000 €</b>, pour 110 € HT de cartons</p>
</div>'''
    inner = f'''{header('Vendre · Argumentaire et objections', 'Une objection, une seule preuve', ORF, tg='MON OUTIL')}
{top}
<div style="flex:1;display:flex;gap:48px;align-items:flex-end">{left}{roi}</div>
{footer(14, 'Vendre')}'''
    return 'objections', inner, dict(gap=28)


def ressources():
    def proof(icon, q, a):
        return (f'<div style="flex:1;display:flex;align-items:center;gap:16px;background:#FFFFFF;border:1px solid {FILET};border-radius:14px;padding:14px 18px">'
                f'<div style="width:60px;height:60px;border-radius:50%;background:{PETROLE};display:flex;align-items:center;justify-content:center;flex:none">'
                f'<x-icon name="{icon}" style="color:{CHAMP};width:34px;height:34px"></x-icon></div>'
                f'<div style="display:flex;flex-direction:column;gap:2px"><p style="font-family:{T};font-style:italic;font-size:26px;line-height:1.15;color:{ENCRE};white-space:nowrap">{q}</p>'
                f'<p style="font-size:24px;line-height:1.25;color:{GRIS}">{a}</p></div></div>')
    strip = f'''<div style="display:flex;gap:18px;align-items:stretch">
{proof('Chart', '« Combien ça coûte ? »', 'Le simulateur, sur SES vins')}
{proof('Trust', '« Et si ça casse ? »', 'Le carton ISTA 3A, sur la table')}
{proof('Star', '« Ça marche vraiment ? »', '4,8/5, 296 avis Google (sept. 2026)')}
<div style="width:470px;background:#E8F3F5;border:2px dashed {SARC};border-radius:14px;padding:12px 18px;display:flex;flex-direction:column;gap:2px">
<p style="font-family:{L};font-size:24px;font-weight:600;color:{PETROLE}">17 ressources : 13 validées, 4 à créer</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS}">vidéo démo · one-pager par ICP · études de cas autorisées · webinaire</p></div>
</div>'''
    months = ['sept.', 'oct.', 'nov.', 'déc.', 'janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.']
    MW = 80
    TW = MW * 11
    LW, HW, BW = 470, 110, 130
    mh = ''.join(f'<p style="position:absolute;left:{i * MW}px;top:0px;width:{MW}px;text-align:center;font-size:24px;color:{GRISD}">{m}</p>' for i, m in enumerate(months))
    mh += f'<div style="position:absolute;left:{4 * MW - 1}px;top:2px;width:2px;height:30px;background:{BLEU}"></div>'
    th = lambda t, w, al='left': f'<p style="width:{w}px;text-align:{al};font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">{t}</p>'
    head = (f'<div style="display:flex;align-items:center;gap:20px">{th("FEUILLE DE ROUTE 2026 → 2027", LW).replace(GRISD, PETROLE)}'
            f'<div style="position:relative;width:{TW}px;height:34px">{mh}</div>{th("Temps", HW, "right")}{th("Budget", BW, "right")}</div>')
    chantiers = [('Nettoyage CRM', 'Emma, Adam', 0, 1, '≥ 95 % des comptes prioritaires exploitables', '24 h', '0 €'),
                 ('One-pagers + landing page', 'Emma, Adam', 1, 1, 'supports validés par la direction', '36 h', '600 €'),
                 ('Séquences Brevo + reporting', 'Emma', 2, 1, 'arrêt automatique sur réponse testé', '20 h', '200 €'),
                 ('Tests LinkedIn, 3 clusters', 'Adam', 2, 7, 'coût par prospect qualifié comparé', '3 h/sem.', '900 €'),
                 ('Webinaire export', 'Emma + expert', 4, 1, '10 inscrits ICP, 3 diagnostics', '20 h', '300 €'),
                 ('Deux salons en visiteur', 'Adam, Emma', 4, 7, '8 RDV qualifiés par salon', '24 h', '1 000 €')]
    rows = ''
    for n, who, m0, ln_, crit, tm, bud in chantiers:
        x, w = m0 * MW + 3, ln_ * MW - 6
        inside = ln_ >= 5
        if inside:
            txt = f'<p style="position:absolute;left:{x + 14}px;top:9px;width:{w - 20}px;font-size:24px;color:#FFFFFF;white-space:nowrap">{crit}</p>'
        else:
            txt = f'<p style="position:absolute;left:{x + w + 12}px;top:9px;width:{TW - x - w - 12}px;font-size:24px;color:{GRIS};white-space:nowrap">{crit}</p>'
        rows += (f'<div style="display:flex;align-items:center;gap:20px;border-top:1px solid {FILET};padding:3px 0px">'
                 f'<p style="width:{LW}px;font-size:24px;line-height:1.2;color:{ENCRE}"><b>{n}</b> <span style="color:{GRISD}">· {who}</span></p>'
                 f'<div style="position:relative;width:{TW}px;height:52px"><div style="position:absolute;left:{x}px;top:8px;width:{w}px;height:36px;border-radius:8px;background:{PETROLE if inside else SARC}"></div>{txt}</div>'
                 f'<p style="width:{HW}px;text-align:right;font-size:24px;color:{GRIS}">{tm}</p>'
                 f'<p style="width:{BW}px;text-align:right;font-family:{L};font-size:28px;font-weight:600;color:{PETROLE}">{bud}</p></div>')
    total = (f'<div style="display:flex;align-items:center;gap:20px;border-top:2px solid {PETROLE};padding-top:8px">'
             f'<p style="flex:1;font-size:24px;color:{ENCRE}"><b>Pas de critère atteint, pas d’étape suivante.</b> Plafond de dépenses externes ; le temps interne se réserve.</p>'
             f'{pill("OBJECTIF", label="OBJECTIF")}<p style="width:{HW + 60}px;text-align:right;font-size:24px;color:{GRIS}">≈ 200 h (calcul)</p>'
             f'<p style="width:{BW}px;text-align:right;font-family:{L};font-size:32px;font-weight:700;color:{PETROLE}">3 000 €</p></div>'
             )
    inner = f'''{header('Piloter · Ressources', 'Une preuve par doute, six chantiers chiffrés', PETROLE, tg='MON OUTIL')}
{strip}
<div style="display:flex;flex-direction:column;gap:0px">{head}{rows}{total}</div>
{footer(15, 'Piloter')}'''
    return 'ressources', inner, dict(gap=24, sect="Piloter : ressources, Sales Operations et indicateurs")


def salesops():
    def sat(x, y, name, obj, kind='old'):
        if kind == 'old':
            st = f'background:#FFFFFF;border:2px solid #B8C4C8'
            nc = ENCRE
        else:
            st = f'background:#E8F4F6;border:3px dashed {SARC}'
            nc = SARCF
        return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:330px;height:150px;border-radius:14px;{st};padding:12px 18px;display:flex;flex-direction:column;gap:4px">'
                f'<p style="font-size:24px;font-weight:700;color:{nc}">{name}</p><p style="font-size:24px;line-height:1.25;color:{GRIS}">{obj}</p></div>')
    hub = f'''<div style="position:relative;width:1000px;height:560px">
<svg style="position:absolute;left:0px;top:0px" width="1000" height="560" viewBox="0 0 1000 560"><defs><marker id="m" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="{GRISD}"/></marker></defs>
<path d="M 330 75 L 410 190" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 590 190 L 664 98" stroke="{GRISD}" stroke-width="4" stroke-dasharray="12 9" fill="none" marker-end="url(#m)"/>
<path d="M 330 280 L 365 280" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 635 280 L 670 280" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 330 485 L 410 370" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 590 370 L 670 485" stroke="{SARC}" stroke-width="4" stroke-dasharray="12 9" fill="none"/></svg>
{sat(0, 0, "Planet'Connect", 'exécuter et tracer chaque envoi')}
{sat(670, 0, 'Brevo', 'relancer sans oublier, stop sur réponse')}
{sat(0, 205, 'Dashboards', 'CA et délais réels, pour la revue mensuelle')}
{sat(670, 205, 'Workspace + WhatsApp', 'une seule source de documents officiels')}
{sat(0, 410, 'E-signature + Drive', 'documentation re-signée chaque année')}
{sat(670, 410, 'Dictionnaire CRM', 'hygiène ≥ 95 % chaque lundi', 'new')}
<div style="position:absolute;left:365px;top:145px;width:270px;height:270px;border-radius:50%;background:{NUIT};border:6px solid {SARC};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
<p style="font-family:{T};font-size:44px;font-weight:700;color:#FFFFFF">HubSpot</p><p style="font-size:24px;color:{BRUME}">source de vérité</p>
<p style="font-size:24px;text-align:center;line-height:1.25;color:{BLEU}">contact loggé<br>&lt; 24 h</p></div>
</div>'''
    legend = (f'<div style="display:flex;gap:26px;align-items:center">'
              f'<div style="display:flex;align-items:center;gap:10px"><div style="width:30px;height:22px;border:2px solid #B8C4C8;border-radius:4px;background:#FFFFFF"></div><p style="font-size:24px;color:{GRIS}">outil existant, objectif fixé</p></div>'
              f'<div style="display:flex;align-items:center;gap:10px"><div style="width:26px;height:26px;border:5px solid {SARC};border-radius:50%"></div><p style="font-size:24px;color:{GRIS}">règle du playbook</p></div>'
              f'<div style="display:flex;align-items:center;gap:10px"><div style="width:30px;height:22px;border:3px dashed {SARC};border-radius:4px"></div><p style="font-size:24px;color:{GRIS}">proposé ou à venir</p></div></div>')
    stairs = ''
    for h, d, s, t, c in [(220, 'J+30', 'CERTIFIÉ', 'simulation sans aide, top 5 objections', SARC), (260, 'J+60', 'AUTONOME', '1 RDV obtenu seul', SARCF), (300, 'J+90', 'PILOTE', '1 amélioration du playbook', PETROLE)]:
        stairs += (f'<div style="flex:1;height:{h}px;background:{c};border-radius:12px 12px 0px 0px;padding:14px 16px;display:flex;flex-direction:column;gap:2px">'
                   f'{num(d, 36, "#FFFFFF")}'
                   f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:1px;color:{CHAMP}">{s}</p>'
                   f'<p style="font-size:24px;line-height:1.25;color:#FFFFFF">{t}</p></div>')
    rit = ''.join(f'<p style="font-size:24px;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:999px;padding:4px 14px;white-space:nowrap"><b>{a}</b> {b}</p>'
                  for a, b in [('Jour', '10 min'), ('Semaine', '45 + 30 min'), ('Mois', '45 min'), ('Trimestre', '90 min')])
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:14px">
{label('Intégrer un commercial en 90 jours', PETROLE, ls=2)}
<div style="display:flex;gap:10px;align-items:flex-end">{stairs}</div>
<p style="font-size:24px;font-style:italic;line-height:1.3;color:{GRIS}">« On observe avant de faire, on fait accompagné avant de faire seul. »</p>
<div style="flex:1"></div>
<div style="display:flex;align-items:center;gap:14px">{label('Rituels', PETROLE, ls=2)}{pill('PROPOSÉ', label='PROPOSÉS')}</div>
<div style="display:flex;flex-wrap:wrap;gap:8px">{rit}</div>
</div>'''
    inner = f'''{header('Piloter · Sales Operations', 'Une donnée, un propriétaire, une décision', PETROLE, tg='MES PROPOSITIONS')}
<div style="flex:1;display:flex;gap:56px">
<div style="width:1000px;display:flex;flex-direction:column;gap:14px">{hub}{legend}</div>
{right}</div>
{footer(16, 'Piloter')}'''
    return 'salesops', inner, dict(gap=32)


def kpi():
    TW = 517

    def gauge(lbl, val, unit, fill, target, note, color=SARCF, cap=False):
        zone = (f'<div style="position:absolute;left:{round(TW * target)}px;top:7px;width:{TW - round(TW * target)}px;height:14px;border-radius:0px 7px 7px 0px;'
                f'background:repeating-linear-gradient(45deg, #E9B79A 0px, #E9B79A 6px, #F6E2D6 6px, #F6E2D6 12px)"></div>') if cap else ''
        return f'''<div style="display:flex;flex-direction:column;gap:4px">
<p style="font-size:24px;color:{GRIS}">{lbl}</p>
<div style="display:flex;align-items:baseline;gap:10px">{num(val, 48, color)}<p style="flex:1;font-size:24px;color:{GRISD}">{unit}</p><p style="font-size:24px;font-weight:600;color:{color}">{note}</p></div>
<div style="position:relative;width:{TW}px;height:28px"><div style="position:absolute;left:0px;top:7px;width:{TW}px;height:14px;border-radius:7px;background:{FILET}"></div>{zone}
<div style="position:absolute;left:0px;top:7px;width:{round(TW * fill)}px;height:14px;border-radius:7px;background:{color}"></div>
<div style="position:absolute;left:{round(TW * target) - 2}px;top:0px;width:4px;height:28px;background:{ENCRE}"></div></div></div>'''

    def goal(lbl, val, note):
        return f'''<div style="display:flex;flex-direction:column;gap:4px">
<p style="font-size:24px;color:{GRIS}">{lbl}</p>
<div style="display:flex;align-items:baseline;gap:10px">{num(val, 48, BORD)}<p style="flex:1;text-align:right;font-size:24px;color:{GRISD}">{note}</p></div>
<div style="width:{TW}px;height:28px;display:flex;align-items:center"><div style="width:{TW}px;height:14px;border-radius:7px;border:2px dashed {BORD}"></div></div></div>'''
    c1 = f'''<div style="display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:12px">{pill('CONSTATÉ')}<p style="font-size:24px;color:{GRISD}">au 24/09/2026</p></div>
{gauge('Nouveaux adhérents signés, 12 mois', '~145', '/ 120 visés', 145 / 160, 120 / 160, '✓ dépassé')}
{gauge('Commandes annulées (plafond 2 %)', '1,45 %', '/ &lt; 2 %', 1.45 / 2.5, 2 / 2.5, '✓ sous le plafond', cap=True)}
{gauge('Envois assurés (option 3 %)', '89,8 %', '/ 90 %', 0.898, 0.90, '≈ 0,2 pt')}
</div>'''
    nodes = [('24/09/2026 · point zéro', '6 643 envois · 64,5 % vers les USA', SARCF),
             ('90 jours de mesure', 'sans maquiller : contact, RDV tenus, activation', SARC),
             ('Fin déc. 2026 · M+3', 'première lecture avant / après', OR),
             ('Puis chaque trimestre', 'cibles fixées par segment et par offre', PETROLE)]
    dots = ''.join(f'<div style="position:absolute;left:0px;top:{6 + i * 112}px;width:26px;height:26px;border-radius:50%;background:{c}"></div>' for i, (_, _, c) in enumerate(nodes))
    txt = ''.join(f'<div style="position:absolute;left:52px;top:{i * 112}px;width:450px;display:flex;flex-direction:column;gap:2px">'
                  f'<p style="font-size:26px;font-weight:700;color:{ENCRE}">{a}</p><p style="font-size:24px;line-height:1.3;color:{GRIS}">{b}</p></div>' for i, (a, b, _) in enumerate(nodes))
    c2 = f'''<div style="display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:12px">{pill('POINT ZÉRO')}<p style="font-size:24px;color:{GRISD}">la méthode</p></div>
<div style="position:relative;width:500px;height:420px"><div style="position:absolute;left:11px;top:20px;width:4px;height:330px;background:{FILET}"></div>{dots}{txt}</div>
</div>'''
    c3 = f'''<div style="display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:12px">{pill('OBJECTIF')}<p style="font-size:24px;color:{GRISD}">pas encore mesuré</p></div>
{goal('Activation : 1er envoi à J+30', '≥ 70 %', 'alerte sous 50 %')}
{goal('Adhérents actifs (1 envoi / 90 j)', '&gt; 60 %', 'sinon : campagne réveil')}
{goal('Taux de gain (win rate) : gagnées / clôturées', '40-60 %', 'à recaler à 90 j')}
</div>'''
    leg = ''.join(pill(k) for k in ['CONSTATÉ', 'OBJECTIF', 'HYPOTHÈSE', 'PROJET'])
    bottom = (f'<div style="display:flex;align-items:center;gap:16px;background:#FFFFFF;border:1px solid {FILET};border-radius:12px;padding:10px 22px">'
              f'<x-icon name="Clock" style="color:{PETROLE};width:36px;height:36px"></x-icon>'
              f'<p style="flex:1;font-size:24px;color:{ENCRE}"><b>Revue mensuelle de 45 min</b>, close par une décision</p>'
              f'<div style="display:flex;gap:8px">{leg}</div></div>')
    inner = f'''{header('Piloter · Indicateurs', 'Mesuré ou espéré ? Chaque chiffre dit son statut', PETROLE, tg='MON OUTIL')}
<div style="flex:1;display:grid;grid-template-columns:repeat(3, 1fr);gap:56px">{c1}{c2}{c3}</div>
{bottom}
{footer(17, 'Piloter')}'''
    return 'kpi', inner, dict(gap=30)


def synthese():
    rows = [('Users', 'Recruter les bons comptes', '448 prospects non qualifiés', '5 ICP, 5 personas, un score PA-FIT', 'l’adéquation prime sur la taille'),
            ('PaperPlane', 'Activer et fidéliser', 'Activation jamais mesurée', '1er envoi ≤ 30 j, score de santé, réveil', 'un signé jamais activé ne vaut rien'),
            ('Book', 'Transmettre et mesurer', 'Des chiffres divergents', 'Parcours 30-60-90, chiffres datés à statut', 'le savoir tenait dans quelques têtes')]
    body = ''
    for ic, e, av, ap, why in rows:
        body += f'''<div style="flex:1;display:flex;align-items:center;gap:18px;border-top:1px solid {FILET}">
<div style="width:58px;height:58px;border-radius:50%;background:{CHAMP};display:flex;align-items:center;justify-content:center;flex:none"><x-icon name="{ic}" style="color:{NUIT};width:32px;height:32px"></x-icon></div>
<p style="width:200px;font-family:{T};font-size:30px;font-weight:700;line-height:1.15;color:{ENCRE}">{e}</p>
<p style="width:220px;background:#ECEFF0;border-radius:12px;padding:10px 14px;font-size:24px;line-height:1.3;color:{GRIS}">{av}</p>
<div style="width:40px">{arrow(40, 26, SARC, 3)}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><p style="background:#FFFFFF;border-left:6px solid {SARC};border-radius:12px;padding:8px 14px;font-size:24px;font-weight:600;line-height:1.3;color:{ENCRE}">{ap}</p>
<p style="font-size:24px;font-style:italic;color:{GRISD};padding-left:20px">car {why}</p></div>
</div>'''
    heads = (f'<div style="display:flex;gap:18px"><div style="width:276px"></div><p style="width:220px;font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{GRISD}">AVANT</p>'
             f'<div style="width:40px"></div><p style="flex:1;font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{SARCF}">AVEC LE PLAYBOOK</p></div>')
    start = (f'<p style="font-size:26px;line-height:1.3;color:{GRIS}"><b><span style="color:{PETROLE}">Point de départ :</span></b> aucun playbook, '
             f'mais des outils et des procédures solides, que le playbook relie et encadre.</p>')
    left = f'<div style="width:1080px;display:flex;flex-direction:column;gap:6px">{heads}{body}</div>'

    def verb(v, txt):
        return (f'<div style="display:flex;flex-direction:column;gap:4px">{label(v, CHAMP, ls=2)}'
                f'<p style="font-size:24px;line-height:1.35;color:{CLAIR}">{txt}</p></div>')
    right = f'''<div style="flex:1;background:{NUIT};border-radius:20px;padding:20px 26px;display:flex;flex-direction:column;gap:12px">
<p style="font-family:{T};font-size:34px;font-weight:700;color:#FFFFFF">Mon apport</p>
{verb('Analysé', 'Top 10 → 5 ICP · 47 réponses sur 70 · 25 sources · enquêtes recalculées')}
{verb('Conçu et rédigé', 'Pipeline et SLA · SPIN · 26 objections · PA-FIT · KPI à statut · 30-60-90')}
{verb('Proposé, à ratifier', 'Règles CRM · rituels · câblage Brevo-HubSpot')}
</div>'''
    ben = (f'<div style="display:flex;align-items:center;gap:12px"><p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;color:{PETROLE};white-space:nowrap">BÉNÉFICES ATTENDUS</p><div style="flex:1"></div>'
           f'{pill("OBJECTIF", "letter-spacing:0px", "≥ 70 % des signés actifs à J+30")}{pill("OBJECTIF", "letter-spacing:0px", "Commercial certifié à J+30")}'
           f'{pill("POINT ZÉRO", "letter-spacing:0px", "Part USA suivie chaque trimestre")}</div>')
    inner = f'''{header('Synthèse', 'Du bouche-à-oreille à une méthode', PETROLE)}
{start}
<div style="flex:1;display:flex;gap:40px">{left}{right}</div>
{ben}
{footer(18, label='Synthèse et ouverture')}'''
    return 'synthese', inner, dict(gap=20, sect="Synthèse, ouverture et retour à l'accroche")


def ouverture():
    diffs = [('Des chiffres divergents', 'une source unique datée'), ('Des projets mouvants', 'le conditionnel'), ('Tout dire en un document', 'un socle et des annexes')]
    dd = ''.join(f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:24px;color:{GRIS}">{a}</p>'
                 f'<p style="font-size:26px;font-weight:700;color:{ENCRE}">→ {b}</p></div>' for a, b in diffs)
    diff = (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {OR};border-radius:14px;padding:16px 24px;display:flex;flex-direction:column;gap:10px">'
            f'{label("Trois difficultés, trois règles", ORF, ls=2)}<div style="display:flex;gap:30px">{dd}</div></div>')
    ms = [('Nov. 2026', "Retours de l'équipe intégrés · objections classées sur nos motifs de perte · câblage Brevo-HubSpot", SARCF),
          ('Fin déc. 2026', 'Première lecture avant / après, à M+3 du point zéro', ORF),
          ('T1 2027', 'Entretiens clients pour les personas · documentation 2027 · études de cas autorisées', BORD),
          ('2027 et après', 'La même méthode pour diversifier : Royaume-Uni, UE, Japon', PETROLE)]
    cols = ''
    for i, (d, t, c) in enumerate(ms):
        cols += f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<div style="display:flex;align-items:center"><div style="width:30px;height:30px;border-radius:50%;background:{c};flex:none"></div><div style="flex:1;height:6px;background:{BLEU if i < 3 else 'transparent'}"></div></div>
{num(d, 40, c)}
<p style="font-size:24px;line-height:1.35;color:{ENCRE};padding-right:24px">{t}</p></div>'''
    projets = f'''<div style="border:3px dashed {GRISD};border-radius:18px;padding:16px 26px;display:flex;align-items:center;gap:26px">
{pill('PROJET', label='PROJETS · CONDITIONNEL')}
<p style="flex:1;font-size:24px;line-height:1.35;color:{GRIS}">Voile-cargo VELA · annexe en Champagne · entrepôt certifié · filiale autonome : ils n’entreraient dans le playbook que s’ils aboutissent.</p>
<p style="font-family:{T};font-style:italic;font-size:28px;color:{ENCRE};width:300px">Une trajectoire, jamais un acquis.</p></div>'''
    inner = f'''{header('Ouverture', 'Un playbook vivant, une suite déjà datée', PETROLE)}
{diff}
<div style="flex:1"></div>
<div style="display:flex;align-items:center;gap:14px">{pill('OBJECTIF', label='JALONS DATÉS')}<p style="font-size:24px;color:{GRISD}">version 2.1 d'octobre 2026, revue chaque trimestre</p></div>
<div style="display:flex">{cols}</div>
<div style="flex:1"></div>
{projets}
{footer(19, label='Synthèse et ouverture')}'''
    return 'ouverture', inner, dict(gap=26)


def cloture():
    inner = f'''<div style="flex:1;display:flex;gap:64px">
<div style="flex:1;display:flex;flex-direction:column;gap:26px">
{eyebrow('Retour au caveau', BLEU)}
<p style="font-family:{T};font-size:84px;font-weight:700;line-height:1.05;color:#FFFFFF">Ils repartent<br>les mains libres.</p>
<div style="flex:1"></div>
{bottles(24, width=1120, bw=34, bh=102)}
<p style="font-size:30px;line-height:1.35;color:{BRUME}">24 bouteilles · <b><span style="color:{CHAMP}">360 € de transport</span></b> en groupage + taxes estimées, réglées d'avance · ~3 semaines estimées</p>
<div style="flex:1"></div>
<p style="font-family:{T};font-style:italic;font-size:36px;line-height:1.25;color:{CHAMP}">Le prospect n'achète pas un transport : il cherche à réduire son risque.</p>
</div>
<div style="width:440px;display:flex;flex-direction:column;justify-content:space-between;align-items:flex-end">
<div style="background:#FFFFFF;border-radius:18px;padding:14px;transform:rotate(-2deg)"><img src="{PHOTO_CARTON}" alt="Photo : un colis d’expédition remis par l’équipe Planet Aura" style="width:400px;height:520px;object-fit:cover;border-radius:10px"></div>
<div style="display:flex;align-items:center;gap:20px">
<img src="{LOGO_MARK_W}" alt="Logo Planet Aura" style="width:66px;height:88px;object-fit:contain">
<div style="display:flex;flex-direction:column;gap:2px"><p style="font-family:{T};font-size:56px;font-weight:700;line-height:1;color:#FFFFFF">Merci.</p><p style="font-size:28px;color:{BRUME}">Place à vos questions</p></div>
</div></div>
</div>'''
    return 'cloture', inner, dict(bg=NUIT, color=CLAIR, pad='104px 128px 96px', gap=0)
