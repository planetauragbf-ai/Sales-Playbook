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
    thumbs = (thumb(PG_PERSONA, 'Page réelle du playbook : fiche persona du vigneron-propriétaire', 'Persona', 128, 136)
              + thumb(PG_SCRIPTS, 'Page réelle du playbook : script d’appel à froid pour un caveau, chapitre 10', 'Script', 128, 136)
              + thumb(PG_OBJ, 'Page réelle du playbook : objections en format court et checklists, annexe B', 'Objections', 128, 136))
    made = ''.join(f'<p style="font-size:24px;color:{ENCRE};background:#E8F3F5;border-radius:999px;padding:4px 14px;white-space:nowrap">{t}</p>'
                   for t in ['Scripts et e-mails', 'Banque SPIN', '26 objections', 'Calcul du ROI', 'Checklists', 'Plan 30-60-90'])
    doubt = ''.join(f'<p style="font-size:24px;line-height:1.3;color:{GRIS}"><i>{q}</i> <b><span style="color:{OR}">→</span></b> <b><span style="color:{ENCRE}">{a}</span></b></p>'
                    for q, a in [('« Combien ça coûte ? »', 'le simulateur'), ('« Et si ça casse ? »', 'le carton ISTA 3A'), ('« Ça marche ? »', '4,8/5, 296 avis Google (09/2026)')])
    left = f"""<div style="width:620px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{label('Créé dans le playbook', SARCF, ls=2)}{ctag('MA CONTRIBUTION')}</div>
<div style="display:flex;gap:16px;align-items:flex-start">{thumbs}</div>
<div style="display:flex;flex-wrap:wrap;gap:8px">{made}</div>
<div style="flex:1"></div>
<div style="display:flex;align-items:center;gap:12px">{label('Existant, mobilisé', GRISD, ls=2)}{ctag('EXISTANT')}</div>
{doubt}
</div>"""
    ch = [('sept. 2026', 'Nettoyage CRM, listes A/B/C', 'Emma, Adam', '24 h', '0 €', '≥ 95 % des comptes prioritaires exploitables'),
          ('oct. 2026', 'One-pager par ICP, landing page', 'Emma, Adam', '36 h', '600 €', 'supports validés par la direction'),
          ('nov. 2026', '3 séquences Brevo, reporting HubSpot', 'Emma', '20 h', '200 €', 'arrêt automatique sur réponse testé')]
    cards = ''
    for i, (m, n, who, h, bud, crit) in enumerate(ch, 1):
        cards += f"""<div style="flex:1;background:#FFFFFF;border:1px solid {FILET};border-top:8px solid {PETROLE};border-radius:16px;padding:14px 18px;display:flex;flex-direction:column;gap:8px">
<div style="display:flex;align-items:baseline;justify-content:space-between"><p style="font-family:{L};font-size:26px;font-weight:700;color:{PETROLE}">{i} · {m}</p></div>
<p style="font-size:26px;font-weight:700;line-height:1.2;color:{ENCRE}">{n}</p>
<p style="font-size:24px;color:{GRIS}">{who} · {h}</p>
{num(bud, 48, ORF)}
<p style="font-size:24px;line-height:1.25;color:{GRIS}"><b><span style="color:{ENCRE}">Critère</span></b> : {crit}</p>
<div style="flex:1"></div></div>"""
    right = f"""<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{label('À déployer : trois chantiers d’abord', PETROLE, ls=2)}{ctag('À DÉPLOYER')}</div>
<div style="flex:1;display:flex;gap:16px">{cards}</div>
<p style="font-size:24px;line-height:1.3;color:{GRIS}"><b><span style="color:{ENCRE}">Ensuite</span></b> (secours B13) : tests LinkedIn 900 € · webinaire 300 € · deux salons 1 000 € · vidéo et études de cas après validation.</p>
</div>"""
    inner = f"""{header3('Piloter · Partie 12 · Ressources', 'Ce que j’ai créé, ce qui reste à déployer', PETROLE, tags=['MA CONTRIBUTION', 'À DÉPLOYER'])}
<div style="flex:1;display:flex;gap:44px">{left}{right}</div>
{why3('4 ressources sur 17 manquent ; la donnée du CRM est incomplète.', 'La donnée, puis les supports, puis l’automatisation : <b>800 €</b> sur 3 000 €.', 'Un critère de passage par chantier ; sinon, pas d’étape suivante.')}
{footer(16, 'Piloter')}"""
    return 'ressources', inner, dict(gap=14, sect=SECT_PILOTER)


