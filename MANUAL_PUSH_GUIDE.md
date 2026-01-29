# Manual Push Guide - Token Issue

## Problem
The token doesn't have push permissions even though the repository exists.

## Solution: Use GitHub Desktop (Easiest!)

### Step 1: Download GitHub Desktop
https://desktop.github.com/

### Step 2: Login
- Open GitHub Desktop
- File → Options → Accounts
- Sign in with your GitHub account (canvameet)

### Step 3: Add Repository
- File → Add Local Repository
- Choose folder: `C:\Users\Meet\Downloads\market-classifier-main\market-classifier-main`
- Click "Add Repository"

### Step 4: Publish
- Click "Publish repository" button
- Repository name: `marketclassifer`
- Uncheck "Keep this code private" (make it public)
- Click "Publish repository"

Done! Your code is now on GitHub!

---

## Alternative: Generate New Token with Correct Scopes

Your current token might be missing the `repo` scope.

### Step 1: Generate New Token
1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Note: "Render Deployment"
4. Select scopes:
   - ✅ **repo** (check ALL sub-items)
     - ✅ repo:status
     - ✅ repo_deployment
     - ✅ public_repo
     - ✅ repo:invite
     - ✅ security_events
   - ✅ **workflow**
5. Click "Generate token"
6. **COPY THE TOKEN** (you won't see it again!)

### Step 2: Use New Token
```bash
cd market-classifier-main
git remote set-url origin https://NEW_TOKEN@github.com/canvameet/marketclassifer.git
git push -u origin main
```

---

## After Code is on GitHub

### Deploy on Render

1. Go to: https://dashboard.render.com/
2. Click **"New +"** → **"Blueprint"**
3. Connect GitHub
4. Select: **canvameet/marketclassifer**
5. Click **"Apply"**
6. Wait 3-5 minutes

Your app will be live at:
```
https://market-classifier-api.onrender.com
```

---

## Quick Test Commands

```bash
# Health check
curl https://market-classifier-api.onrender.com/api/health

# Predict stocks
curl -X POST https://market-classifier-api.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d "{\"tickers\": \"AAPL,TSLA\"}"
```

---

## Repository Status

✅ Repository exists: https://github.com/canvameet/marketclassifer  
✅ Code is ready and committed locally  
⚠️ Need to push code (use GitHub Desktop or new token)  
⚠️ Then deploy on Render  

---

**Recommended**: Use GitHub Desktop - it's the easiest and most reliable method!
