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
    crit = ''.join(f'''<div style="display:flex;align-items:center;gap:12px"><div style="width:30px;height:30px;border-radius:50%;background:{BORD};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{i}</p></div>
<p style="font-size:24px;line-height:1.25;color:{ENCRE}">{t}</p></div>''' for i, t in enumerate(['Clientèle étrangère (&gt; 20 / sem. en saison)', 'Bouteille à plus de 12 €', 'Responsable caveau ou e-shop', 'Destinations, USA en tête', 'Saisonnalité'], 1))
    eff = ''.join(f'''<div style="display:flex;align-items:center;gap:10px"><p style="width:250px;font-size:24px;color:{ENCRE}">{n}</p>
<div style="width:{w}px;height:24px;background:{BORD if i == 0 else '#C9A5B1'};border-radius:4px"></div><p style="font-family:{L};font-size:24px;font-weight:600;color:{BORD}">{p}</p></div>'''
                  for i, (n, w, p) in enumerate([('Domaines avec caveau', 210, '60 %'), ('Maisons de champagne', 52, '15 %'), ('Œnotourisme, salons', 52, '15 %'), ('Cavistes', 35, '10 %')]))
    left = f'''<div style="width:620px;display:flex;flex-direction:column;gap:12px">
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{ENCRE}">Ce que nous apprend notre top 10</span></b> (anonymisé) : pas la taille, mais des visiteurs étrangers, partout</p>
<div style="display:flex;flex-direction:column;gap:4px"><p style="font-size:24px;font-weight:700;color:{ENCRE}">5 critères, hiérarchisés</p>{crit}</div>
<p style="font-size:24px;line-height:1.35;color:{GRIS}"><b><span style="color:{ENCRE}">5 ICP</span></b> : <b><span style="color:{BORD}">caveaux 60 %</span></b> · champagne 15 % · œnotourisme 15 % · cavistes 10 % · distilleries en test</p>
<div style="flex:1"></div>
<div style="background:{NUIT};border-radius:14px;padding:12px 18px;display:flex;flex-direction:column;gap:4px"><p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP}">MA RECOMMANDATION</p>
<p style="font-size:24px;line-height:1.3;color:{CLAIR}"><b>60 % de l’effort sur les caveaux</b> : c’est là que se pose la question de Houston.</p></div>
</div>'''
    dims = [('Adéquation ICP', 15, 1, 'domaine avec caveau'), ('Adéquation du flux', 15, 1, 'clientèle US majoritaire'),
            ('Problème et impact', 15, 2, 'découverte : ventes perdues'), ('Volume et économie', 15, 1, '60 à 100 envois/an : tiers B'),
            ('Événement et timing', 15, 2, 'rappel avant saison : échéance'), ('Décision et accès', 10, 2, 'visite : propriétaire vu'),
            ('Préparation opérationnelle', 10, 0, 'données à collecter'), ('Valeur stratégique', 5, 0, 'non établie')]
    rows = ''
    for n, mx, st, ev in dims:
        w = mx * 12
        if st == 1:
            fill, sc, col = f'background:{SARCF}', f'{mx}', SARCF
        elif st == 2:
            fill, sc, col = f'background:repeating-linear-gradient(45deg, {ORF} 0px, {ORF} 7px, #E9D9B8 7px, #E9D9B8 14px)', f'+{mx}', ORF
        else:
            fill, sc, col = 'background:repeating-linear-gradient(45deg, #E3E9EB 0px, #E3E9EB 6px, #F3F6F7 6px, #F3F6F7 12px)', '0', GRISD
        rows += f'''<div style="display:flex;align-items:center;gap:12px">
<p style="width:310px;font-size:24px;color:{ENCRE}">{n}</p>
<div style="width:180px;flex:none"><div style="width:{w}px;height:24px;{fill};border-radius:4px"></div></div>
<p style="width:60px;font-family:{L};font-size:24px;font-weight:600;color:{col}">{sc}</p>
<p style="flex:1;font-size:24px;color:{GRIS if st else GRISD}">{ev}</p></div>'''
    right = f'''<div style="flex:1;{CASE_BOX};border-radius:18px;padding:18px 26px;display:flex;flex-direction:column;gap:10px">
<div style="display:flex;align-items:center;gap:14px">{label('Le domaine du cas, au score PA-FIT', ORF, ls=2)}<div style="flex:1"></div>{pill('ILLUSTRATIF', label='POINTS ILLUSTRATIFS')}</div>
<p style="font-size:24px;line-height:1.3;color:{GRIS}">Provence · 20+ étrangers / semaine en saison · panier ~300 € · e-shop</p>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Plein : acquis au départ · hachuré : prouvé ensuite</p>
<div style="display:flex;flex-direction:column;gap:5px">{rows}</div>
<div style="display:flex;align-items:center;gap:22px;border-top:1px solid {FILET};padding-top:10px">
<div style="display:flex;align-items:baseline;gap:8px">{num('45', 56, SARCF)}<p style="font-size:24px;color:{GRIS}">nurture</p></div>
{arrow(44, 30, ORF, 4)}
<div style="display:flex;align-items:baseline;gap:8px">{num('60', 56, ORF)}<p style="font-size:24px;color:{ORF}">cadence</p></div>
{arrow(44, 30, ORF, 4)}
<div style="display:flex;align-items:baseline;gap:8px">{num('85', 56, ORF)}<p style="font-size:24px;font-weight:700;color:{ORF}">P1</p></div>
<p style="flex:1;font-size:24px;line-height:1.3;color:{GRISD}">Un point n’est accordé qu’avec sa preuve.</p></div>
</div>'''
    inner = f'''{head_case(header3('Cibler · Partie 8 · ICP', 'Des meilleurs clients aux critères, des critères au score', BORD, tags=['MON ANALYSE', 'MA CONTRIBUTION']), 'Qualifier')}
<div style="flex:1;display:flex;gap:44px">{left}{right}</div>
{footer(8, 'Cibler')}'''
    return 'icp', inner, dict(gap=22, sect=SECT_CIBLER)


