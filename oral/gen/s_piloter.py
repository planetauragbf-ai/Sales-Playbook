# Diapos 16 à 20 : ressources, Sales Ops et alignement, onboarding, indicateurs, synthèse et ouverture
from kit import *

PG_PERSONA = '/_blob/84a2951d653fd7045bcb9b701fba9569'   # p. 104 : persona A, le vigneron-propriétaire
PG_OBJ = '/_blob/1a1249ec783f083e93f39c9e6ce07821'       # p. 110 : objections en format court, checklists
PG_SCRIPTS = '/_blob/ae61ce0322e73dc18d6f021d00343874'   # p. 54 : script cold call caveau
PG_ONB = '/_blob/733e333b40678a6a91b5f36643e93151'       # p. 169 : annexe U, onboarding jour par jour
PG_ROAD = '/_blob/254d126c9282167d65058c0e3ff94597'      # p. 171 : feuille de route budgétée
DASH_NEW = '/_blob/23896dc16cb677697a898418b408bfda'
LOGO_MARK_W = '/_blob/8b40700e136fb4e2e66480f214bc3ee5'

SECT_PILOTER = 'Piloter : ressources, Sales Operations, onboarding et indicateurs'


def thumb(src, alt, cap, w=124, h=175):
    return (f'<div style="width:{w}px;display:flex;flex-direction:column;gap:6px;flex:none">'
            f'<img src="{src}" alt="{alt}" style="width:{w}px;height:{h}px;object-fit:cover;object-position:top;border:1px solid {FILET};border-radius:6px;background:#FFFFFF">'
            f'<p style="font-size:24px;line-height:1.15;color:{GRIS}">{cap}</p></div>')


