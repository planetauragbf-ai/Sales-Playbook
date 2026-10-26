# Diapositives de secours B1 à B17 (questions du jury), même système visuel que le deck principal.
# v5 : 130 mots visibles au plus par secours ; B17, ajoutée en v5 : les sept étapes du processus (qui, preuve, délai, outil), retirées de l’écran de la diapo 11.
from kit import *

ORG = '/_blob/f6153fe677b16873e49378b0adbd4f01'  # ancienne image de l’organigramme (B9 recomposée en natif)
USMAP = '/_blob/c237626e9530474ba834563336e2b6c9'
ARBRE = '/_blob/c0b87ff1fc42b54deca64e6c705b3137'
SEQ = '/_blob/1386c229e7278bcd00815efe2155b121'
USMAP2 = '/_blob/6e61857966cc7cade3f90e50fc4ced2c'


def bhead(n, sujet, title):
    return header3(f'Secours · B{n} · {sujet}', title, GRISD)


def bfoot(n):
    return footer(f'B{n}', label='Diapositives de secours')


def table(head, rows, widths, size=24, pad=11):
    th = ''.join(f'<th style="width:{w}%;font-family:{L};font-size:{size}px;font-weight:600;color:{PETROLE};padding:0px 18px 10px 0px">{h}</th>' for h, w in zip(head, widths))
    tr = ''.join('<tr>' + ''.join(f'<td style="padding:{pad}px 18px {pad}px 0px">{c}</td>' for c in r) + '</tr>' for r in rows)
    return f'<table style="width:100%;font-size:{size}px;color:{ENCRE}"><tr>{th}</tr>{tr}</table>'


def box(lbl, body, color=PETROLE, dark=False):
    if dark:
        return (f'<div style="background:{NUIT};border-radius:16px;padding:20px 26px;display:flex;flex-direction:column;gap:8px">'
                f'{label(lbl, CHAMP, ls=2)}<p style="font-size:24px;line-height:1.35;color:{CLAIR}">{body}</p></div>')
    return (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {color};border-radius:14px;padding:18px 24px;display:flex;flex-direction:column;gap:6px">'
            f'{label(lbl, color, ls=2)}<p style="font-size:24px;line-height:1.35;color:{ENCRE}">{body}</p></div>')


def _b1_check():
    # coche verte (statut « confirmé »), dessinée : pas de glyphe hors police
    return ('<svg width="26" height="26" viewBox="0 0 26 26" style="flex:none"><path d="M5 13.5 L10.5 19 L21 7" stroke="#2F7A50" '
            'stroke-width="3.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def _b1_row(letter, name, nuance, n):
    # une ligne par persona : lettre, nom, verdict (coche + nuance), barre des contacts rattachés
    circ = (f'<div style="width:48px;height:48px;border-radius:50%;background:{BORD};display:flex;align-items:center;'
            f'justify-content:center;flex:none"><p style="font-family:{L};font-size:26px;font-weight:700;color:#FFFFFF">{letter}</p></div>')
    rest = f'<span style="color:{GRIS}"> {nuance}</span>' if nuance else ''
    verdict = (f'<div style="display:flex;align-items:flex-start;gap:8px">{_b1_check()}'
               f'<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:#2F7A50">Confirmé</span></b>{rest}</p></div>')
    bar = (f'<div style="display:flex;align-items:center;gap:14px">'
           f'<div style="width:{round(n * 11)}px;height:26px;border-radius:6px;background:{BORD};flex:none"></div>'
           f'{num(str(n), 40, BORD)}</div>')
    return (f'<div style="display:flex;align-items:center;gap:20px;padding:7px 0px;border-bottom:1px solid {FILET}">'
            f'{circ}'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-size:28px;font-weight:600;line-height:1.2;color:{ENCRE}">{name}</p>{verdict}</div>'
            f'<div style="width:230px;flex:none;display:flex;align-items:center">{bar}</div></div>')


def _b1_blind(name, text):
    # l'angle mort : même gabarit que les personas, cercle en pointillé orange, sans barre
    circ = (f'<div style="width:48px;height:48px;border-radius:50%;border:3px dashed {ORANGE};display:flex;align-items:center;'
            f'justify-content:center;flex:none"><p style="font-family:{L};font-size:26px;font-weight:700;color:{TXT[ORANGE]}">+</p></div>')
    return (f'<div style="display:flex;align-items:center;gap:20px;padding:10px 0px 0px 0px">{circ}'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-size:28px;font-weight:600;line-height:1.2;color:{TXT[ORANGE]}">{name}</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{GRIS}">{text}</p></div></div>')


def _b1_stat(n, what, sub):
    return (f'<div style="display:flex;align-items:center;gap:14px">'
            f'<div style="width:84px;flex:none">{num(n, 52, PETROLE)}</div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:2px">'
            f'<p style="font-size:28px;font-weight:600;line-height:1.2;color:{ENCRE}">{what}</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{GRISD}">{sub}</p></div></div>')


def b1():
    # Message : les cinq personas tiennent face à nos données réelles (5 sur 5 confirmés).
    # Point focal : les cinq lignes, chacune avec sa coche verte et sa barre de contacts rattachés (14, 8, 7, 15, 5 = 49).
    # En appui à droite : la base de l'étude (70 · 47 · 15) et la limite assumée.
    # Hors écran (indications non dites de la note) : détail des 47 réponses par enquête, le cas unique de conciergerie.
    rows = ''.join([
        _b1_row('A', 'Vigneron-propriétaire', '', 14),
        _b1_row('B', 'Responsable caveau', '· fort turnover', 8),
        _b1_row('C', 'Caviste', 'et élargi : caves touristiques, en ligne, réseaux', 7),
        _b1_row('D', 'Directeur commercial', '· accès par l’ADV dans les grandes maisons', 15),
        _b1_row('E', 'Client final étranger', ': particulier ou collectionneur', 5)])
    left = f'''<div style="flex:1;display:flex;flex-direction:column;gap:6px">
<div style="display:flex;align-items:center;gap:16px">{label('49 contacts rattachés', BORD, size=26, ls=2)}{pill('CONSTATÉ', 'align-self:center')}</div>
<div style="display:flex;flex-direction:column">{rows}</div>
{_b1_blind('Angle mort', 'une dizaine d’ADV, comptables et logisticiens, traités par le comité d’achat')}
</div>'''
    base = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {PETROLE};border-radius:16px;padding:20px 26px 22px 26px;display:flex;flex-direction:column;gap:14px">
<div style="display:flex;align-items:center;gap:14px">{label('La base', PETROLE, ls=2)}<div style="flex:1"></div>{pill('CONSTATÉ', 'align-self:center')}</div>
{_b1_stat('70', 'contacts pro', '40 e‑mails · 30 salons et CRM')}
{_b1_stat('47', 'réponses', '3 enquêtes')}
{_b1_stat('15', 'avis Google', '+ top 10 anonymisé')}
</div>'''
    limit = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {ORANGE};border-radius:16px;padding:18px 26px 20px 26px;display:flex;flex-direction:column;gap:8px">
{label('Limite assumée', ORANGE, ls=2)}
<p style="font-size:24px;line-height:1.35;color:{ENCRE}">Échanges écrits, pas d’entretien dédié<br>Prospects sous‑représentés (4 réponses)<br>Entretiens prévus au T1 2027</p>
</div>'''
    right = f'<div style="width:560px;flex:none;display:flex;flex-direction:column;gap:22px">{base}{limit}</div>'
    # marge basse : padding 64 + entretoise 66 + écart 30 = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates principales (au rendu +10 %, le texte du pied de page épinglé n'est plus compté dans le flux).
    inner = f'''{bhead(1, 'Personas', 'Cinq personas sur cinq confirmés par nos données')}
<div style="flex:1;display:flex;gap:48px;align-items:flex-start">{left}{right}</div>
<div style="height:66px;flex:none"></div>
{bfoot(1)}'''
    return 'b1', inner, dict(gap=30, pad='128px 128px 64px')


def _b2_chip(tool, role, hi=False):
    # un outil de la chaîne, et son seul rôle, sur une ligne ; le PA-FIT (la grille qui fait foi) est plein
    bg, fg, rc, bd = (BORD, '#FFFFFF', CHAMP, BORD) if hi else ('#FFFFFF', BORD, GRISD, FILET)
    return (f'<div style="flex:1;background:{bg};border:2px solid {bd};border-radius:14px;padding:8px 18px;display:flex;align-items:center">'
            f'<p style="font-size:24px;line-height:1.25;color:{rc}"><b><span style="font-family:{L};font-size:26px;color:{fg}">{tool}</span></b> · {role}</p></div>')


def _b2_crit(name, pts, color):
    # un critère du PA-FIT : nom, barre proportionnelle aux points, points
    return (f'<div style="display:flex;align-items:center;gap:18px">'
            f'<p style="width:260px;flex:none;font-size:26px;line-height:1.2;color:{ENCRE}">{name}</p>'
            f'<div style="width:{pts * 30}px;height:30px;border-radius:6px;background:{color};flex:none"></div>'
            f'{num(str(pts), 30, BORD)}</div>')


def _b2_band(rng, meaning, bg, fg):
    # un palier de lecture du total
    return (f'<div style="display:flex;align-items:center;gap:16px">'
            f'<div style="width:132px;flex:none;background:{bg};border-radius:10px;padding:4px 0px;display:flex;justify-content:center">'
            f'<p style="font-family:{L};font-size:26px;font-weight:700;color:{fg};white-space:nowrap">{rng}</p></div>'
            f'<p style="flex:1;font-size:26px;line-height:1.25;color:{ENCRE}">{meaning}</p></div>')


def b2():
    # Message : quatre outils, un rôle chacun, et une seule grille saisie au CRM, le PA-FIT.
    # Point focal : le PA-FIT, 8 critères en barres proportionnelles (100 points), et ce que le total décide (75 · 55 · 35).
    # En haut : la chaîne CAVE → express /20 → PA-FIT /100 → tiers ; en bas, la règle (bandeau sombre).
    # Hors écran (indications non dites de la note) : sens de CAVE et « qualifié = C confirmé, A identifié, E daté » ;
    # paliers du score express (≥ 14, 8-13, < 8). Rôle de chaque outil et cadence dès 55 : dits dans la note.
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, BLEU, 4)}</div>'
    chain = (f'<div style="display:flex;align-items:stretch;gap:12px">'
             f'{_b2_chip("CAVE", "trier")}{ar}{_b2_chip("Express /20", "brouillon")}{ar}'
             f'{_b2_chip("PA-FIT /100", "fait foi", hi=True)}{ar}{_b2_chip("Tiers A · B · C", "rythme")}</div>')
    crits = [('ICP', 15, BORD), ('Flux', 15, BORD), ('Problème', 15, BORD), ('Volume', 15, BORD), ('Timing', 15, BORD),
             ('Décision', 10, '#A86A7E'), ('Préparation', 10, '#A86A7E'), ('Valeur stratégique', 5, '#C9A5B1')]
    left = (f'<div style="flex:1;display:flex;flex-direction:column;gap:14px">'
            f'{label("PA-FIT : 8 critères, 100 points", BORD, size=26, ls=2)}'
            f'<div style="display:flex;flex-direction:column;gap:4px">{"".join(_b2_crit(*c) for c in crits)}</div></div>')
    right = (f'<div style="width:620px;flex:none;display:flex;flex-direction:column;gap:14px">'
             f'<div style="display:flex;align-items:center;gap:14px">{label("Le total décide", BORD, size=26, ls=2)}<div style="flex:1"></div>{pill("RÈGLE", "align-self:center")}</div>'
             f'<div style="display:flex;flex-direction:column;gap:6px">'
             f'{_b2_band("75–100", "P1 · priorité active", BORD, "#FFFFFF")}'
             f'{_b2_band("55–74", "P2 · à développer", "#A86A7E", "#FFFFFF")}'
             f'{_b2_band("35–54", "nurture", "#DDBFC9", BORD)}'
             f'{_b2_band("&lt; 35", "disqualifié ou veille", "#EEF3F4", GRISD)}</div>'
             f'<div style="height:2px;background:{FILET}"></div>'
             f'<div style="display:flex;align-items:center;gap:14px">{label("Tiers, en envois par an", PETROLE, ls=2)}<div style="flex:1"></div>{pill("OBJECTIF", "align-self:center")}</div>'
             f'<p style="font-size:26px;line-height:1.3;color:{ENCRE}">A &gt; 150 · B 40–150 · C &lt; 40<br>80 % du temps sur A et B</p></div>')
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:12px 26px;display:flex;align-items:center;gap:22px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">LA RÈGLE</p>'
            f'<p style="flex:1;font-size:28px;line-height:1.3;color:{CLAIR}">Un score sans preuve vaut zéro · barème recalibré après 90 jours</p></div>')
    # marge basse : padding 64 + entretoise 72 + écart 24 = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates principales (au rendu +10 %, le texte du pied de page épinglé n'est plus compté dans le flux).
    inner = f'''{bhead(2, 'Priorisation', 'Trier vite, noter une fois : une seule grille fait foi')}
{chain}
<div style="flex:1;display:flex;gap:56px;align-items:center">{left}{right}</div>
{band}
<div style="height:72px;flex:none"></div>
{bfoot(2)}'''
    return 'b2', inner, dict(gap=24, pad='128px 128px 64px')


