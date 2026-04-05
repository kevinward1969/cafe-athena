#!/bin/bash
# ============================================================
# Café Athena — Build & Deploy to FastComet
#
# Usage: bash scripts/deploy.sh
#
# Prerequisites:
#   - SSH access to FastComet configured
#   - Subdomain created in cPanel (cookbook.kevinward.com)
# ============================================================

set -euo pipefail

# ── Configuration ─────────────────────────────────────────────
REMOTE_HOST="fastcomet-passiton"
REMOTE_PATH="~/public_html/cookbook"
# ──────────────────────────────────────────────────────────────

echo "════════════════════════════════════════"
echo " Café Athena — The Manual · Deploy"
echo "════════════════════════════════════════"
echo ""

# Step 1: Prepare content
echo "📋 Step 1: Preparing content..."
python3 site/scripts/prepare-content.py
echo ""

# Step 2: Build
echo "🔨 Step 2: Building static site..."
cd "$(dirname "$0")/.."
npm run build
echo "   ✅ Build complete (dist/)"
echo ""

# Step 3: Deploy
echo "🚀 Step 3: Deploying to FastComet..."
rsync -avz --delete \
  --exclude='.DS_Store' \
  --filter='protect images/**.webp' \
  dist/ \
  "${REMOTE_HOST}:${REMOTE_PATH}/"

echo ""
echo "════════════════════════════════════════"
echo "✅ Deployed successfully!"
echo "   Visit: https://cookbook.kevinward.com"
echo "════════════════════════════════════════"
