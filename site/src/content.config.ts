import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const recipes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/recipes' }),
  schema: z.object({
    title: z.string(),
    index: z.string(),
    chapter: z.number(),
    chapterName: z.string(),
    type: z.enum(['recipe', 'technique']),
    heroImage: z.string().optional(),
    referenceImages: z.array(z.string()).optional().default([]),
    subtitle: z.string().optional(),
    keywords: z.array(z.string()).optional().default([]),
    cuisine: z.string().optional().default(''),
    style: z.string().optional().default(''),
    dietary: z.string().optional().default(''),
  }),
});

export const collections = { recipes };
