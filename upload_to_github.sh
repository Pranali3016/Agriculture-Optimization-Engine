#!/bin/bash
# ============================================
# GitHub Upload Script — CropSense Project
# Run this from inside crop-recommendation-app/
# ============================================

echo "🌱 CropSense GitHub Upload Script"
echo "=================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found. Install it from https://git-scm.com"
    exit 1
fi

# Step 1: Initialize git
echo ""
echo "📁 Step 1: Initializing git repository..."
git init
git branch -M main

# Step 2: Add all files
echo ""
echo "📦 Step 2: Adding files..."
git add .
git status

# Step 3: First commit
echo ""
echo "💾 Step 3: Creating initial commit..."
git commit -m "🌱 Initial commit: CropSense - Agriculture Production Optimization Engine

- Random Forest ML model (99.32% accuracy) 
- Flask REST API with /predict, /crops, /health endpoints
- Beautiful responsive frontend (HTML/CSS/JS)
- Full deployment config (Render + GitHub Pages)
- GitHub Actions CI/CD pipeline
- 22 crop types, 7 soil/climate parameters
- Training script + pre-trained model included"

# Step 4: Add remote (user fills this in)
echo ""
echo "🔗 Step 4: Add your GitHub remote"
echo "   Create a new repo at https://github.com/new"
echo "   Name it: crop-recommendation-app"
echo "   Then run:"
echo ""
echo "   git remote add origin https://github.com/YOUR_USERNAME/crop-recommendation-app.git"
echo "   git push -u origin main"
echo ""
echo "✅ Done! After pushing:"
echo "   → Go to repo Settings → Pages → Set source to GitHub Actions"
echo "   → Your frontend will be live at: https://YOUR_USERNAME.github.io/crop-recommendation-app"
echo ""
echo "🚀 To deploy the backend on Render:"
echo "   1. Go to https://render.com → New → Web Service"
echo "   2. Connect your GitHub repo"  
echo "   3. Root Directory: backend"
echo "   4. Build Command: pip install -r requirements.txt"
echo "   5. Start Command: gunicorn app:app"
echo "   6. Copy the Render URL and update API_BASE in frontend/index.html"
