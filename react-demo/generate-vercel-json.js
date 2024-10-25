const fs = require('fs');

const template = fs.readFileSync('vercel.template.json', 'utf-8');
const VITE_API_URL = process.env.VITE_API_URL;

if (!VITE_API_URL) {
 throw new Error('VITE_API_URL is not defined');
}

const content = template.replace('${VITE_API_URL}', VITE_API_URL);

fs.writeFileSync('vercel.json', content);

console.log(':marca_de_verificación_blanca: vercel.json generated successfully');
