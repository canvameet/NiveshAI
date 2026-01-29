# 🚀 START HERE - Deploy to Render

## Your Repository
**GitHub**: https://github.com/canvameet/marketclassifer

---

## 🎯 Deploy in 2 Ways

### Option 1: Automated Script (Easiest)

**Windows:**
```bash
cd market-classifier-main
deploy.bat
```

**Mac/Linux:**
```bash
cd market-classifier-main
chmod +x deploy.sh
./deploy.sh
```

Then:
1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Blueprint"**
3. Connect: https://github.com/canvameet/marketclassifer
4. Click **"Apply"**

### Option 2: Manual Commands

```bash
cd market-classifier-main

# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Deploy to Render"

# Add remote
git remote add origin https://github.com/canvameet/marketclassifer.git

# Push
git branch -M main
git push -u origin main
```

Then deploy on Render (same as Option 