def salesops():
    def sat(x, y, name, obj, tg):
        st = 'background:#E8F4F6;border:3px dashed ' + SARC if tg == 'MA CONTRIBUTION' else 'background:#FFFFFF;border:2px solid #B8C4C8'
        return (f'<div style="position:absolute;left:{x}px;top:{y}px;width:340px;height:150px;border-radius:14px;{st};padding:8px 16px 6px;display:flex;flex-direction:column;gap:4px">'
                f'<div style="display:flex;align-items:center;gap:10px"><p style="font-size:24px;font-weight:700;line-height:1.2;color:{ENCRE};white-space:nowrap">{name}</p></div>'
                f'{ctag(tg, "line-height:1.2")}<p style="font-size:24px;line-height:1.2;color:{GRIS}">{obj}</p></div>')
    hub = f'''<div style="position:relative;width:1000px;height:470px">
<svg style="position:absolute;left:0px;top:0px" width="1000" height="470" viewBox="0 0 1000 470"><defs><marker id="m" orient="auto" markerWidth="5" markerHeight="5" refX="2" refY="2" overflow="visible"><path d="M0 0 L4 2 L0 4 Z" fill="{ORANGE}"/></marker></defs>
<path d="M 340 75 L 415 150" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 585 150 L 662 92" stroke="{ORANGE}" stroke-width="4" stroke-dasharray="12 9" fill="none" marker-end="url(#m)"/>
<path d="M 340 235 L 375 235" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 625 235 L 660 235" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 340 395 L 415 320" stroke="#B8C4C8" stroke-width="4" fill="none"/>
<path d="M 585 320 L 660 395" stroke="{SARC}" stroke-width="4" stroke-dasharray="12 9" fill="none"/></svg>
{sat(0, 0, "Planet'Connect", 'exécuter et tracer chaque envoi', 'EXISTANT')}
{sat(660, 0, 'Brevo (existant)', 'câblage HubSpot, stop sur réponse : prévu en nov.', 'À DÉPLOYER')}
{sat(0, 160, 'Tableaux de bord', 'CA en temps réel, délais réels', 'EXISTANT')}
{sat(660, 160, 'Workspace + WhatsApp', 'documents officiels, messagerie adhérents', 'EXISTANT')}
{sat(0, 320, 'E-signature + Drive', 'documentation re-signée chaque année', 'EXISTANT')}
{sat(660, 320, 'Dictionnaire CRM', 'à ratifier : motifs de perte, hygiène', 'MA CONTRIBUTION')}
<div style="position:absolute;left:375px;top:110px;width:250px;height:250px;border-radius:50%;background:{NUIT};border:6px solid {SARC};display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px">
<p style="font-family:{T};font-size:44px;font-weight:700;color:#FFFFFF">HubSpot</p><p style="font-size:24px;color:{BRUME}">source de vérité</p>
<p style="font-size:24px;text-align:center;line-height:1.25;color:{BLEU}">contact loggé<br>&lt; 24 h</p></div>
</div>'''
    al = ''.join(f'''<div style="display:flex;gap:12px;align-items:flex-start"><div style="width:30px;height:30px;border-radius:50%;background:{c};display:flex;align-items:center;justify-content:center;flex:none"><p style="font-family:{L};font-size:24px;font-weight:700;color:#FFFFFF">{i}</p></div>
<p style="font-size:24px;line-height:1.3;color:{ENCRE}">{t}</p></div>''' for i, t, c in [
        (1, '<b>Même définition</b> : cadence dès PA-FIT 55', SARCF),
        (2, '<b>Même délai</b> : lead entrant rappelé &lt; 24 h', SARCF),
        (3, '<b>Le marketing nourrit</b> : nurture 45 j, campagnes de saison', ORF),
        (4, '<b>Le terrain remonte</b> : motifs de perte → objections', BORD)])
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
{why3('Des outils déjà là, sans règles communes : 448 prospects non qualifiés.', 'HubSpot source de vérité, un dictionnaire à ratifier, Brevo câblé dessus : chaque relance s’arrête à la réponse.', 'Pipeline complet à ≥ 95 % chaque lundi ; tout contact loggé sous 24 h.')}
{footer(17, 'Piloter')}'''
    return 'salesops', inner, dict(gap=20)


def onboarding():
    stairs = ''
    for h, d, s, t, c in [(205, 'J+30', 'CERTIFIÉ', 'offre, ICP, CRM · 1 simulation sans aide · top 5 objections', SARCF),
                          (235, 'J+60', 'AUTONOME', '5 découvertes observées, 3 propositions sans écart, 1 RDV obtenu seul', PETROLE),
                          (265, 'J+90', 'PILOTE', 'pipeline propre, analyse gagné/perdu, 1 amélioration du playbook', NUIT)]:
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
    cap = shot(DASH_NEW, 'Capture réelle du tableau de bord Planet’Connect : évolution des nouveaux adhérents du 24/09/2025 au 24/09/2026', 640, 186, 'Planet’Connect', fit='contain')
    const = ''.join(f'''<div style="flex:1;display:flex;flex-direction:column;gap:0px">{num(v, 34, SARCF)}<p style="font-size:24px;line-height:1.15;color:{GRIS}">{t}</p></div>'''
                    for v, t in [('~145', 'signés en 12 mois'), ('1,45 %', 'annulations'), ('89,8 %', 'envois assurés')])
    crm = f'''<div style="{CASE_BOX};border-radius:14px;padding:6px 16px;display:flex;align-items:center;gap:16px">
{label('Le cas, dans HubSpot', ORF, ls=1)}<p style="flex:1;font-size:24px;line-height:1.25;color:{ENCRE}"><b>Activé (6 sur 7)</b> · tiers B · santé <b><span style="color:#3A8A5C">verte</span></b> · prochaine action : <b>le commercial appelle à\u00a0J+30</b></p>{pill('ILLUSTRATIF')}</div>'''
    left = f'''<div style="width:640px;display:flex;flex-direction:column;gap:12px">
