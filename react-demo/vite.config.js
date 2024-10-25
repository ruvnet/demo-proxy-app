import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '')
  const API_URL = `${env.VITE_API_URL}/api/v1`;
  const isDev = mode === 'development'

  console.log("🚀 ~ defineConfig ~ API_URL:", API_URL)
  
  return {
    server: {
      proxy: {
        '/proxy/api/capitolai': {
          target: API_URL,
          changeOrigin: isDev,
          secure: !isDev,
          rewrite: (path) => path.replace(/^\/proxy\/api\/capitolai/, ''),
        },
      },
    },
    plugins: [react()],
  }}
)
