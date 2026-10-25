# Diapositives de secours B1 à B13 (questions du jury), même système visuel que le deck principal
from kit import *

ORG = '/_blob/f6153fe677b16873e49378b0adbd4f01'
USMAP = '/_blob/c237626e9530474ba834563336e2b6c9'
ARBRE = '/_blob/c0b87ff1fc42b54deca64e6c705b3137'
SEQ = '/_blob/1386c229e7278bcd00815efe2155b121'
USMAP2 = '/_blob/6e61857966cc7cade3f90e50fc4ced2c'


def bhead(n, sujet, title):
    return header(f'Secours · B{n} · {sujet}', title, GRISD)


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


def b1():
    t = table(['Persona', 'Contacts', 'Verdict de l’étude'],
              [['A · Vigneron-propriétaire', '14', 'Confirmé'],
               ['B · Responsable caveau', '8', 'Confirmé, fort turnover'],
               ['C · Caviste', '7', 'Confirmé et élargi : caves touristiques, en ligne, réseaux'],
               ['D · Directeur commercial', '15', "Confirmé ; accès par l'ADV dans les grandes maisons"],
               ['E · Client final étranger', '5', 'Confirmé : particulier ou collectionneur']], [34, 14, 52])
    inner = f'''{bhead(1, 'Personas', 'Cinq personas confrontés au réel en octobre 2026')}
<div style="display:flex;gap:48px;flex:1">
<div style="width:1080px;display:flex;flex-direction:column;gap:18px">{t}
<p style="font-size:24px;line-height:1.35;color:{GRIS}">49 contacts rattachés aux personas, plus une dizaine d'ADV, comptables et logisticiens (l'angle mort, traité par le comité d'achat) et un seul cas de conciergerie.</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box('La base', '70 contacts pro : 40 issus des e-mails 2024-2026, 30 des salons et du CRM · 47 réponses : satisfaction 2024 (23), transport écologique 2025 (20), prospects voilier-cargo (4) · 15 avis Google · top 10 anonymisé')}
{box('Limite assumée', "Échanges écrits, pas d'entretien dédié · prospects sous-représentés (4 réponses) · entretiens prévus au T1 2027", ORANGE)}
</div></div>
{bfoot(1)}'''
    return 'b1', inner, dict(gap=36)