def personas():
    cols = [('A', 'DÉCIDE', 'Le vigneron-propriétaire', BORD, 'Vendre plus au caveau, sans embaucher', '« Encore un prestataire qui promet »', 'Visite terrain, confrère, appel court',
             '« Vous remettez le colis, on s’occupe de tout. »', 'Le carton ISTA 3A en main, le simulateur sur son vin'),
            ('B', 'UTILISE', 'La responsable caveau', SARCF, 'Un parcours de vente fluide, du verre au colis', '« Un client étranger mécontent qui laisse un avis négatif »', 'E-mail, démo',
             '« Le simulateur donne un prix en 20 secondes, pendant la dégustation. »', 'La démo Planet’Connect, la fiche réflexe'),
            ('E', 'PAIE', 'Le client final étranger', ORF, 'Rapporter son vin, sans valise ni douane', '« Des frais surprises à la livraison »', 'Au comptoir, par l’adhérent',
             '« About €360 shipping for 24 bottles, plus prepaid duties and a €17 fee; insurance option 3 %. »', 'L’order form en anglais, avec le total')]
    cards = ''
    for code, role, name, c, want, fear, chan, say, proof in cols:
        cards += f'''<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {c};border-radius:16px;padding:14px 20px;display:flex;flex-direction:column;gap:6px">
<div style="display:flex;align-items:center;gap:12px"><div style="width:42px;height:42px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{code}</p></div>{label(role, c, ls=2)}</div>
<p style="font-family:{T};font-size:30px;font-weight:700;color:{ENCRE}">{name}</p>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Veut</b> : {want}</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b>Craint</b> : {fear}</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b>Canal</b> : {chan}</p>
<div style="background:{CLAIR};border-left:5px solid {c};border-radius:8px;padding:10px 14px;display:flex;flex-direction:column;gap:4px">
<p style="font-family:{L};font-size:24px;font-weight:600;color:{c}">{'Ce que le caveau lui dit' if code == 'E' else 'Ce que je lui dis'}</p>
<p style="font-family:{T};font-style:italic;font-size:26px;line-height:1.3;color:{ENCRE}">{say}</p></div>
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Preuve : {proof}</p>
</div>'''
    study = f'''<div style="width:390px;background:{NUIT};border-radius:16px;padding:18px 22px;display:flex;flex-direction:column;gap:10px">
{label('Mon étude · oct. 2026', CHAMP, ls=2)}
<div style="display:flex;gap:18px">{num('70', 48, '#FFFFFF')}<p style="font-size:24px;line-height:1.2;color:{BRUME}">contacts<br>pro</p></div>
<div style="display:flex;gap:18px">{num('47', 48, '#FFFFFF')}<p style="font-size:24px;line-height:1.2;color:{BRUME}">réponses à<br>3 enquêtes</p></div>
<div style="display:flex;gap:18px">{num('15', 48, '#FFFFFF')}<p style="font-size:24px;line-height:1.2;color:{BRUME}">avis<br>Google</p></div>
<p style="font-size:24px;line-height:1.3;color:{CLAIR}"><b>5/5 confirmés</b>, 3 ajustements, 1 angle mort : l’ADV, utilisatrice au quotidien</p>
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.3;color:#8FB0BA">Échanges écrits ; entretiens prévus au T1 2027</p>
</div>'''
    inner = f'''{header3('Cibler · Partie 9 · Personas', 'Un même domaine, trois interlocuteurs, trois discours', BORD, tags=['MON ANALYSE', 'MA CONTRIBUTION'])}
<p style="font-size:26px;color:{GRIS}">L’ICP décrit l’entreprise, le persona la personne. <b><span style="color:{ENCRE}">Ailleurs</span></b> : C le caviste, D la maison de champagne, et les comités d’achat.</p>
<div style="flex:1;display:flex;gap:22px">{cards}{study}</div>
{footer(9, 'Cibler')}'''
    return 'personas', inner, dict(gap=18)


