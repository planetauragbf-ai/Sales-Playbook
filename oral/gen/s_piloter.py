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


def ressources():
    thumbs = (thumb(PG_PERSONA, 'Page réelle du playbook : fiche persona du vigneron-propriétaire', 'Persona')
              + thumb(PG_SCRIPTS, 'Page réelle du playbook : script d’appel à froid pour un caveau, chapitre 10', 'Script')
              + thumb(PG_OBJ, 'Page réelle du playbook : objections en format court et checklists, annexe B', 'Objections')
              + thumb(PG_ROAD, 'Page réelle du playbook : feuille de route commerciale budgétée', 'Feuille de route'))
    doubt = ''.join(f'''<div style="display:flex;align-items:baseline;gap:12px;border-bottom:1px solid {FILET};padding:5px 0px">
<p style="width:330px;font-family:{T};font-style:italic;font-size:26px;color:{ENCRE}">{q}</p><p style="flex:1;font-size:24px;color:{GRIS}">{a}</p></div>'''
                    for q, a in [('« Combien ça coûte ? »', 'le simulateur, sur SES vins'), ('« Et si ça casse ? »', 'le carton ISTA 3A, sur la table'),
                                 ('« Ça marche vraiment ? »', '4,8/5, 296 avis Google (sept. 2026)')])
    top = f'''<div style="display:flex;gap:40px">
<div style="display:flex;flex-direction:column;gap:8px">{label('Livrés : de vraies pages du playbook', SARCF, ls=1)}<div style="display:flex;gap:14px">{thumbs}</div></div>
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><div style="display:flex;align-items:center;gap:12px">{label('À chaque doute, une preuve montrée', SARCF, ls=1)}{ctag('EXISTANT')}</div>{doubt}
<p style="font-size:24px;line-height:1.3;color:{ENCRE};padding-top:4px"><b>17 ressources</b> : 13 validées, <b>4 à créer</b> (vidéo démo, one-pager par ICP, études de cas autorisées, webinaire)</p></div>
</div>'''
    months = ['sept.', 'oct.', 'nov.', 'déc.', 'janv.', 'févr.', 'mars', 'avr.', 'mai', 'juin', 'juil.']
    MW = 72
    TW = MW * 11
    LW, HW, BW = 490, 100, 120
    mh = ''.join(f'<p style="position:absolute;left:{i * MW}px;top:0px;width:{MW}px;text-align:center;font-size:24px;color:{GRISD}">{m}</p>' for i, m in enumerate(months))
    th = lambda t, w, al='left': f'<p style="width:{w}px;text-align:{al};font-family:{L};font-size:24px;font-weight:600;color:{GRISD}">{t}</p>'
    head = (f'<div style="display:flex;align-items:center;gap:20px">{th("FEUILLE DE ROUTE 2026 → 2027", LW).replace(GRISD, PETROLE)}'
            f'<div style="position:relative;width:{TW}px;height:32px">{mh}</div>{th("Temps", HW, "right")}{th("Budget", BW, "right")}</div>')
    chantiers = [('Nettoyage CRM', 'Emma, Adam', 0, 1, '≥ 95 % des comptes prioritaires exploitables', '24 h', '0 €'),
                 ('One-pagers, landing page', 'Emma, Adam', 1, 1, 'supports validés par la direction', '36 h', '600 €'),
                 ('Séquences Brevo + reporting', 'Emma', 2, 1, 'arrêt automatique sur réponse testé', '20 h', '200 €'),
                 ('Tests LinkedIn, 3 clusters', 'Adam', 2, 7, 'coût par prospect qualifié comparé', '3 h/sem.', '900 €'),
                 ('Webinaire export', 'Emma + expert', 4, 1, '10 inscrits ICP, 3 diagnostics', '20 h', '300 €'),
                 ('Deux salons en visiteur', 'Adam, Emma', 4, 7, '8 RDV qualifiés par salon', '24 h', '1 000 €')]
    rows = ''
    for n, who, m0, ln_, crit, tm, bud in chantiers:
        x, w = m0 * MW + 3, ln_ * MW - 6
        inside = ln_ >= 5
        if inside:
            txt = f'<p style="position:absolute;left:{x + 14}px;top:4px;width:{w - 20}px;font-size:24px;color:#FFFFFF;white-space:nowrap">{crit}</p>'
        else:
            txt = f'<p style="position:absolute;left:{x + w + 12}px;top:4px;width:{TW - x - w - 12}px;font-size:24px;color:{GRIS};white-space:nowrap">{crit}</p>'
        rows += (f'<div style="display:flex;align-items:center;gap:20px;border-top:1px solid {FILET};padding:2px 0px">'
                 f'<p style="width:{LW}px;font-size:24px;line-height:1.2;color:{ENCRE};white-space:nowrap"><b>{n}</b> <span style="color:{GRISD}">· {who}</span></p>'
                 f'<div style="position:relative;width:{TW}px;height:38px"><div style="position:absolute;left:{x}px;top:4px;width:{w}px;height:30px;border-radius:8px;background:{PETROLE if inside else SARC}"></div>{txt}</div>'
                 f'<p style="width:{HW}px;text-align:right;font-size:24px;color:{GRIS}">{tm}</p>'
                 f'<p style="width:{BW}px;text-align:right;font-family:{L};font-size:26px;font-weight:600;color:{PETROLE}">{bud}</p></div>')
    total = (f'<div style="display:flex;align-items:center;gap:20px;border-top:2px solid {PETROLE};padding-top:6px">'
             f'<p style="width:{LW + 20 + TW}px;font-size:24px;color:{ENCRE}"><b>Total</b> · pas de critère atteint, pas d’étape suivante <span style="color:{GRISD}">(temps : calcul)</span></p>'
             f'<p style="width:{HW}px;text-align:right;font-size:24px;font-weight:700;color:{ENCRE};white-space:nowrap">≈ 200 h</p>'
             f'<p style="width:{BW}px;text-align:right;font-family:{L};font-size:28px;font-weight:700;color:{PETROLE};white-space:nowrap">3 000 €</p></div>')
    inner = f'''{header3('Piloter · Partie 12 · Ressources', 'Une preuve par doute, un chantier par manque', PETROLE, tags=['MA CONTRIBUTION', 'À DÉPLOYER'])}
{top}
<div style="flex:1"></div>
<div style="display:flex;flex-direction:column">{head}{rows}{total}</div>
{footer(16, 'Piloter')}'''
    return 'ressources', inner, dict(gap=14, sect=SECT_PILOTER)


