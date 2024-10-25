// scripts/generate-vercel-json.js
import fs from 'fs';

const template = fs.readFileSync('vercel.template.json', 'utf-8');
console.log("🚀 ~ template:", template)
const VITE_API_URL = process.env.VITE_API_URL;

console.log("🚀 ~ VITE_API_URL:", VITE_API_URL)

if (!VITE_API_URL) {
  throw new Error('VITE_API_URL it is not defined');
}

const content = template.replace('${VITE_API_URL}', VITE_API_URL);
console.log("🚀 ~ content:", content)

fs.writeFileSync('vercel.json', content);
console.log('✅ vercel.json generated successfully');