def solutions():
    rows = [('Domaine avec caveau', BORD, 'Ventes perdues avec les visiteurs étrangers', 'Livrer chez le client, sans douane ni temps administratif',
             'Simulateur au comptoir · order form CB · groupage USA DDP · cartons ISTA 3A', 'Panier visé : de 2 bouteilles à la caisse, zéro douane', 'Simulateur sur ses vins, carton en main, voisins adhérents'),
            ('Maison de champagne', SARCF, 'Certificat CIVC hors UE : colis immobilisé', 'Conformité sans charge interne, image protégée',
             'Certificat géré à chaque envoi (15 € HT) · groupage USA DDP', 'Certificat géré à chaque envoi : un motif de blocage écarté', 'Une maison de champagne du top 5 du réseau'),
            ('Caviste', ORF, 'Le client achète 2 bouteilles au lieu de 12', 'Vendre plus, sans rien avancer',
             'Order form CB · simulateur sur tablette · PLV « We ship worldwide »', 'Vente de 12, payée au comptoir', 'Deux caves touristiques du top 10')]
    heads = ['Problème', 'Besoin', 'Solution Planet Aura', 'Bénéfice client', 'Preuve']
    W = [300, 300, 380, 290, 300]
    hd = '<div style="width:250px"></div>' + ''.join(f'<p style="width:{w}px;font-family:{L};font-size:24px;font-weight:600;letter-spacing:1px;color:{GRISD}">{h}</p>' for h, w in zip(heads, W))
    body = ''
    for name, c, *cells in rows:
        cs = ''
        for k, (t, w) in enumerate(zip(cells, W)):
            bg = '#FFFFFF' if k != 2 else '#E8F3F5'
            fw = '700' if k == 2 else '400'
            cs += (f'<p style="width:{w}px;background:{bg};border:1px solid {FILET};border-radius:10px;padding:6px 12px;font-size:24px;font-weight:{fw};line-height:1.25;color:{ENCRE}">{t}</p>')
            if k < 4:
                cs += f'<div style="width:24px;display:flex;align-items:center;justify-content:center">{arrow(24, 20, c, 3)}</div>'
        case = name == 'Domaine avec caveau'
        tagc = f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{ORF}">LE CAS</p>' if case else ''
        body += f'''<div style="flex:1;display:flex;align-items:stretch;gap:0px">
<div style="width:250px;display:flex;flex-direction:column;justify-content:center;border-left:8px solid {c};padding-left:14px;{'background:#FBF6EA' if case else ''}">{tagc}<p style="font-family:{T};font-size:28px;font-weight:700;line-height:1.15;color:{ENCRE}">{name}</p></div>{cs}</div>'''
    hd = '<div style="display:flex;gap:24px">' + hd + '</div>'
    no = ''.join(f'<p style="font-size:24px;color:{CLAIR};white-space:nowrap"><b><span style="color:{CHAMP}">×</span></b> {t}</p>' for t in ['Délais garantis', 'Crédit fournisseur', '100 % B2B sans étude', 'Caisses bois en colis', '&gt; 21° hors spiritueux USA'])
    inner = f'''{header3('Vendre · Partie 10 · Problèmes et solutions', 'Chaque solution répond à un problème, et se prouve', ORF, tags=['MA CONTRIBUTION'])}
{hd}
<div style="flex:1;display:flex;flex-direction:column;gap:10px">{body}</div>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Pourquoi c’est différenciant</b> : face à la valise ou au compte express, un porte-à-porte assurable (option 3 %), des taxes prépayées, un\u00a0seul\u00a0interlocuteur.</p>
<div style="background:{NUIT};border-radius:14px;padding:12px 24px;display:flex;align-items:center;gap:26px"><p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{CHAMP};white-space:nowrap;flex:none">Nous refusons</p>{no}</div>
{footer(10, 'Vendre')}'''
    return 'solutions', inner, dict(gap=14)