_b3_W = (330, 364, 384)  # largeurs des trois premières colonnes ; la question prend le reste (≈ 538 px)


def _b3_head(text, color, tail=True):
    # en-tête de colonne : l'étape de la méthode ; une flèche en bout de colonne mène à l'étape suivante (l'ordre est la méthode)
    ar = f'<div style="flex:1"></div><div style="display:flex;align-items:center;flex:none">{arrow(40, 24, BLEU, 4)}</div>' if tail else ''
    return (f'<div style="display:flex;align-items:center;gap:10px">'
            f'<p style="font-family:{L};font-size:28px;font-weight:700;color:{color};white-space:nowrap">{text}</p>{ar}</div>')


def _b3_row(said, recog, refocus, ask, last=False):
    bb = '' if last else f'border-bottom:1px solid {FILET};'
    return (f'<div style="display:flex;align-items:flex-start;gap:16px;padding:9px 0px;{bb}">'
            f'<p style="width:{_b3_W[0]}px;flex:none;font-size:24px;font-weight:600;line-height:1.3;color:{ENCRE}">{said}</p>'
            f'<p style="width:{_b3_W[1]}px;flex:none;font-size:24px;line-height:1.3;color:{GRIS}">{recog}</p>'
            f'<p style="width:{_b3_W[2]}px;flex:none;font-size:24px;line-height:1.3;color:{GRIS}">{refocus}</p>'
            f'<p style="flex:1;font-size:24px;font-weight:600;line-height:1.3;color:{SARCF}">{ask}</p></div>')


def b3():
    # Message : face à un concurrent, on ne dénigre jamais : on reconnaît, on recentre, on questionne.
    # Point focal : la méthode en trois étapes fléchées (en-têtes de colonnes), appliquée aux cinq fiches.
    # En bas (bandeau sombre) : les trois questions gagnantes, communes à tous les concurrents.
    # Hors écran : les trois faiblesses assumées (dites dans la note) ; la date des sources publiques (indication de la note).
    head = (f'<div style="display:flex;align-items:center;gap:16px;padding-bottom:10px;border-bottom:3px solid {BRUME}">'
            f'<div style="width:{_b3_W[0]}px;flex:none">{label("Le prospect dit", GRISD, ls=2)}</div>'
            f'<div style="width:{_b3_W[1]}px;flex:none">{_b3_head("On reconnaît", PETROLE)}</div>'
            f'<div style="width:{_b3_W[2]}px;flex:none">{_b3_head("On recentre", PETROLE)}</div>'
            f'<div style="flex:1">{_b3_head("On demande", SARCF, tail=False)}</div></div>')
    rows = [('« J’ai déjà un compte\u00a0UPS »', 'Le transport physique', 'Douane, taxes, suivi, destinataire', '« Qui intervient en cas de blocage ? »'),
            (f'« Viticolis est moins cher\u00a0<span style="color:{GRISD}">[…]</span> »', 'Un très bon standard digital', 'Comparer le flux complet', '« Quel cas sort de leur standard ? »'),
            ('« Dartess offre tout »', 'Une forte capacité', 'Agilité, un seul interlocuteur', '« Quelle personnalisation vous manque ? »'),
            ('« DHL est mondial »', 'Un réseau incontestable', 'L’expertise vin', '« Qui connaît votre cuvée et vos\u00a0contraintes ? »'),
            ('« On gère tout en\u00a0interne »', 'Une équipe qui connaît ses\u00a0clients', 'Temps et risque', '« Que se passe\u2011t\u2011il quand la personne référente est\u00a0absente ? »')]
    table = head + ''.join(_b3_row(*r, last=(i == len(rows) - 1)) for i, r in enumerate(rows))
    qs = [('« Qui paie les taxes, et quand ? »', 34), ('« Sur quelle valeur êtes‑vous indemnisé si ça casse ? »', 55), ('« Qui fait la paperasse ? »', 27)]
    cells = ''.join(f'<p style="flex:{n};font-size:24px;line-height:1.3;color:{CLAIR}">{q}</p>' for q, n in qs)
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 28px 16px 28px;display:flex;flex-direction:column;gap:6px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP}">QUESTIONS GAGNANTES</p>'
            f'<div style="display:flex;gap:28px">{cells}</div></div>')
    # marge basse : padding 64 + entretoise 72 + écart 24 = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates principales (au rendu +10 %, le texte du pied de page épinglé n'est plus compté dans le flux).
    inner = f'''{bhead(3, 'Concurrence', 'Reconnaître, recentrer, questionner, sans dénigrer')}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center"><div style="display:flex;flex-direction:column">{table}</div></div>
{band}
<div style="height:72px;flex:none"></div>
{bfoot(3)}'''
    return 'b3', inner, dict(gap=24, pad='128px 128px 64px')


def _b4_step(n, cap, color):
    # un temps de l'approche : le chiffre en grand, sa légende dessous (écart ≥ 6 px)
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:6px">{num(n, 44, color)}'
            f'<p style="font-size:24px;line-height:1.3;color:{GRIS}">{cap}</p></div>')


def _b4_card(lbl, a, a_cap, b, b_cap, color):
    # une carte « permission » : premier contact → ce qu'il obtient
    ar = f'<div style="display:flex;align-items:center;flex:none;padding-top:10px">{arrow(48, 28, color, 4)}</div>'
    return (f'<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {color};border-radius:16px;padding:16px 24px 18px 24px;display:flex;flex-direction:column;gap:8px">'
            f'{label(lbl, color, ls=2)}'
            f'<div style="display:flex;align-items:flex-start;gap:16px">{_b4_step(a, a_cap, color)}{ar}{_b4_step(b, b_cap, color)}</div></div>')


def _b4_rung(k, q, w, bg, hi=False):
    # un barreau du tunnel 2 (S, P, I, N) ; I ressort, comme sur la diapo 13
    circ_bg, circ_fg = ('#FFFFFF', ORF) if hi else (SARCF, '#FFFFFF')
    fg = '#FFFFFF' if hi else ENCRE
    return (f'<div style="width:{w}px;align-self:center;background:{bg};border-radius:14px;padding:12px 26px 12px 14px;display:flex;align-items:center;gap:18px">'
            f'<div style="width:52px;height:52px;border-radius:50%;background:{circ_bg};display:flex;align-items:center;justify-content:center;flex:none">'
            f'<p style="font-family:{L};font-size:28px;font-weight:700;color:{circ_fg}">{k}</p></div>'
            f'<p style="flex:1;font-size:26px;{"font-weight:600;" if hi else ""}line-height:1.3;color:{fg}">{q}</p></div>')


