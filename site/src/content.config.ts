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
    family: z.string().optional().default(''),
    course: z.string().optional().default(''),
    dietary: z.string().optional().default(''),
  }),
});

const expo = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/expo' }),
  schema: z.object({
    title: z.string(),
    date: z.date(),
    publishDate: z.date().optional(),
    excerpt: z.string(),
    heroImage: z.string().optional(),
    relatedRecipes: z.array(z.string()).optional().default([]),
    category: z.enum([
      'Recipe Walkthroughs',
      'Meal Prep Walkthroughs',
      'Technique in Context',
      'Ingredient Spotlight',
      'Story & Tradition',
      'Plating & Presentation',
      'Menu & Service',
    ]).optional(),
    tags: z.array(z.string()).optional().default([]),
  }),
});

export const collections = { recipes, expo };