<div style="display:flex;align-items:center;gap:12px">{pill('CONSTATÉ')}<p style="font-size:24px;color:{GRISD}">point zéro, 24/09/2026</p></div>
{cap}
<div style="display:flex;gap:16px">{const}</div>
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
</div>'''
    inner = f'''{head_case(header3('Piloter · Partie 14 · Indicateurs', 'Mesuré ou espéré ? Chaque indicateur déclenche une action', PETROLE, tags=['EXISTANT', 'MA CONTRIBUTION', 'À MESURER']), 'Suivre')}
<div style="flex:1;display:flex;gap:36px">{left}{right}</div>
{crm}
{why3('~145 signatures en 12 mois ; conversions et activation jamais mesurées.', 'Point zéro au 24/09/2026 ; revue mensuelle proposée, close par une décision.', 'Première lecture fin décembre 2026, puis chaque trimestre.')}
{footer(19, 'Piloter')}'''
    return 'kpi', inner, dict(gap=12)


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
{col('Mon apport', BLEU, ['<b>Analysé</b> : top 10, 70 contacts, 24 sources', '<b>Construit</b> : 18 chapitres, 24 annexes', '<b>Proposé</b> : règles CRM, rituels, câblage', '<b>J’accompagne</b> : mises à jour, formation'])}
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
