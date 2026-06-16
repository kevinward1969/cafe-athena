const SITE_URL = 'https://cookbook.kevinward.com';

function stripMarkdown(text: string): string {
  return text
    .replace(/\[ref:[^\]]*\]/g, '')
    .replace(/\*\*(.+?)\*\*/g, '$1')
    .replace(/\*(.+?)\*/g, '$1')
    .replace(/\s+/g, ' ')
    .trim();
}

function extractSection(body: string, heading: string): string | null {
  const re = new RegExp(`##\\s+${heading}[^\\n]*\\n([\\s\\S]*?)(?=\\n##\\s|$)`, 'i');
  const match = body.match(re);
  return match ? match[1] : null;
}

function extractIngredients(body: string): string[] {
  const section = extractSection(body, 'Ingredients');
  if (!section) return [];
  const items: string[] = [];
  for (const line of section.split('\n')) {
    const m = line.match(/^\s*[*-]\s+(.+)/);
    if (m) items.push(stripMarkdown(m[1]));
  }
  return items;
}

function extractInstructions(body: string): { name: string; text: string }[] {
  const section = extractSection(body, 'Method');
  if (!section) return [];
  const paragraphs = section.split(/\n\s*\n/).map((p) => p.trim()).filter(Boolean);
  return paragraphs.map((p) => {
    const nameMatch = p.match(/^\*\*(.+?)\*\*/);
    const name = nameMatch ? stripMarkdown(nameMatch[1]) : stripMarkdown(p).split(' ').slice(0, 6).join(' ');
    return { name, text: stripMarkdown(p) };
  });
}

function extractYield(body: string): string | undefined {
  const m = body.match(/\*\*Yield:\*\*\s*([^|\n]+)/);
  return m ? m[1].trim() : undefined;
}

function getFirstParagraph(body: string): string | undefined {
  for (const line of body.split('\n')) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith('#') || /^\*\*Yield:\*\*/.test(trimmed)) continue;
    return stripMarkdown(trimmed);
  }
  return undefined;
}

export interface RecipeSchemaInput {
  type: string;
  title: string;
  body: string;
  heroImage?: string;
  cuisine?: string;
  course?: string;
  keywords?: string[];
}

/**
 * Builds Recipe JSON-LD from the recipe's raw markdown body.
 * Returns null (no schema emitted) if required Google rich-result fields
 * (image, recipeIngredient, recipeInstructions) can't be parsed — emitting
 * partial schema fails validation, so we skip rather than emit broken markup.
 */
export function buildRecipeJsonLd(input: RecipeSchemaInput): Record<string, unknown> | null {
  if (input.type !== 'recipe') return null;
  if (!input.heroImage) return null;

  const recipeIngredient = extractIngredients(input.body);
  const recipeInstructions = extractInstructions(input.body);
  if (recipeIngredient.length === 0 || recipeInstructions.length === 0) return null;

  const schema: Record<string, unknown> = {
    '@context': 'https://schema.org',
    '@type': 'Recipe',
    name: input.title,
    image: `${SITE_URL}/images/${input.heroImage}`,
    author: { '@type': 'Organization', name: 'Café Athena' },
    recipeIngredient,
    recipeInstructions: recipeInstructions.map((step) => ({
      '@type': 'HowToStep',
      name: step.name,
      text: step.text,
    })),
  };

  const description = getFirstParagraph(input.body);
  if (description) schema.description = description;
  if (input.course) schema.recipeCategory = input.course;
  if (input.cuisine) schema.recipeCuisine = input.cuisine;
  const recipeYield = extractYield(input.body);
  if (recipeYield) schema.recipeYield = recipeYield;
  if (input.keywords && input.keywords.length > 0) schema.keywords = input.keywords.join(', ');

  return schema;
}

export interface BreadcrumbItem {
  name: string;
  url: string;
}

export function buildBreadcrumbJsonLd(items: BreadcrumbItem[]): Record<string, unknown> {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, idx) => ({
      '@type': 'ListItem',
      position: idx + 1,
      name: item.name,
      item: `${SITE_URL}${item.url}`,
    })),
  };
}