def b4():
    # Message : au premier appel, on demande la permission ; le tunnel SPIN vient ensuite, adapté au profil.
    # Point focal : le tunnel 2 (maison de champagne), S → P → I → N, en entonnoir, I mis en valeur (même code que la diapo 13).
    # À gauche, en appui : la permission en deux cartes (caveau : < 3 min → 30 min ; compte structuré : 45 s → 25 min).
    # Hors écran : les deux questions de permission et les deux exemples de la banque (indications de la note) ;
    # « sur ses vins », « deux questions », « du vigneron à la distillerie » : dits dans la note.
    cards = (_b4_card('Caveau', f'<span style="font-family:{B};font-weight:600">&lt;</span> 3 min', 'd’appel', '30 min', 'de démo, pas\u00a0une\u00a0vente', SARCF)
             + _b4_card('Compte structuré', '45 s', 'de permission', '25 min', 'de cartographie du flux', ORF))
    left = (f'<div style="width:560px;flex:none;display:flex;flex-direction:column;gap:16px">'
            f'<div style="display:flex;align-items:center;gap:14px">{label("Avant le tunnel", ORF, size=26, ls=2)}<div style="flex:1"></div>{pill("RÈGLE", "align-self:center")}</div>'
            f'{cards}'
            f'<p style="font-size:24px;line-height:1.35;color:{GRISD}">Avant les pics, pas pendant<br>Bloc 10 h–12 h au téléphone</p></div>')
    W, STEP = 1040, 48
    fam = [('S', '« Quels marchés, modes, fréquences et incoterms utilisez-vous pour vos particuliers hors UE ? »', '#E4EFF2', False),
           ('P', '« Où perdez-vous visibilité ou temps : certificat CIVC, douane américaine, suivi ? »', '#D5E7EC', False),
           ('I', '« Que coûte un colis immobilisé en douane à l’image de la maison ? […] »', ORF, True),
           ('N', '« Que changerait un plan de flux documenté où le certificat et les taxes sont gérés à chaque envoi ? »', '#C3DCE2', False)]
    rungs = ''.join(_b4_rung(k, q, W - i * STEP, bg, hi) for i, (k, q, bg, hi) in enumerate(fam))
    right = (f'<div style="flex:1;display:flex;flex-direction:column;gap:12px">'
             f'{label("Tunnel 2 · Maison de champagne", SARCF, size=26, ls=2)}'
             f'<div style="display:flex;flex-direction:column;gap:10px">{rungs}</div>'
             f'<p style="font-size:24px;line-height:1.35;color:{GRISD}">La banque de questions décline le tunnel en 8 profils</p></div>')
    # marge basse : padding 64 + entretoise 66 + écart 30 = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les candidates principales (au rendu +10 %, le texte du pied de page épinglé n'est plus compté dans le flux).
    inner = f'''{bhead(4, 'SPIN sur le terrain', 'La permission avant le tunnel ; un tunnel par profil')}
<div style="flex:1;display:flex;flex-direction:column;justify-content:center"><div style="display:flex;gap:48px;align-items:flex-start">{left}{right}</div></div>
<div style="height:66px;flex:none"></div>
{bfoot(4)}'''
    return 'b4', inner, dict(gap=30, pad='128px 128px 64px')


def _b5_panel(word, sub, c, items):
    # une colonne = un mot-clé en grand (la forme / le fond), sa ligne d'appui, puis trois preuves courtes
    dot = (f'<div style="padding-top:13px;flex:none"><div style="width:12px;height:12px;border-radius:50%;background:{c}"></div></div>')
    li = ''.join(f'<div style="display:flex;gap:16px">{dot}<p style="font-size:28px;line-height:1.3;color:{ENCRE}">{i}</p></div>' for i in items)
    tc = TXT.get(c, c)
    return (f'<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {c};border-radius:16px;'
            f'padding:16px 32px 16px 32px;display:flex;flex-direction:column;gap:8px">'
            f'<p style="font-family:{T};font-size:52px;font-weight:700;line-height:1.1;color:{tc}">{word}</p>'
            f'<p style="font-family:{L};font-size:28px;font-weight:600;line-height:1.3;color:{tc}">{sub}</p>'
            f'<div style="display:flex;flex-direction:column;gap:24px;padding-top:8px">{li}</div></div>')


def b5():
    # Message (titre) : l'IA a aidé la forme ; le fond reste sourcé et vérifié.
    # Point focal : deux colonnes face à face, « La forme » (avec Claude) / « Le fond » (les sources), puis le test, en bas.
    # Hors écran (note, indication non dite) : la liste des huit chantiers (annexe W), le détail des règles harmonisées,
    # les noms des références externes (OIV, FEVS, Atout France…), « aucun identifiant ».
    forme = _b5_panel('La forme', 'avec Claude (Anthropic),<br>crédité dès l’avant\u2011propos', SARCF,
                      ['<b>8 chantiers de forme</b>, prompts en annexe\u00a0W',
                       '<b>Aussi, à déclarer</b> : des mises en cohérence, chaque\u00a0correction vérifiée à sa\u00a0source',
                       '<b>Ce support oral</b>, travaillé avec Claude, puis\u00a0relu'])
    fond = _b5_panel('Le fond', 'chaque chiffre<br>vérifié à sa source (annexe\u00a0C)', PETROLE,
                     ['<b>Documentation officielle 2026</b>, tableaux de bord Planet’Connect au\u00a024/09/2026',
                      '<b>3 enquêtes</b> (47 réponses), <b>24 références externes</b>\u00a0vérifiées',
                      '<b>Aucune image générée par IA</b>, aucune donnée personnelle de client\u00a0final'])
    test = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 32px 16px 32px;display:flex;flex-direction:column;gap:4px">'
            f'{label("Le meilleur contrôle, c’est vous", CHAMP, ls=2)}'
            f'<p style="font-family:{T};font-size:34px;font-weight:700;line-height:1.25;color:#FFFFFF">« Quel chiffre ou quelle procédure voulez-vous que je vous explique ? »</p></div>')
    # marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px) ;
    # même dispositif que les autres candidates : au rendu +10 %, le pied de page épinglé reste hors du flux.
    inner = f'''{bhead(5, 'Transparence IA', 'L’IA a aidé la forme ; le fond reste sourcé et vérifié')}
<div style="flex:1;display:flex;gap:40px">{forme}{fond}</div>
{test}
<div style="height:72px;flex:none"></div>
{bfoot(5)}'''
    return 'b5', inner, dict(gap=24, pad='128px 128px 64px')


_B6_W = (250, 490, 360)  # colonnes : fréquence, KPI, cible ; l'action prend le reste


def _b6_row(kpi, cible, action, last=False):
    # une ligne : le KPI, sa cible (en bordeaux, comme sur la diapo 19), l'action si l'écart se creuse
    bb = '' if last else f'border-bottom:1px solid {FILET};'
    return (f'<div style="display:flex;align-items:baseline;{bb}padding:6px 0px">'
            f'<p style="width:{_B6_W[1]}px;flex:none;padding-right:16px;font-size:26px;font-weight:700;line-height:1.25;color:{ENCRE}">{kpi}</p>'
            f'<p style="width:{_B6_W[2]}px;flex:none;padding-right:16px;font-family:{L};font-size:26px;font-weight:700;line-height:1.25;color:{BORD}">{cible}</p>'
            f'<p style="flex:1;font-size:26px;line-height:1.25;color:{ENCRE}">{action}</p></div>')


def _b6_group(freq, rows):
    # un groupe par fréquence : la fréquence n'est écrite qu'une fois, en tête de son groupe
    body = ''.join(_b6_row(*r, last=(i == len(rows) - 1)) for i, r in enumerate(rows))
    return (f'<div style="display:flex;border-top:2px solid {BLEU}">'
            f'<div style="width:{_B6_W[0]}px;flex:none;padding:10px 16px 0px 0px">{label(freq, PETROLE, size=24, ls=2)}</div>'
            f'<div style="flex:1;display:flex;flex-direction:column">{body}</div></div>')


def b6():
    # Message (titre) : chaque KPI a sa fréquence, sa cible, son action (titre raccourci : une ligne, même à +10 %).
    # Point focal : le tableau, groupé par fréquence (mensuel, hebdomadaire, par dossier) ; cibles = objectifs (pastille).
    # Ajout : la ligne « RDV → proposition » (déjà dans l'entonnoir de cette diapo ; action et fréquence de la diapo 19 v4),
    # que la note de la diapo 19 renvoie ici. En bas : le constaté, satisfaction 2024 (renvoi de la note du diagnostic).
    # Hors écran (note, indication non dite) : les cinq autres taux de l'entonnoir cible ; SAV 21 sur 22 ; 4,87/5 déjà en note ;
    # sources et responsables de chaque KPI (renvoi de la diapo 19), revue mensuelle de 45 minutes.
    # « Baseline » (OTIF, RDV tenus) en gris : un point de départ à mesurer, pas une cible chiffrée sous OBJECTIF.
    sub = lambda t: f'<span style="font-family:{B};font-size:24px;font-weight:400;color:{GRISD}">{t}</span>'
    groups = [('Mensuel', [('Adhérents actifs ' + sub('(≥ 1 envoi en 90 j)'), '&gt; 60 %', 'campagne réveil'),
                           ('Activation à J+30', '≥ 70 %', 'revoir l’onboarding'),
                           ('RDV → proposition', '≥ 70 %', 'retravailler la découverte'),
                           ('Taux de gain', '40–60 %', 'closing, objections'),
                           ('Cycle de vente médian', '7 à 21 j ' + sub('(dossier standard)'), 'lever les blocages'),
                           ('OTIF', sub('Baseline'), 'aligner le discours délais')]),
              ('Hebdomadaire', [('RDV tenus', sub('Baseline 90 j'), 'revoir l’accroche, relancer'),
                                ('Hygiène du forecast', '≥ 95 %', 'sortie du forecast')]),
              ('Par dossier', [('Marge contributive', '&gt; plancher ' + sub('(non affiché)'), 'disqualifier ou renégocier le périmètre')])]
    th = lambda t, w: (f'<p style="{"width:" + str(w) + "px;flex:none;" if w else "flex:1;"}padding-right:16px;font-family:{L};font-size:24px;'
                       f'font-weight:600;color:{PETROLE};white-space:nowrap">{t}</p>')
    head = (f'<div style="display:flex;align-items:center;padding-bottom:6px">{th("Fréquence", _B6_W[0])}{th("KPI", _B6_W[1])}'
            f'<div style="width:{_B6_W[2]}px;flex:none;padding-right:16px;display:flex;align-items:center;gap:12px">{th("Cible", None).replace("flex:1;", "").replace("padding-right:16px;", "")}{pill("OBJECTIF", "align-self:center")}</div>'
            f'{th("Si écart", None)}</div>')
    table = f'<div style="display:flex;flex-direction:column">{head}{"".join(_b6_group(f, r) for f, r in groups)}</div>'
    sat = (f'<div style="background:#E8F3F5;border-radius:14px;padding:10px 26px;display:flex;align-items:center;gap:22px">'
           f'{pill("CONSTATÉ", "align-self:center")}'
           f'<p style="font-family:{L};font-size:26px;font-weight:600;color:{TXT[SARC]};white-space:nowrap">Satisfaction 2024</p>'
           f'{num("4,65/5", 40, SARCF)}'
           f'<p style="font-size:26px;line-height:1.25;color:{ENCRE}">23 réponses · recommandation 4,87/5, pas un NPS</p></div>')
    # marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{bhead(6, 'Indicateurs', 'Chaque KPI : sa fréquence, sa cible, son action')}
{table}
<div style="flex:1"></div>
{sat}
<div style="height:72px;flex:none"></div>
{bfoot(6)}'''
    return 'b6', inner, dict(gap=24, pad='128px 128px 64px')


def _b7_line(txt, val, tag=''):
    # une ligne du ticket : le poste, sa pastille de statut éventuelle, le montant
    return (f'<div style="display:flex;align-items:center;gap:16px;padding:12px 0px;border-bottom:1px solid {FILET}">'
            f'<p style="font-size:30px;line-height:1.25;color:{ENCRE}">{txt}</p>{tag}<div style="flex:1"></div>'
            f'{num(val, 36, PETROLE, extra="white-space:nowrap")}</div>')


def b7():
    # Message (titre) : le prix rendu, sans maquillage : le client final paie.
    # Point focal : le ticket de l'exemple du playbook (chap. 04), qui s'additionne jusqu'au total ≈ 270 € en grand.
    # Le ≈ 17,50 € par bouteille passe sous le total (une ligne, chiffre en num() 32 px), au lieu d'un second grand chiffre concurrent.
    # À droite, d'un bloc : les règles (droits US, remise, périmètre), puis les réserves (taxes estimées, ~21 jours, le simulateur fait foi).
    # Hors écran (note, indication non dite) : « volatils depuis 2025 » pour les droits US.
    lines = ''.join([
        _b7_line('Transport, groupage DDP', '210 €', pill('GRILLE 2026', 'align-self:center')),
        _b7_line('Taxes estimées', '~30 €'),
        _b7_line('Frais de dossier DDP', '17 €'),
        _b7_line('Assurance en option : 3 % × (300 € + 210 €)', '≈ 15 €')])
    total = (f'<div style="background:{NUIT};border-radius:14px;padding:14px 26px;display:flex;align-items:center;gap:24px">'
             f'<p style="flex:1;font-size:28px;font-weight:600;line-height:1.25;color:{CLAIR}">Total avec l’option assurance, réglé d’avance</p>'
             f'{num("≈ 270 €", 64, CHAMP, extra="white-space:nowrap")}</div>')
    ticket = f'''<div style="width:1040px;flex:none;background:#FFFFFF;border:1px solid {FILET};border-radius:18px;padding:22px 32px 24px 32px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:16px">{label('Exemple du playbook · chap. 04', SARCF, ls=2)}<div style="flex:1"></div>{pill('ILLUSTRATIF', 'align-self:center')}</div>
