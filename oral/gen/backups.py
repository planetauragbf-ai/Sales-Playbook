# Génère les diapos de secours B1-B7 (même gabarit que le deck : bande 9EC5CE, sur-titre « DIAPO DE SECOURS »)
import os
OUT = os.path.join(os.path.dirname(__file__), '..', 'deck', 'project', 'slides')
FONT_P = "font-family:'Poppins', Arial, sans-serif"
FONT_H = "font-family:'Playfair Display', Georgia, serif"
TD = 'padding:12px 18px'

def slide(sid, num, eyebrow, title, body, notes, gap=28):
    return f'''<section id="{sid}" data-transition="fade" style="background:#F6F8F7;color:#14303B;font-family:'Inter', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:{gap}px">
<div style="position:absolute;left:0;top:0;width:20px;height:1080px;background:#9EC5CE"></div>
<div style="display:flex;flex-direction:column;gap:12px">
<p style="{FONT_P};font-size:24px;font-weight:600;letter-spacing:4px;color:#12475B">DIAPO DE SECOURS · {num} — {eyebrow}</p>
<h2 style="{FONT_H};font-size:52px;font-weight:700;line-height:1.12;color:#12475B">{title}</h2>
</div>
{body}
<p style="position:absolute;left:128px;width:1400px;bottom:64px;font-size:24px;color:#6A7B82">Planet Aura · Sales Playbook 2026 · Soutenance d’Emma Soares Britschgy</p>
<p style="position:absolute;right:128px;width:80px;bottom:64px;text-align:right;{FONT_P};font-size:24px;font-weight:600;color:#12475B">{num}</p>
<aside>{notes}</aside>
</section>
'''

def table(head, rows, widths, size=24, pad=TD, head_bg='#12475B', head_fg='#FFFFFF', first_bold=True, style=''):
    h = ''.join(f'<th style="width:{w}%;{pad};color:{head_fg};font-weight:600">{c}</th>' for c, w in zip(head, widths))
    out = [f'<table style="{style}font-family:\'Inter\', Arial, sans-serif;font-size:{size}px;color:#3E5058;background:#FFFFFF;border-radius:12px">',
           f'<tr style="background:{head_bg}">{h}</tr>']
    for i, r in enumerate(rows):
        bg = ' style="background:#F4F8F9"' if i % 2 else ''
        cells = []
        for j, c in enumerate(r):
            st = pad + (';font-weight:700;color:#14303B' if (j == 0 and first_bold) else '')
            cells.append(f'<td style="{st}">{c}</td>')
        out.append(f'<tr{bg}>' + ''.join(cells) + '</tr>')
    out.append('</table>')
    return '\n'.join(out)

def box(label, text, bg='#EAF0F4', lc='#12475B', tc='#14303B', size=26):
    return (f'<div style="display:flex;align-items:center;gap:28px;background:{bg};border-radius:12px;padding:18px 32px">'
            f'<p style="{FONT_P};font-size:24px;font-weight:600;letter-spacing:3px;color:{lc};white-space:nowrap">{label}</p>'
            f'<p style="font-size:{size}px;line-height:1.35;color:{tc}">{text}</p></div>')

S = {}