def processus():
    st = [('Lead', 'Commercial (+ marketing)', 'ICP et signal vérifiés', 'rappel &lt; 24 h', 'HubSpot'),
          ('Qualifié', 'Commercial', 'CAVE + score PA-FIT', '≤ 7 j', 'HubSpot'),
          ('RDV · démo', 'Commercial', 'reformulation validée', 'CR &lt; 24 h', 'Simulateur'),
          ('Proposition', 'Commercial + exploitation', 'faisabilité validée', '&lt; 24 h', 'Doc. 2026'),
          ('Adhésion', 'Adhérent + commercial', 'signée + cartons', '≤ 14 j', 'E-signature'),
          ('Activé', 'Commercial + exploitation', '1er envoi fait, débriefé', '≤ 30 j', 'Planet’Connect'),
          ('Récurrent', 'Commercial', '≥ 3 envois / trimestre', 'retour &lt; 2 j', 'Dashboards')]
    cols = ''
    for i, (n, who, proof, sla, tool) in enumerate(st, 1):
        hi = i == 6
        cc = ORF if hi else SARCF
        cols += f'''<div style="flex:1;display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:center"><div style="width:52px;height:52px;border-radius:50%;background:{cc};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:26px;font-weight:700;color:#FFFFFF">{i}</p></div><div style="flex:1;height:4px;background:{BLEU if i < 7 else 'transparent'}"></div></div>
<p style="font-family:{L};font-size:26px;font-weight:700;color:{ORF if hi else ENCRE}">{n}</p>
<p style="height:60px;font-size:24px;line-height:1.25;color:{GRIS}">{who}</p>
<p style="height:104px;font-size:24px;line-height:1.25;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:8px;padding:6px 10px"><b>Preuve</b> : {proof}</p>
<p style="font-family:{L};font-size:24px;font-weight:600;color:{BORD}">{sla}</p>
<p style="font-size:24px;color:{GRISD}">{tool}</p>
</div>'''
    src = ' · '.join(['formulaires entrants', 'recommandations', 'salons', 'terrain', 'comptes ciblés', 'partenaires prescripteurs'])
    cyc = f'''<div style="display:flex;gap:28px;align-items:stretch">
<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-radius:14px;padding:12px 20px;display:flex;align-items:center;gap:18px">
{label('Durée du cycle', PETROLE, ls=2)}<p style="font-size:24px;color:{ENCRE}">Dossier standard <b>7 à 21 j</b></p>{pill('OBJECTIF')}<p style="font-size:24px;color:{ENCRE}">Maison de champagne <b>6 à 12 sem.</b></p>{pill('HYPOTHÈSE')}</div>
<div style="width:520px;background:#FFFFFF;border:1px solid {FILET};border-radius:14px;padding:12px 20px;display:flex;align-items:center"><p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{PETROLE}">Six portes d’entrée</span></b> : entrants, recommandations, salons, terrain, comptes ciblés, prescripteurs</p></div>
</div>'''
    inner = f'''{header3('Vendre · Partie 11 · Processus', 'Sept étapes, une preuve pour passer chacune', ORF, tags=['MA CONTRIBUTION'])}
<p style="font-size:26px;color:{GRIS}"><b><span style="color:{ENCRE}">Règle</span></b> : une étape n’existe que si sa preuve est dans le CRM.</p>
<div style="flex:1;display:flex;gap:14px">{cols}</div>
{decision('<b>Ligne d’arrivée : le premier envoi (étape 6), pas la signature.</b> Le commercial en reste responsable.', label='MON CHOIX')}
{cyc}
{footer(11, 'Vendre')}'''
    return 'processus', inner, dict(gap=20)