<p style="font-family:{L};font-size:32px;font-weight:600;line-height:1.25;color:{ENCRE}">12 bouteilles, 300 € de vin</p>
<div style="display:flex;flex-direction:column">{lines}</div>
{total}
<div style="display:flex;align-items:baseline;gap:12px">{num('≈ 17,50 €', 32, PETROLE, extra='white-space:nowrap')}<p style="font-size:26px;line-height:1.3;color:{ENCRE}">de transport par bouteille <span style="color:{GRIS}">(210 € / 12)</span></p></div>
</div>'''
    rule = lambda t: f'<p style="font-size:28px;line-height:1.3;color:{ENCRE};padding:12px 0px;border-bottom:1px solid {FILET}">{t}</p>'
    rules = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {BORD};border-radius:16px;padding:20px 28px 12px 28px;display:flex;flex-direction:column">
{label('Les règles', BORD, ls=2)}
{rule('<b>Droits US</b> : taux du jour au simulateur')}
{rule('<b>Pas de remise</b> sans contrepartie ni validation de la direction')}
<p style="font-size:28px;line-height:1.3;color:{ENCRE};padding:12px 0px">On négocie <b>le périmètre avant le prix</b></p>
</div>'''
    note = (f'<div style="border-left:6px solid {BLEU};padding:4px 0px 4px 22px;display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-size:26px;line-height:1.3;color:{GRIS}">Taxes estimées, révisables (CGS art.\u00a05)</p>'
            f'<p style="font-size:26px;line-height:1.3;color:{GRIS}">~21 jours estimés, hors douane</p>'
            f'<p style="font-size:26px;font-weight:700;line-height:1.3;color:{PETROLE}">Le simulateur fait foi</p></div>')
    right = f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{rules}{note}</div>'
    # marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{bhead(7, 'Prix rendu', 'Le prix rendu, sans maquillage : le client final paie')}
<div style="flex:1;display:flex;align-items:flex-start;gap:48px">{ticket}{right}</div>
<div style="height:72px;flex:none"></div>
{bfoot(7)}'''
    return 'b7', inner, dict(gap=24, pad='128px 128px 64px')


def _b8_quad(title, c, bg, items, top='', tag=''):
    # une case du SWOT : son titre, puis une idée par ligne
    # chaque idée porte sa puce, texte en retrait : une ligne qui passe à la ligne ne se lit plus comme une nouvelle idée
    li = ''.join(f'<div style="display:flex;gap:10px"><div style="padding-top:12px;flex:none"><div style="width:8px;height:8px;border-radius:50%;background:{c}"></div></div>'
                 f'<p style="font-size:26px;line-height:1.25;color:{ENCRE}">{i}</p></div>' for i in items)
    return (f'<div style="flex:1;background:{bg};border-top:6px solid {c};border-radius:14px;padding:14px 22px 12px 22px;display:flex;flex-direction:column;gap:10px">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;gap:12px">{label(title, c, size=26, ls=2)}{tag}</div>{top}{li}</div>')


def _b8_cell(when, what, c, f=1):
    # un horizon de la stratégie, dans le bandeau sombre
    return (f'<div style="flex:{f};display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-family:{L};font-size:28px;font-weight:700;line-height:1.2;color:{c};white-space:nowrap">{when}</p>'
            f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{what}</p></div>')


def b8():
    # Message (titre) : miser sur le trio (statut, filiale, plateforme), diversifier sans sacrifier les USA.
    # Titre raccourci (« Capitaliser » → « Miser ») pour tenir sur une ligne, même à +10 %.
    # Point focal : le SWOT en quatre colonnes, le trio mis en évidence dans les forces (CONSTATÉ : le seul chiffre, 9 fois sur 10) ;
    # en bas, le bandeau des trois horizons (0–12 mois → 1–3 ans → 3 ans et plus), les trois durées en CHAMP (aucune hiérarchie).
    # Hors écran (note, indication non dite) : « lancer Spiritueux USA », « assainir le CRM », « événementiel, importateurs » ;
    # les mots « court, moyen, long terme » sont dits dans la note.
    # trois noms en gras, un par force ; « obligation de résultat » en sous-ligne grise, sous « Commissionnaire »
    trio = (f'<div style="border-left:6px solid {ORF};padding:0px 0px 0px 16px;display:flex;flex-direction:column;gap:8px">'
            f'{label("Le trio", ORF, size=24, ls=2)}'
            + ''.join(f'<p style="font-size:26px;font-weight:700;line-height:1.25;color:{ENCRE}">{t}</p>'
                      for t in ['Commissionnaire<br><span style="font-size:24px;font-weight:400;color:' + GRISD + '">obligation de résultat</span>',
                                'Filiale US licenciée', 'Planet’Connect'])
            + '</div>')
    swot = f'''<div style="display:flex;gap:16px">
{_b8_quad('Forces', SARCF, '#E8F3F5', ['Spécialiste vins, champagnes, spiritueux', 'Assurance en option, choisie 9 fois sur 10'], top=trio, tag=pill('CONSTATÉ', 'align-self:center'))}
{_b8_quad('Faiblesses', BORD, '#F6EAEE', ['Notoriété limitée', 'Capacité commerciale de PME', 'Dépendance aux partenaires', 'Forte concentration sur quelques grands comptes'])}
{_b8_quad('Opportunités', '#3A8A5C', '#EAF4EE', ['Vente directe et œnotourisme', 'Nouvelles destinations', 'Demande RSE', 'Vignerons indépendants à équiper'])}
{_b8_quad('Menaces', ORANGE, '#FBEFE8', ['Droits US, volatilité réglementaire', 'Recul de la consommation', 'Pression tarifaire', 'Coûts logistiques et énergie'])}
</div>'''
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(44, 26, CHAMP, 3)}</div>'
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 30px 16px 30px;display:flex;align-items:stretch;gap:16px">'
            f'{_b8_cell("0–12 mois", "Consolider le groupage USA, activer les signés", CHAMP)}{ar}'
            f'{_b8_cell("1–3 ans", "Diversifier : UK, Canada, Japon, Scandinavie", CHAMP)}{ar}'
            f'{_b8_cell("3 ans et plus", "Devenir la référence du transport international du vin (projets en développement)", CHAMP, 1.6)}</div>')
    # marge basse : 64 px de padding + 76 px d'entretoise + 20 px d'écart = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{bhead(8, 'Stratégie', 'Miser sur le trio, diversifier sans sacrifier les USA')}
{swot}
<div style="flex:1"></div>
{band}
<div style="height:76px;flex:none"></div>
{bfoot(8)}'''
    return 'b8', inner, dict(gap=20, pad='128px 128px 64px')


def _b9_who(name, role):
    # une personne : prénom en gras, son rôle après les deux-points
    return f'<p style="font-size:26px;line-height:1.3;color:{ENCRE}"><b><span style="color:{PETROLE}">{name}</span></b> : {role}</p>'


def _b9_what(text):
    # les missions du pôle, en gris, sous les personnes
    return f'<p style="font-size:24px;line-height:1.3;color:{GRISD}">{text}</p>'


def _b9_card(pole, c, bg, groups):
    # un pôle : filet haut de sa couleur, son nom, puis ses groupes (une personne et ses missions, ou une équipe)
    body = ''.join(f'<div style="display:flex;flex-direction:column">{g}</div>' for g in groups)
    return (f'<div style="flex:1;background:{bg};border-top:6px solid {c};border-radius:14px;padding:14px 22px 16px 22px;'
            f'display:flex;flex-direction:column;gap:8px">{label(pole, c, ls=2)}{body}</div>')


