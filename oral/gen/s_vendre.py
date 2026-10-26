# Diapos 8 à 15 : cibler (ICP + qualification du cas, personas), vendre (solutions, processus, prospection, SPIN, proposition), activer
from kit import *

GRID = '/_blob/9d99493db14f73e1949e42e9c9bcbe4a'  # grille officielle 2026, USA groupage (annexe F, p. 132 du dossier), sans la colonne des délais

SECT_CIBLER = 'Cibler et vendre : le cas fil rouge, de la qualification à la signature'
SECT_ACTIVER = 'Activer : la vente finit au premier envoi'


def _check(ok):
    c = SARCF if ok else '#B9C5CA'
    t = '✓' if ok else '–'
    return (f'<div style="width:34px;height:34px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{t}</p></div>')


def icp():
    # Message : le score ne juge pas la taille, il juge la preuve.
    # Point focal : trois barres qui montent, 45 -> 60 -> 85 ; plein = acquis au départ (la fiche), hachuré = prouvé ensuite.
    # À gauche, en appui : les 5 critères ICP, puis « Ma recommandation » (60 % de l'effort sur les caveaux).
    # Détail du barème (8 critères, plafonds, seuils) : secours B2 ; profil complet du domaine et tiers B : secours B16.
    k = 3.0  # px par point du score
    hatch = f'repeating-linear-gradient(45deg, {ORF} 0px, {ORF} 7px, #E9D9B8 7px, #E9D9B8 14px)'

    def seg(pts, bg, top=False):
        r = '10px 10px 0px 0px' if top else '0px'
        return f'<div style="width:150px;height:{round(pts * k)}px;background:{bg};border-radius:{r}"></div>'

    # (score, palier, couleur, segments de haut en bas, preuve) ; la fiche prouve 45 points, puis échéance (+15), décideur et douleur (+25)
    # paliers du barème, mêmes mots que le secours B2 : nurture (35-54), P2 (55-74), P1 (75-100) ; « cadence » est dit dans la note
    steps = [('45', 'nurture', SARCF, [(45, SARCF)], 'caveau · clientèle US<br>60–100 envois/an'),
             ('60', 'P2', ORF, [(15, hatch), (45, SARCF)], '+ échéance datée'),
             ('85', 'P1', ORF, [(25, hatch), (15, hatch), (45, SARCF)], '+ décideur + douleur')]
    AW = 52
    slot = f'<div style="width:{AW}px;flex:none"></div>'
    ar = f'<div style="width:{AW}px;flex:none;align-self:center;display:flex;justify-content:center">{arrow(AW, 30, ORF, 4)}</div>'
    bars, caps = [], []
    for v, st, c, segs, proof in steps:
        stack = ''.join(seg(n, bg, top=(i == 0)) for i, (n, bg) in enumerate(segs))
        bars.append(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:12px">'
                    f'<div style="display:flex;align-items:baseline;gap:10px">{num(v, 72, c)}'
                    f'<p style="font-family:{L};font-size:30px;font-weight:700;color:{c};white-space:nowrap">{st}</p></div>'
                    f'<div style="display:flex;flex-direction:column;gap:3px">{stack}</div></div>')
        caps.append(f'<div style="flex:1;display:flex;justify-content:center">'
                    f'<p style="font-size:24px;line-height:1.3;text-align:center;color:{c}">{proof}</p></div>')
    right = f'''<div style="flex:1;{CASE_BOX};border-radius:18px;padding:22px 30px 24px 30px;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:center;gap:14px">{label('Le domaine du cas, au score PA-FIT', ORF, ls=2)}<div style="flex:1"></div>{pill('ILLUSTRATIF', 'align-self:center', label='POINTS ILLUSTRATIFS')}</div>
<div style="flex:1"></div>
<div style="display:flex;align-items:flex-end;gap:10px;border-bottom:3px solid #D9CBA8">{bars[0]}{ar}{bars[1]}{ar}{bars[2]}</div>
<div style="display:flex;gap:10px">{caps[0]}{slot}{caps[1]}{slot}{caps[2]}</div>
</div>'''

    crit = ''.join(f'''<div style="display:flex;align-items:center;gap:16px"><div style="width:40px;height:40px;border-radius:50%;background:{BORD};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{i}</p></div>
<p style="font-size:28px;line-height:1.25;color:{ENCRE}">{t}</p></div>''' for i, t in enumerate(['Clientèle étrangère', 'Bouteille &gt; 12 €', 'Responsable caveau ou e-shop', 'Destinations, USA en tête', 'Saisonnalité'], 1))
    left = f'''<div style="width:600px;flex:none;display:flex;flex-direction:column;gap:14px">
{label('5 critères ICP', BORD, size=26, ls=3)}
<div style="display:flex;flex-direction:column;gap:12px">{crit}</div>
<div style="flex:1;min-height:24px"></div>
<div style="background:{NUIT};border-radius:16px;padding:18px 26px 22px 26px;display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:center;gap:14px">{label('Ma recommandation', CHAMP, ls=2)}<div style="flex:1"></div>{pill('OBJECTIF', 'align-self:center')}</div>
{num('60 %', 60, '#FFFFFF')}
<p style="font-size:28px;line-height:1.3;color:{CLAIR}">de l’effort sur les caveaux</p>
</div>
</div>'''
    # marge basse : 64 px de padding + 66 px d'entretoise + 30 px d'écart = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que la diapo « offre » : au rendu +10 %, le gras du pied de page (épinglé) n'est plus compté dans le flux.
    inner = f'''{head_case(header3('Cibler · Partie 8 · ICP', 'Le score ne juge pas la taille : il juge la preuve', BORD, tags=['MON ANALYSE', 'MA CONTRIBUTION']), 'Qualifier')}
<div style="flex:1;display:flex;gap:56px">{left}{right}</div>
<div style="height:66px;flex:none"></div>
{footer(8, 'Cibler')}'''
    return 'icp', inner, dict(gap=30, pad='128px 128px 64px', sect=SECT_CIBLER)


