# CLAUDE DESKTOP PROJECT - COPY/PASTE TEMPLATE

Use this file to quickly set up your Claude Desktop project. Copy the exact text from each section.

---

## STEP 1: Project Name & Description

### Project Name (Required)
Copy exactly:
```
Café Athena - Recipe Development & Documentation
```

### Project Description (Optional but recommended)
Copy exactly:
```
AI Chef for iterative recipe development, manuscript-ready formatting, and culinary technique education. Three modes: The Lab (development), The Manual (publication), The MasterClass (education).
```

---

## STEP 2: Project Instructions

Go to Claude project settings → **Instructions** field

Copy the entire content of `PROJECT_INSTRUCTIONS.md` from this folder and paste it there.

This is ~400 lines. The project will reference attached files for detailed standards.

---

## STEP 3: Attach Files (In Order)

In Claude project → **Attach Files** button

Attach these 6 files in this exact order:

### File 1: Recipe-Format-Standard.md
**Location:** `/Guidance/Recipe-Format-Standard.md`  
**Purpose:** Master formatting rules for all recipe outputs

### File 2: Cafe-Athena-Workflow-Guide.md
**Location:** `/Guidance/Cafe-Athena-Workflow-Guide.md`  
**Purpose:** Strategic workflow methodology (Lab → Manual → Publish)

### File 3: Recipe-Example.md
**Location:** `/Guidance/Recipe-Example.md`  
**Purpose:** Sample recipe following the standard (reference for Mode 1 & 2)

### File 4: Technique-Folio-Example.md
**Location:** `/Guidance/Technique-Folio-Example.md`  
**Purpose:** Sample technique folio (reference for Mode 3)

### File 5: Technique_Folio_Template_v1.md
**Location:** `/Guidance/Technique_Folio_Template_v1.md`  
**Purpose:** Structural template for all technique folios (Mode 3)

### File 6: Cafe-Athena-The-Manual-Current-Version.md ⭐ CRITICAL
**Location:** `/The Manual/Cafe-Athena-The-Manual-Current-Version.md`  
**Purpose:** Master index of all cookbook content (required for Mode 2 indexing)

---

## STEP 4: Test the Setup

In your new Claude project, try:

```
Let's work on a new pasta recipe.
```

### Expected Response:
```
I understand you want to develop a recipe. Let's proceed in Mode 1: The Lab.

[Claude proceeds with recipe development guidance]
```

If Claude detects Mode 1 correctly, your setup is working.

---

## FIELD REFERENCE: What Goes Where

| Claude Field | What Goes Here | From This Folder |
|--------------|---|---|
| **Project Name** | `Café Athena - Recipe Development & Documentation` | Copy above |
| **Project Description** | `AI Chef for iterative recipe...` | Copy above |
| **Project Instructions** | Full content of `PROJECT_INSTRUCTIONS.md` | This folder |
| **Attached Files** | 6 files listed above (in order) | From `/Guidance/` + `/The Manual/` |

---

## QUICK VALIDATION

After setup, check:

- [ ] Project name appears at top of project
- [ ] Description visible in project settings
- [ ] Instructions field contains ~400 lines of PROJECT_INSTRUCTIONS.md
- [ ] All 6 files show in "Attached files" list
- [ ] Test message triggers Mode 1 detection
- [ ] Claude references Recipe-Format-Standard.md when asked about format

---

## TROUBLESHOOTING

**Problem:** Claude doesn't recognize modes  
**Solution:** Paste all of PROJECT_INSTRUCTIONS.md into Instructions field (check for missing lines)

**Problem:** Can't find files to attach  
**Solution:** Verify file paths match exactly (use CMD+K in VS Code to jump to file)

**Problem:** Index errors in Mode 2  
**Solution:** Ensure `Cafe-Athena-The-Manual-Current-Version.md` is attached (File 6)

**Problem:** Format validation skipped  
**Solution:** Verify `Recipe-Format-Standard.md` is attached (File 1)