def b9():
    # Message (titre) : treize personnes, quatre pôles et une filiale.
    # Point focal : l'organigramme 2026, recomposé en natif avec le texte de l'image d'origine (aucun mot ajouté) :
    # le bandeau Direction (fond NUIT, avec les deux sociétés), puis les quatre pôles reliés, couleur du pôle en filet haut ;
    # en bas, la phrase en italique, sur une ligne (« règles de délégation au chap. 03 »).
    # Retiré : le titre interne de l'image (doublon du titre de la diapo). Le texte passe désormais par fr() :
    # apostrophes courbes, espaces insécables ; « - » devient « : » ; « cut-off » insécable ; une personne par ligne.
    # Marge basse : 64 px de padding + 76 px d'entretoise + 20 px d'écart = les 160 px habituels (bas du corps à 920 px).
    nb, nbh = '\u00a0', '\u2011'
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:12px 28px 14px 28px;display:flex;flex-direction:column;gap:2px">'
            f'<div style="display:flex;align-items:center;gap:20px">{label("Direction", CHAMP, ls=2)}<div style="flex:1"></div>'
            f'<p style="font-size:24px;line-height:1.3;color:{BRUME}">SARL Planet Aura, Castres · filiale Planet Aura Inc., New York</p></div>'
            f'<p style="font-size:28px;line-height:1.3;color:{CLAIR}"><b>Floriane Février</b> : Fondatrice &amp; Gérante · '
            f'<b>Brice de Monplanet</b> : Associé fondateur</p>'
            f'<p style="font-size:24px;line-height:1.3;color:{BRUME}">Arbitrages tarifaires · comptes stratégiques · risque &amp; contrats · décision finale</p></div>')
    # liaisons : un tronc sous la direction, une barre d'un centre de carte à l'autre, une descente par pôle
    line = lambda w, h: f'<div style="width:{w}px;height:{h}px;background:{BLEU};flex:none"></div>'
    conn = (f'<div style="display:flex;justify-content:center">{line(3, 10)}</div>'
            f'<div style="display:flex"><div style="width:199px;flex:none"></div><div style="flex:1;height:3px;background:{BLEU}"></div>'
            f'<div style="width:199px;flex:none"></div></div>'
            f'<div style="display:flex;gap:20px">'
            + ''.join(f'<div style="flex:1;display:flex;justify-content:center">{line(3, 10)}</div>' for _ in range(4))
            + '</div>')
    poles = [
        ('Commerce &amp; développement', SARCF, '#E8F3F5',
         [_b9_who('Adam', 'Commercial') + _b9_what('Pipeline, prospection, supports de vente'),
          _b9_who('Emma', f'Chargée de projets{nb}&amp; développement') + _b9_what('Partenariats, projets, développement logiciel')]),
        ('Planet Aura Inc. (New York)', ORANGE, '#FBEFE8',
         [_b9_who('Alessandro', f'Business{nb}Developer') + _b9_what('Relais marché USA'),
          _b9_what(f'Licences TTB importateur{nb}&amp;{nb}grossiste · 95 Inip Dr, Inwood{nb}(NY)')]),
        ('Logistique / exploitation', BORD, '#F6EAEE',
         [_b9_who('Vincent', 'Chef d’entrepôt') + _b9_who('Frantz', 'Cariste') + _b9_what('Juliana · Sarah · Robin · Sofian · Swan'),
          _b9_what(f'Enlèvements, suivi, cut{nbh}off, litiges, cotations hors grille')]),
        ('Administration', ORF, '#F8F3E9',
         [_b9_who('Teddy', 'Comptabilité &amp; RH') + _b9_what('Facturation, mandats SEPA, impayés, RH')])]
    cards = f'<div style="display:flex;gap:20px;align-items:stretch">{"".join(_b9_card(*pl) for pl in poles)}</div>'
    org = f'<div style="display:flex;flex-direction:column">{band}{conn}{cards}</div>'
    note = (f'<p style="font-size:24px;font-style:italic;line-height:1.3;color:{GRISD}">Équipe resserrée : chaque commercial parle directement '
            f'à la direction, à l’exploitation et à l’administration ; règles de délégation au chap.{nb}03</p>')
    inner = f'''{bhead(9, 'Organisation', 'Treize personnes, quatre pôles et une filiale')}
{org}
<div style="flex:1"></div>
{note}
<div style="height:76px;flex:none"></div>
{bfoot(9)}'''
    return 'b9', inner, dict(gap=20, pad='128px 128px 64px')


def _b10_rule(val, txt):
    # une règle du groupage : le chiffre en appui, sa phrase à côté
    return (f'<div style="display:flex;align-items:baseline;gap:14px">'
            f'<div style="width:124px;flex:none">{num(val, 32, SARCF, extra="white-space:nowrap")}</div>'
            f'<p style="flex:1;font-size:24px;line-height:1.3;color:{ENCRE}">{txt}</p></div>')


def b10():
    # Diapo-image : la carte officielle 2026 reste le point focal, titre inchangé.
    # Robustesse et lecture : l'encadré « Groupage DDP » passe d'une phrase à points médians à trois règles
    # alignées (chiffre, puis phrase), avec leur statut, calé en bas, au ras de la carte (l'image s'étire sur la hauteur de la rangée) ; la ligne « Vermont » devient
    # la dernière entrée de la légende (l'anneau orange qui cercle le VT sur la carte), en deux lignes équilibrées
    # (plus de mot seul en fin de bloc). L'étiquette « Légende » est retirée (les pastilles de couleur se lisent seules),
    # ce qui rend la hauteur nécessaire à la colonne de droite au rendu +10 %. Seul mot ajouté : le tampon de statut.
    # Marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px).
    leg = [('#A6CEE3', 'Ouvert'), ('#B1DE89', 'Groupage et direct'), ('#C9B1D4', 'Groupage (certains codes postaux) et direct'),
           ('#EBEB30', 'Envoi direct uniquement'), ('#FED9A6', 'Certains codes postaux'), ('#999999', 'Fermé')]
    lg = ''.join(f'<div style="display:flex;align-items:center;gap:12px"><div style="width:30px;height:22px;border-radius:4px;background:{c};flex:none"></div>'
                 f'<p style="font-size:24px;line-height:1.25;color:{ENCRE}">{t}</p></div>' for c, t in leg)
    # le Vermont, cerclé d'orange sur la carte, devient la dernière ligne de la légende (même anneau orange)
    lg += (f'<div style="display:flex;align-items:flex-start;gap:12px;padding-top:6px"><div style="width:30px;height:22px;border-radius:50%;border:3px solid {ORANGE};flex:none"></div>'
           f'<p style="font-size:24px;line-height:1.25;color:{GRISD}">Vermont : livré par un prestataire interne<br>après regroupement</p></div>')
    rules = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {SARCF};border-radius:16px;padding:16px 24px 18px 24px;display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:center;gap:14px">{label('Groupage DDP', SARCF, ls=2)}<div style="flex:1"></div>{pill('RÈGLE', 'align-self:center')}</div>
{_b10_rule('36', 'bouteilles max.<br>par personne et par envoi')}
{_b10_rule('2 100 $', 'de valeur déclarée : POA au-delà')}
{_b10_rule('~21 j', 'estimés')}
</div>'''
    inner = f'''{bhead(10, 'États-Unis', 'Où livre-t-on aux États-Unis ? La carte 2026')}
<div style="flex:1;display:flex;gap:40px;align-items:flex-start">
<img src="{USMAP2}" alt="Carte 2026 des États américains desservis par Planet Aura, en groupage ou en direct" style="width:1000px;align-self:stretch;object-fit:contain;background:#FFFFFF;border-radius:16px">
<div style="flex:1;align-self:stretch;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;flex-direction:column;gap:6px">{lg}</div>
<div style="flex:1"></div>
{rules}
</div></div>
<div style="height:72px;flex:none"></div>
{bfoot(10)}'''
    return 'b10', inner, dict(gap=24, pad='128px 128px 64px')


def _b11_yn(yn, txt, c):
    # une issue de la question « le domaine a-t-il encore les bouteilles ? »
    return (f'<div style="display:flex;align-items:flex-start;gap:14px">'
            f'<p style="width:76px;flex:none;font-family:{L};font-size:24px;font-weight:700;text-align:center;color:#FFFFFF;background:{c};border-radius:999px;padding:2px 0px">{yn}</p>'
            f'<p style="flex:1;font-size:26px;line-height:1.3;color:{ENCRE}">{txt}</p></div>')


def _b11_branch(name, c, body, leaf_lbl, leaf_txt, leaf_bg, leaf_c, leaf_fg, flex):
    # une branche de l'arbre : son nom, son déroulé, puis ce qui est facturé ou remboursé (la feuille)
    return (f'<div style="flex:{flex};background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {c};border-radius:16px;padding:18px 24px 22px 24px;display:flex;flex-direction:column;gap:14px">'
            f'<p style="font-family:{L};font-size:30px;font-weight:700;letter-spacing:1px;line-height:1.3;color:{TXT.get(c, c)}">{name}</p>'
            f'{body}<div style="flex:1"></div>'
            f'<div style="background:{leaf_bg};border-radius:14px;padding:14px 20px 16px 20px;display:flex;flex-direction:column;gap:4px">'
            f'{label(leaf_lbl, leaf_c, ls=2)}<p style="font-size:30px;font-weight:700;line-height:1.25;color:{leaf_fg}">{leaf_txt}</p></div></div>')


def _b11_stat(v, t, extra=''):
    # un chiffre de l'assurance, sa phrase à côté (et son statut sous la phrase)
    return (f'<div style="display:flex;align-items:center;gap:16px">'
            f'<div style="width:196px;flex:none">{num(v, 52, SARCF, extra="white-space:nowrap")}</div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:8px"><p style="font-size:26px;line-height:1.3;color:{ENCRE}">{t}</p>{extra}</div></div>')


def b11():
    # Message (titre) : si ça casse, l'incident devient une seconde vente (titre raccourci de 3 caractères :
    # « Et si ça casse ? » passait sur deux lignes au rendu +10 %).
    # Point focal : l'arbre de la procédure sinistre 2026. Signalement sous 48 h → le client choisit →
    # deux branches qui finissent chacune sur leur règle de facture : en réexpédition, « le domaine facture les seules
    # bouteilles » = la seconde vente (feuille sombre) ; en remboursement, bouteilles, transport et taxes.
    # La règle des factures (ancienne carte de droite) est donc fondue dans les feuilles de l'arbre ;
    # « Procédure sinistre 2026 » passe dans le sur-titre.
    # À droite, en appui : l'assurance, une option (3 %, 20 000 €, 89,8 % CONSTATÉ), puis les exclusions.
    # La portée reste visible : le bandeau commence par « Envoi assuré » et la carte des exclusions rappelle
    # « Sans option : conditions de base » (le détail « pas le régime ad valorem » est dit dans la note) ;
    # passé à la note : « client et domaine informés à chaque étape ».
    # Marge basse : 64 px de padding + 72 px d'entretoise + 24 px d'écart = les 160 px habituels (bas du corps à 920 px).
    rxp_body = (f'<p style="font-size:26px;font-weight:600;line-height:1.3;color:{ENCRE}">Le domaine a-t-il encore les bouteilles ?</p>'
                f'<div style="display:flex;flex-direction:column;gap:10px">'
                f'{_b11_yn("Oui", "Enlèvement planifié, RXP suivie jusqu’à la livraison", SARCF)}'
                f'{_b11_yn("Non", "Remplacement équivalent proposé ; refusé : remboursement", ORF)}</div>')
    rem_body = f'<p style="font-size:26px;line-height:1.3;color:{ENCRE}">Dossier vérifié<br>(valeur déclarée, preuves),<br>puis instruction avec l’assureur</p>'
    branches = (f'<div style="display:flex;gap:24px;align-items:stretch">'
                f'{_b11_branch("RÉEXPÉDITION (RXP)", SARCF, rxp_body, "La seconde vente", "Le domaine facture<br>les seules bouteilles", NUIT, CHAMP, "#FFFFFF", 1.3)}'
                f'{_b11_branch("REMBOURSEMENT", ORANGE, rem_body, "Le domaine facture", "Bouteilles, transport<br>et taxes", "#FBEFE8", ORANGE, ENCRE, 1)}'
                f'</div>')
    arrows = (f'<div style="display:flex;gap:24px">'
              f'<div style="flex:1.3;display:flex;justify-content:center">{arrow_down(32, 34, BLEU, 4)}</div>'
              f'<div style="flex:1;display:flex;justify-content:center">{arrow_down(32, 34, BLEU, 4)}</div></div>')
    tree = f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px">
<div style="background:{NUIT};border-radius:16px;padding:16px 28px;display:flex;justify-content:center">
<p style="font-size:28px;line-height:1.3;color:{CLAIR};text-align:center"><b>Envoi assuré</b> · signalement sous 48 h, avec photos : <b><span style="color:{CHAMP}">le client choisit</span></b></p></div>
{arrows}
{branches}
</div>'''
    insur = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {SARCF};border-radius:16px;padding:20px 26px 22px 26px;display:flex;flex-direction:column;gap:14px">
{label('L’assurance, une option', SARCF, ls=2)}
{_b11_stat('3 %', 'de la valeur<br>(vin + transport)')}
<p style="font-size:26px;line-height:1.3;color:{ENCRE}">Jusqu’à <b>20 000 € par envoi</b>,<br>avec emballage homologué</p>
{_b11_stat('89,8 %', 'des envois<br>l’ont choisie', pill('CONSTATÉ'))}
</div>'''
    excl = f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {ORANGE};border-radius:16px;padding:20px 26px 22px 26px;display:flex;flex-direction:column;gap:8px">
{label('Les exclusions', ORANGE, ls=2)}
<p style="font-size:26px;line-height:1.3;color:{ENCRE}">Altération thermique, oxydation,<br>bouchons, étiquettes</p>
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Sans option : conditions de base</p>
</div>'''
    inner = f'''{bhead(11, 'Procédure sinistre 2026', 'Si ça casse, l’incident devient une seconde vente')}
<div style="flex:1;display:flex;gap:44px">{tree}
<div style="width:520px;flex:none;display:flex;flex-direction:column;gap:20px">{insur}{excl}</div></div>
<div style="height:72px;flex:none"></div>
{bfoot(11)}'''
    return 'b11', inner, dict(gap=24, pad='128px 128px 64px')