def _ressources_why(constat, decision, mesure):
    # même bandeau que kit.why3 (Constat → Ma décision → Ce que l'on mesure), avec le statut CONSTATÉ visible à côté du constat chiffré
    def cell(lab, txt, c, st=''):
        head = (f'<div style="display:flex;align-items:center;gap:12px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{c};white-space:nowrap">{lab}</p>{st}</div>')
        return (f'<div style="flex:1;display:flex;flex-direction:column;gap:6px">{head}'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    pst = 'align-self:center;padding:0px 12px;line-height:1.2;background:transparent;color:#FFFFFF;border-color:#FFFFFF'
    return (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:stretch;gap:18px">'
            f'{cell("CONSTAT", constat, BLEU, pill("CONSTATÉ", pst))}{ar}'
            f'{cell("MA DÉCISION", decision, CHAMP)}{ar}'
            f'{cell("CE QUE L’ON MESURE", mesure, BLEU)}</div>')


def _ressources_page(src, alt, cap, w=164, h=232):
    # page réelle du playbook, en entier (format A4), légendée d'un mot
    return (f'<div style="width:{w}px;display:flex;flex-direction:column;gap:10px;flex:none">'
            f'<img src="{src}" alt="{alt}" style="width:{w}px;height:{h}px;object-fit:cover;border:1px solid {FILET};border-radius:8px;background:#FFFFFF;box-shadow:0 4px 24px rgba(0,0,0,.08)">'
            f'<p style="font-size:26px;line-height:1.2;color:{ENCRE}">{cap}</p></div>')


def ressources():
    # Message (titre) : trois chantiers d'abord, 800 € sur un plafond de 3 000 €.
    # Point focal : les trois cartes reliées par des flèches (l'ordre est la décision), le budget en grand.
    # Zone secondaire : trois pages réelles du playbook (ce que j'ai créé, déjà livré).
    # Hors écran : critères de passage, intitulés complets, suite de la feuille de route (secours B13) ;
    # pastilles des ressources créées (diapos 13, 14, 18 ; secours B4, B14, B15) ; doute → preuve existante (note).
    pages = (_ressources_page(PG_PERSONA, 'Page réelle du playbook : fiche persona du vigneron-propriétaire', 'Persona')
             + _ressources_page(PG_SCRIPTS, 'Page réelle du playbook : script d’appel à froid pour un caveau, chapitre 10', 'Script')
             + _ressources_page(PG_OBJ, 'Page réelle du playbook : objections en format court et checklists, annexe B', 'Objections'))
    # rangée du libellé à la hauteur de la rangée à tampon OBJECTIF (42 px) : les deux colonnes partent de la même ligne
    left = f'''<div style="display:flex;flex-direction:column;gap:18px;flex:none">
<div style="display:flex;align-items:center;min-height:42px">{label('Déjà livré', SARCF, ls=2)}</div>
<div style="display:flex;gap:18px;align-items:flex-start">{pages}</div>
</div>'''
    ch = [('Septembre', 'Nettoyage CRM', '0 €', 'Emma + Adam · 24 h'),
          ('Octobre', 'One-pager par\u00a0ICP', '600 €', 'Emma + Adam · 36 h'),
          ('Novembre', 'Séquences Brevo', '200 €', 'Emma · 20 h')]
    cards = []
    for m, n, bud, who in ch:
        cards.append(f'''<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {PETROLE};border-radius:16px;padding:18px 22px 20px;display:flex;flex-direction:column;gap:8px">
<p style="font-family:{L};font-size:26px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{PETROLE}">{m}</p>
<p style="font-size:28px;font-weight:700;line-height:1.2;color:{ENCRE}">{n}</p>
{num(bud, 80, ORF)}
<p style="font-size:24px;line-height:1.25;color:{GRIS}">{who}</p></div>''')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 30, SARC, 4)}</div>'
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;align-items:center;gap:14px">{label('À déployer en 2026', TXT[ORANGE], ls=2)}{pill('OBJECTIF')}</div>
<div style="display:flex;gap:12px;align-items:stretch">{ar.join(cards)}</div>
</div>'''
    why = _ressources_why('4 ressources sur 17 manquent ; CRM\u00a0incomplet.',
                          'La donnée, puis les supports, puis\u00a0l’automatisation.',
                          'Un critère par chantier ; sinon, pas\u00a0d’étape suivante.')
    sp = '<div style="flex:1"></div>'
    # pied : padding bas 64 + cale fixe de 72 px (sans texte) = même bas de contenu (920 px) que le gabarit standard
    inner = f'''{header3('Piloter · Partie 12 · Ressources', 'Trois chantiers d’abord : 800 € sur 3 000 €', PETROLE, tags=['MA CONTRIBUTION', 'À DÉPLOYER'])}
{sp}
<div style="display:flex;gap:56px;align-items:flex-start">{left}{right}</div>
{sp}
{why}
<div style="height:72px;flex:none"></div>
{footer(16, 'Piloter')}'''
    return 'ressources', inner, dict(gap=24, pad='128px 128px 64px', sect=SECT_PILOTER)


def _salesops_why(constat, decision, mesure):
    # même bandeau que kit.why3 (Constat → Ma décision → Ce que l'on mesure), avec le statut OBJECTIF visible à côté de la cible
    def cell(lab, txt, c, st=''):
        head = (f'<div style="display:flex;align-items:center;gap:12px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{c};white-space:nowrap">{lab}</p>{st}</div>')
        return (f'<div style="flex:1;display:flex;flex-direction:column;gap:6px">{head}'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    pst = 'align-self:center;padding:0px 12px;line-height:1.2;background:transparent;color:#FFFFFF;border-color:#FFFFFF'
    return (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:stretch;gap:18px">'
            f'{cell("CONSTAT", constat, BLEU)}{ar}'
            f'{cell("MA DÉCISION", decision, CHAMP)}{ar}'
            f'{cell("CE QUE L’ON MESURE", mesure, BLEU, pill("OBJECTIF", pst))}</div>')


def _salesops_tool(name, role):
    # outil existant : carte blanche à filet gris plein (même code que la pastille EXISTANT)
    return (f'<div style="align-self:center;background:#FFFFFF;border:2px solid #B8C4C8;border-radius:14px;padding:8px 20px;display:flex;flex-direction:column;gap:2px">'
            f'<p style="font-size:30px;font-weight:700;line-height:1.2;color:{ENCRE}">{name}</p>'
            f'<p style="font-size:26px;line-height:1.25;color:{GRIS}">{role}</p></div>')


def _salesops_add(name, tg, role, box):
    # ce qui change autour de HubSpot : une pastille de statut par carte
    return (f'<div style="grid-row:span 2;align-self:center;{box};border-radius:16px;padding:14px 20px;display:flex;flex-direction:column;gap:6px">'
            f'<div style="display:flex;flex-wrap:wrap;align-items:center;gap:8px 14px"><p style="font-size:30px;font-weight:700;line-height:1.2;color:{ENCRE}">{name}</p>{ctag(tg)}</div>'
            f'<p style="font-size:26px;line-height:1.25;color:{GRIS}">{role}</p></div>')


def salesops():
    # Message (titre) : une donnée, un propriétaire, une décision (le principe dit dans la note).
    # Point focal : HubSpot au centre, source de vérité ; à gauche les quatre outils existants branchés dessus ;
    # à droite ce qui change : le câblage Brevo (flèche orange, à déployer) et le dictionnaire CRM (ma contribution).
    # Hors écran : le détail des quatre règles marketing-ventes (note ; cadence dès PA-FIT 55 et nurture 45 j : secours B12 ;
    # motifs de perte → objections : secours B14) ; les durées des rituels (note : de 10 min par jour à 90 min par trimestre) ;
    # « contact loggé < 24 h » (note) ; « 448 prospects non qualifiés » (diapo 7, note de la diapo 8, secours B15) ;
    # « prévu en nov. » (note : « à partir de novembre »). Le score d'hygiène = la mesure du bandeau (pipeline complet ≥ 95 % le lundi).
    grey = '#B8C4C8'
    stub = f'<div style="align-self:center;height:4px;background:{grey}"></div>'
    to_brevo = (f'<svg width="64" height="24" viewBox="0 0 64 24">'
                f'<path d="M2 12 H50" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="9 6" fill="none"/>'
                f'<path d="M46 4 L58 12 L46 20" stroke="{ORANGE}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')
    to_hub = (f'<svg width="64" height="24" viewBox="0 0 64 24">'
              f'<path d="M62 12 H14" stroke="{SARC}" stroke-width="4" stroke-dasharray="9 6" fill="none"/>'
              f'<path d="M18 4 L6 12 L18 20" stroke="{SARC}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" fill="none"/></svg>')
    hub = (f'<div style="grid-row:span 4;background:{NUIT};border:6px solid {SARC};border-radius:36px;padding:24px 20px;'
           f'display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px">'
           f'<p style="font-family:{T};font-size:60px;font-weight:700;line-height:1.1;color:#FFFFFF">HubSpot</p>'
           f'<p style="font-size:28px;line-height:1.25;text-align:center;color:{BRUME}">source de vérité</p></div>')
    brevo = _salesops_add('Brevo (existant)', 'À DÉPLOYER', 'câblage HubSpot, stop sur réponse',
                          f'background:#FFFFFF;border:2px solid {grey}')
    dico = _salesops_add('Dictionnaire CRM', 'MA CONTRIBUTION', 'motifs de perte, à ratifier',
                         f'background:#E8F4F6;border:3px dashed {SARC}')
    tools = [("Planet'Connect", 'trace chaque envoi'), ('Tableaux de bord', 'CA et délais réels'),
             ('Workspace + WhatsApp', 'documents, messagerie adhérents'), ('E-signature + Drive', 'documentation annuelle')]
    t = [_salesops_tool(n, r) for n, r in tools]
    e = '<div></div>'
    # grille : outils | branchement | HubSpot | branchement | ce qui change ; cellules remplies dans l'ordre du source
    cells = (f'<div style="display:flex">{ctag("EXISTANT")}</div>{e}{e}{e}{e}'
             f'{t[0]}{stub}{hub}<div style="grid-row:span 2;align-self:center;display:flex">{to_brevo}</div>{brevo}'
             f'{t[1]}{stub}'
             f'{t[2]}{stub}<div style="grid-row:span 2;align-self:center;display:flex">{to_hub}</div>{dico}'
             f'{t[3]}{stub}')
    diagram = f'<div style="display:grid;grid-template-columns:1fr 56px 340px 64px 1fr;gap:10px 0px">{cells}</div>'
    why = _salesops_why('Outils déjà là, sans règles\u00a0communes.',
                        'Règles communes proposées : marketing-ventes, rituels.',
                        'Pipeline complet ≥ 95 % chaque\u00a0lundi.')
    sp = '<div style="flex:1"></div>'
    # pied : padding bas 64 + cale fixe de 96 px (sans texte) = bas du contenu à 920 px, comme le gabarit standard
    # en-tête : MA CONTRIBUTION seule ; EXISTANT et À DÉPLOYER sont posés dans le schéma, sur les éléments qu'ils qualifient
    inner = f'''{header3('Piloter · Partie 13 · Sales Operations', 'Une donnée, un propriétaire, une décision', PETROLE, tags=['MA CONTRIBUTION'])}
{sp}
{diagram}
{sp}
{why}
<div style="height:96px;flex:none"></div>
{footer(17, 'Piloter')}'''
    return 'salesops', inner, dict(gap=0, pad='128px 128px 64px')


def _onboarding_step(day, status, proof, color):
    # une marche de l'escalier : le jalon en grand, le palier, puis LA preuve qui le valide (celle que dit la note)
    return (f'<div style="flex:1;background:{color};border-radius:16px 16px 0px 0px;padding:20px 28px 24px;display:flex;flex-direction:column;gap:8px">'
            f'{num(day, 64, "#FFFFFF")}'
            f'<p style="font-family:{L};font-size:28px;font-weight:600;letter-spacing:2px;line-height:1.2;color:{CHAMP}">{status}</p>'
            f'<p style="font-size:30px;line-height:1.25;color:#FFFFFF">{proof}</p></div>')


def onboarding():
    # Message (titre) : opérationnel en 90 jours, chaque palier validé par une preuve (la note le dit).
    # Point focal : l'escalier J+30 → J+60 → J+90, une preuve par marche ; le drapeau S8 (premier adhérent
    # signé et activé, « ligne d'arrivée », même code orange que la diapo 15) est planté sur la marche J+60 : S8 tombe au mois 2.
    # Coin haut gauche : statut OBJECTIF + « parcours livré, pas encore testé » (limite dite dans la note).
    # Bandeau : la règle pédagogique. Hors écran : contenus détaillés des paliers, S1-S4 et socle (dossier, chap. 15,
    # annexe U, avant-propos) ; qui forme qui (ajouté à la note) ; page de l'annexe U (secours B15 la cite).
    gapc = 16
    s1 = _onboarding_step('J+30', 'CERTIFIÉ', 'Certification signée', SARCF)
    s2 = _onboarding_step('J+60', 'AUTONOME', '1 RDV obtenu seul', PETROLE)
    s3 = _onboarding_step('J+90', 'PILOTE', '1 amélioration du playbook', NUIT)
    status = (f'<div style="display:flex;flex-direction:column;gap:6px">{pill("OBJECTIF")}'
              f'<p style="font-size:24px;line-height:1.25;color:{GRIS}">parcours livré, pas encore testé</p></div>')
    flag = (f'<div style="display:flex;gap:16px;padding-left:28px">'
            f'<div style="width:6px;background:{ORF};flex:none"></div>'
            f'<div style="display:flex;flex-direction:column;gap:8px;padding-bottom:16px">'
            f'<div style="display:flex"><p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:1px;color:#FFFFFF;background:{ORF};border-radius:999px;padding:2px 16px;white-space:nowrap">LIGNE D’ARRIVÉE</p></div>'
            f'<div style="display:flex;align-items:center;gap:16px">{num("S8", 52, ORF)}'
            f'<p style="font-size:28px;font-weight:700;line-height:1.2;color:{ENCRE}">1er adhérent<br>signé et activé</p></div>'
            f'</div></div>')
    # marches sans hauteur fixe : chaque colonne s'étire à la hauteur de la plus haute ; la marche remplit (flex:1)
    # sous une cale sans texte (col. 1) ou sous le drapeau (col. 2) ; la col. 3 est pleine hauteur.
    col1 = f'<div style="flex:1;display:flex;flex-direction:column">{status}<div style="height:180px;flex:none"></div>{s1}</div>'
    col2 = f'<div style="flex:1;display:flex;flex-direction:column">{flag}{s2}</div>'
    col3 = f'<div style="flex:1;display:flex;flex-direction:column">{s3}</div>'
    stairs = f'<div style="display:flex;gap:{gapc}px;align-items:stretch">{col1}{col2}{col3}</div>'
    rule = (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:center;gap:24px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">LA RÈGLE</p>'
            f'<p style="flex:1;font-family:{T};font-style:italic;font-size:32px;line-height:1.25;color:#FFFFFF">« On observe avant de faire, on fait accompagné avant de faire seul. »</p></div>')
    sp = '<div style="flex:1"></div>'
    # marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{header3('Piloter · Partie 13 · Onboarding', 'Opérationnel en 90 jours : une preuve par palier', PETROLE, tags=['MA CONTRIBUTION', 'À MESURER'])}
{sp}
{stairs}
{sp}
{rule}
<div style="height:72px;flex:none"></div>
{footer(18, 'Piloter')}'''
    return 'onboarding', inner, dict(gap=24, pad='128px 128px 64px')


