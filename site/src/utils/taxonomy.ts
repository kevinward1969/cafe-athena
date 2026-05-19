export function familyToSlug(family: string): string {
  return family
    .toLowerCase()
    .normalize('NFD')
    .replace(/[̀-ͯ]/g, '')  // ragù → ragu, purée → puree
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9\s]/g, '')
    .trim()
    .replace(/\s+/g, '-');
}

export interface CategoryGroup {
  label: string;
  families: string[];
}

export const CATEGORY_GROUPS: CategoryGroup[] = [
  {
    label: 'Proteins & Seafood',
    families: ['Chicken', 'Beef', 'Pork', 'Duck', 'Ground & Formed', 'Finfish', 'Mollusc'],
  },
  {
    label: 'Starches',
    families: ['Pasta', 'Bread', 'Rice', 'Polenta', 'Gnocchi', 'Grain & Legume', 'Pasta Dough'],
  },
  {
    label: 'Sauces & Building Blocks',
    families: [
      'Mother Sauce', 'Stock', 'Derivative Sauce', 'Cold Blended Sauce',
      'Compound Butter', 'Emulsion', 'Ragù & Meat Sauce', 'Cream Sauce', 'Dipping Sauce',
    ],
  },
  {
    label: 'Pastry & Sweets',
    families: [
      'Pastry Dough', 'Cream & Filling', 'Brownie & Bar', 'Cookie',
      'Small Cake & Pastry', 'Caramel & Sugar', 'Posset & Panna Cotta',
    ],
  },
  {
    label: 'Vegetables & Garde Manger',
    families: [
      'Mushroom', 'Roasted & Grilled', 'Mash & Purée', 'Salad & Dressed',
      'Tuber', 'Stuffed', 'Steamed & Braised', 'Salad',
      'Mousse & Pâté', 'Cold Plate', 'Tartare & Raw', 'Preserved & Pickled',
      'Amuse-Bouche', 'Canapé',
    ],
  },
  {
    label: 'Technique & Science',
    families: [
      'Heat & Thermodynamics', 'Emulsification & Bonding', 'Fermentation',
      'Starch & Dough Science', 'Preservation & Transformation',
      'Hydrocolloids & Gels', 'Salinity & Seasoning',
      'Kitchen Management', 'Skills',
    ],
  },
  {
    label: 'Components & Larder',
    families: [
      'Platform & Vessel', 'Garnish & Component', 'Batter & Coating',
      'Herb Oil', 'Specialty Salt', 'Wet Paste', 'Dry Spice Blend',
    ],
  },
];

// Subset shown in the nav dropdown (curated for discovery, not exhaustive)
export const NAV_CATEGORY_GROUPS: CategoryGroup[] = [
  {
    label: 'Proteins & Seafood',
    families: ['Chicken', 'Beef', 'Pork', 'Duck', 'Finfish', 'Mollusc'],
  },
  {
    label: 'Starches',
    families: ['Pasta', 'Bread', 'Rice', 'Polenta'],
  },
  {
    label: 'Sauces',
    families: ['Mother Sauce', 'Stock', 'Derivative Sauce', 'Compound Butter', 'Emulsion', 'Ragù & Meat Sauce'],
  },
  {
    label: 'Pastry & Sweets',
    families: ['Pastry Dough', 'Cream & Filling', 'Cookie', 'Brownie & Bar'],
  },
  {
    label: 'Vegetables',
    families: ['Mushroom', 'Roasted & Grilled', 'Mash & Purée', 'Salad & Dressed'],
  },
  {
    label: 'Technique',
    families: ['Fermentation', 'Emulsification & Bonding', 'Starch & Dough Science', 'Heat & Thermodynamics'],
  },
];