def _b12_touch(day, name, sub, c, first=False, last=False):
    # une touche de la cadence : le jour dans une pastille sur le fil, le canal, puis ce qu'on y fait
    seg = lambda on: f'<div style="flex:1;height:6px;background:{FILET if on else "transparent"}"></div>'
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:8px">'
            f'<div style="display:flex;align-items:center">{seg(not first)}'
            f'<div style="width:64px;height:64px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none">'
            f'<p style="font-family:{L};font-size:26px;font-weight:700;color:#FFFFFF;white-space:nowrap">{day}</p></div>'
            f'{seg(not last)}</div>'
            f'<p style="font-size:26px;font-weight:700;line-height:1.2;text-align:center;color:{ENCRE}">{name}</p>'
            f'<p style="font-size:24px;line-height:1.3;text-align:center;color:{GRIS}">{sub}</p></div>')


def _b12_card(lbl, c, rows, tag=''):
    # carte d'appui : une idée par ligne
    li = ''.join(f'<p style="font-size:26px;line-height:1.3;color:{ENCRE}">{r}</p>' for r in rows)
    return (f'<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-left:6px solid {c};border-radius:16px;padding:14px 26px 16px 26px;display:flex;flex-direction:column;gap:6px">'
            f'<div style="display:flex;align-items:center;gap:14px">{label(lbl, c, ls=2)}<div style="flex:1"></div>{tag}</div>{li}</div>')


def b12():
    # Message (titre) : 8 touches en 18 jours, et la réponse arrête tout (chiffres en clair : titre sur une ligne,
    # même à +10 % ; l'ancien titre en toutes lettres passait sur deux lignes).
    # Point focal : la frise J1 → J18, reconstruite en flux (huit colonnes égales, plus aucun texte épinglé) ;
    # une accolade sous J2 → J14 dit « 6 contacts actifs » (rappel de la note, désormais visible).
    # En appui : « Pour qui » et les trois seuils du vendredi ; en bas, le bandeau sombre de la règle d'or
    # (toute réponse arrête tout), avec le câblage Brevo + HubSpot étiqueté À DÉPLOYER.
    # Retiré : « (P1 et P2) » (déjà contenu dans « dès PA-FIT 55 » ; seuils détaillés en secours B2).
    # Coupures posées à la main (« problème » / « + valeur », bandeau en deux lignes) : deux colonnes voisines
    # ne se touchent plus et aucun mot ne reste seul en fin de bloc, même à +10 %.
    # Marge basse : 64 px de padding + 76 px d'entretoise + 20 px d'écart = les 160 px habituels (bas du corps à 920 px).
    nb = ' '
    T = [('J1', 'Recherche', 'vue LinkedIn', GRISD), ('J2', 'E-mail 1', 'problème<br>+ valeur', SARC),
         ('J4', 'Appel 1', '2 questions,<br>45 s', ORANGE), ('J6', 'LinkedIn', 'invitation', PETROLE),
         ('J8', 'E-mail 2', 'preuve<br>de méthode', SARC), ('J11', 'Appel 2', f'+{nb}message vocal', ORANGE),
         ('J14', 'E-mail 3', f'décision<br>1{nb}/{nb}2{nb}/{nb}3', SARC), ('J18', 'Sortie', 'nurture 45 j', BORD)]
    frise = ''.join(_b12_touch(d, a, b, c, i == 0, i == len(T) - 1) for i, (d, a, b, c) in enumerate(T))
    piece = lambda side: (f'<div style="flex:1;height:18px;border-bottom:3px solid {BLEU};border-{side}:3px solid {BLEU};'
                          f'border-radius:{"0px 0px 0px 10px" if side == "left" else "0px 0px 10px 0px"}"></div>')
    brace = (f'<div style="display:grid;grid-template-columns:repeat(8, 1fr);gap:0px">'
             f'<div></div>'
             f'<div style="grid-column:span 6;display:flex;align-items:center;gap:16px;padding:0px 40px">'
             f'{piece("left")}<p style="font-family:{L};font-size:26px;font-weight:600;line-height:1.2;color:{PETROLE};white-space:nowrap">6 contacts actifs</p>{piece("right")}</div>'
             f'<div></div></div>')
    who = _b12_card('Pour qui', SARCF, ['<b>~20 comptes P1</b>, en ABM 1:1', 'Cadence ouverte dès PA-FIT 55',
                                        'Caveaux : cadence courte, J1, J+4, J+10, visite'])
    fri = _b12_card('Mesurer chaque vendredi', BORD, ['Réponse &lt; 10 % : revoir l’angle', '&lt; 5 RDV pour 100 : resserrer',
                                              'Opt-out &gt; 2 % : stopper'], pill('RÈGLE', 'align-self:center'))
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:16px 28px 18px 32px;display:flex;align-items:center;gap:24px">'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP}">RÈGLE D’OR</p>'
            f'<p style="font-size:28px;line-height:1.3;color:{CLAIR}">Réponse, RDV, opposition ou erreur :<br><b>cadence stoppée, tâche humaine créée</b></p></div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:6px;padding-left:20px">'
            f'{ctag("À DÉPLOYER")}'
            f'<p style="font-size:24px;line-height:1.3;color:{BRUME}">Câblage Brevo + HubSpot,<br>novembre 2026</p></div></div>')
    inner = f'''{bhead(12, 'Cadence', '8 touches en 18 jours, et la réponse arrête tout')}
<div style="display:flex;flex-direction:column;gap:12px"><div style="display:flex">{frise}</div>{brace}</div>
<div style="display:flex;gap:24px">{who}{fri}</div>
{band}
<div style="height:76px;flex:none"></div>
{bfoot(12)}'''
    return 'b12', inner, dict(gap=20, pad='128px 128px 64px')


def _b13_cell(inner, extra=''):
    return f'<div style="display:flex;flex-direction:column;{extra}">{inner}</div>'


