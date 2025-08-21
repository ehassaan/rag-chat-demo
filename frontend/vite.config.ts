import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { createVuetify } from 'vuetify';
import { resolve } from 'path';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    createVuetify()
  ],
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  server: {
    port: 3000,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: false,
        secure: false,
      }
    }
  },
  build: {
    outDir: 'dist',
  },
});