# B1 — validation des personas
S['b1'] = slide('b1', 'B1', 'PERSONAS', 'Cinq personas confrontés au réel en octobre 2026',
'''<div style="display:flex;gap:16px">
<div style="flex:1;display:flex;flex-direction:column;gap:2px;background:#FFFFFF;border-radius:12px;padding:16px 22px"><p style="''' + FONT_H + ''';font-size:48px;font-weight:700;line-height:1.05;color:#12475B">70</p><p style="font-size:24px;line-height:1.3;color:#3E5058">contacts pro : 40 emails 2024-2026, 30 salons et CRM</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:2px;background:#FFFFFF;border-radius:12px;padding:16px 22px"><p style="''' + FONT_H + ''';font-size:48px;font-weight:700;line-height:1.05;color:#12475B">47</p><p style="font-size:24px;line-height:1.3;color:#3E5058">réponses à 3 enquêtes clients et prospects (2024-2025)</p></div>
<div style="flex:1;display:flex;flex-direction:column;gap:2px;background:#FFFFFF;border-radius:12px;padding:16px 22px"><p style="''' + FONT_H + ''';font-size:48px;font-weight:700;line-height:1.05;color:#12475B">15</p><p style="font-size:24px;line-height:1.3;color:#3E5058">avis Google, plus le top 10 anonymisé</p></div>
</div>
''' + table(['Persona', 'Contacts', 'Verdict'], [
    ['A · Vigneron-propriétaire', '14', 'Confirmé'],
    ['B · Responsable caveau', '8', 'Confirmé, fort turnover'],
    ['C · Caviste', '7', 'Confirmé et élargi : caves touristiques, en ligne'],
    ['D · Directeur commercial', '15', 'Confirmé, accès par l’ADV dans les grandes maisons'],
    ['E · Client final étranger', '5', 'Confirmé : particulier ou collectionneur'],
], [34, 14, 52], pad='padding:10px 18px') + '\n' +
box('LIMITE ASSUMÉE', 'Échanges écrits, pas encore d’entretiens dédiés · prospects sous-représentés (4 réponses) · entretiens prévus au T1 2027', bg='#F6EDF0', lc='#722F45'),
'''Si on me demande si mes personas sont réels : je les ai confrontés en octobre 2026 à 70 contacts professionnels réels et à 47 réponses de nos trois enquêtes, plus 15 avis Google. Résultat : cinq profils confirmés, trois ajustements, comme le caviste, qui n’est pas seulement urbain, et un angle mort, l’ADV, les comptables et la logistique, traités dans le comité d’achat.

Ma limite, je la dis : ce sont des échanges écrits, pas encore des entretiens dédiés, et les prospects sont sous-représentés. Les entretiens sont prévus pour la version 2027.

(Ne jamais dire « j’ai interviewé 70 clients ». 49 contacts rattachés aux personas : 14 + 8 + 7 + 15 + 5. Enquêtes : 23 satisfaction 2024, 20 transport écologique 2025, 4 prospects voilier-cargo 2025. Aucun nom.)''')

# B2 — CAVE → PA-FIT
S['b2'] = slide('b2', 'B2', 'PRIORISATION', 'Trier vite, noter une fois : une seule grille fait foi',
'''<div style="display:flex;gap:16px">
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#FFFFFF;border-top:8px solid #9EC5CE;border-radius:12px;padding:20px 24px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;color:#20768B">1 · TRIER : CAVE</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058">Clientèle, Autorité, Volume, Échéance</p>
<p style="font-size:24px;line-height:1.3;color:#14303B;font-weight:600">Qualifié = C confirmé, A identifié, E daté</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#FFFFFF;border-top:8px solid #2D92A8;border-radius:12px;padding:20px 24px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;color:#20768B">2 · SCORE EXPRESS /20</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058">Le brouillon de terrain</p>
<p style="font-size:24px;line-height:1.3;color:#14303B;font-weight:600">≥ 14 : P1 · 8-13 : P2 · &lt; 8 : nurture</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#12475B;border-top:8px solid #12475B;border-radius:12px;padding:20px 24px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;color:#E8D3A6">3 · PA-FIT /100</p>
<p style="font-size:24px;line-height:1.3;color:#D7E5EA">La seule grille saisie au CRM</p>
<p style="font-size:24px;line-height:1.3;color:#F4F8F9;font-weight:600">Cadence à partir de 55</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#FFFFFF;border-top:8px solid #C6A15B;border-radius:12px;padding:20px 24px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;color:#8A6A33">4 · TIERS A / B / C</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058">Le rythme de suivi, pas la priorité</p>
<p style="font-size:24px;line-height:1.3;color:#14303B;font-weight:600">Mensuel · trimestriel · campagnes</p>
</div>
</div>
<div style="display:flex;gap:24px;align-items:flex-start">
''' + table(['Critère PA-FIT', 'Points'], [
    ['Adéquation ICP · adéquation du flux', '15 + 15'],
    ['Problème et impact · volume et économie', '15 + 15'],
    ['Événement et timing', '15'],
    ['Décision et accès · préparation opérationnelle', '10 + 10'],
    ['Valeur stratégique', '5'],
], [78, 22], pad='padding:10px 18px', first_bold=False, style='flex:1;') + '''
<div style="width:520px;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border-radius:12px;padding:20px 26px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">SEUILS</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">75-100</b> · priorité active (P1)</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">55-74</b> · à développer (P2)</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">35-54</b> · nurture</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">&lt; 35</b> · disqualifié ou veille</p>
</div>
</div>
''' + box('LA RÈGLE', 'Un score sans preuve vaut zéro · barème recalibré après 90 jours · 80 % du temps commercial sur les tiers A et B'),
'''Si on me dit que c’est une usine à gaz : chaque outil a un rôle différent, et un seul fait foi. CAVE sert à trier en deux minutes. Le score express sur 20 est un brouillon de terrain. Le PA-FIT sur 100 est la seule grille saisie dans le CRM : c’est lui qui décide de l’entrée en cadence, à partir de 55. Et les tiers A, B, C ne disent pas qui appeler en premier : ils fixent le rythme de suivi.

La règle qui évite l’usine à gaz : un score sans preuve vaut zéro, et le barème sera recalibré après 90 jours de données.

(Tiers : A plus de 150 envois par an, B de 40 à 150, C moins de 40. Ne jamais citer la part du CA réalisée sur les comptes A.)''', gap=26)