def salesops():
    def sat(x, y, name, obj, tg):
        st = 'background:#E8F4F6;border:3px dashed ' + SARC if tg == 'MA CONTRIBUTION' else 'background:#FFFFFF;border:2px solid #B8C4C8'
        return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:340px;height:156px;border-radius:14px;{st};padding:10px 16px;display:flex;flex-direction:column;gap:4px">'
                f'<div style="display:flex;align-items:center;gap:10px"><p style="font-size:24px;font-weight:700;color:{ENCRE};white-space:nowrap">{name}</p></div>'
                f'{ctag(tg)}<p style="font-size:24px;line-height:1.2;color:{GRIS}">{obj}</p></div>')
    hub = f'''<div style="position:relative;width:1000px;height:560px">
<svg style="position:absolute;left:0px;top:0px" width="1000" height="560" viewBox="0 0 1000 560"><defs><marker id="m" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="{ORANGE}"/></marker></defs>
<path d="M 340 78 L 410 190" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 590 190 L 664 100" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="12 9" fill="none" marker-end="url(#m)"/>
<path d="M 340 280 L 365 280" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 635 280 L 660 280" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 340 482 L 410 370" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 590 370 L 660 482" stroke="{SARC}" stroke-width="4" stroke-dasharray="12 9" fill="none"/></svg>
{sat(0, 0, "Planet'Connect", 'exécuter et tracer chaque envoi', 'EXISTANT')}
{sat(660, 0, 'Brevo (existant)', 'câblage HubSpot, stop sur réponse : prévu en nov.', 'À DÉPLOYER')}
{sat(0, 202, 'Tableaux de bord', 'CA en temps réel, délais réels', 'EXISTANT')}
{sat(660, 202, 'Workspace + WhatsApp', 'documents officiels, messagerie adhérents', 'EXISTANT')}
{sat(0, 404, 'E-signature + Drive', 'documentation re-signée chaque année', 'EXISTANT')}
{sat(660, 404, 'Dictionnaire CRM', 'à ratifier : motifs de perte, hygiène', 'MA CONTRIBUTION')}
<div style="position:absolute;left:365px;top:145px;width:270px;height:270px;border-radius:50%;background:{NUIT};border:6px solid {SARC};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
<p style="font-family:{T};font-size:44px;font-weight:700;color:#FFFFFF">HubSpot</p><p style="font-size:24px;color:{BRUME}">source de vérité</p>
<p style="font-size:24px;text-align:center;line-height:1.25;color:{BLEU}">contact loggé<br>&lt; 24 h</p></div>
</div>'''
    al = ''.join(f'''<div style="display:flex;gap:12px;align-items:flex-start"><div style="width:30px;height:30px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{i}</p></div>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}">{t}</p></div>''' for i, t, c in [
        (1, '<b>Une même définition</b> : un compte entre en cadence dès PA-FIT 55', SARCF),
        (2, '<b>Un délai commun</b> : le lead entrant est rappelé en moins de 24 h', SARCF),
        (3, '<b>Le marketing nourrit</b> : nurture 45 jours, campagnes de saison, séquences Brevo dès le câblage', ORF),
        (4, '<b>Le terrain remonte</b> : les motifs de perte réordonneront objections et contenus', BORD)])
    rit = ''.join(f'<p style="font-size:24px;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:999px;padding:4px 14px;white-space:nowrap"><b>{a}</b> {b}</p>'
                  for a, b in [('Jour', '10 min'), ('Semaine', '45 + 30 min'), ('Mois', '45 min'), ('Trimestre', '90 min')])
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{label('Marketing et ventes', PETROLE, ls=2)}{ctag('À DÉPLOYER')}</div>
{al}
<div style="flex:1"></div>
<div style="display:flex;align-items:center;gap:14px">{label('Rituels', PETROLE, ls=2)}{pill('PROPOSÉ', label='PROPOSÉS, À RATIFIER')}</div>
<div style="display:flex;flex-wrap:wrap;gap:8px">{rit}</div>
</div>'''
    inner = f'''{header3('Piloter · Partie 13 · Sales Operations', 'Une donnée, un propriétaire, une décision', PETROLE, tags=['EXISTANT', 'MA CONTRIBUTION', 'À DÉPLOYER'])}
