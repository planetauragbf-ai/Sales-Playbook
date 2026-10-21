// Lit la taille d'un PNG depuis son en-tête IHDR (width, height en pixels).
const fs = require('fs');
function PNG(file) {
  const b = fs.readFileSync(file);
  if (b.length < 24 || b.readUInt32BE(12) !== 0x49484452) throw new Error('PNG invalide : ' + file);
  return [b.readUInt32BE(16), b.readUInt32BE(20)];
}
module.exports = { PNG };
