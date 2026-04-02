import fs from 'fs';
const content = fs.readFileSync('src/content/recipes/01-01.md', 'utf8');
console.log(content.slice(0, 50));