def b13():
    # Message (titre) : la règle qui tient la feuille de route ; pas de critère atteint, pas d'étape suivante.
    # Point focal : la frise des six chantiers, dans l'ordre (les cartes de la diapo 16, prolongées à six) :
    # échéance, chantier, budget en grand, responsable et temps ; le critère de passage aligné en dessous.
    # En bas : le bandeau du plafond (3 000 € de dépenses externes, OBJECTIF).
    # Hors écran (note) : la ligne « hors budget, après validations » (vidéo démo, études de cas avec accord écrit
    # des adhérents cités, pilote VELA en projet) ; « le temps interne est une capacité à réserver » ;
    # la somme détaillée (0 + 600 + … : lisible dans la ligne des budgets).
    ch = [('Sept. 2026', 'Nettoyage CRM, listes A/B/C', '0 €', 'Emma + Adam · 24 h', '≥ 95 % des comptes prioritaires exploitables'),
          ('Oct.', 'One-pager par ICP, landing page', '600 €', 'Emma + Adam · 36 h', 'Supports validés par la direction'),
          ('Nov.', '3 séquences Brevo, reporting HubSpot', '200 €', 'Emma · 20 h', 'Arrêt automatique sur réponse testé'),
          ('Nov. → mai', 'Tests LinkedIn, 3 clusters', '900 €', 'Adam · 3 h/sem.', 'Coût par SQL comparé à l’outbound'),
          ('Janv. 2027', 'Webinaire export', '300 €', 'Emma + expert · 20 h', '10 inscrits ICP, 3 diagnostics'),
          ('Janv. → juil.', 'Deux salons en visiteur', '1 000 €', 'Adam + Emma · 24 h', '8 RDV qualifiés par événement')]
    dates = ''.join(_b13_cell(label(d, PETROLE, size=24, ls=2), f'border-top:6px solid {PETROLE};padding-top:8px') for d, *_ in ch)
    names = ''.join(_b13_cell(f'<p style="font-size:26px;font-weight:700;line-height:1.2;color:{ENCRE}">{n}</p>') for _, n, *_ in ch)
    buds = ''.join(_b13_cell(num(b, 48, ORF)) for _, _, b, *_ in ch)
    who = ''.join(_b13_cell(f'<p style="font-size:24px;line-height:1.25;color:{GRIS}">{w}</p>') for *_, w, _ in ch)
    gate = (f'<div style="grid-column:span 6;display:flex;align-items:center;gap:14px">'
            f'{label("Critère", SARCF, size=24, ls=2)}<div style="flex:1;height:2px;background:{FILET}"></div></div>')
    crit = ''.join(_b13_cell(f'<p style="font-size:24px;line-height:1.25;color:{ENCRE}">{c}</p>',
                             f'border-left:5px solid {SARCF};padding:2px 0px 2px 14px')
                   for *_, c in ch)
    grid = (f'<div style="display:grid;grid-template-columns:repeat(6, 1fr);gap:6px 12px;padding-top:8px">'
            f'{dates}{names}{buds}{who}</div>')
    gates = (f'<div style="display:grid;grid-template-columns:repeat(6, 1fr);gap:8px 12px">'
             f'{gate}{crit}</div>')
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:10px 28px;display:flex;align-items:center;gap:22px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">PLAFOND</p>'
            f'{num("3 000 €", 48, "#FFFFFF")}'
            f'<p style="flex:1;font-size:28px;line-height:1.3;color:{CLAIR}">de dépenses externes</p>'
            f'{pill("OBJECTIF", "align-self:center;background:transparent;color:#FFFFFF;border-color:#FFFFFF")}</div>')
    sp = '<div style="flex:1"></div>'
    # marge basse : padding 64 + cale fixe de 80 px + écart 16 = les 160 px habituels (bas du corps à 920 px),
    # même dispositif que les autres candidates (le texte du pied de page épinglé reste hors du flux au rendu +10 %).
    inner = f'''{bhead(13, 'Feuille de route', 'Pas de critère atteint, pas d’étape suivante')}
{grid}
<div style="height:28px;flex:none"></div>
{gates}
{sp}
{band}
<div style="height:80px;flex:none"></div>
{bfoot(13)}'''
    return 'b13', inner, dict(gap=16, pad='128px 128px 64px')


def _b14_row(code, quote, proof, detail, c, st=''):
    # une objection : ce que dit le prospect → la seule preuve ; statut du chiffre dans la colonne de droite
    tc = TXT.get(c, c)
    det = f'<p style="font-size:24px;line-height:1.3;color:{GRIS}">{detail}</p>' if detail else ''
    return (f'<div style="flex:1;display:flex;align-items:center;gap:24px;background:#FFFFFF;border:1px solid {FILET};'
            f'border-left:8px solid {c};border-radius:14px;padding:8px 24px">'
            f'<div style="width:390px;flex:none;display:flex;flex-direction:column;gap:2px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;line-height:1.25;color:{tc}">{code}</p>'
            f'<p style="font-family:{T};font-style:italic;font-size:30px;line-height:1.2;color:{ENCRE}">{quote}</p></div>'
            f'<div style="width:40px;flex:none;display:flex;align-items:center">{arrow(40, 26, c, 3)}</div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:4px">'
            f'<p style="font-size:28px;font-weight:700;line-height:1.25;color:{ENCRE}">{proof}</p>{det}</div>'
            f'<div style="width:200px;flex:none;display:flex;justify-content:flex-end">{st}</div></div>')


def b14():
    # Message (titre) : le top 5, une objection → une seule preuve.
    # Point focal : les cinq lignes, citation du prospect (italique) → preuve unique (gras), statut du chiffre à droite.
    # En bas : le bandeau des quatre temps et la banque de 26 objections (annexe D).
    # Hors écran : « classement terrain, hiérarchisé sur les motifs de perte CRM en novembre » (note, dit) ;
    # « Je ne vous demande pas de changer » (note) ; signalement sous 48 h avec photos (secours B11) ;
    # codes O-1 à O-14 (annexe D) ;
    # « une fois » après « Prouver » (déjà dit par le titre : une seule preuve).
    rows = ''.join([
        _b14_row('Prix', f'« C’est cher <span style="color:{GRISD}">[…]</span> »', '15 € par bouteille, payés par le client final',
                 '360 € HT de transport pour 24 btl vers les USA', BORD, pill('GRILLE 2026')),
        _b14_row('Casse', '« Et si ça casse ? »', 'Assurance en option : 3 % (vin + transport)',
                 'jusqu’à 20 000 € par envoi · choisie sur 89,8 % des envois', SARCF, pill('CONSTATÉ')),
        _b14_row('Chaleur', '« Le vin va cuire dans le camion en été. »', 'Départ différé',
                 'l’altération thermique est exclue de l’assurance (CGS)', ORANGE),
        _b14_row('Statu quo', '« On a déjà quelqu’un »', 'Comparer sur UN envoi', '', PETROLE),
        _b14_row('Temps', f'« Je n’ai pas le temps <span style="color:{GRISD}">[…]</span> »', '3 min de saisie par envoi',
                 'saisonniers formés en 30 min', ORF, pill('OBJECTIF')),
    ])
    ar = f'<div style="display:flex;align-items:center;flex:none">{arrow(36, 24, CHAMP, 3)}</div>'
    steps = ar.join(f'<p style="font-family:{L};font-size:26px;font-weight:600;color:#FFFFFF;white-space:nowrap">{s}</p>'
                    for s in ['Accueillir', 'Clarifier', 'Prouver', 'Vérifier'])
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 28px;display:flex;align-items:center;gap:16px;flex-wrap:wrap">'
            f'{steps}<p style="flex:1;font-size:24px;line-height:1.3;color:{BRUME};text-align:right">réponse notée mot pour mot · 26 objections, annexe D</p></div>')
    # marge basse : padding 64 + cale fixe de 72 px + écart 24 = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{bhead(14, 'Objections', 'Le top 5 : une objection, une seule preuve')}