def b2():
    pts = [(15, 'ICP'), (15, 'Flux'), (15, 'Problème'), (15, 'Volume'), (15, 'Timing'), (10, 'Décision'), (10, 'Prépa.'), (5, '')]
    cols = [PETROLE, SARCF, SARC, '#4FA7BA', '#7DBCCA', ORF, OR, CHAMP]
    seg = ''.join(f'<div style="flex:{n};height:64px;background:{c};display:flex;align-items:center;justify-content:center"><p style="font-size:24px;font-weight:600;color:#FFFFFF">{n}</p></div>' for (n, _), c in zip(pts, cols))
    lab = ''.join(f'<p style="flex:{n};font-size:24px;text-align:center;color:{GRIS}">{t}</p>' for n, t in pts)
    steps = [('1 · Trier : CAVE', 'Clientèle, Autorité, Volume, Échéance · qualifié = C confirmé, A identifié, E daté'),
             ('2 · Score express /20', 'le brouillon de terrain · ≥ 14 : P1 · 8-13 : P2 · &lt; 8 : nurture'),
             ('3 · PA-FIT /100', 'la seule grille saisie au CRM · cadence dès 55'),
             ('4 · Tiers A / B / C', 'le rythme de suivi, pas la priorité · 80 % du temps sur A et B')]
    st = ''.join(f'<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:6px solid {BORD};border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;gap:6px">'
                 f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{BORD}">{a}</p><p style="font-size:24px;line-height:1.3;color:{ENCRE}">{b}</p></div>' for a, b in steps)
    inner = f'''{bhead(2, 'Priorisation', 'Trier vite, noter une fois : une seule grille fait foi')}
<div style="display:flex;gap:16px">{st}</div>
<div style="display:flex;flex-direction:column;gap:8px">
{label('PA-FIT : 100 points, 8 critères', BORD, ls=2)}
<div style="display:flex;gap:3px;border-radius:10px;overflow:hidden">{seg}</div>
<div style="display:flex;gap:3px">{lab}</div>
<p style="font-size:24px;color:{GRISD}">Dernier segment : valeur stratégique (5 points)</p></div>
<div style="flex:1"></div>
<div style="display:flex;gap:24px">
{box('Seuils', '75-100 : priorité active (P1) · 55-74 : à développer (P2) · 35-54 : nurture · &lt; 35 : disqualifié ou veille', BORD)}
{box('La règle', 'Un score sans preuve vaut zéro · barème recalibré après 90 jours · tiers : A &gt; 150 envois/an, B 40-150, C &lt; 40', PETROLE)}
</div>
{bfoot(2)}'''
    return 'b2', inner, dict(gap=30)


def b3():
    t = table(['Le prospect dit', 'On reconnaît', 'On recentre', 'On demande'],
              [["« J'ai un compte UPS »", 'Il assure le transport physique', 'Douane, taxes, suivi, destinataire', '« Qui intervient en cas de blocage ? »'],
               ['« Viticolis est moins cher »', 'Un très bon standard digital', 'Comparer le flux complet', '« Quel cas sort de leur standard ? »'],
               ['« Dartess fait tout »', 'Une forte capacité', 'Agilité, un seul interlocuteur', '« Quelle personnalisation vous manque ? »'],
               ['« DHL est mondial »', 'Un réseau incontestable', "L'expertise vin", '« Qui connaît votre cuvée et vos contraintes ? »'],
               ['« On gère en interne »', 'Une équipe qui connaît ses clients', 'Le temps et le risque', '« Et quand la personne référente est absente ? »']], [24, 24, 22, 30], pad=8)
    inner = f'''{bhead(3, 'Concurrence · fiches de comparaison, sources publiques oct. 2026', 'Reconnaître, recentrer, questionner : jamais dénigrer')}
{t}
<div style="flex:1"></div>
<div style="display:flex;gap:24px">
{box('3 questions gagnantes', '« Qui paie les taxes, et quand ? » · « Sur quelle valeur êtes‑vous indemnisé si ça casse ? » · « Qui fait la paperasse ? »', SARCF)}
{box('3 faiblesses assumées', 'Groupage USA en ~21 j (direct ~5 j) · prix des petites quantités (ramené au coût par bouteille) · notre taille (statut réglementé, filiale US)', ORANGE)}
</div>
{bfoot(3)}'''
    return 'b3', inner, dict(gap=24)


def b4():
    inner = f'''{bhead(4, 'SPIN sur le terrain', 'Sur le terrain : la permission avant le tunnel')}
<div style="display:flex;gap:40px;flex:1">
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box('Compte structuré, premier appel : la permission en 45 s', '« Quelle destination ou quel flux concentre aujourd’hui le plus d’enjeux logistiques ? » · « Le principal risque est-il le délai, la douane, la traçabilité, le coût ou la cohérence RSE ? » · puis proposer 25 minutes de cartographie du flux, avec deux créneaux', ORF)}
{box('Caveau : un appel de moins de 3 minutes', 'Il vise 30 minutes de démonstration sur ses vins, pas une vente · on prospecte avant les pics (mai, juin, septembre), pas pendant · le playbook réserve le bloc 10 h-12 h au téléphone', SARCF)}
</div>
<div style="width:820px;display:flex;flex-direction:column;gap:12px">
{label('La banque compte 8 lignes : trois exemples de plus', ORF, ls=2)}
{box('Responsable caveau · I', '« Quel effet a une réponse floue ou un refus sur la vente en cours, et sur l’avis que laissera ce visiteur ? »', SARC)}
{box('Caviste · I', '« Sur un mois, combien de ventes de 2 bouteilles auraient pu être des ventes de 12 ? »', BORD)}
{box('Distillerie · P', '« Quels prestataires vous ont dit non, et pourquoi ? »', PETROLE)}
</div></div>
{bfoot(4)}'''
    return 'b4', inner, dict(gap=36)


def b5():
    inner = f'''{bhead(5, 'Transparence IA', 'L’IA a aidé la forme ; le fond reste sourcé et vérifié')}
<div style="display:flex;gap:40px;flex:1">
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box("L'outil et son usage", 'Claude (Anthropic), crédité dès l’avant-propos, prompts représentatifs en annexe W · 8 chantiers de forme : maquette, identité visuelle, pagination et sommaire, ponts de navigation, schémas, calage des pages, ordre des annexes, relecture de forme', SARCF)}
{box('Le fond et ses sources', 'Documentation officielle et procédures 2026 · dashboards Planet’Connect au 24/09/2026 · 3 enquêtes (47 réponses) · 25 sources externes datées (OIV, FEVS, Atout France…)', PETROLE)}
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box('Aussi, à déclarer', "Des passes de mise en cohérence avec Claude : chiffres corrigés d’après les sources, règles harmonisées (assurance, feuille de route, seuils), bibliographie, renvois ; chaque correction vérifiée à sa source · ce support oral : titres, mises en page, visualisations et formulation des notes travaillés avec Claude, à partir du dossier, puis relus", OR)}
{box('Garde-fous', "Aucune donnée personnelle de client final · aucun identifiant · aucune image générée par IA (schémas codés à partir des données) · chaque chiffre vérifié à sa source (annexe C)", BORD)}
</div></div>
{box('Le test', 'Le meilleur contrôle, c’est vous : quel chiffre ou quelle procédure voulez-vous que je vous explique ?', CHAMP, dark=True)}
{bfoot(5)}'''
    return 'b5', inner, dict(gap=30)


def b6():
    t = table(['KPI', 'Fréquence', 'Cible', 'Si écart'],
              [['Adhérents actifs (≥ 1 envoi en 90 j)', 'Mensuel', '&gt; 60 %', 'Campagne réveil'],
               ['Activation à J+30', 'Mensuel', '≥ 70 %', "Revoir l'onboarding"],
               ['RDV tenus', 'Hebdomadaire', 'Baseline 90 j', "Revoir l'accroche, relancer"],
               ['Win rate', 'Mensuel', '40-60 %', 'Closing, objections'],
               ['Cycle de vente médian', 'Mensuel', '7 à 21 j visés', 'Lever les blocages'],
               ['OTIF', 'Mensuel', 'Baseline', 'Aligner le discours délais'],
               ['Marge contributive', 'Par dossier', '&gt; plancher (non affiché)', 'Disqualifier ou renégocier le périmètre'],
               ['Hygiène du forecast', 'Hebdomadaire', '≥ 95 %', 'Sortie du forecast']], [38, 18, 18, 26])
    inner = f'''{bhead(6, 'Indicateurs', 'Chaque KPI a une fréquence, une cible et une action')}
<div style="display:flex;gap:44px;flex:1">
<div style="width:1080px">{t}</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box('Entonnoir cible (objectifs)', 'Lead → qualifié 40-60 % · qualifié → RDV tenu 50-70 % · RDV → proposition ≥ 70 % · proposition → signature 40-60 % · signature → activé ≥ 70 % · activé → récurrent ≥ 60 %', BORD)}
{box('Satisfaction 2024 (23 réponses)', '4,65/5 de satisfaction · 4,87/5 de probabilité de recommander (ce n’est pas un NPS) · 21 utilisateurs du SAV sur 22 satisfaits', SARCF)}
</div></div>
{bfoot(6)}'''
    return 'b6', inner, dict(gap=32)


def b7():
    lines = [('Transport, groupage DDP (grille 2026)', '210 €'), ('Taxes estimées (exemple du playbook)', '~30 €'),
             ('Frais de dossier DDP', '17 €'), ('Assurance en option : 3 % × (300 € + 210 €)', '≈ 15 €')]
    rows = ''.join(f'<div style="display:flex;justify-content:space-between;padding:12px 0px;border-bottom:1px solid {FILET}"><p style="font-size:26px;color:{ENCRE}">{a}</p>'
                   f'<p style="font-family:{T};font-size:30px;font-weight:700;color:{PETROLE}">{b}</p></div>' for a, b in lines)
    inner = f'''{bhead(7, 'Prix rendu', 'Le prix rendu, sans maquillage : le client final paie')}
<div style="display:flex;gap:56px;flex:1">
<div style="width:980px;display:flex;flex-direction:column;gap:6px">
{label('12 bouteilles au Texas, 300 € de vin', SARCF, ls=2)}
{rows}
<div style="display:flex;justify-content:space-between;padding-top:14px"><p style="font-size:28px;font-weight:700;color:{ENCRE}">Total avec l'option assurance, réglé d'avance</p><p style="font-family:{T};font-size:44px;font-weight:700;color:{ORF}">≈ 270 €</p></div>
<p style="font-size:24px;line-height:1.35;color:{GRISD}">Les taxes restent une estimation, révisable (CGS art. 5) · ~21 jours estimés, hors douane · le simulateur fait foi</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
<div style="background:{NUIT};border-radius:18px;padding:24px 28px;display:flex;flex-direction:column;gap:6px">
<p style="font-family:{T};font-size:72px;font-weight:700;line-height:1;color:{CHAMP}">≈ 17,50 €</p>
<p style="font-size:24px;color:{BRUME}">de transport par bouteille (210 € / 12)</p></div>
{box('Les règles', 'Droits US : 10 % depuis février 2026 (15 % d’août 2025 à février 2026) · pas de remise sans contrepartie ni validation de la direction · on négocie le périmètre avant le prix', BORD)}
</div></div>
{bfoot(7)}'''
    return 'b7', inner, dict(gap=32)


def b8():
    def q(t, c, bg, items):
        li = ''.join(f'<p style="font-size:24px;line-height:1.3;color:{ENCRE}">· {i}</p>' for i in items)
        return (f'<div style="background:{bg};border-top:6px solid {c};border-radius:12px;padding:14px 20px;display:flex;flex-direction:column;gap:6px">'
                f'{label(t, c, ls=2)}{li}</div>')
    swot = f'''<div style="width:1060px;display:grid;grid-template-columns:repeat(2, 1fr);gap:14px">
{q('Forces', SARCF, '#E8F3F5', ['Commissionnaire, obligation de résultat', 'Spécialiste vins, champagnes, spiritueux', 'Filiale US licenciée', "Planet'Connect", 'Assurance en option, choisie 9 fois sur 10'])}
{q('Faiblesses', BORD, '#F6EAEE', ['Notoriété limitée', 'Capacité commerciale de PME', 'Dépendance aux partenaires', 'Forte concentration sur quelques grands comptes'])}
{q('Opportunités', '#3A8A5C', '#EAF4EE', ['Vente directe et œnotourisme', 'Nouvelles destinations', 'Demande RSE', 'Vignerons indépendants à équiper'])}
{q('Menaces', ORANGE, '#FBEFE8', ['Droits US, volatilité réglementaire', 'Recul de la consommation', 'Pression tarifaire', 'Coûts logistiques et énergie'])}
</div>'''
    hz = [('Court terme · 0-12 mois', 'Consolider le groupage USA, lancer Spiritueux USA, activer les signés, assainir le CRM', SARCF),
          ('Moyen terme · 1-3 ans', 'Diversifier : UK, Canada, Japon, Scandinavie ; événementiel, importateurs', ORF),
          ('Long terme · 3 ans et plus', 'Devenir la référence du transport international du vin ; projets au conditionnel', PETROLE)]
    hzs = ''.join(box(a, b, c) for a, b, c in hz)
    inner = f'''{bhead(8, 'Stratégie', 'Capitaliser sur le trio, diversifier sans sacrifier les USA')}
<div style="display:flex;gap:40px;flex:1">{swot}<div style="flex:1;display:flex;flex-direction:column;gap:14px">{hzs}</div></div>
{bfoot(8)}'''
    return 'b8', inner, dict(gap=32)


def b9():
    inner = f'''{bhead(9, 'Organisation', 'Treize personnes, quatre pôles et une filiale')}
<div style="flex:1;display:flex;justify-content:center"><img src="{ORG}" alt="Organigramme Planet Aura 2026 : direction, commerce et développement, filiale de New York, logistique, administration" style="width:1500px;height:640px;object-fit:contain"></div>
{bfoot(9)}'''
    return 'b9', inner, dict(gap=24)


def b10():
    leg = [('#A6CEE3', 'Ouvert'), ('#B1DE89', 'Groupage et direct'), ('#C9B1D4', 'Groupage (certains codes postaux) et direct'),
           ('#EBEB30', 'Envoi direct uniquement'), ('#FED9A6', 'Certains codes postaux'), ('#999999', 'Fermé')]
    lg = ''.join(f'<div style="display:flex;align-items:center;gap:12px"><div style="width:30px;height:22px;border-radius:4px;background:{c};flex:none"></div>'
                 f'<p style="font-size:24px;line-height:1.25;color:{ENCRE}">{t}</p></div>' for c, t in leg)
    inner = f'''{bhead(10, 'États-Unis', 'Où livre-t-on aux États-Unis ? La carte 2026')}
<div style="display:flex;gap:40px;flex:1">
<img src="{USMAP2}" alt="Carte 2026 des États américains desservis par Planet Aura, en groupage ou en direct" style="width:1000px;height:631px;object-fit:contain;background:#FFFFFF;border-radius:16px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
{label('Légende', GRISD, ls=2)}
<div style="display:flex;flex-direction:column;gap:8px">{lg}</div>
<div style="flex:1"></div>
{box('Groupage DDP', '36 bouteilles max. par personne et par envoi · POA dès 2 100 $ (≈ 12 bouteilles) · ~21 jours estimés', SARCF)}
<p style="font-size:24px;line-height:1.3;color:{GRISD}">Vermont : livré par un prestataire interne après regroupement</p>
</div></div>
{bfoot(10)}'''
    return 'b10', inner, dict(gap=28)


def b11():
    def nd(title, body, c, w):
        return (f'<div style="width:{w}px;background:#FFFFFF;border:1px solid {FILET};border-top:6px solid {c};border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;gap:6px">'
                f'<p style="font-family:{L};font-size:24px;font-weight:600;color:{c}">{title}</p><p style="font-size:24px;line-height:1.3;color:{ENCRE}">{body}</p></div>')
    tree = f'''<div style="width:1020px;display:flex;flex-direction:column;gap:14px">
<p style="background:{NUIT};color:#FFFFFF;font-size:26px;font-weight:600;text-align:center;padding:14px 20px;border-radius:12px">Envoi assuré (option 3 %) · signalement sous 48 h, avec photos : le client choisit</p>
<div style="display:flex;gap:20px">
<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<p style="background:{SARCF};color:#FFFFFF;font-family:{L};font-size:24px;font-weight:600;text-align:center;padding:10px;border-radius:10px">RÉEXPÉDITION (RXP)</p>
<p style="font-size:24px;text-align:center;color:{ENCRE}"><b>Le domaine a-t-il encore les bouteilles ?</b></p>
<div style="display:flex;gap:12px">{nd('Oui', 'Enlèvement planifié, RXP suivie jusqu’à la livraison', SARC, 290)}{nd('Non', 'Remplacement équivalent proposé ; refusé : bascule en remboursement', ORF, 290)}</div>
</div>
<div style="width:330px;display:flex;flex-direction:column;gap:12px">
<p style="background:{ORANGE};color:#FFFFFF;font-family:{L};font-size:24px;font-weight:600;text-align:center;padding:10px;border-radius:10px">REMBOURSEMENT</p>
{nd('Instruction', 'Vérification du dossier (valeur déclarée, preuves), puis instruction avec l’assureur', ORANGE, 330)}
</div></div>
<p style="font-size:24px;color:{GRISD}">Procédure sinistre 2026 · client et domaine informés à chaque étape</p>
</div>'''
    inner = f'''{bhead(11, 'Sinistre', "Et si ça casse ? L’incident devient une seconde vente")}
<div style="display:flex;gap:40px;flex:1">{tree}
<div style="flex:1;display:flex;flex-direction:column;gap:16px">
{box("L’assurance, une option", '3 % de la valeur (vin + transport), jusqu’à 20 000 € par envoi avec emballage homologué, choisie sur 89,8 % des envois', SARCF)}
{box('Les exclusions', 'Altération thermique, oxydation, bouchons, étiquettes · sans option : conditions de base, pas le régime ad valorem', ORANGE)}
{box('La règle des factures', 'Réexpédition : le domaine facture les seules bouteilles · remboursement : bouteilles, transport et taxes', PETROLE)}
</div></div>
{bfoot(11)}'''
    return 'b11', inner, dict(gap=28)


def b12():
    touches = [(1, 'Recherche', 'vue LinkedIn', GRISD), (2, 'E-mail 1', 'problème + valeur', SARC), (4, 'Appel 1', '2 questions, 45 s', ORANGE),
               (6, 'LinkedIn', 'invitation', PETROLE), (8, 'E-mail 2', 'preuve de méthode', SARC), (11, 'Appel 2', '+ message vocal', ORANGE),
               (14, 'E-mail 3', 'décision 1 / 2 / 3', SARC), (18, 'Sortie', 'nurture 45 j', BORD)]
    W = 1600
    x = lambda d: round((d - 1) / 17 * (W - 160)) + 80
    els = [f'<div style="position:absolute;left:{x(1)}px;top:58px;width:{x(18) - x(1)}px;height:6px;background:{FILET}"></div>']
    for i, (d, a, b, c) in enumerate(touches):
        els.append(f'<p style="position:absolute;left:{x(d) - 32}px;top:29px;width:64px;height:64px;border-radius:50%;background:{c};color:#FFFFFF;font-family:{L};font-size:24px;font-weight:600;text-align:center;line-height:64px">J{d}</p>')
        top = 112 if i % 2 == 0 else 196
        els.append(f'<p style="position:absolute;left:{x(d) - 100}px;top:{top}px;width:200px;text-align:center;font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{ENCRE}">{a}</span></b><br>{b}</p>')
    line = f'<div style="position:relative;width:{W}px;height:280px">{"".join(els)}</div>'
    inner = f'''{bhead(12, 'Cadence', 'Huit touches en dix-huit jours, et la réponse arrête tout')}
{line}
<div style="flex:1"></div>
<div style="display:flex;gap:24px">
{box('Pour qui', '~20 comptes P1 en ABM 1:1 · cadence ouverte dès PA-FIT 55 (P1 et P2) · caveaux : cadence courte, J1, J+4, J+10 puis visite', SARCF)}
{box('Toute réponse arrête tout', 'Réponse, RDV, opposition ou erreur : cadence stoppée et tâche humaine créée · câblage Brevo + HubSpot en novembre 2026', ORANGE)}
{box('Mesurer, chaque vendredi', 'Réponse &lt; 10 % : revoir l’angle · &lt; 5 RDV pour 100 : resserrer · opt-out &gt; 2 % : stopper', BORD)}
</div>
{bfoot(12)}'''
    return 'b12', inner, dict(gap=28)


def b13():
    t = table(['Échéance', 'Chantier', 'Responsable', 'Temps', 'Budget', 'Critère de passage'],
              [['Sept. 2026', 'Nettoyage CRM, listes A/B/C', 'Emma + Adam', '24 h', '0 €', '≥ 95 % des comptes prioritaires exploitables'],
               ['Oct. 2026', 'One-pager par ICP + landing page', 'Emma + Adam', '36 h', '600 €', 'Supports validés par la direction'],
               ['Nov. 2026', '3 séquences Brevo + reporting HubSpot', 'Emma', '20 h', '200 €', 'Arrêt automatique sur réponse testé'],
               ['Nov. → mai', 'Tests LinkedIn, 3 clusters', 'Adam', '3 h/sem.', '900 €', 'Coût par SQL comparé à l’outbound'],
               ['Janv. 2027', 'Webinaire export', 'Emma + expert', '20 h', '300 €', '10 inscrits ICP et 3 diagnostics'],
               ['Janv. → juil.', 'Deux salons en visiteur', 'Adam + Emma', '24 h', '1 000 €', '8 RDV qualifiés par événement'],
               ['Après validations', 'Vidéo démo, études de cas · pilote VELA (projet)', 'Emma · direction', '-', 'hors budget', 'Accords écrits des adhérents cités']],
              [12, 26, 14, 9, 10, 29])
    inner = f'''{bhead(13, 'Feuille de route', 'Six chantiers datés, chiffrés et conditionnés')}
{t}
<div style="flex:1"></div>
<p style="font-size:24px;color:{GRIS}"><b>Plafond : 3 000 € de dépenses externes</b> (0 + 600 + 200 + 900 + 300 + 1 000) · le temps interne est une capacité à réserver · pas de critère atteint, pas d'étape suivante</p>
{bfoot(13)}'''
    return 'b13', inner, dict(gap=28)


def b14():
    objs = [('O-1', 'Le prix', '« C’est cher »', '210 € HT de transport pour 12 btl vers les USA : <b>≈ 17,50 € par bouteille, payés par le client final</b>', BORD),
            ('O-6', 'La casse', '« Et si ça casse ? »', 'Assurance <b>en option, 3 %</b> (vin + transport), jusqu’à 20 000 € par envoi, choisie sur 89,8 % des envois · signalement sous 48 h, avec photos', SARCF),
            ('O-9', 'La chaleur', '« Et en plein été ? »', '<b>Départ différé</b> · et on le dit : l’altération thermique est exclue de l’assurance (CGS)', ORANGE),
            ('O-12', 'Le statu quo', '« On a déjà quelqu’un »', '« Je ne vous demande pas de changer, <b>je vous demande de comparer sur UN envoi.</b> »', PETROLE),
            ('O-14', 'Le temps', '« Je n’ai pas le temps »', '<b>3 min de saisie</b> par envoi · saisonniers formés en 30 min', ORF)]
    rows = ''
    for code, name, quote, proof, c in objs:
        rows += f"""<div style="flex:1;display:flex;align-items:center;gap:24px;background:#FFFFFF;border:1px solid {FILET};border-left:8px solid {c};border-radius:14px;padding:10px 24px">
<div style="width:300px;display:flex;flex-direction:column;gap:2px;flex:none"><p style="font-family:{L};font-size:24px;font-weight:600;color:{c}">{code} · {name}</p>
<p style="font-family:{T};font-style:italic;font-size:26px;color:{ENCRE}">{quote}</p></div>
<div style="width:40px;flex:none">{arrow(40, 26, c, 3)}</div>
<p style="flex:1;font-size:24px;line-height:1.35;color:{ENCRE}">{proof}</p></div>"""
    inner = f"""{bhead(14, 'Objections', 'Le top 5 : une objection, une seule preuve')}
<div style="flex:1;display:flex;flex-direction:column;gap:12px">{rows}</div>
<p style="font-size:24px;line-height:1.35;color:{GRIS}"><b><span style="color:{PETROLE}">Accueillir → Clarifier → Prouver, une fois → Vérifier</span></b> · réponse du prospect notée mot pour mot · banque de 26 objections (annexe D) · classement terrain, hiérarchisé sur les motifs de perte CRM en novembre 2026</p>
{bfoot(14)}"""
    return 'b14', inner, dict(gap=26)


def b15():
    ST = {'Livré': SARCF, 'Objectif': BORD, 'Proposé': SARC, 'Règle': PETROLE}
    data = [('Des chiffres qui divergent d’un support à l’autre', 'Source unique au 24/09/2026, preuve en 3 statuts', 'Un chiffre sans source ni date ne sort pas', 'Livré', ''),
            ('448 prospects non qualifiés', '5 ICP, PA-FIT, tiers A/B/C', 'L’adéquation prime sur la taille', 'Livré', 'recalibré à 90 j'),
            ('Aucun persona écrit', '5 personas confrontés au réel, angle mort ADV', 'Ne pas parler au mauvais interlocuteur', 'Livré', 'entretiens T1 2027'),
            ('Activation jamais mesurée', '7 étapes, SLA, vente finie au 1er envoi', 'Un signé jamais activé ne vaut rien', 'Objectif', '≥ 70 % à J+30'),
            ('Savoirs de vente dispersés', 'SPIN, 26 objections, ROI, négociation', 'Le prix est notre point faible', 'Livré', ''),
            ('HubSpot, Brevo, Planet’Connect sans règles', 'Dictionnaire CRM, hygiène, RACI, rituels', 'Une donnée, un propriétaire, une décision', 'Proposé', 'à ratifier'),
            ('Un savoir dans quelques têtes', 'Plan 30-60-90 et annexe U jour par jour', 'Rendre la vente transmissible', 'Livré', 'non testé')]
    rows = []
    for ex, ap, why, st, sub in data:
        tag_ = f'<b><span style="color:{ST[st]}">{st}</span></b>' + (f'<br><span style="color:{GRISD}">{sub}</span>' if sub else '')
        rows.append([ex, f'<b>{ap}</b>', f'<span style="font-style:italic">{why}</span>', tag_])
    t = table(['L’existant', 'Mon apport', 'Pourquoi', 'Statut'], rows, [26, 33, 26, 15], pad=7)
    inner = f"""{bhead(15, 'Contribution', 'Ce qui existait, ce que j’ai apporté, et pourquoi')}
{t}
<div style="flex:1"></div>
<p style="font-size:24px;line-height:1.35;color:{GRIS}"><b><span style="color:{PETROLE}">Ce qui n’est pas de moi :</span></b> CGS et grilles 2026, filiale (direction) · procédures 2026, ~145 signés (équipe) · Planet’Connect, développé avec Halt Solutions, j’y ai contribué</p>
{bfoot(15)}"""
    return 'b15', inner, dict(gap=24)


ALL = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