def _kpi_why(constat, decision, mesure):
    # même bandeau que kit.why3 (Constat → Ma décision → Ce que l'on mesure), texte à 26 px comme les autres candidates
    def cell(lab, txt, c, f=1):
        return (f'<div style="flex:{f};display:flex;flex-direction:column;gap:6px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{c};white-space:nowrap">{lab}</p>'
                f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{txt}</p></div>')
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    return (f'<div style="background:{NUIT};border-radius:16px;padding:18px 28px;display:flex;align-items:stretch;gap:18px">'
            f'{cell("CONSTAT", constat, BLEU)}{ar}{cell("MA DÉCISION", decision, CHAMP)}{ar}{cell("CE QUE L’ON MESURE", mesure, BLEU)}</div>')


def _kpi_mini(name, tgt):
    # objectif secondaire : un nom, une cible (fréquence et action si écart : secours B6)
    return (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {BORD};border-radius:14px;padding:10px 16px;'
            f'display:flex;align-items:center;justify-content:space-between;gap:16px">'
            f'<p style="font-size:26px;font-weight:700;line-height:1.2;color:{ENCRE};white-space:nowrap">{name}</p>{num(tgt, 32, BORD)}</div>')


def kpi():
    # Message (titre) : mesuré ou espéré ? Chaque KPI déclenche une action.
    # Point focal : à droite, la fiche de l'indicateur d'activation (cible ≥ 70 % en grand ; source · fréquence · responsable ;
    # l'action si l'écart se creuse) où l'on retrouve le domaine du cas ; à gauche, le constaté (capture réelle, ~145 signés).
    # Hors écran : 1,45 % d'annulations (dit dans la note) ; 89,8 % d'envois assurés (secours B11 · B14) ; formules, sources,
    # responsables et actions des trois autres indicateurs (secours B6 et indication de la note) ; « puis chaque trimestre » (note) ;
    # « close par une décision » (note).
    cap = shot(DASH_NEW, 'Capture réelle du tableau de bord Planet’Connect : évolution des nouveaux adhérents du 24/09/2025 au 24/09/2026',
               540, 166, 'Planet’Connect', fit='contain')
    left = f'''<div style="width:540px;flex:none;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:center;gap:14px">{pill('CONSTATÉ', 'align-self:center')}<p style="font-size:24px;line-height:1.3;color:{GRISD};white-space:nowrap">point zéro, 24/09/2026</p></div>
{cap}
<div style="display:flex;align-items:center;gap:20px">{num('~145', 56, SARCF)}<p style="font-size:28px;line-height:1.2;color:{ENCRE}">signés en 12 mois</p></div>
</div>'''
    focal = f'''<div style="flex:1.25;background:#FFFFFF;border:2px solid {BORD};border-top:10px solid {BORD};border-radius:16px;padding:16px 26px 20px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;justify-content:space-between;gap:20px"><p style="font-family:{L};font-size:32px;font-weight:700;line-height:1.2;color:{ENCRE}">Activation J+30</p>{num('≥ 70 %', 72, BORD)}</div>
<p style="font-size:26px;line-height:1.25;color:{GRISD}">CRM · mensuel · commercial</p>
<p style="background:#F6EAEE;border-radius:10px;padding:8px 18px;font-size:28px;line-height:1.25;color:{ENCRE}"><b>Sous 50 %</b> → revoir l’onboarding</p>
<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap"><p style="{CASE_BOX};border-radius:10px;padding:6px 18px;font-family:{T};font-style:italic;font-size:28px;line-height:1.25;color:{ENCRE};white-space:nowrap">Domaine activé</p>{pill('ILLUSTRATIF', 'align-self:center')}</div>
</div>'''
    minis = ''.join(_kpi_mini(n, t) for n, t in [('RDV → proposition', '≥ 70 %'), ('Taux de gain', '40–60 %'), ('Adhérents actifs', '&gt; 60 %')])
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:14px">
{pill('OBJECTIF')}
<div style="flex:1;display:flex;gap:20px;align-items:stretch">{focal}<div style="flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:12px">{minis}</div></div>
</div>'''
    why = _kpi_why('Conversions et activation jamais mesurées.',
                   'Revue mensuelle proposée.',
                   'Première lecture : fin décembre.')
    sp = '<div style="flex:1"></div>'
    # marge basse : 64 px de padding + entretoise fixe de 76 px (sans texte) + 20 px d'écart = bas du contenu à 920 px,
    # même dispositif que les autres candidates (au rendu +10 %, le pied de page épinglé reste hors du flux).
    inner = f'''{head_case(header3('Piloter · Partie 14 · Indicateurs', 'Mesuré ou espéré ? Chaque KPI déclenche une action', PETROLE, tags=['EXISTANT', 'MA CONTRIBUTION', 'À MESURER']), 'Suivre')}
{sp}
<div style="display:flex;gap:56px;align-items:stretch">{left}{right}</div>
{sp}
{why}
<div style="height:76px;flex:none"></div>
{footer(19, 'Piloter')}'''
    return 'kpi', inner, dict(gap=20, pad='128px 128px 64px')


def _conclusion_enjeu(i, enjeu, reponse):
    # même pastille et même libellé que les trois enjeux du diagnostic (diapo 7) : la réponse se lit enjeu par enjeu
    return (f'<div style="flex:1;display:flex;gap:16px;align-items:flex-start">'
            f'<div style="width:48px;height:48px;border-radius:50%;background:{CHAMP};display:flex;align-items:center;justify-content:center;flex:none">'
            f'<p style="font-family:{L};font-size:26px;font-weight:700;color:{NUIT}">{i}</p></div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:6px">'
            f'<p style="font-family:{T};font-size:32px;font-weight:700;line-height:1.2;color:#FFFFFF">{enjeu}</p>'
            f'<p style="font-size:28px;line-height:1.3;color:{BRUME}">{reponse}</p></div></div>')


def _conclusion_cell(lab, c, text, extra=''):
    return (f'<div style="flex:1;border-top:4px solid {c};padding-top:12px;display:flex;flex-direction:column;gap:8px">'
            f'<div style="display:flex;align-items:center;gap:14px">{label(lab, c, ls=2)}{extra}</div>'
            f'<p style="font-size:28px;line-height:1.3;color:{CLAIR}">{text}</p></div>')


def conclusion():
    # Message (titre) : retour à l'accroche, ils repartent les mains libres.
    # Point focal : les 24 bouteilles pleines, au même gabarit que les 2 sur 24 de l'accroche (diapo 2).
    # Puis la réponse à la problématique, enjeu par enjeu (mêmes pastilles que la diapo 7), et un bandeau :
    # bénéfice visé (OBJECTIF), limite, ouverture. Le panier, l'apport détaillé, la difficulté, le second bénéfice,
    # la phrase finale sur le risque sont dits dans la note ; l'apport et la difficulté sont aussi en secours B15.
    answer = f'''<div style="display:flex;flex-direction:column;gap:20px">
<div style="display:flex;align-items:baseline;gap:18px">{label('Ma réponse', BLEU, ls=3)}<p style="font-family:{T};font-size:34px;font-weight:700;line-height:1.2;color:{CHAMP}">une méthode reproductible et mesurable</p></div>
<div style="display:flex;gap:40px">
{_conclusion_enjeu(1, 'Recruter les bons comptes', '5 ICP, un score, une cadence')}
{_conclusion_enjeu(2, 'Activer et fidéliser', 'la vente finit au 1er envoi')}
{_conclusion_enjeu(3, 'Transmettre et mesurer', '90 jours, des KPI à statut')}
</div></div>'''
    merci = (f'<div style="display:flex;align-items:flex-end;gap:18px;flex:none">'
             f'<img src="{LOGO_MARK_W}" alt="Logo Planet Aura" style="width:54px;height:72px;object-fit:contain">'
             f'<p style="font-family:{T};font-size:52px;font-weight:700;line-height:1.1;color:#FFFFFF">Merci.</p></div>')
    band = f'''<div style="display:flex;gap:40px;align-items:flex-end">
<div style="flex:1;display:flex;gap:40px;align-items:stretch">
{_conclusion_cell('Bénéfice visé', CHAMP, '<b>≥ 70 %</b> des signés<br>activés à J+30', pill('OBJECTIF', 'line-height:1.2'))}
{_conclusion_cell('Limite', '#E2A39A', '<b>Effet pas encore mesuré</b> :<br>lecture fin décembre')}
{_conclusion_cell('Ouverture', BLEU, '<b>Diversifier</b> :<br>UK, UE, Japon')}
</div>
{merci}
</div>'''
    sp = '<div style="flex:1;min-height:20px"></div>'
    inner = f'''{header3('Synthèse et ouverture', 'Ils repartent les mains libres', BLEU, tags=['MA CONTRIBUTION', 'À MESURER'], tcolor='#FFFFFF')}
{sp}
{bottles(24)}
{sp}
{answer}
{sp}
{band}
<div style="height:96px;flex:none"></div>
{footer(20, dark=True, label='Comprendre · Cibler · Vendre · Activer · Piloter')}'''
    # marge basse : 64 px de padding + 96 px d'entretoise sans texte = les 160 px habituels (bas du corps à 920 px) ;
    # le pied de page (les cinq étapes en blanc : le parcours est complet) reste dans la limite du banc, même à +10 %
    return 'conclusion', inner, dict(bg=NUIT, color=CLAIR, gap=0, pad='128px 128px 64px',
                                     sect="Synthèse et ouverture : réponse à la problématique, apport, limites, retour à l'accroche")