<div style="flex:1;display:flex;flex-direction:column;gap:10px">{rows}</div>
{band}
<div style="height:72px;flex:none"></div>
{bfoot(14)}'''
    return 'b14', inner, dict(gap=24, pad='128px 128px 64px')


def _b15_row(apport, why, st, sub='', first=False):
    # une ligne de mon apport : ce que j'ai livré (gras), pourquoi (italique), statut à droite
    top = '' if first else f'border-top:1px solid {FILET};'
    s2 = f'<p style="font-size:24px;line-height:1.2;color:{GRISD};white-space:nowrap">{sub}</p>' if sub else ''
    return (f'<div style="display:flex;align-items:center;gap:40px;{top}padding:5px 0px">'
            f'<p style="flex:1;font-size:26px;font-weight:700;line-height:1.25;color:{ENCRE}">{apport}</p>'
            f'<p style="flex:1;font-size:24px;font-style:italic;line-height:1.25;color:{GRIS}">{why}</p>'
            f'<div style="width:360px;flex:none;display:flex;align-items:center;justify-content:flex-end;gap:14px">{s2}{st}</div></div>')


def _b15_item(what, who, f=1):
    return (f'<div style="flex:{f};display:flex;flex-direction:column;gap:2px">'
            f'<p style="font-size:26px;font-weight:600;line-height:1.25;color:{ENCRE}">{what}</p>'
            f'<p style="font-size:24px;line-height:1.25;color:{GRISD}">{who}</p></div>')


def b15():
    # Message (titre) : mon apport, c'est la méthode qui relie l'existant (même idée que la note).
    # Point focal : mes sept apports, chacun avec son pourquoi (italique) et son statut (LIVRÉ, OBJECTIF, PROPOSÉ) ;
    # en bas, en gris, ce qui existait et n'est pas de moi (pastilles MA CONTRIBUTION / EXISTANT de la grille de lecture).
    # Hors écran : la colonne « L'existant » ligne par ligne (les six manques sont DITS dans la note : « Ce qui manquait : … ») ;
    # « au 24/09/2026 » (point zéro, diapos 5 et 19) ; « angle mort ADV », « entretiens T1 2027 » (secours B1) ;
    # « recalibré à 90 j » (secours B2) ; « SLA », « jour par jour », « hygiène ».
    LIV = pill('CONSTATÉ', 'align-self:center', label='LIVRÉ')
    rows = ''.join([
        _b15_row('Source unique, preuve en 3 statuts', 'Pas de chiffre sans source ni date', LIV, first=True),
        _b15_row('5 ICP, PA-FIT, tiers A/B/C', 'L’adéquation prime sur la taille', LIV),
        _b15_row('5 personas confrontés au réel', 'Parler au bon interlocuteur', LIV),
        _b15_row('7 étapes, vente finie au 1er envoi', 'Un signé jamais activé ne vaut rien', pill('OBJECTIF', 'align-self:center'), '≥ 70 % à J+30'),
        _b15_row('SPIN, 26 objections, ROI, négociation', 'Le prix est notre point faible', LIV),
        _b15_row('Dictionnaire CRM, RACI, rituels', 'Une donnée, un propriétaire, une décision', pill('PROPOSÉ', 'align-self:center'), 'à ratifier'),
        _b15_row('Plan 30-60-90, annexe U', 'Rendre la vente transmissible', LIV, 'non testé'),
    ])
    head = (f'<div style="display:flex;align-items:center;gap:40px">'
            f'<div style="flex:1;display:flex">{ctag("MA CONTRIBUTION")}</div>'
            f'<div style="flex:1;display:flex">{label("Pourquoi", GRISD, size=24, ls=2)}</div>'
            f'<div style="width:360px;flex:none"></div></div>')
    top = f'<div style="display:flex;flex-direction:column;gap:6px">{head}<div style="display:flex;flex-direction:column">{rows}</div></div>'
    band = (f'<div style="background:#EEF3F4;border-left:6px solid {GRISD};border-radius:16px;padding:16px 28px 18px 24px;'
            f'display:flex;align-items:center;gap:28px">'
            f'<div style="width:160px;flex:none;display:flex">{ctag("EXISTANT")}</div>'
            f'{_b15_item("CGS, grilles 2026, filiale", "direction")}'
            f'{_b15_item("Procédures 2026, ~145 signés", "équipe")}'
            f'{_b15_item("Planet’Connect", "développé avec Halt Solutions, j’y ai contribué", 1.25)}</div>')
    # marge basse : padding 64 + cale fixe de 76 px + écart 20 = les 160 px habituels (bas du corps à 920 px)
    sp = '<div style="flex:1"></div>'
    inner = f'''{bhead(15, 'Contribution', 'Mon apport : la méthode qui relie l’existant')}
{sp}
{top}
{sp}
{band}
<div style="height:76px;flex:none"></div>
{bfoot(15)}'''
    return 'b15', inner, dict(gap=20, pad='128px 128px 64px')


def _b16_row(n, step, what, kind, first=False):
    # une étape du parcours : rond numéroté (couleur du statut), étape, ce que montre le cas, statut
    if kind == 'CHAP':
        circ = f'background:{SARCF};border:3px solid {SARCF};color:#FFFFFF'
        st = f'<p style="font-size:24px;line-height:1.3;color:{GRISD};white-space:nowrap">chap. 11</p>'
    elif kind == 'RÈGLE':
        circ = f'background:{PETROLE};border:3px solid {PETROLE};color:#FFFFFF'
        st = pill('RÈGLE', 'align-self:center')
    elif kind == 'GRILLE':
        circ = f'background:{PETROLE};border:3px solid {PETROLE};color:#FFFFFF'
        st = pill('GRILLE 2026', 'align-self:center')
    else:
        circ = f'background:#FFFFFF;border:3px dotted {GRISD};color:{GRISD}'
        st = pill('ILLUSTRATIF', 'align-self:center')
    top = '' if first else f'border-top:1px solid {FILET};'
    return (f'<div style="display:flex;align-items:center;gap:24px;{top}padding:10px 0px">'
            f'<div style="width:46px;height:46px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;{circ}">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;line-height:1">{n}</p></div>'
            f'<p style="width:210px;flex:none;font-family:{L};font-size:26px;font-weight:600;line-height:1.25;color:{PETROLE}">{step}</p>'
            f'<p style="flex:1;font-size:26px;line-height:1.3;color:{ENCRE}">{what}</p>'
            f'<div style="width:230px;flex:none;display:flex;justify-content:flex-end">{st}</div></div>')


def b16():
    # Message (titre) : un parcours type, pas une vente réalisée (la phrase de sécurité).
    # Point focal : les sept étapes, chacune avec son statut ; le motif se lit d'un coup d'œil :
    # chap. 11 aux deux bouts, règles du playbook et grille 2026 au milieu, score illustratif.
    # En bas : d'où vient chaque statut (chap. 11, règles des chap. 09 à 16, grille 2026).
    # Hors écran : « chiffré à 12 btl, 210 € » (note : douze bouteilles ; 210 € en secours B7) ; « adapté au panier
    # de 24 btl du chap. 04 et de la fiche ICP 1 » (note) ; « aucun domaine nommé, aucun chiffre client » (note) ;
    # détail du score (45 nurture, 60 cadence, 85 décideur et douleur : diapo 8 et sa note) ; « objection en 4 temps » (diapo 14, secours B14).
    rows = ''.join([
        _b16_row(1, 'Lead', 'Domaine provençal avec caveau, 20+ étrangers / sem. en saison, panier ~300 €', 'CHAP', first=True),
        _b16_row(2, 'Qualifié', 'Points PA-FIT : 45 → 60 → 85', 'ILLU'),
        _b16_row(3, 'RDV', 'Questions SPIN de l’annexe E ; réponses du prospect illustratives', 'RÈGLE'),
        _b16_row(4, 'Proposition', 'Grille 2026 : 24 btl = 360 € de transport, 15 €/btl', 'GRILLE'),
        _b16_row(5, 'Adhésion', 'Signature en ligne, SEPA, 1er lot de cartons (110 € HT)', 'RÈGLE'),
        _b16_row(6, 'Activé', 'Formation caveau J+5, 1er envoi suivi, point J+30', 'RÈGLE'),
        _b16_row(7, 'Récurrent', 'Score de santé ; potentiel 60 à 100 envois/an, tiers B', 'CHAP'),
    ])
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 28px;display:flex;align-items:center;gap:22px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">SOURCES</p>'
            f'<p style="flex:1;font-size:26px;line-height:1.3;color:{CLAIR}">Chap. 11 : le fil rouge · règles : chap. 09 à 16 · prix : grille 2026</p></div>')
    sp = '<div style="flex:1"></div>'
    # marge basse : padding 64 + cale fixe de 76 px + écart 20 = les 160 px habituels (bas du corps à 920 px)
    inner = f'''{bhead(16, 'Cas fil rouge', 'Un parcours type, pas une vente réalisée')}
{sp}
<div style="display:flex;flex-direction:column">{rows}</div>
{sp}
{band}
<div style="height:76px;flex:none"></div>
{bfoot(16)}'''
    return 'b16', inner, dict(gap=20, pad='128px 128px 64px')


_B17_W = (270, 400, 280, 240)  # colonnes fixes : étape (rond + nom), responsable, délai, outil ; la preuve prend le reste


def _b17_row(i, name, who, proof, sla, tool, first=False):
    # une étape : rond numéroté, nom, responsable, preuve, délai, outil (contenu mot pour mot de l'ancienne diapo 11)
    hi = i == 6
    c = ORF if hi else SARCF
    bg = 'background:#FBF6EA;border-radius:12px;' if hi else ''
    top = '' if first or hi or i == 7 else f'border-top:1px solid {FILET};'
    cell = lambda w, t, extra='': (f'<p style="{"width:" + str(w) + "px;flex:none;" if w else "flex:1;"}padding-right:16px;'
                                   f'font-size:26px;line-height:1.25;color:{ENCRE};{extra}">{t}</p>')
    return (f'<div style="display:flex;align-items:center;{top}{bg}padding:9px 12px">'
            f'<div style="width:{_B17_W[0]}px;flex:none;display:flex;align-items:center;gap:18px">'
            f'<div style="width:46px;height:46px;border-radius:50%;flex:none;background:{c};display:flex;align-items:center;justify-content:center">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;line-height:1;color:#FFFFFF">{i}</p></div>'
            f'<p style="font-family:{L};font-size:26px;font-weight:600;line-height:1.25;color:{ORF if hi else PETROLE}">{name}</p></div>'
            f'{cell(_B17_W[1], who)}{cell(None, proof)}'
            f'{cell(_B17_W[2], sla, f"font-family:{L};font-weight:600;color:{BORD}")}'
            f'{cell(_B17_W[3], tool, f"color:{GRISD}")}</div>')


def b17():
    # Message (titre) : chaque étape a son responsable, sa preuve, son délai, son outil (titre court : une ligne, même à +10 %).
    # Point focal : le tableau des sept étapes (l'étape 6, ligne d'arrivée, ressort en doré, comme sur la diapo 11).
    # Contenu repris mot pour mot de l'ancienne diapo 11 (gen5/s_vendre.py, processus) : n°, nom, responsable, preuve, délai, outil.
    # Retirés (déjà ailleurs) : « Six portes d'entrée » et « Durée du cycle » (note de la diapo 11 ; cycle visé : secours B6),
    # bandeau Constat → Ma décision → Mesure (diapo 11). Délais = objectifs (pastille dans l'en-tête de colonne).
    st = [('Lead', 'Commercial (+ marketing)', 'ICP et signal vérifiés', 'rappel &lt; 24 h', 'HubSpot'),
          ('Qualifié', 'Commercial', 'CAVE + score PA-FIT', '&lt; 7 j', 'HubSpot'),
          ('RDV · démo', 'Commercial', 'reformulation validée', 'CR &lt; 24 h', 'Simulateur'),
          ('Proposition', 'Commercial +&nbsp;exploitation', 'faisabilité validée', '&lt; 24 h', 'Doc. 2026'),
          ('Adhésion', 'Adhérent + commercial', 'signée + cartons', '≤ 14 j', 'E-signature'),
          ('Activé', 'Commercial +&nbsp;exploitation', '1er envoi fait, débriefé', '≤ 30 j', 'Planet’Connect'),
          ('Récurrent', 'Commercial', '≥ 3 envois / trimestre', 'retour &lt; 2 j', 'Dashboards')]
    th = lambda t, w: (f'<p style="{"width:" + str(w) + "px;flex:none;" if w else "flex:1;"}padding-right:16px;font-family:{L};font-size:24px;'
                       f'font-weight:600;color:{PETROLE};white-space:nowrap">{t}</p>')
    head = (f'<div style="display:flex;align-items:center;padding:0px 12px 8px 12px;border-bottom:2px solid {BLEU}">'
            f'{th("Étape", _B17_W[0])}{th("Responsable", _B17_W[1])}{th("Preuve", None)}'
            f'<div style="width:{_B17_W[2]}px;flex:none;padding-right:16px;display:flex;align-items:center;gap:12px">{th("Délai", None).replace("flex:1;", "").replace("padding-right:16px;", "")}{pill("OBJECTIF", "align-self:center")}</div>'
            f'{th("Outil", _B17_W[3])}</div>')
    rows = ''.join(_b17_row(i, *s, first=(i == 1)) for i, s in enumerate(st, 1))
    table = f'<div style="display:flex;flex-direction:column">{head}{rows}</div>'
    band = (f'<div style="background:{NUIT};border-radius:16px;padding:14px 28px;display:flex;align-items:center;gap:22px">'
            f'<p style="font-family:{L};font-size:24px;font-weight:700;letter-spacing:2px;color:{CHAMP};white-space:nowrap">SOURCE</p>'
            f'<p style="flex:1;font-size:26px;line-height:1.3;color:{CLAIR}">Dossier, chap. 09 : « Le pipeline en sept étapes » ; outils : chap. 15</p></div>')
    sp = '<div style="flex:1"></div>'
    # marge basse : padding 64 + cale fixe de 76 px + écart 20 = les 160 px habituels (bas du corps à 920 px), comme B16
    inner = f'''{bhead(17, 'Processus', 'Sept étapes : qui, preuve, délai, outil')}
{sp}
{table}
{sp}
{band}
<div style="height:76px;flex:none"></div>
{bfoot(17)}'''
    return 'b17', inner, dict(gap=20, pad='128px 128px 64px')


ALL = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]