def personas():
    # Message : un domaine, trois interlocuteurs (décide, utilise, paie), et à chacun son discours.
    # Point focal : les trois rôles en tête de carte, et sous chacun sa citation, en grand.
    # Craintes et preuves montrées : dites dans la note ; fiches complètes (canal, KPI) : dossier, chap. 07 ;
    # détail de l'étude (angle mort ADV, limite, base) : note + secours B1 ; verdict « 5/5 confirmés » à l'écran (v4, B1).
    cols = [('Décide', 'Vigneron-propriétaire', BORD, 'encore un prestataire qui\u00a0promet', 'Je lui dis',
             '« Vous remettez le colis, on\u00a0s’occupe de tout. »', ''),
            ('Utilise', 'Responsable caveau', SARCF, 'un client mécontent qui laisse un avis\u00a0négatif', 'Je lui dis',
             '« Le simulateur donne un prix en 20 secondes, pendant la\u00a0dégustation. »', ''),
            ('Paie', 'Client final étranger', ORF, 'des taxes ou frais surprises à\u00a0la\u00a0livraison', 'Le caveau lui dit',
             '« About €360 shipping for 24 bottles, plus prepaid duties and a €17 fee; insurance option: 3%. »',
             pill('GRILLE 2026', 'align-self:center'))]
    cards = ''
    # « Craint » réserve deux lignes (2 × 24 × 1,3 ≈ 63 px) : filets, « Je lui dis » et citations alignés d'une carte à l'autre
    for role, name, c, fear, who, say, st in cols:
        who_p = f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">{who}</p>'
        # carte 3 : le statut GRILLE 2026 monte sur la ligne du libellé, au-dessus des chiffres qu'il qualifie ;
        # une entretoise vide (sans texte) à la hauteur de la pastille garde les trois citations alignées
        who_row = (f'<div style="display:flex;align-items:center;gap:12px">{who_p}<div style="flex:1"></div>'
                   f'<div style="width:0;height:44px;flex:none"></div>{st}</div>')
        cards += f"""<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-radius:16px;overflow:hidden;display:flex;flex-direction:column">
<div style="background:{c};padding:12px 28px">{label(role, '#FFFFFF', size=30, ls=5)}</div>
<div style="padding:18px 28px 24px 28px;display:flex;flex-direction:column;gap:14px">
<p style="font-family:{T};font-size:36px;font-weight:700;line-height:1.15;color:{ENCRE}">{name}</p>
<p style="font-size:24px;line-height:1.3;min-height:63px;color:{GRIS}"><b><span style="color:{TXT.get(c, c)}">Craint</span></b> : {fear}</p>
<div style="height:2px;background:{FILET}"></div>
{who_row}
<p style="font-family:{T};font-style:italic;font-size:32px;line-height:1.3;color:{ENCRE}">{say}</p>
</div>
</div>"""
    stat = lambda n, t: (f'<div style="display:flex;align-items:baseline;gap:10px">{num(n, 48, PETROLE)}'
                         f'<p style="font-size:26px;color:{GRIS}">{t}</p></div>')
    study_lab = label('Confrontés au réel, oct.\u00a02026', PETROLE, size=24, ls=2)
    study = f"""<div style="background:#FFFFFF;border:1px solid {FILET};border-radius:16px;padding:12px 28px;display:flex;align-items:center;gap:40px">
{study_lab}
{stat('70', 'contacts')}{stat('47', 'réponses')}{stat('15', 'avis')}
{pill('CONSTATÉ', extra='align-self:center')}
<div style="flex:1"></div>
<p style="font-size:26px;font-weight:700;color:{ENCRE};white-space:nowrap">5/5 confirmés</p></div>"""
    sp = '<div style="flex:1;min-height:28px"></div>'
    # marge basse : padding 64 + entretoise 96 = les 160 px habituels (bas du corps à 920) ;
    # même dispositif que les candidates icp, offre et processus : au rendu +10 %, le gras du pied de page épinglé
    # n'est plus compté dans le flux.
    inner = f"""{header3('Cibler · Partie 9 · Personas', 'Un domaine, trois interlocuteurs, trois discours', BORD, tags=['MON ANALYSE', 'MA CONTRIBUTION'])}
{sp}
<div style="display:flex;gap:32px;align-items:stretch">{cards}</div>
{sp}
{study}
<div style="height:96px;flex:none"></div>
{footer(9, 'Cibler')}"""
    return 'personas', inner, dict(gap=0, pad='128px 128px 64px')


def _solutions_cross(c):
    # croix de refus dessinée (un « × » typographique compterait comme un mot visible)
    return (f'<svg width="18" height="18" viewBox="0 0 18 18"><path d="M3 3 L15 15 M15 3 L3 15" stroke="{c}" '
            f'stroke-width="3.2" stroke-linecap="round" fill="none"/></svg>')