# B3 — battle card
S['b3'] = slide('b3', 'B3', 'CONCURRENCE', 'Reconnaître, recentrer, questionner : jamais dénigrer',
table(['Le prospect dit', 'On reconnaît', 'On recentre', 'On demande'], [
    ['« J’ai un compte UPS »', 'Il assure le transport physique', 'Douane, taxes, suivi, destinataire', '« Qui intervient en cas de blocage ? »'],
    ['« Viticolis est moins cher »', 'Un très bon standard digital', 'Comparer le flux complet', '« Quel cas sort de leur standard ? »'],
    ['« Dartess fait tout »', 'Une forte capacité', 'Agilité, un seul interlocuteur', '« Quelle personnalisation vous manque ? »'],
    ['« DHL est mondial »', 'Un réseau incontestable', 'L’expertise vin', '« Qui connaît votre cuvée et vos contraintes ? »'],
    ['« On gère en interne »', 'Une équipe qui connaît ses clients', 'Le temps et le risque', '« Et quand la personne référente est absente ? »'],
], [22, 24, 24, 30], size=24, pad='padding:12px 16px') + '''
<div style="display:flex;gap:20px">
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#12475B;border-radius:12px;padding:20px 26px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#E8D3A6">3 QUESTIONS GAGNANTES</p>
<p style="font-size:24px;line-height:1.35;color:#F4F8F9">« Qui paie les taxes, et quand ? » · « Sur quelle valeur êtes-vous indemnisé si ça casse ? » · « Qui fait la paperasse ? »</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:8px;background:#FFFFFF;border-radius:12px;padding:20px 26px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#722F45">3 FAIBLESSES ASSUMÉES</p>
<p style="font-size:24px;line-height:1.35;color:#3E5058">Groupage USA en 21 jours (direct ~5 j) · prix sur petites quantités (coût par bouteille livrée) · notre taille (statut réglementé, filiale US)</p>
</div>
</div>''',
'''Si on me demande de me battre contre UPS ou DHL : on ne dénigre jamais. On reconnaît ce que le concurrent fait bien, on recentre sur ce qui fait mal au prospect, la douane, les taxes, la casse, et on pose une question qui l’amène à le constater lui-même.

Les trois questions gagnantes : qui paie les taxes, et quand ? Sur quelle valeur êtes-vous indemnisé si ça casse ? Qui fait la paperasse ?

Et j’assume nos faiblesses avant qu’on me les oppose : 21 jours en groupage, mais l’envoi direct existe en 5 jours environ ; un prix unitaire élevé sur les petites quantités, que je ramène au coût par bouteille livrée ; notre taille, compensée par un statut réglementé et une filiale aux États-Unis.

(Sources publiques datées d’octobre 2026. Le premier adversaire observé, c’est le statu quo : ne pas dire « plus de la moitié des affaires perdues », ce n’est pas mesuré.)''')

