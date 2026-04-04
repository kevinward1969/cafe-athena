// @ts-check
import { defineConfig } from 'astro/config';
import { remarkRefImages } from './src/plugins/remark-ref-images.mjs';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  site: 'https://cookbook.kevinward.com',
  markdown: {
    shikiConfig: {
      theme: 'github-dark',
    },
    remarkPlugins: [remarkRefImages],
  },
  vite: {
    css: {
      preprocessorOptions: {},
    },

    plugins: [tailwindcss()],
  },
});