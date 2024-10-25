import fs from 'fs';
import path from 'path';
import dotenv from 'dotenv';

// Load environment variables from .env file
dotenv.config();

const rootDir = process.cwd();
const templatePath = path.join(rootDir, 'vercel.template.json');
const outputPath = path.join(rootDir, 'vercel.json');

try {
  const template = fs.readFileSync(templatePath, 'utf-8');
  const VITE_API_URL = process.env.VITE_API_URL;

  if (!VITE_API_URL) {
    throw new Error('VITE_API_URL no está definida');
  }

  const content = template.replace('${VITE_API_URL}', VITE_API_URL);

  fs.writeFileSync(outputPath, content);
  console.log('✅ vercel.json generado exitosamente en', outputPath);
} catch (error) {
  console.error('❌ Error al generar vercel.json:', error);
  process.exit(1);
}
