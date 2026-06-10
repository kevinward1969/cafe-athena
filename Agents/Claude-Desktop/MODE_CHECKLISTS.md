# CAFÉ ATHENA - MODE CHECKLISTS FOR USER

Use these checklists before starting a conversation in each mode. They help you provide complete information and reduce STOP points.

---

## MODE 1: THE LAB (Recipe Development)

**Pre-Conversation Checklist:**

- [ ] I have a dish concept or recipe to develop
- [ ] I can describe the desired texture, flavor profile, or key characteristics
- [ ] I have a rough ingredient list (doesn't need to be final)
- [ ] I understand this is iterative (we'll refine multiple times)
- [ ] I'm ready to test specific variables (temperature, timing, technique)

**Conversation Starter:**

```
"Let's work on [dish name]. Here's what I'm thinking: [concept, texture, flavor]. 
Starting ingredients: [list]. I want to focus on [specific technique or element]."
```

**During Development:**

- Tell Claude when to "finalize" or you're "ready for Manual"
- Describe what's not working (taste, texture, timing)
- Provide tasting notes and observations
- Ask "Why?" questions about techniques

**Signs You're Ready for Mode 2:**

- Recipe tested multiple times
- Consistent results achieved
- All instructions clear and sensory cues included
- You've said: "Finalize this" or "Ready for Manual"

---

## MODE 2: THE MANUAL (Production Formatting)

**Pre-Conversation Checklist:**

- [ ] Recipe has been tested and refined (from Mode 1)
- [ ] I know the target Chapter (e.g., "Chapter 9 - The Pâtissier")
- [ ] I have a finalized ingredient list (with weights and volumes)
- [ ] I have all method steps with timing and sensory cues
- [ ] I've read Recipe-Format-Standard.md (attached)
- [ ] I understand the recipe will be assigned an INDEX number (XX-YY)

**Conversation Starter:**

```
"Generate the final recipe for [dish name]. Target chapter: [Chapter Name]. 
Here's the finalized version: [paste recipe content from Mode 1]."
```

**What Claude Will Do:**

1. Format according to Recipe-Format-Standard.md
2. Check that all 7 required sections are present
3. Scan Cafe-Athena-The-Manual-Current-Version.md for the correct XX-YY number
4. Output manuscript-ready recipe with INDEX DATA block

**Critical Stop Points (Claude Will Ask):**

- "What chapter does this belong to?"
- "I found the last entry in [Chapter] is [XX-YY]. The next number will be [XX-YY+1]. Confirm?"
- "This is missing [section]. Please provide before I continue."
- "I cannot read the index file. Please tell me the last 3 entries in [Chapter]."

---

## MODE 3: THE MASTERCLASS (Technique Education)

**Pre-Conversation Checklist:**

- [ ] I want to learn about a specific culinary technique
- [ ] I can describe what I know about it (or what confuses me)
- [ ] I understand this will become a formal Technique Folio
- [ ] I'm ready to read detailed science and practical applications
- [ ] I have access to Technique_Folio_Template_v1.md and Technique-Folio-Example.md

**Conversation Starter:**

```
"Teach me about [technique]. Here's what I understand: [current knowledge]. 
What I want to know: [specific questions]."
```

**Examples:**

```
"Teach me about spherification. I know it's Algin + Calcium, but I don't understand the chemistry."

"Explain the Maillard reaction. I want to understand why it happens faster at higher temps."

"How does emulsification work? I keep breaking hollandaise and want to understand why."
```

**During Conversation:**

- Ask "Why?" questions
- Request practical applications and examples
- Request testing formulas or reference values
- Say "Ready to convert this to a Technique Folio?" when you want formalization

**What Claude Will Output:**

1. **Tutorial Phase**: Detailed explanation of science, practical application, sensory cues
2. **Folio Phase** (on request): Formatted Technique Folio with:
   - Concept Definition
   - The Science
   - Technique/Practical Application
   - Reference Values (table)
   - Safety & Constraints
   - Applications & Links
   - Sources

**Signs You're Ready for Folio Conversion:**

- You understand the underlying science
- You have practical application steps
- You have reference values (temperatures, ratios, timing)
- You've identified safety concerns or constraints
- You can list related recipes or techniques

---

## SWITCHING MODES

**In any mode, you can switch by saying:**

```
"Switch to Mode 1: The Lab" 
"Change to Mode 2: The Manual"
"Go to Mode 3: The MasterClass"
```

Claude will confirm and context remains available.

---

## CRITICAL SAFETY STOPS (All Modes)

Claude will **always** STOP and ask you to confirm if:

❌ **Food Safety Issue**

- Unsafe temperature range
- HACCP violation (time/temperature abuse)
- Potential allergen or contamination concern

❌ **Format Contradiction**

- Your instruction contradicts Recipe-Format-Standard.md
- Technical term usage conflicts with standard definition

❌ **Index Conflict**

- Chapter assignment doesn't match content
- Chapter prefix (XX-) doesn't match expected sequence
- Manual index cannot be scanned

❌ **Missing Information**

- Yield, cooking method, or ingredient list incomplete (Mode 2)
- Diagram required but only text available (Mode 3)

**When Claude Stops:**

- Wait for the question
- Provide clarification or confirmation
- Do NOT override food safety concerns