# B4 — SPIN Champagne + appel 45 s
S['b4'] = slide('b4', 'B4', 'SPIN PAR PERSONA', 'Le même tunnel, adapté à une maison de Champagne',
'''<div style="display:flex;gap:16px">
''' + ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border-top:8px solid #C6A15B;border-radius:12px;padding:22px 24px">
<p style="{FONT_H};font-size:56px;font-weight:700;line-height:1;color:#8A6A33">{l}</p>
<p style="{FONT_P};font-size:24px;font-weight:600;letter-spacing:2px;color:#14303B">{n}</p>
<p style="font-size:26px;line-height:1.35;font-style:italic;color:#3E5058">{q}</p>
</div>
''' for l, n, q in [
    ('S', 'SITUATION', '« Quels marchés, modes, fréquences et Incoterms pour vos particuliers hors UE ? »'),
    ('P', 'PROBLÈME', '« Où perdez-vous visibilité ou temps : certificat CIVC, douane américaine, suivi ? »'),
    ('I', 'IMPLICATION', '« Que coûte un colis immobilisé en douane à l’image de la maison ? »'),
    ('N', 'BÉNÉFICE ATTENDU', '« Que changerait un plan de flux où le certificat et les taxes sont gérés à chaque envoi ? »'),
]) + '''</div>
<div style="display:flex;flex-direction:column;gap:10px;background:#F8F3E9;border-radius:12px;padding:22px 32px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#8A6A33">AU PREMIER APPEL : LA PERMISSION EN 45 SECONDES</p>
<p style="font-size:26px;line-height:1.35;color:#14303B">« Quelle destination ou quel flux concentre aujourd’hui le plus d’enjeux logistiques ? »</p>
<p style="font-size:26px;line-height:1.35;color:#14303B">« Le principal risque est-il le délai, la douane, la traçabilité, le coût ou la cohérence RSE ? »</p>
<p style="font-size:26px;line-height:1.35;color:#8A6A33;font-weight:600">Puis : proposer 25 minutes de cartographie du flux, avec 2 créneaux</p>
</div>''',
'''Si on me demande comment le SPIN s’adapte : la banque de questions de l’annexe E décline le tunnel par persona. Pour une maison de Champagne, le cycle est plus long et plusieurs personnes décident ; les questions portent sur le certificat CIVC, la douane américaine et l’image de la maison.

Et si on m’objecte qu’en pleine saison aucun vigneron n’accorde 35 minutes : on prospecte avant les pics, pas pendant. Et au premier appel, on ne déroule pas tout le tunnel : on demande la permission de poser deux questions en 45 secondes, puis on propose 25 minutes de cartographie du flux, avec deux créneaux.

(Cycle Champagne : 6 à 12 semaines. Le certificat CIVC est obligatoire hors UE ; Planet Aura en fait la demande pour 15 € HT par expédition.)''')

# B5 — transparence IA
S['b5'] = slide('b5', 'B5', 'TRANSPARENCE IA', 'L’IA a servi la forme ; le fond vient de sources vérifiables',
'''<div style="display:flex;gap:20px">
<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border-radius:12px;padding:22px 28px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">L’OUTIL ET SON USAGE</p>
<p style="font-size:24px;line-height:1.35;color:#3E5058"><b style="color:#14303B">Claude (Anthropic)</b>, crédité dès l’avant-propos, prompts détaillés en annexe W</p>
<p style="font-size:24px;line-height:1.35;color:#3E5058">8 chantiers : maquette, identité visuelle, pagination et sommaire, ponts de navigation, schémas, calage des pages, ordre des annexes, relecture de forme</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border-radius:12px;padding:22px 28px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">LE FOND ET SES SOURCES</p>
<p style="font-size:24px;line-height:1.35;color:#3E5058">Documentation officielle et procédures 2026 · tableaux de bord Planet’Connect au 24/09/2026 · 3 enquêtes (47 réponses) · sources externes datées : FEVS, OIV, Atout France</p>
</div>
</div>
''' + box('GARDE-FOUS', 'Aucune donnée personnelle de client final · aucun identifiant ni clé API · aucune image générée par IA · chaque chiffre vérifié à sa source (annexe C)') + '\n' +
box('LE TEST', 'Le meilleur contrôle, c’est vous : quel chiffre ou quelle procédure voulez-vous que je vous explique ?', bg='#12475B', lc='#9EC5CE', tc='#F4F8F9'),
'''Si on me demande ce que l’IA a fait : j’ai utilisé Claude, d’Anthropic, et je l’ai crédité dès l’avant-propos. L’annexe W détaille huit chantiers, avec un prompt représentatif pour chacun : la maquette, l’identité visuelle, la pagination, les ponts de navigation entre les pages, les schémas, le calage des pages, l’ordre des annexes et la relecture de forme.

Le fond vient de sources que je peux citer : la documentation officielle 2026, nos tableaux de bord du 24 septembre, nos trois enquêtes clients, et des sources externes datées. Aucune image n’a été générée par IA, aucune donnée personnelle n’a été partagée.

Et je retourne la question avec le sourire : quel chiffre ou quelle procédure voulez-vous que je vous explique ?

(Rester calme et factuelle : c’est une question d’intégrité, pas un piège. Le CDC autorise l’IA si elle est créditée, ses prompts indiqués et ses résultats enrichis.)''')

# B6 — KPI complet
S['b6'] = slide('b6', 'B6', 'INDICATEURS', 'Chaque KPI a une fréquence, une cible et une action',
'''<div style="display:flex;gap:28px;align-items:flex-start">
''' + table(['KPI', 'Fréquence', 'Cible', 'Si écart'], [
    ['Adhérents actifs (≥ 1 envoi en 90 j)', 'Mensuel', '&gt; 60 %', 'Campagne réveil'],
    ['Activation à J+30', 'Mensuel', '≥ 70 %', 'Revoir l’onboarding'],
    ['RDV tenus', 'Hebdomadaire', 'Baseline 90 j', 'Revoir l’accroche, relancer les absents'],
    ['Win rate', 'Mensuel', '40-60 %', 'Closing, objections'],
    ['Cycle de vente médian', 'Mensuel', '7 à 21 j visés', 'Lever les blocages'],
    ['OTIF', 'Mensuel', 'Baseline', 'Revue avec l’exploitation'],
    ['Complétude du prévisionnel', 'Hebdomadaire', '≥ 95 %', 'Sortie du prévisionnel'],
], [36, 17, 20, 27], size=24, pad='padding:10px 14px', style='flex:1;') + '''
<div style="width:660px;display:flex;flex-direction:column;gap:12px">
<img src="/_blob/23896dc16cb677697a898418b408bfda" alt="Courbe cumulée des nouveaux adhérents sur 12 mois, tableau de bord Planet’Connect" style="width:660px;height:203px;object-fit:contain;background:#FFFFFF;border-radius:12px">
<p style="font-size:24px;line-height:1.3;color:#3E5058">Nouveaux adhérents signés, cumul sur 12 mois : <b style="color:#14303B">~145 pour 120 visés</b>, rythme irrégulier</p>
<div style="display:flex;flex-direction:column;gap:6px;background:#FFFFFF;border-radius:12px;padding:16px 22px">
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">4,65/5</b> de satisfaction</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058"><b style="color:#14303B">4,87/5</b> de probabilité de recommander</p>
<p style="font-size:24px;line-height:1.3;color:#6A7B82">Enquête 2024, 23 réponses</p>
</div>
</div>
</div>
''' + box('LA REVUE MENSUELLE', '45 minutes : KPI · entonnoir · comptes · win/loss · décisions, avec un responsable et une date'),
'''Si on me demande d’où viennent les cibles : ce sont des objectifs de pilotage, étiquetés comme tels, parce que notre CRM n’historise que depuis 2025. Chaque indicateur a une fréquence, une cible et une action si l’écart se creuse. Là où je n’ai pas de base, j’écris « baseline 90 jours » plutôt que d’inventer un chiffre.

La courbe montre le constaté : environ 145 nouveaux adhérents signés sur douze mois, pour 120 visés, avec un rythme irrégulier, un pic en février-mars et des mois plus creux. L’objectif est tenu en cumul, pas chaque mois.

(4,87/5 est une probabilité de recommandation sur 23 réponses, pas un NPS. Ne pas calculer 227/262 : les 227 sont des adhérents récents, pas le KPI « actifs ». La marge contributive se suit par dossier, sans valeur affichée.)''', gap=26)

# B7 — prix rendu
S['b7'] = slide('b7', 'B7', 'PRIX ET ROI', 'Le prix rendu, sans maquillage : c’est le client final qui paie',
'''<div style="display:flex;gap:20px;align-items:stretch">
<div style="flex:1.2;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border-radius:12px;padding:22px 28px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">12 BOUTEILLES AU TEXAS</p>
<p style="font-size:24px;line-height:1.3;color:#6A7B82">300 € de vin, groupage DDP, grille officielle 2026</p>
<div style="display:flex;justify-content:space-between;font-size:24px"><p style="font-size:24px;color:#3E5058">Transport</p><p style="font-size:24px;color:#14303B;font-weight:600">210 €</p></div>
<div style="display:flex;justify-content:space-between"><p style="font-size:24px;color:#3E5058">Taxes estimées (exemple du playbook)</p><p style="font-size:24px;color:#14303B;font-weight:600">~30 €</p></div>
<div style="display:flex;justify-content:space-between"><p style="font-size:24px;color:#3E5058">Frais de dossier DDP</p><p style="font-size:24px;color:#14303B;font-weight:600">17 €</p></div>
<div style="display:flex;justify-content:space-between"><p style="font-size:24px;color:#3E5058">Assurance 3 %, en option</p><p style="font-size:24px;color:#14303B;font-weight:600">≈ 15 €</p></div>
<div style="display:flex;justify-content:space-between;border-top:2px solid #12475B;padding-top:10px"><p style="font-size:26px;color:#14303B;font-weight:700">Tout prépayé, ~21 jours</p><p style="''' + FONT_H + ''';font-size:40px;color:#12475B;font-weight:700;line-height:1">≈ 270 €</p></div>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#FFFFFF;border-radius:12px;padding:22px 28px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#12475B">À LA BOUTEILLE</p>
<p style="''' + FONT_H + ''';font-size:64px;font-weight:700;line-height:1;color:#12475B">≈ 17,50 €</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058">de transport par bouteille livrée</p>
<p style="font-size:24px;line-height:1.3;color:#3E5058">Face à 50 à 100 € d’excédent de bagages, sans assurance contre la casse, dans une valise</p>
</div>
<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:#12475B;border-radius:12px;padding:22px 28px">
<p style="''' + FONT_P + ''';font-size:24px;font-weight:600;letter-spacing:3px;color:#E8D3A6">LE ROI DU CAVEAU</p>
<p style="font-size:24px;line-height:1.35;color:#D7E5EA">30 visiteurs étrangers/sem. × 1 sur 3 × 300 € × 20 semaines</p>
<p style="''' + FONT_H + ''';font-size:44px;font-weight:700;line-height:1.05;color:#F4F8F9">60 000 €</p>
<p style="font-size:24px;line-height:1.3;color:#D7E5EA">de ventes potentielles ; 15 000 € à 25 %</p>
<p style="font-size:24px;line-height:1.3;color:#9EC5CE">Pour 110 € HT de cartons</p>
</div>
</div>
''' + box('LA RÈGLE', 'Le simulateur fait foi, jamais un taux cité de mémoire · droits US de 10 % depuis février 2026 · pas de remise sans contrepartie ni validation de la direction'),
'''Si on me dit que c’est trop cher : 43 % de nos clients jugent le prix moyennement compétitif, je ne le cache pas. Je ramène le prix à ce que paie vraiment le client final : pour douze bouteilles au Texas, environ 270 euros avec les taxes estimées, le dossier et l’assurance en option, soit environ 17,50 euros de transport par bouteille livrée. Dans une valise, c’est 50 à 100 euros d’excédent bagage, et aucune assurance si ça casse.

Et pour le domaine, le calcul se fait avec ses propres chiffres : trente visiteurs étrangers par semaine, un sur trois, 300 euros, vingt semaines, soit 60 000 euros de ventes potentielles, et 15 000 euros si 25 % seulement se concrétisent, pour 110 euros de cartons.

(Le simulateur fait foi. Droits US à 10 % depuis février 2026, après 15 % d’août 2025 à février 2026 : vérifier la veille. L’assurance est une option, jamais « incluse ». Remise : jamais sans contrepartie ni validation de la direction ; on négocie le périmètre avant le prix. Refaire la simulation Texas la veille : les taxes dépendent de la valeur déclarée.)''', gap=26)

for k, v in S.items():
    with open(os.path.join(OUT, f'{k}.html'), 'w') as f:
        f.write(v)
print('ok', list(S))
