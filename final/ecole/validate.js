// Contrôle de ecole/anonymisation.json contre les fichiers ACTUELS, exactement comme build-emma.js :
// md lus bruts, fiches-emma.js via JSON.stringify(require()) avec échappement JSON ; application séquentielle.
const fs = require('fs'), path = require('path');
const S = path.join(__dirname, '..');
const A = '/home/user/Sales-Playbook/build/assets';
const ANON = JSON.parse(fs.readFileSync(path.join(__dirname, 'anonymisation.json'), 'utf8'));
const src = {};
const load = (f) => {
  if (src[f] !== undefined) return;
  if (f === 'fiches-emma.js') { delete require.cache[require.resolve(path.join(S, f))]; src[f] = JSON.stringify(require(path.join(S, f))); }
  else src[f] = fs.readFileSync(path.join(S, 'content-emma', f), 'utf8');
};
let ok = 0, bad = 0;
ANON.text.forEach((r, i) => {
  load(r.file);
  const js = r.file === 'fiches-emma.js';
  const enc = (t) => js ? JSON.stringify(t).slice(1, -1) : t;
  const n = src[r.file].split(enc(r.old)).length - 1;
  // compte aussi dans le fichier source brut (avant tout remplacement)
  const raw = js ? fs.readFileSync(path.join(S, r.file), 'utf8') : fs.readFileSync(path.join(S, 'content-emma', r.file), 'utf8');
  const nRaw = raw.split(r.old).length - 1;
  const pipesOk = (r.old.match(/\|/g) || []).length === (r.new.match(/\|/g) || []).length;
  const good = n === (r.count || 1) && nRaw === (r.count || 1) && pipesOk;
  good ? ok++ : bad++;
  console.log(`${good ? 'OK ' : 'ERR'} #${String(i + 1).padStart(2)} ${r.file.padEnd(15)} attendu ${r.count} · trouvé ${n} (brut ${nRaw})${pipesOk ? '' : ' · PIPES'} « ${r.old.slice(0, 55)} »`);
  src[r.file] = src[r.file].split(enc(r.old)).join(enc(r.new));
});
(ANON.images || []).forEach(im => {
  const a = fs.existsSync(path.join(A, im.asset)), b = fs.existsSync(path.join(A, im.redacted));
  (a && b) ? ok++ : bad++;
  console.log(`${a && b ? 'OK ' : 'ERR'} image ${im.asset} -> ${im.redacted}`);
});
// noms qui ne doivent plus apparaître dans le texte transformé
const FORBID = ['Planet Provence (n', 'Pommard', 'Ambacia', 'O Chateau', 'O Château', 'Penet', 'La Coste', 'Caves du Louvre', 'Citadelle', 'Ogier',
  'Croche', 'Mingot', 'Lafont', 'Mazirh', 'Bruneau', 'Arthus', 'Kuyper', 'Filaquier', 'Gonnet', 'Barroche', 'Dalmeran', 'Fleurus', 'Cavale',
  'Domaine de Marie', 'Henri IV', 'Vignobles Jade', 'Fontenille', 'Maison du Vouvray', 'Pol Couronne', 'références réelles'];
fs.readdirSync(path.join(S, 'content-emma')).filter(f => f.endsWith('.md')).forEach(f => load(f));
Object.entries(src).forEach(([f, t]) => FORBID.forEach(w => { if (t.includes(w)) { bad++; console.log(`ERR reste « ${w} » dans ${f}`); } }));
console.log(`\n${ok} contrôles OK, ${bad} erreur(s) - ${ANON.text.length} remplacements, ${(ANON.images || []).length} images`);
process.exit(bad ? 1 : 0);