def _solutions_stat(n, t):
    # grand chiffre + sa légende, jamais collés (gap 14 px) ; colonne du chiffre assez large pour le rendu +10 %
    return (f'<div style="display:flex;align-items:center;gap:14px">'
            f'<div style="width:96px;flex:none">{num(n, 68, BORD)}</div>'
            f'<p style="font-size:28px;line-height:1.2;color:{ENCRE}">{t}</p></div>')


def _solutions_item(t):
    # un composant de la solution : puce dorée + texte (retrait suspendu si le texte passe à la ligne)
    return (f'<div style="display:flex;align-items:flex-start;gap:14px">'
            f'<div style="padding-top:13px;flex:none"><svg width="12" height="12" viewBox="0 0 12 12"><circle cx="6" cy="6" r="6" fill="{CHAMP}"/></svg></div>'
            f'<p style="font-size:30px;font-weight:600;line-height:1.25;color:#FFFFFF">{t}</p></div>')


def solutions():
    # Message (titre) : chaque solution répond à un problème, et se prouve.
    # Point focal : la chaîne du cas, problème → besoin → solution → bénéfice → preuve, le pavé sombre « Solution » au centre.
    # Bandeau d'argument : ce que nous refusons (savoir dire non).
    # Hors écran : « Même logique, autres cibles » (champagne, caviste) et « Pourquoi c'est différenciant » → note ;
    # différenciation face aux concurrents : secours B3 ; assurance en option à 3 % : secours B14.
    # « > 21° hors spiritueux USA » retiré du bandeau (refus le moins lisible en 3 s) : indication non dite de la note, dossier chap. 08.
    steps = [('Problème', BORD, 1, f'<div style="display:flex;flex-direction:column;gap:16px">'
                                   f'{_solutions_stat("24", "bouteilles voulues")}{_solutions_stat("2", "emportées")}</div>'),
             ('Besoin', ORF, 1, 'Livrer chez lui, sans douane ni&#160;paperasse pour&#160;le&#160;domaine'),
             ('Solution', PETROLE, 1.45, f'<div style="display:flex;flex-direction:column;gap:14px">'
                                        f'{_solutions_item("Simulateur au&#160;comptoir")}{_solutions_item("Groupage USA&#160;DDP")}{_solutions_item("Cartons ISTA 3A")}</div>'),
             ('Bénéfice', SARCF, 1, 'Caisse vendue, transport payé par&#160;le&#160;client'),
             ('Preuve', '#2F7A50', 1, 'Simulation sur ses vins, carton en&#160;main')]
    chain = ''
    for i, (k, c, fl, t) in enumerate(steps):
        sol = k == 'Solution'
        bg = f'background:{PETROLE}' if sol else f'background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {c}'
        body = t if t.startswith('<div') else f'<p style="font-size:30px;font-weight:500;line-height:1.25;color:{ENCRE}">{t}</p>'
        chain += (f'<div style="flex:{fl};{bg};border-radius:16px;padding:{"36px" if sol else "28px"} 22px 34px 22px;display:flex;flex-direction:column;gap:18px">'
                  f'<p style="font-family:{L};font-size:26px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{CHAMP if sol else TXT.get(c, c)}">{k}</p>'
                  f'{body}</div>')
        if i < len(steps) - 1:
            chain += f'<div style="display:flex;align-items:center;flex:none">{arrow(32, 26, OR, 4)}</div>'
    cas = (f'<div style="display:flex;align-items:center;gap:16px">'
           f'<p style="font-family:{L};font-size:26px;font-weight:700;letter-spacing:2px;color:{ORF}">LE CAS</p>'
           f'<p style="font-size:28px;color:{ENCRE}">Domaine avec caveau</p>{pill("ILLUSTRATIF", extra="align-self:center")}</div>')
    no = ''.join(f'<div style="display:flex;align-items:center;gap:10px">{_solutions_cross(CHAMP)}'
                 f'<p style="font-size:24px;color:{CLAIR};white-space:nowrap">{t}</p></div>'
                 for t in ['Délais garantis', 'Crédit fournisseur', 'B2B pur sans étude', 'Caisses bois en colis'])
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:16px 26px;display:flex;align-items:center;gap:26px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap;flex:none">NOUS REFUSONS</p>'
            f'<div style="flex:1;display:flex;flex-wrap:wrap;align-items:center;gap:8px 24px">{no}</div></div>')
    sp = '<div style="flex:1;min-height:24px"></div>'
    inner = f"""{header3('Vendre · Partie 10 · Problèmes et solutions', 'Chaque solution répond à un problème, et se prouve', ORF, tags=['MA CONTRIBUTION'])}
{sp}
<div style="display:flex;flex-direction:column;gap:18px">{cas}
<div style="display:flex;gap:8px;align-items:stretch">{chain}</div></div>
{sp}
{band}
<div style="height:96px;flex:none"></div>
{footer(10, 'Vendre')}"""
    return 'solutions', inner, dict(gap=0, pad='128px 128px 64px')


