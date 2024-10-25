import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd());
  const API_URL = `${env.VITE_API_URL}/api/v1`;

  return {
    server: {
      proxy: {
        '/proxy/api/capitolai': {
          target: API_URL,
          changeOrigin: true,
          rewrite: (path) => path.replace(/^\/proxy\/api\/capitolai/, ''),
        },
      },
    },
    plugins: [vue()],
  }}
)