<div style="flex:1;display:flex;gap:52px">
<div style="width:1000px;display:flex;flex-direction:column">{hub}</div>
{right}</div>
{footer(17, 'Piloter')}'''
    return 'salesops', inner, dict(gap=28)


def onboarding():
    stairs = ''
    for h, d, s, t, c in [(205, 'J+30', 'CERTIFIÉ', 'offre, ICP, CRM · 1 simulation sans aide · top 5 objections', SARC),
                          (235, 'J+60', 'AUTONOME', '5 découvertes observées, 3 propositions sans écart, 1 RDV obtenu seul', SARCF),
                          (265, 'J+90', 'PILOTE', 'pipeline propre, analyse gagné/perdu, 1 amélioration du playbook', PETROLE)]:
        stairs += (f'<div style="flex:1;height:{h}px;background:{c};border-radius:12px 12px 0px 0px;padding:14px 18px;display:flex;flex-direction:column;gap:4px">'
                   f'{num(d, 40, "#FFFFFF")}'
                   f'<p style="font-family:{L};font-size:24px;font-weight:600;letter-spacing:1px;color:{CHAMP}">{s}</p>'
                   f'<p style="font-size:24px;line-height:1.25;color:#FFFFFF">{t}</p></div>')
    wk = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:4px;border-left:3px solid {SARC};padding-left:12px">
<p style="font-family:{L};font-size:24px;font-weight:700;color:{SARCF}">{a}</p><p style="font-size:24px;line-height:1.25;color:{ENCRE}">{b}</p></div>''' for a, b in [
        ('S1', '10 devis justes au simulateur'), ('S2', 'quiz grilles et incoterms ≥ 90 %'), ('S3', 'pipeline complet à ≥ 95 %'),
        ('S4', 'certification J+30 signée'), ('S8', '1er adhérent signé et activé')])
    who = ''.join(f'<p style="font-size:24px;color:{ENCRE};background:#FFFFFF;border:1px solid {FILET};border-radius:999px;padding:4px 14px;white-space:nowrap"><b>{a}</b> · {b}</p>'
                  for a, b in [('Emma', 'simulateur'), ('Adam', 'appels en binôme'), ('Vincent, Frantz', 'entrepôt'), ('Floriane', 'certification')])
    left = thumb(PG_ONB, 'Page réelle du playbook : annexe U, le parcours d’onboarding jour par jour', 'Annexe U : le parcours, jour par jour', 300, 424)
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:18px">
<div style="display:flex;gap:12px;align-items:flex-end">{stairs}</div>
<div style="display:flex;gap:14px">{wk}</div>
<div style="display:flex;flex-direction:column;gap:8px">{label('Qui le forme', PETROLE, ls=2)}<div style="display:flex;gap:10px">{who}</div></div>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{ENCRE}">Socle à maîtriser avant J+30</span></b> : six chapitres, six règles d’or, la fiche réflexe. Le reste se consulte, au moment utile.</p>
</div>'''
    inner = f'''{header3('Piloter · Partie 13 · Onboarding', 'Un parcours pour être opérationnel en 90 jours', PETROLE, tags=['MA CONTRIBUTION', 'À MESURER'])}