def _doc(title, kind, body, c=SARCF, w=None):
    ww = f'width:{w}px;' if w else ''
    return (f'<div style="{ww}background:#FFFFFF;border:1px solid {FILET};border-radius:14px;overflow:hidden;display:flex;flex-direction:column">'
            f'<div style="background:{c};padding:8px 18px;display:flex;align-items:center;gap:12px"><p style="font-family:{L};font-size:24px;font-weight:600;color:#FFFFFF">{kind}</p>'
            f'<p style="font-size:24px;color:#FFFFFF;opacity:0.85">{title}</p></div>'
            f'<div style="padding:12px 18px;display:flex;flex-direction:column;gap:8px">{body}</div></div>')


def prospecter():
    q = lambda k, t: (f'<div style="display:flex;flex-direction:column;gap:4px"><p style="font-family:{L};font-size:24px;font-weight:700;color:{ORF}">{k}</p>'
                      f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}">{t}</p></div>')
    steps = ''.join(f'''<div style="display:flex;flex-direction:column;align-items:center;gap:4px;width:120px"><div style="width:68px;height:48px;border-radius:24px;background:{c};display:flex;align-items:center;justify-content:center"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{d}</p></div><p style="font-size:24px;line-height:1.2;text-align:center;color:{GRIS}">{t}</p></div>'''
                    for d, t, c in [('J1', 'appel + e-mail', ORF), ('J+4', 'relance', SARC), ('J+10', 'relance', SARC), ('↗', 'visite ou salon', BORD)])
    left = f'''<div style="width:600px;display:flex;flex-direction:column;gap:16px">
{q('Qui ?', 'Le vigneron décide ; la responsable caveau utilisera l’outil : je vise les deux.')}
{q('Par quel canal ?', 'Un caveau se prospecte sur le terrain : appel court et e-mail avec la grille, puis relances.')}
<div style="display:flex;align-items:flex-start;gap:6px">{steps}</div>
{q('Quand ?', 'En basse saison (janvier-avril), avant les pics ; au téléphone de 10 h à midi.')}
<p style="font-size:24px;color:{GRISD}">Sans réponse : nurture 45 jours</p>
</div>'''
    script = (f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Ouverture</b> · « […] les ventes perdues au caveau avec les visiteurs étrangers. Vous avez 30 secondes ? »</p>'
              f'<p style="font-size:26px;font-weight:700;line-height:1.3;color:{ENCRE}"><b>Question</b> · « Quand un Américain ou un Belge visite votre caveau et voudrait repartir avec 12 bouteilles, qu’est-ce que vous lui proposez aujourd’hui ? »</p>'
              f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Clôture</b> · « […] 30 minutes au domaine : je vous montre notre simulateur avec VOS vins et VOS destinations […]. Plutôt mardi matin ou jeudi après-midi ? »</p>')
    mail = (f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Objet</b> : [Domaine X] - vos visiteurs américains repartent les mains vides ?</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{GRIS}">« Chaque été, des visiteurs étrangers achètent 2 bouteilles dans votre caveau… alors qu’ils en voulaient 12. <b>Le frein n’est pas le prix : c’est la valise.</b> »</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{GRIS}">« 30 minutes suffisent pour vous montrer le simulateur avec vos vins. Seriez-vous disponible [date 1] ou [date 2] ? »</p>')
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{_doc('moins de 3 minutes, un seul but : 30 min de démo', 'SCRIPT D’APPEL', script, ORF)}
{_doc('annexe E, prêt à copier', 'E-MAIL 1', mail, SARCF)}
</div>'''
    inner = f'''{head_case(header3('Vendre · Partie 11 · Prospection', 'Prospecter : le bon interlocuteur, le bon canal, les bons mots', ORF, tags=['MA CONTRIBUTION']), 'Prospecter')}
<div style="flex:1;display:flex;gap:44px">{left}{right}</div>
{footer(12, 'Vendre')}'''
    return 'prospecter', inner, dict(gap=22)


def spin():
    trame = [('Cadrer', 3, '#B9D6DD'), ('Contexte', 5, '#B9D6DD'), ('Questions SPIN · 12 min', 12, SARCF), ('Reformuler', 5, '#8FBFCB'),
             ('Besoin → offre', 5, '#B9D6DD'), ('Décider', 5, '#B9D6DD')]
    tb = ''.join(f'<div style="flex:{n};height:40px;background:{c};display:flex;align-items:center;justify-content:center"><p style="font-size:24px;font-weight:600;color:{"#FFFFFF" if c == SARCF else ENCRE};white-space:nowrap">{t}</p></div>' for t, n, c in trame)
    dlg = [('S', 'Situation', '« Comment organisez-vous vos envois aujourd’hui quand un visiteur étranger veut plus que sa valise ? »', '« On lui conseille La Poste… ou on ne fait rien. »'),
           ('P', 'Problème', '« Combien de fois par semaine un client repart en achetant moins que ce qu’il voulait ? »', '« En saison ? Plusieurs fois par semaine. »'),
           ('I', 'Implication', '« Sur une saison, combien de ventes de 12 bouteilles se réduisent à 2 ? Que représente ce manque en CA ? »', '« Je n’avais jamais fait le calcul… »'),
           ('N', 'Need-payoff', '« Si vos visiteurs pouvaient se faire livrer chez eux en payant par carte au comptoir, qu’est-ce que ça changerait pour votre panier moyen ? »', '« Je ne dirais plus non à celui qui veut une caisse. »')]
    rows = ''
    for k, fam, q, a in dlg:
        rows += f'''<div style="display:flex;gap:14px;align-items:center">
<div style="width:52px;height:52px;border-radius:50%;background:{SARCF};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:28px;font-weight:700;color:#FFFFFF">{k}</p></div>
<p style="width:690px;background:{SARCF};color:#FFFFFF;border-radius:16px 16px 16px 4px;padding:8px 16px;font-size:24px;line-height:1.25">{q}</p>
<p style="flex:1;background:#FBF6EA;border:2px solid #E9D9B8;border-radius:16px 16px 4px 16px;padding:8px 16px;font-family:{T};font-style:italic;font-size:24px;line-height:1.25;color:{ENCRE}">{a}</p></div>'''
    t2 = ''.join(f'<p style="font-size:24px;line-height:1.25;color:{ENCRE}"><b><span style="color:{ORF}">{k}</span></b> {t}</p>' for k, t in [
        ('S', 'Quels marchés et incoterms pour vos particuliers hors UE ?'), ('P', 'Où perdez-vous du temps : CIVC, douane, suivi ?'),
        ('I', 'Que coûte un colis bloqué à l’image de la maison ?'), ('N', 'Et si certificat et taxes étaient gérés à chaque envoi ?')])
    side = f'''<div style="width:400px;background:#FFFFFF;border:1px solid {FILET};border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:8px">
{label('Tunnel 2 · Maison de champagne', PETROLE, ls=2)}{t2}
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Banque complète : 8 profils, personas et rôles (secours B4)</p></div>'''
    inner = f'''{head_case(header3('Vendre · Partie 11 · Tunnels SPIN', 'Découvrir : le prospect chiffre lui-même sa perte', ORF, tags=['MA CONTRIBUTION']), 'Découvrir')}
<div style="display:flex;align-items:center;gap:16px"><p style="font-family:{L};font-size:24px;font-weight:600;color:{GRISD};white-space:nowrap">35 min (RDV de 45)</p><div style="flex:1;display:flex;gap:3px;border-radius:8px;overflow:hidden">{tb}</div></div>
<div style="flex:1;display:flex;gap:24px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<div style="display:flex;gap:14px"><div style="width:52px"></div><p style="width:690px;font-family:{L};font-size:24px;font-weight:600;color:{SARCF}">Tunnel 1 · Vigneron avec caveau : mes questions</p><div style="flex:1;display:flex;gap:10px;align-items:center"><p style="font-family:{L};font-size:24px;font-weight:600;color:{ORF}">Ses réponses</p>{pill('ILLUSTRATIF')}</div></div>
{rows}
</div>{side}</div>
{decision('« Si je résume : vous perdez environ <b>[X] ventes</b> par <b>[période]</b> parce que <b>[problème]</b>, et cela vous coûte à peu près <b>[montant]</b>. C’est bien ça - ou je me trompe quelque part ? »', label='REFORMULER')}
{footer(13, 'Vendre')}'''
    return 'spin', inner, dict(gap=10)


def proposer():
    hl = f'<div style="position:absolute;left:893px;top:134px;width:100px;height:28px;border:4px solid {ORF};border-radius:4px"></div>'
    cap = shot(GRID, 'Document réel : grille officielle 2026 Planet Aura, USA groupage, tarifs HT, DDP obligatoire ; reste des États : 360 € pour 24 bouteilles, 21 jours ; taxes estimées à 10 % de la valeur',
               1180, 185, 'grille officielle 2026, USA groupage (annexe F)', fit='contain', kind='Document réel', overlay=hl)
    line = lambda a, b, bold=False: (f'<div style="display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid #E9D9B8;padding:2px 0px">'
                                     f'<p style="font-size:24px;color:{ENCRE}">{a}</p><p style="font-family:{L};font-size:{40 if bold else 48}px;font-weight:700;line-height:1.1;color:{ORF if bold else PETROLE}">{b}</p></div>')
    price = f'''<div style="flex:1;{CASE_BOX};border-radius:14px;padding:10px 16px;display:flex;flex-direction:column;gap:2px">
{label('Le panier du cas', ORF, ls=1)}
<p style="font-size:24px;color:{GRIS}">Couple texan · 24 btl · ~21 j estimés</p>
{line('Transport HT', '360 €')}
{line('Par bouteille', '15 €', True)}
<p style="font-size:24px;line-height:1.3;color:{GRISD}">+ taxes estimées, 17 € de dossier ; assurance en option, 3 %</p>
</div>'''
    obj = ''.join(f'''<div style="display:flex;gap:12px;align-items:baseline"><p style="width:150px;font-family:{L};font-size:24px;font-weight:700;color:{c}">{k}</p><p style="flex:1;font-size:24px;line-height:1.25;color:{ENCRE}">{t}</p></div>'''
                  for k, t, c in [('Accueillir', '« Vous avez raison de la poser. »', SARCF), ('Clarifier', '« Qu’est-ce qui vous fait dire ça ? »', SARCF),
                                  ('Prouver', '15 € de transport par bouteille, payés par son client', ORF), ('Vérifier', '« Si ce point est réglé, qu’est-ce qui nous empêche de créer votre compte cette semaine ? »', SARCF)])
    roi = f'''<div style="width:680px;background:{NUIT};border-radius:16px;padding:14px 22px;display:flex;flex-direction:column;gap:6px">
<div style="display:flex;align-items:center;gap:12px">{label('Sa valeur, chiffrée avec lui', CHAMP, ls=1)}<div style="flex:1"></div>{pill('ILLUSTRATIF', 'background:transparent;color:#FFFFFF;border-color:#FFFFFF', 'CALCUL ILLUSTRATIF')}</div>
<p style="font-size:24px;line-height:1.3;color:{CLAIR}">20 étrangers / sem. × 1 sur 3 × 300 € × 20 sem.</p>
<div style="display:flex;align-items:baseline;gap:14px">{num('40 000 €', 36, '#FFFFFF')}<p style="font-size:24px;color:{BRUME}">de ventes de vin perdues</p></div>
<p style="font-size:24px;line-height:1.3;color:{CLAIR}">Un quart récupéré : <b>10 000 €</b>, pour 110 € HT de cartons</p>
<p style="font-size:24px;line-height:1.3;color:#8FB0BA">Méthode du chap. 13, avec les chiffres du prospect</p>
</div>'''
    inner = f'''{head_case(header3('Vendre · Partie 11 · Proposition et objections', 'Proposer : chiffrer, lever l’objection, fixer la suite', ORF, tags=['EXISTANT', 'MA CONTRIBUTION']), 'Proposer')}
<div style="display:flex;gap:40px">{cap}{price}</div>
<div style="flex:1;display:flex;gap:40px">
<div style="flex:1;display:flex;flex-direction:column;gap:6px">{label('Objection « c’est cher » : quatre temps', SARCF, ls=1)}{obj}<div style="flex:1"></div><p style="font-size:24px;line-height:1.3;color:{ENCRE};border-left:5px solid {ORF};padding-left:14px"><b>Prochaine étape</b> : e-mail de proposition sous 24 h (récap et ROI, documentation 2026, deux créneaux de formation), décision datée.</p></div>
{roi}</div>
{footer(14, 'Vendre')}'''
    return 'proposer', inner, dict(gap=18)


def activer():
    ms = [('J0', 'Signature', 'documentation 2026 signée en ligne, SEPA, 1er lot de cartons', SARCF),
          ('J+1', 'Bienvenue', 'e-mail de l’exploitation : identifiants, manuel, grilles ; je confirme cartons et formation', SARC),
          ('J+5', 'Formation caveau', '30 min : pitch client final, saisie et simulation, encaissement, emballage, cas particuliers', ORF),
          ('≤ J+30', 'Premier envoi', 'le couple texan, 24 bouteilles : 360 € de transport, taxes estimées réglées d’avance, suivi', BORD),
          ('J+30', 'Point d’étape', 'volumes prévus, saisonniers à former, demande de recommandation', PETROLE)]
    tl = ''
    for i, (d, t, x, c) in enumerate(ms):
        tl += f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<div style="display:flex;align-items:center"><div style="width:30px;height:30px;border-radius:50%;background:{c};flex:none"></div><div style="flex:1;height:6px;background:{BLEU if i < 4 else 'transparent'}"></div></div>
{num(d, 40, c)}
<p style="font-family:{L};font-size:26px;font-weight:700;color:{ENCRE}">{t}</p>
<p style="font-size:24px;line-height:1.3;color:{GRIS};padding-right:18px">{x}</p></div>'''
    life = f'''<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-radius:16px;padding:16px 22px;display:flex;flex-direction:column;gap:8px">
{label('Ensuite, le compte se suit', SARCF, ls=2)}
<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Score de santé</b> : envois comparés à N-1, délai depuis le dernier envoi, incidents, connexions, documentation signée. <b>Rouge</b> : appel du commercial sous 7 jours.</p>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}"><b>Incident</b> (exemple) : une bouteille cassée, signalée sous 48 h avec photos. L’envoi était assuré (option 3 %) : elle est réexpédiée et le domaine nous <b>refacture la bouteille</b>.</p></div>'''
    kpi = f'''<div style="width:520px;background:{NUIT};border-radius:16px;padding:16px 22px;display:flex;flex-direction:column;gap:8px">
{label('Ce que je mesurerai', CHAMP, ls=2)}
<div style="display:flex;align-items:baseline;gap:14px">{num('≥ 70 %', 56, '#FFFFFF')}<p style="font-size:24px;color:{BRUME}">des signés<br>expédient sous 30 j</p></div>
<p style="font-size:24px;line-height:1.3;color:#8FB0BA">Objectif de départ ; jamais mesuré avant le playbook</p></div>'''
    inner = f'''{head_case(header3('Activer · Partie 11 · Activation', 'Activer : la vente finit au premier envoi, pas à la signature', SARC, tags=['MA CONTRIBUTION', 'À MESURER']), 'Activer')}
<div style="display:flex">{tl}</div>
<div style="flex:1"></div>
<div style="display:flex;gap:24px">{life}{kpi}</div>
{footer(15, 'Activer')}'''
    return 'activer', inner, dict(gap=24, sect=SECT_ACTIVER)
