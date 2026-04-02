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
    subtitle: z.string().optional(),
  }),
});

export const collections = { recipes };