def _processus_why(constat, decision, mesure):
    # même bandeau que kit.why3 (Constat → Ma décision → Ce que l'on mesure), avec le statut OBJECTIF visible à côté des cibles
    def cell(lab, txt, c, st=''):
        head = (f'<div style="display:flex;align-items:center;gap:12px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{c};white-space:nowrap">{lab}</p>{st}</div>')
        return (f'<div style="flex:1;display:flex;flex-direction:column;gap:6px">{head}'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    st = pill('OBJECTIF', 'align-self:center;padding:0px 12px;line-height:1.2;background:transparent;color:#FFFFFF;border-color:#FFFFFF')
    return (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:stretch;gap:18px">'
            f'{cell("CONSTAT", constat, BLEU)}{ar}{cell("MA DÉCISION", decision, CHAMP)}{ar}{cell("CE QUE L’ON MESURE", mesure, BLEU, st)}</div>')


def processus():
    # Message : sept étapes, une preuve pour passer chacune ; la ligne d'arrivée est le premier envoi (étape 6).
    # Point focal : la chaîne 1 → 7 ; l'étape 6 (Activé) ressort, avec sa fiche complète (responsable, preuve, délai, outil).
    # Hors écran : responsables, preuves, délais et outils des sept étapes : secours B17 (tableau complet, indiqué dans la note) ;
    # six portes d'entrée, rappel du lead entrant sous 24 h et durées de cycle : dits dans la note (cycle médian visé : secours B6).
    # « Ligne d'arrivée » : même pastille dorée pleine que les diapos 15 (activer) et 18 (onboarding).
    steps = [('Lead', 'ICP + signal vérifiés'), ('Qualifié', 'CAVE + score PA-FIT'), ('RDV · démo', 'reformulation validée'),
             ('Proposition', 'faisabilité validée'), ('Adhésion', 'signée + cartons'), ('Activé', 'premier envoi fait, débriefé'),
             ('Récurrent', '≥ 3 envois<br>par trimestre')]
    HI = 6
    flags, dots, names, cards = [], [], [], []
    for i, (n, proof) in enumerate(steps, 1):
        hi = i == HI
        c = ORF if hi else SARCF
        flags.append(f'<div style="display:flex;align-items:flex-end"><p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:1px;color:#FFFFFF;background:{ORF};border-radius:999px;padding:2px 16px;white-space:nowrap">LIGNE D’ARRIVÉE</p></div>'
                     if hi else '<div></div>')
        line = f'<div style="flex:1;height:4px;background:{BLEU}"></div>' if i < 7 else '<div style="flex:1"></div>'
        dots.append(f'<div style="display:flex;align-items:center"><div style="width:64px;height:64px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none">'
                    f'<p style="font-family:{L};font-size:30px;font-weight:700;color:#FFFFFF">{i}</p></div>{line}</div>')
        names.append(f'<p style="font-family:{L};font-size:28px;font-weight:700;line-height:1.2;color:{ORF if hi else ENCRE}">{n}</p>')
        if hi:
            # la fiche complète d'une étape : preuve, puis responsable, délai, outil
            # libellés en blanc gras, valeurs en blanc normal : contraste 5:1 sur ORF (CHAMP sur ORF n'était qu'à 3,4:1)
            # « Délai visé » : le délai est un objectif (SLA, secours B17) ; une pastille OBJECTIF ajouterait une ligne (flux dépassé à +10 %)
            kv = lambda k, v: f'<p style="font-size:24px;line-height:1.3;color:#FFFFFF"><b>{k}</b> : {v}</p>'
            cards.append(f'<div style="align-self:start;background:{ORF};border-radius:14px;padding:14px 18px 16px 18px;display:flex;flex-direction:column;gap:8px">'
                         f'<p style="font-size:26px;font-weight:700;line-height:1.25;color:#FFFFFF">{proof}</p>'
                         f'<div style="height:2px;background:rgba(255,255,255,0.35)"></div>'
                         f'{kv("Qui", "commercial +&nbsp;exploitation")}{kv("Délai visé", "≤ 30 j")}{kv("Outil", "Planet’Connect")}</div>')
        else:
            cards.append(f'<div style="align-self:start;background:#FFFFFF;border:1px solid {FILET};border-top:6px solid {SARCF};border-radius:14px;padding:12px 12px">'
                         f'<p style="font-size:26px;line-height:1.25;color:{ENCRE}">{proof}</p></div>')
    cols = ' '.join('1.5fr' if i == HI else '1fr' for i in range(1, 8))
    chain = (f'<div style="display:grid;grid-template-columns:{cols};gap:14px 14px">'
             f'{"".join(flags)}{"".join(dots)}{"".join(names)}{"".join(cards)}</div>')
    why = _processus_why('CRM historisé depuis 2025 seulement.',
                         'Sans preuve au CRM, pas d’étape.',
                         'Pipeline complet ≥ 95 % ;<br>activation ≥ 70 %.')
    sp = '<div style="flex:1;min-height:20px"></div>'
    inner = f'''{header3('Vendre · Partie 11 · Processus', 'Sept étapes, une preuve pour passer chacune', ORF, tags=['MA CONTRIBUTION'])}
{sp}
{chain}
{sp}
{why}
<div style="height:96px;flex:none"></div>
{footer(11, 'Vendre')}'''
    # marge basse : padding 64 + entretoise 96 = 160 px (bas du corps à 920, comme ailleurs) ;
    # même dispositif que les candidates icp et offre : au rendu +10 %, le gras du pied de page épinglé n'est plus compté dans le flux.
    return 'processus', inner, dict(gap=0, pad='128px 128px 64px')


def _doc(title, kind, body, c=SARCF, w=None):
    ww = f'width:{w}px;' if w else ''
    return (f'<div style="{ww}background:#FFFFFF;border:1px solid {FILET};border-radius:14px;overflow:hidden;display:flex;flex-direction:column">'
            f'<div style="background:{c};padding:8px 18px;display:flex;align-items:center;gap:12px"><p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF">{kind}</p>'
            f'<p style="font-size:24px;color:#FFFFFF;opacity:0.85">{title}</p></div>'
            f'<div style="padding:12px 18px;display:flex;flex-direction:column;gap:8px">{body}</div></div>')


_prospecter_RAIL = '#D9CBA8'


def _prospecter_step(n, title, body, tail=True):
    # un geste du commercial : pastille numérotée sur un rail vertical, verbe en clé (30 px), contenu en dessous
    line = f'<div style="flex:1;width:3px;background:{_prospecter_RAIL}"></div>' if tail else ''
    return (f'<div style="display:flex;gap:20px">'
            f'<div style="width:52px;flex:none;display:flex;flex-direction:column;align-items:center">'
            f'<div style="width:52px;height:52px;border-radius:50%;background:{ORF};display:flex;align-items:center;justify-content:center;flex:none">'
            f'<p style="font-family:{L};font-size:26px;font-weight:700;color:#FFFFFF">{n}</p></div>{line}</div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;padding-top:6px">'
            f'<p style="font-family:{L};font-size:30px;font-weight:700;line-height:1.2;color:{ENCRE}">{title}</p>{body}</div></div>')


def _prospecter_link():
    # le rail qui relie deux gestes : il prend la hauteur libre de la colonne
    return (f'<div style="flex:1;min-height:24px;display:flex"><div style="width:52px;flex:none;display:flex;justify-content:center">'
            f'<div style="width:3px;background:{_prospecter_RAIL}"></div></div></div>')


def prospecter():
    # Message : l'appel ne vend pas, il obtient la démo (chap. 10 ; secours B4 : « 30 minutes de démonstration sur ses vins, pas une vente »).
    # Point focal : la question clé du script d'appel, en grand, dans la carte du cas.
    # En appui à gauche : les trois gestes (préparer, viser, cadencer) ; sous la question : l'e-mail 1, réduit à sa phrase.
    # Hors écran : accroche et créneaux du script (dits : « une accroche, une question, deux créneaux ») ; objet et appel à l'action de l'e-mail
    # (annexe E du dossier) ; bloc 10 h-12 h et « avant les pics » : secours B4 ; sortie en nurture 45 j : secours B12 ; basse saison : dite.
    chip = lambda who, role, c: (f'<p style="font-size:26px;color:{c};background:#FFFFFF;border:2px solid {c};border-radius:999px;'
                                 f'padding:4px 18px;white-space:nowrap"><b>{who}</b> · {role}</p>')
    prep = f'<p style="font-size:26px;line-height:1.3;color:{GRIS}">site · e-shop · avis · prix · saisonnalité</p>'
    who = f'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px">{chip("Vigneron", "décide", BORD)}{chip("Responsable caveau", "utilise", SARCF)}</div>'
    house = ('<svg width="30" height="28" viewBox="0 0 30 28"><path d="M3 13 L15 3 L27 13" fill="none" stroke="#FFFFFF" stroke-width="3.5" '
             'stroke-linecap="round" stroke-linejoin="round"/><path d="M7 11 V25 H23 V11" fill="none" stroke="#FFFFFF" stroke-width="3.5" '
             'stroke-linecap="round" stroke-linejoin="round"/></svg>')
    touches = [('J1', 'appel', ORF), ('J+4', 'relance', SARCF), ('J+10', 'relance', SARCF), (house, 'visite', BORD)]
    pills, caps = [], []
    for i, (d, t, c) in enumerate(touches):
        inside = d if d.startswith('<svg') else f'<p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF;white-space:nowrap">{d}</p>'
        pills.append(f'<div style="border-radius:24px;background:{c};display:flex;align-items:center;justify-content:center;padding:7px 12px">{inside}</div>')
        caps.append(f'<p style="font-size:24px;text-align:center;color:{GRIS}">{t}</p>')
        if i < 3:
            pills.append(f'<div style="display:flex;align-items:center;justify-content:center">{arrow(26, 20, BLEU, 3)}</div>')
            caps.append('<div></div>')
    cad = (f'<div style="display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr 26px 1fr;gap:6px 6px">'
           f'{"".join(pills)}{"".join(caps)}</div>')
    left = f'''<div style="width:600px;flex:none;display:flex;flex-direction:column">
{_prospecter_step(1, 'Préparer', prep)}{_prospecter_link()}
{_prospecter_step(2, 'Viser', who)}{_prospecter_link()}
{_prospecter_step(3, 'Cadencer', cad, tail=False)}
</div>'''
    tag3 = (f'<p style="font-size:26px;font-weight:700;color:{ORF};background:#FFFFFF;border:2px solid {ORF};'
            f'border-radius:999px;padding:2px 16px;white-space:nowrap">&lt; 3 min</p>')
    call = f'''<div style="flex:1;{CASE_BOX};border-radius:18px;padding:26px 40px 28px 40px;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:16px">{label('Script d’appel', ORF, ls=3)}{tag3}</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center">
<p style="font-family:{T};font-style:italic;font-size:44px;font-weight:600;line-height:1.3;color:{ENCRE}">« Quand un Américain ou un Belge visite votre caveau et voudrait repartir avec 12 bouteilles, qu’est‑ce que vous lui proposez aujourd’hui ? »</p></div>
<div style="display:flex;align-items:center;gap:16px">{arrow(52, 30, ORF, 4)}<p style="font-family:{L};font-size:30px;font-weight:700;color:{ORF}">30 min de démo, sur ses vins</p></div>
</div>'''
    mail = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {SARCF};border-radius:16px;padding:18px 30px;display:flex;align-items:center;gap:26px">
{label('E-mail', SARCF, ls=2)}
<p style="flex:1;font-family:{T};font-style:italic;font-size:32px;font-weight:600;line-height:1.3;color:{ENCRE}">« Le frein n’est pas le prix : c’est la valise. »</p></div>'''
    right = f'<div style="flex:1;display:flex;flex-direction:column;gap:24px">{call}{mail}</div>'
    # marge basse : 64 px de padding + 66 px d'entretoise + 30 px d'écart = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates icp, offre et processus : au rendu +10 %, le pied de page épinglé n'est plus compté dans le flux.
    inner = f'''{head_case(header3('Vendre · Partie 11 · Prospection', 'L’appel ne vend pas : il obtient la démo', ORF, tags=['MA CONTRIBUTION']), 'Prospecter')}
<div style="flex:1;display:flex;gap:56px">{left}{right}</div>
<div style="height:66px;flex:none"></div>
{footer(12, 'Vendre')}'''
    return 'prospecter', inner, dict(gap=30, pad='128px 128px 64px')


def _spin_cut(color):
    # marque d'élision discrète : la citation reste fidèle sans que les coupes ne dominent la lecture
    return f'<span style="color:{color}">[…]</span>'


def _spin_cut(color):
    # marque d'élision discrète : la citation reste fidèle sans que les coupes ne dominent la lecture
    return f'<span style="color:{color}">[…]</span>'


def spin():
    # Message : découvrir, c'est faire chiffrer sa perte par le prospect lui-même.
    # Point focal : l'entonnoir S → P → I → N (questions du tunnel 1, vigneron avec caveau, annexe E), qui se resserre
    # jusqu'à la reformulation à trous ; la bande I, le chiffrage, ressort.
    # Hors écran : rôles des familles, trame (45 min, dont 35 de découverte et 12 de SPIN), réaction du vigneron et
    # validation par le prospect (« C'est bien ça… », chap. 12) : dits dans la note ; tunnel 2 (maison de champagne) et banque des 8 profils : secours B4.
    cw = '#7D8F96'
    fam = [('S', 'Situation', '« Comment organisez‑vous vos envois aujourd’hui quand un visiteur étranger veut plus que sa\u00a0valise ? »', '#E4EFF2'),
           ('P', 'Problème', '« Combien de fois par semaine un client repart en achetant moins que ce qu’il\u00a0voulait ? »', '#D5E7EC'),
           ('I', 'Implication', '« Sur une saison, combien de ventes de 12 bouteilles se réduisent à 2 ? Que représente ce manque en\u00a0CA ? »', ORF),
           ('N', 'Need-payoff', '« Si vos visiteurs pouvaient se faire livrer chez eux en payant par carte au comptoir, qu’est‑ce que ça changerait pour votre panier\u00a0moyen ? »', '#C3DCE2')]
    W, STEP = 1664, 40
    # S, P et N en GRIS 26 px : la bande I (dorée) et la reformulation (sombre) restent les seules zones à fort contraste.
    # « REFORMULER » sur 248 px : la citation commence à x = 208 + 28 + 248 + 24 = 508, à l'aplomb de celle de N.
    rows = ''
    for i, (k, name, q, bg) in enumerate(fam):
        hi = k == 'I'
        circ_bg, circ_fg = ('#FFFFFF', ORF) if hi else (SARCF, '#FFFFFF')
        rows += (f'<div style="width:{W - i * STEP}px;align-self:center;background:{bg};border-radius:16px;padding:10px 28px 10px 14px;display:flex;align-items:center;gap:18px">'
                 f'<div style="width:56px;height:56px;border-radius:50%;background:{circ_bg};display:flex;align-items:center;justify-content:center;flex:none">'
                 f'<p style="font-family:{L};font-size:34px;font-weight:700;color:{circ_fg}">{k}</p></div>'
                 f'<p style="width:214px;flex:none;font-family:{L};font-size:28px;font-weight:700;line-height:1.2;color:{"#FFFFFF" if hi else ENCRE};white-space:nowrap">{name}</p>'
                 f'<p style="flex:1;font-size:{27 if hi else 26}px;{"font-weight:600;" if hi else ""}line-height:1.25;color:{"#FFFFFF" if hi else GRIS}">{q}</p></div>')
    tr = lambda t: f'<b><span style="color:{CHAMP}">{t}</span></b>'
    cn = _spin_cut('#8FB0BA')
    reform = (f'<div style="width:{W - 4 * STEP}px;align-self:center;background:{NUIT};border-radius:16px;padding:12px 28px;display:flex;align-items:center;gap:24px">'
              f'<p style="width:248px;flex:none;font-family:{L};font-size:26px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">REFORMULER</p>'
              f'<p style="flex:1;font-size:27px;line-height:1.25;color:{CLAIR}">« Si je résume : vous perdez environ {tr("[X] ventes")} par {tr("[période]")} parce que {tr("[problème]")}, '
              f'et cela vous coûte à peu près {tr("[montant]")}. C’est bien ça – ou je me trompe quelque part ? »</p></div>')
    body = f'<div style="display:flex;flex-direction:column;gap:12px">{rows}{reform}</div>'
    # marge basse : padding 64 + entretoise 96 = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates icp, offre et processus (au rendu +10 %, le gras du pied de page épinglé n'est plus compté dans le flux).
    inner = f"""{head_case(header3('Vendre · Partie 11 · Tunnels SPIN', 'Découvrir : le prospect chiffre lui-même sa perte', ORF, tags=['MA CONTRIBUTION']), 'Découvrir')}
<div style="flex:1;min-height:24px"></div>
{body}
<div style="flex:1;min-height:20px"></div>
<div style="height:96px;flex:none"></div>
{footer(13, 'Vendre')}"""
    return 'spin', inner, dict(gap=0, pad='128px 128px 64px')


def _proposer_step(t, hi=False):
    # un temps de la méthode : pastille ; « Prouver » en plein (la preuve unique = les 15 € du panier)
    st = (f'background:{ORF};border:2px solid {ORF};color:#FFFFFF' if hi else
          f'background:#FFFFFF;border:2px solid {SARCF};color:{SARCF}')
    return (f'<p style="font-family:{L};font-size:28px;font-weight:700;padding:6px 18px;border-radius:999px;'
            f'white-space:nowrap;{st}">{t}</p>')


def proposer():
    # Message (titre) : le prix se prouve d'un chiffre, 15 € de transport par bouteille, payés par son client (transport seul, faits.md).
    # Point focal : la grille officielle 2026 (document réel), case 24 bouteilles encadrée, et à côté le 15 € en grand.
    # Puis : l'objection « c'est cher » en quatre temps (Prouver = ces 15 €) ; le bloc Simulation, 40 000 € potentiellement perdus.
    # Hors écran : formule de la simulation, 10 000 € / 110 € de cartons, « ce n'est pas une promesse », proposition sous 24 h
    # et décision datée (dits dans la note) ; deux créneaux de formation (ajoutés à la note) ; ~21 j et assurance à 3 % (secours B7) ;
    # répliques des quatre temps (dossier, chap. 13 ; la chaîne et les cinq objections : secours B14).
    # La grille est recadrée sous le tableau : la ligne « Estimation des taxes : 10 % » n'est plus affichée (aucun taux de droits US à l'écran).
    W = 1044  # capture 128-1172, bloc prix 1212-1792 (580 px) : la colonne du bloc « Profil du cas » en dessous
    k = W / 1187
    x0, y0, x1, y1 = 901 * k, 138 * k, 996 * k, 161 * k
    # cadre abaissé de 3 px (bas inchangé) : à cette échelle, son filet haut ne raye plus la case « 575 € » du dessus
    hl = (f'<div style="position:absolute;left:{x0 - 5:.0f}px;top:{y0 - 3:.0f}px;width:{x1 - x0 + 10:.0f}px;height:{y1 - y0 + 5:.0f}px;'
          f'border:5px solid {ORF};border-radius:6px"></div>')
    cap = shot(GRID, 'Document réel : grille officielle 2026 Planet Aura, USA groupage, tarifs HT, DDP obligatoire ; reste des États : 360 € pour 24 bouteilles',
               W, round(165 * k), 'grille officielle 2026, USA groupage', fit='cover', pos='top', kind='Document réel', overlay=hl,
               caption='+ taxes estimées, 17 € de dossier ; assurance en option')
    price = f'''<div style="flex:1;{CASE_BOX};border-radius:16px;padding:12px 26px;display:flex;flex-direction:column;justify-content:center;gap:6px">
<p style="font-family:{L};font-size:28px;font-weight:600;color:{PETROLE};white-space:nowrap">24 btl = 360 € HT</p>
{num('15 €', 80, ORF)}
<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap"><p style="font-size:28px;line-height:1.2;color:{ENCRE};white-space:nowrap">par bouteille</p>{pill('GRILLE 2026', 'align-self:center')}</div>
</div>'''
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(30, 24, BLEU, 3)}</div>'
    steps = ar.join([_proposer_step('Accueillir'), _proposer_step('Clarifier'), _proposer_step('Prouver, une fois', True), _proposer_step('Vérifier')])
    obj = f'''<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-radius:16px;padding:20px 26px;display:flex;flex-direction:column;justify-content:center;gap:22px">
<div style="display:flex;flex-direction:column;gap:6px">{label('Objection O-1', SARCF, ls=2)}
<p style="font-family:{T};font-style:italic;font-size:44px;font-weight:600;line-height:1.2;color:{ENCRE}">« C’est cher <span style="color:{GRISD}">[…]</span> »</p></div>
<div style="display:flex;align-items:center;gap:8px">{steps}</div>
</div>'''
    roi = f'''<div style="width:580px;flex:none;background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;flex-direction:column;justify-content:center;gap:6px">
<div style="display:flex;align-items:center;gap:14px">{label('Profil du cas', CHAMP, ls=2)}<div style="flex:1"></div>{pill('SIMULATION', 'background:transparent;color:#FFFFFF;border-color:#FFFFFF')}</div>
{num('40 000 €', 44, '#FFFFFF')}
<p style="font-size:28px;line-height:1.25;color:{BRUME}">de ventes potentiellement perdues</p>
<p style="font-size:24px;line-height:1.3;color:#8FB0BA">à refaire avec ses réponses</p>
</div>'''
    # marge basse : 64 px de padding + 70 px d'entretoise + 26 px d'écart = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les autres candidates : au rendu +10 %, le pied de page épinglé n'est plus exclu du flux par le banc.
    inner = f'''{head_case(header3('Vendre · Partie 11 · Proposition et objections', '15 € de transport par bouteille, payés par son client', ORF, tags=['EXISTANT', 'MA CONTRIBUTION']), 'Proposer')}
<div style="display:flex;gap:40px">{cap}{price}</div>
<div style="flex:1;display:flex;gap:40px">{obj}{roi}</div>
<div style="height:70px;flex:none"></div>
{footer(14, 'Vendre')}'''
    return 'proposer', inner, dict(gap=26, pad='128px 128px 64px')


def _activer_why(constat, decision, mesure):
    # même bandeau que kit.why3 (Constat → Ma décision → Ce que l'on mesure), avec le statut visible à côté des chiffres ;
    # colonnes à poids égaux, comme les bandeaux des diapos 11, 16 et 17
    def cell(lab, txt, c, st='', f=1):
        head = (f'<div style="display:flex;align-items:center;gap:12px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{c};white-space:nowrap">{lab}</p>'
                f'{st}</div>')
        return (f'<div style="flex:{f};display:flex;flex-direction:column;gap:6px">{head}'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    pst = 'align-self:center;padding:0px 12px;line-height:1.2;background:transparent;color:#FFFFFF;border-color:#FFFFFF'
    return (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:stretch;gap:18px">'
            f'{cell("CONSTAT", constat, BLEU, pill("CONSTATÉ", pst), 1)}{ar}'
            f'{cell("MA DÉCISION", decision, CHAMP, "", 1)}{ar}'
            f'{cell("CE QUE L’ON MESURE", mesure, BLEU, pill("OBJECTIF", pst), 1)}</div>')


def activer():
    # Message (titre) : la vente finit au premier envoi (même formule que l'étape 04 du sommaire).
    # Point focal : la frise J0 → J+30 ; le premier envoi porte le drapeau « ligne d'arrivée » (même code que la diapo 11)
    # et la carte du cas (code beige du fil rouge). Après la ligne d'arrivée, le suivi (pointillé) jusqu'au point d'étape.
    # Hors écran : 360 € (diapo 14, secours B16) ; détails du J+1, de la formation et du point J+30 (dossier, chap. 16) ;
    # score de santé (ajouté à la note ; secours B16) ; casse (indication de la note ; secours B11) ; alerte sous 50 % (diapo 19).
    steps = [('J0', 'Signature', 'en ligne, SEPA,\u00a0cartons'),
             ('J+1', 'Bienvenue', 'manuel, grilles'),
             ('J+5', 'Formation caveau', '30 min'),
             ('≤ J+30', 'Premier envoi', None),
             ('J+30', 'Point d’étape', 'volumes, recommandation')]
    HI = 3
    flags, dots, days, names, subs = [], [], [], [], []
    for i, (d, t, x) in enumerate(steps):
        hi = i == HI
        c = ORF if hi else SARCF
        flags.append(f'<div style="display:flex"><p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:1px;color:#FFFFFF;background:{ORF};border-radius:999px;padding:2px 16px;white-space:nowrap">LIGNE D’ARRIVÉE</p></div>'
                     if hi else '<div></div>')
        sz = 48 if hi else 30
        if i < HI:
            line = f'<div style="flex:1;height:6px;background:{BLEU}"></div>'
        elif i == HI:
            line = f'<div style="flex:1;height:0px;border-top:6px dotted {BLEU}"></div>'
        else:
            line = '<div style="flex:1"></div>'
        dots.append(f'<div style="height:48px;display:flex;align-items:center"><div style="width:{sz}px;height:{sz}px;border-radius:50%;background:{c};flex:none"></div>{line}</div>')
        days.append(num(d, 56 if hi else 44, c))
        names.append(f'<p style="font-family:{L};font-size:{32 if hi else 28}px;font-weight:700;line-height:1.2;color:{TXT.get(c, c) if hi else ENCRE};padding-right:12px">{t}</p>')
        if hi:
            # la carte du cas porte son statut, comme sur les diapos 8, 10 et 19 : parcours type, pas une vente réalisée
            # (écart 6 px et marge interne 8 px : la pastille tient dans le flux au rendu +10 %)
            subs.append(f'<div style="align-self:start;display:flex;flex-direction:column;align-items:flex-start;gap:6px;padding-right:28px">'
                        f'<div style="align-self:stretch;{CASE_BOX};border-radius:14px;padding:8px 20px">'
                        f'<p style="font-family:{T};font-style:italic;font-size:28px;line-height:1.25;color:{ENCRE}">Le couple texan, suivi</p></div>'
                        f'{pill("ILLUSTRATIF")}</div>')
        else:
            subs.append(f'<p style="font-size:24px;line-height:1.3;color:{GRIS};padding-right:{0 if i == 4 else 12}px">{x}</p>')
    cols = '1fr 1fr 1fr 1.3fr 1.1fr'  # la ligne d'arrivée plus large (carte du cas) ; la dernière colonne tient sa légende sur une ligne
    frise = (f'<div style="display:grid;grid-template-columns:{cols};gap:12px 0px">'
             f'{"".join(flags)}{"".join(dots)}{"".join(days)}{"".join(names)}{"".join(subs)}</div>')
    why = _activer_why('~145 signés en 12 mois, activation non\u00a0mesurée.',
                       'Commercial responsable jusqu’au premier envoi.',
                       '≥ 70 % des signés expédient sous 30 jours.')
    sp = '<div style="flex:1"></div>'
    # marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les autres candidates : au rendu +10 %, le pied de page épinglé n'est plus exclu du flux par le banc.
    inner = f'''{head_case(header3('Activer · Partie 11 · Activation', 'La vente finit au premier envoi', SARC, tags=['MA CONTRIBUTION', 'À MESURER']), 'Activer')}
{sp}
{frise}
{sp}
{why}
<div style="height:72px;flex:none"></div>
{footer(15, 'Activer')}'''
    return 'activer', inner, dict(gap=24, pad='128px 128px 64px', sect=SECT_ACTIVER)
