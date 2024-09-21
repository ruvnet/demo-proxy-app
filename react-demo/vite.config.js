import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  server: {
    proxy: {
      '/proxy/api/capitolai': {
        target: 'http://localhost:8000/api/v1',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/proxy\/api\/capitolai/, ''),
    },
    },
  },
  plugins: [react()],
})
