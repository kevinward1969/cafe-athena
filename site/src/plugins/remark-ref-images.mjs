import { visit } from 'unist-util-visit';

const REF_PATTERN  = /^\[ref:(\d{2}-\d{2}[a-z])\s*\|\s*([^\]]+)\]$/;
const EXPO_PATTERN = /^\[expo:([^\]]+\.webp)\s*\|\s*([^\]]+)\]$/;

function makeFigure(src, caption) {
  return {
    type: 'html',
    value: `<figure class="ref-image">
  <img src="${src}" alt="${caption}" loading="lazy" />
  <figcaption>${caption}</figcaption>
</figure>`,
  };
}

export function remarkRefImages() {
  return (tree) => {
    visit(tree, 'paragraph', (node, index, parent) => {
      if (!parent || index === null) return;
      if (node.children.length !== 1 || node.children[0].type !== 'text') return;

      const text = node.children[0].value.trim();

      const refMatch = text.match(REF_PATTERN);
      if (refMatch) {
        const [, imageId, caption] = refMatch;
        parent.children[index] = makeFigure(`/images/${imageId}.webp`, caption.trim());
        return;
      }

      const expoMatch = text.match(EXPO_PATTERN);
      if (expoMatch) {
        const [, filename, caption] = expoMatch;
        parent.children[index] = makeFigure(`/images/${filename}`, caption.trim());
      }
    });
  };
}
