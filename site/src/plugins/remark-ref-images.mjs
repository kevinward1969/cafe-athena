import { visit } from 'unist-util-visit';

const REF_PATTERN = /^\[ref:(\d{2}-\d{2}[a-z])\s*\|\s*([^\]]+)\]$/;

export function remarkRefImages() {
  return (tree) => {
    visit(tree, 'paragraph', (node, index, parent) => {
      if (!parent || index === null) return;
      if (node.children.length !== 1 || node.children[0].type !== 'text') return;

      const match = node.children[0].value.trim().match(REF_PATTERN);
      if (!match) return;

      const [, imageId, caption] = match;
      const trimmedCaption = caption.trim();

      parent.children[index] = {
        type: 'html',
        value: `<figure class="ref-image">
  <img src="/images/${imageId}.webp" alt="${trimmedCaption}" loading="lazy" />
  <figcaption>${trimmedCaption}</figcaption>
</figure>`,
      };
    });
  };
}
