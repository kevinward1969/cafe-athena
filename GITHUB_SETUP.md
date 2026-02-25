# GitHub Setup Instructions for Café Athena

Follow these steps to initialize the repository locally and push it to GitHub.

---

## Step 1: Create Repository on GitHub

1. Go to [github.com](https://github.com) and log in
2. Click **New** (top left, or your profile → Repositories → New)
3. Fill in:
   - **Repository name:** `cafe-athena`
   - **Description:** `AI-powered recipe development, manuscript production, and technique education system`
   - **Public** (recommended for Claude Desktop integration)
   - **Add .gitignore:** No (we already have one)
   - **Add README:** No (we already have one)
4. Click **Create repository**
5. Copy the repository URL (HTTPS or SSH)

**Example URL:**
```
https://github.com/YOUR_USERNAME/cafe-athena.git
```

---

## Step 2: Initialize Git Locally

Open Terminal and navigate to your project directory:

```bash
cd /Users/kevinward/Projects/Cafe\ Athena
```

Initialize the repository:

```bash
git init
```

---

## Step 3: Add Remote & Configure

Add the GitHub repository as the remote:

```bash
git remote add origin https://github.com/YOUR_USERNAME/cafe-athena.git
```

Replace `YOUR_USERNAME` with your actual GitHub username.

Verify the remote:

```bash
git remote -v
```

You should see:
```
origin  https://github.com/YOUR_USERNAME/cafe-athena.git (fetch)
origin  https://github.com/YOUR_USERNAME/cafe-athena.git (push)
```

---

## Step 4: Add All Files

Add all files to staging:

```bash
git add .
```

Verify what's being added (optional):

```bash
git status
```

You should see:
```
Changes to be committed:
  new file:   .gitignore
  new file:   README.md
  new file:   Claude-Desktop/...
  ... (all files)
```

---

## Step 5: Create Initial Commit

```bash
git commit -m "Initial commit: Café Athena AI system setup"
```

---

## Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

If prompted for authentication:
- **HTTPS:** Enter your GitHub username and personal access token (not password)
- **SSH:** Use your SSH key (if configured)

---

## Step 7: Verify on GitHub

Go to your GitHub repository URL:
```
https://github.com/YOUR_USERNAME/cafe-athena
```

You should see:
- ✅ README.md displayed
- ✅ .gitignore applied
- ✅ All folders visible (Claude-Desktop/, Guidance/, The Manual/)
- ✅ Shows "main" branch

---

## Step 8: Connect to Claude Desktop

1. Open [Claude Desktop](https://claude.ai/projects)
2. Create a new project or open existing one
3. Go to project settings → **Files** section
4. Click **Connect GitHub**
5. Authorize Claude to access your GitHub
6. Select repository: `cafe-athena`
7. Select branch: `main`

Claude will now automatically sync Guidance/ files from GitHub.

---

## Ongoing Workflow

### After Making Local Changes

```bash
# See what changed
git status

# Stage changes
git add .

# Commit with message
git commit -m "Update Recipe-Format-Standard.md - clarified mise en place rules"

# Push to GitHub
git push
```

### Pull Latest Changes from GitHub

```bash
git pull origin main
```

### View History

```bash
git log --oneline
```

---

## Branching (Optional)

If you want to separate public and private content:

### Create a Private Branch for The Manual

```bash
git checkout -b private/manuscripts
```

Add only The Manual/ files:

```bash
git add "The Manual/"
git commit -m "Add cookbook manuscript (private)"
git push -u origin private/manuscripts
```

Then in `.gitignore`, add:
```
# Keep private
The Manual/
```

Push updated .gitignore to main:

```bash
git checkout main
git add .gitignore
git commit -m "Exclude The Manual from main branch"
git push
```

**Result:** 
- `main` branch: Claude Desktop syncs public Guidance/ files
- `private/manuscripts` branch: Local backup of cookbook content

---

## SSH vs HTTPS

### HTTPS (Easier, Recommended)
- Use personal access token instead of password
- Requires token generation in GitHub settings
- Works on any network

### SSH (More Secure)
- Requires SSH key setup
- Faster after initial setup
- Better for frequent commits

Choose whichever you prefer; HTTPS is simpler for most users.

---

## Troubleshooting

### "fatal: not a git repository"
```bash
cd /Users/kevinward/Projects/Cafe\ Athena
git init
```

### "Permission denied (publickey)" (SSH only)
- Verify SSH key is added to GitHub: https://github.com/settings/keys
- Or switch to HTTPS: `git remote set-url origin https://github.com/...`

### "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/cafe-athena.git
```

### Files not appearing on GitHub
```bash
git status  # Check if files are tracked
git add .   # Add all files
git commit -m "Add missing files"
git push
```

### Claude can't access GitHub repo
1. Verify repo is **Public** (not Private)
2. Verify Claude project GitHub integration is connected
3. Try disconnecting and reconnecting the GitHub integration in Claude project

---

## After Initial Setup

Your repository is ready! Next:

1. ✅ Clone on other machines: `git clone https://github.com/YOUR_USERNAME/cafe-athena.git`
2. ✅ Invite collaborators: GitHub Settings → Collaborators
3. ✅ Sync with Claude Desktop: Claude Files section → Connect GitHub
4. ✅ Push updates regularly: `git push` after commits

---

## Quick Reference (Copy/Paste)

### First-time setup (all at once):
```bash
cd /Users/kevinward/Projects/Cafe\ Athena
git init
git remote add origin https://github.com/YOUR_USERNAME/cafe-athena.git
git add .
git commit -m "Initial commit: Café Athena AI system setup"
git branch -M main
git push -u origin main
```

### Ongoing updates:
```bash
git add .
git commit -m "Your message here"
git push
```

---

**Done!** Your Café Athena repository is now on GitHub and ready for Claude Desktop integration.