<div style="flex:1;display:flex;gap:44px">{left}{right}</div>
{decision('« On observe avant de faire, on fait accompagné avant de faire seul. » Parcours livré, pas encore testé sur un recrutement : c’est sa première mesure.', label='LA RÈGLE')}
{footer(18, 'Piloter')}'''
    return 'onboarding', inner, dict(gap=18)


def kpi():
    cap = shot(DASH_NEW, 'Capture réelle du tableau de bord Planet’Connect : évolution des nouveaux adhérents du 24/09/2025 au 24/09/2026', 640, 197, 'Planet’Connect', fit='contain')
    const = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:0px">{num(v, 34, SARCF)}<p style="font-size:24px;line-height:1.15;color:{GRIS}">{t}</p></div>'''
                    for v, t in [('~145', 'signés / 120 visés'), ('1,45 %', 'annulations'), ('89,8 %', 'envois assurés')])
    crm = f'''<div style="{CASE_BOX};border-radius:14px;padding:10px 16px;display:flex;flex-direction:column;gap:4px">
<div style="display:flex;align-items:center;gap:12px">{label('Le cas, dans HubSpot', ORF, ls=1)}<div style="flex:1"></div>{pill('ILLUSTRATIF')}</div>
<p style="font-size:24px;line-height:1.25;color:{ENCRE}">Pipeline : <b>Activé (6 sur 7)</b> · tiers B · santé <b><span style="color:#3A8A5C">verte</span></b>, incident clos</p>
<p style="font-size:24px;line-height:1.25;color:{ENCRE}">Prochaine action : <b>Adam appelle à\u00a0J+30</b>\u00a0(recommandation)</p></div>'''
    left = f'''<div style="width:640px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{pill('CONSTATÉ')}<p style="font-size:24px;color:{GRISD}">point zéro, 24/09/2026</p></div>
{cap}
<div style="display:flex;gap:16px">{const}</div>
{crm}
</div>'''
    cards = [('Activation à J+30', '≥ 70 %', '1er envoi sous 30 j / signés', 'CRM · mensuel · commercial', 'sous 50 % : revoir l’onboarding'),
             ('RDV → proposition', '≥ 70 %', 'qualité de la découverte', 'HubSpot · mensuel · commercial', 'en dessous : retravailler le SPIN'),
             ('Adhérents actifs', '&gt; 60 %', '≥ 1 envoi sur 90 j / parc', 'Planet’Connect · mensuel · commercial', 'sinon : campagne réveil'),
             ('Taux de gain', '40-60 %', 'gagnées / clôturées', 'HubSpot · mensuel · direction', 'sinon : closing et objections')]
    cc = ''
    for n, tgt, f, src, act in cards:
        cc += f'''<div style="background:#FFFFFF;border:1px solid {FILET};border-top:6px solid {BORD};border-radius:12px;padding:8px 16px;display:flex;flex-direction:column;gap:2px">
<div style="display:flex;align-items:baseline;justify-content:space-between"><p style="font-family:{L};font-size:24px;font-weight:700;color:{ENCRE}">{n}</p>{num(tgt, 32, BORD)}</div>
<p style="font-size:24px;line-height:1.2;color:{GRIS}">{f}</p>
<p style="font-size:24px;line-height:1.2;color:{GRISD}">{src}</p>
<p style="font-size:24px;line-height:1.2;color:{ENCRE}"><b>→</b> {act}</p></div>'''
    right = f'''<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{pill('OBJECTIF')}<p style="font-size:24px;color:{GRISD}">pas encore mesuré : source · fréquence · responsable</p></div>
<div style="display:grid;grid-template-columns:repeat(2, 1fr);gap:12px">{cc}</div>
<div style="flex:1"></div>
{decision('Revue mensuelle proposée, 45 min : une décision datée, un propriétaire. Première lecture avant / après : fin décembre 2026.', label='LA REVUE')}
</div>'''
    inner = f'''{head_case(header3('Piloter · Partie 14 · Indicateurs', 'Mesuré ou espéré ? Chaque indicateur déclenche une action', PETROLE, tags=['EXISTANT', 'MA CONTRIBUTION', 'À MESURER']), 'Suivre')}
<div style="flex:1;display:flex;gap:36px">{left}{right}</div>
{footer(19, 'Piloter')}'''
    return 'kpi', inner, dict(gap=16)


