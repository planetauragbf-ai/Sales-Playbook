// Lit la taille d'un PNG (IHDR) sans dépendance
const fs = require('fs');
function PNG(p) {
  const b = fs.readFileSync(p);
  return [b.readUInt32BE(16), b.readUInt32BE(20)];
}
module.exports = { PNG };
