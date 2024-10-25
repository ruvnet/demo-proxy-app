// import { defineConfig, loadEnv } from 'vite'
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
// export default defineConfig(({ mode }) => {
export default defineConfig(() => {
  // const env = loadEnv(mode, process.cwd());
  const API_URL = 'http://a5c3b35c3017f43b293a28d0a9009202-106008128.us-east-1.elb.amazonaws.com';

  console.log("🚀 ~ defineConfig ~ API_URL:", API_URL)

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
    plugins: [react()],
  }}
)