def conclusion():
    band = f'''{bottles(24, width=1664, bw=40, bh=120)}
<div style="display:flex;align-items:center;gap:40px">
<p style="font-family:{T};font-size:60px;font-weight:700;line-height:1.05;color:#FFFFFF;white-space:nowrap">Ils repartent les mains libres.</p>
<p style="flex:1;font-size:26px;line-height:1.3;color:{BRUME}">24 bouteilles · <b><span style="color:{CHAMP}">360 € de transport HT</span></b> + taxes estimées et 17 € de dossier, réglés d’avance · assurance en option</p>
</div>'''

    def col(t, c, items):
        li = ''.join(f'<p style="font-size:26px;line-height:1.3;color:{CLAIR}">{i}</p>' for i in items)
        return (f'<div style="flex:1;border-top:4px solid {c};padding-top:10px;display:flex;flex-direction:column;gap:8px">'
                f'{label(t, c, ls=2)}{li}</div>')
    cols = f'''<div style="display:flex;gap:40px">
{col('La réponse', CHAMP, ['Une méthode <b>reproductible et mesurable</b>', '<b>Recruter</b> : 5 ICP, un score, une cadence', '<b>Activer</b> : la vente finit au 1er envoi', '<b>Transmettre</b> : 90 jours, des KPI à statut'])}
{col('Mon apport', BLEU, ['<b>Analysé</b> : top 10, 70 contacts, 24 sources', '<b>Construit</b> : 18 chapitres, 24 annexes', '<b>Proposé</b> : règles CRM, rituels, câblage', '<b>Accompagné</b> : formation, mise à jour'])}
{col('Limites et suite', '#E2A39A', ['<b>Effet pas encore mesuré</b> : lecture fin déc.', 'Personas : entretiens au T1 2027', 'Parcours à tester au 1er recrutement', '<b>Difficulté</b> : chiffres divergents → une source datée', '<b>Ouverture</b> : diversifier, UK, UE, Japon'])}
</div>'''
    inner = f'''{band}
<div style="height:2px;background:#2A5765"></div>
{cols}
<div style="flex:1"></div>
<div style="display:flex;align-items:center;gap:14px;flex-wrap:wrap">{label('Bénéfices attendus', CHAMP, ls=2)}<div style="width:6px"></div>{pill('OBJECTIF', 'letter-spacing:0px', '≥ 70 % des signés activés à J+30')}{pill('OBJECTIF', 'letter-spacing:0px', 'Un commercial certifié à J+30')}{pill('POINT ZÉRO', 'letter-spacing:0px;background:transparent;color:#FFFFFF;border-color:#FFFFFF', 'Part USA suivie chaque trimestre')}</div>
<div style="flex:1"></div>
<div style="display:flex;align-items:flex-end;gap:40px">
<p style="flex:1;font-family:{T};font-style:italic;font-size:34px;line-height:1.25;color:{CHAMP}">Le prospect n’achète pas seulement du transport : il cherche à réduire son risque.</p>
<div style="display:flex;align-items:center;gap:18px"><img src="{LOGO_MARK_W}" alt="Logo Planet Aura" style="width:54px;height:72px;object-fit:contain">
<div style="display:flex;flex-direction:column;gap:2px"><p style="font-family:{T};font-size:48px;font-weight:700;line-height:1;color:#FFFFFF">Merci.</p><p style="font-size:26px;color:{BRUME}">Place à vos questions</p></div></div>
</div>'''
    return 'conclusion', inner, dict(bg=NUIT, color=CLAIR, pad='96px 128px 96px', gap=22,
                                     sect="Synthèse et ouverture : réponse à la problématique, apport, limites, retour à l'accroche")
