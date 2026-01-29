# 🚀 Quick Deploy to Render

Deploy your Market Classifier in 5 minutes!

## Prerequisites

- GitHub account
- Render account (free): https://render.com/

## Deploy Steps

### 1️⃣ Push to GitHub

```bash
git init
git add .
git commit -m "Deploy to Render"
git remote add origin https://github.com/canvameet/marketclassifer.git
git push -u origin main
```

### 2️⃣ Deploy on Render

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository
4. Click **"Apply"**
5. Wait 3-5 minutes for build

### 3️⃣ Access Your App

Your app will be live at:
```
https://market-classifier-api.onrender.com
```

**API Endpoints:**
- Health: `https://YOUR-APP.onrender.com/api/health`
- Predict: `https://YOUR-APP.onrender.com/api/predict`
- Frontend: `https://YOUR-APP.onrender.com/`

### 4️⃣ Test It

```bash
# Health check
curl https://YOUR-APP.onrender.com/api/health

# Predict stocks
curl -X POST https://YOUR-APP.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{"tickers": "AAPL,TSLA"}'
```

## That's It! 🎉

Your Market Classifier is now live and accessible worldwide!

## What's Deployed?

✅ Flask API server (Python 3.11.14)  
✅ XGBoost ML models  
✅ Real-time stock data (Yahoo Finance)  
✅ Interactive frontend  
✅ Automatic HTTPS  
✅ Auto-scaling  

## Free Tier Notes

⚠️ **Cold Starts**: App sleeps after 15 min of inactivity  
⚠️ **First Request**: May take 30-60 seconds to wake up  
✅ **Solution**: Upgrade to Starter plan ($7/month) for always-on

## Need Help?

📖 Full Guide: See `RENDER_DEPLOYMENT.md`  
📋 Checklist: See `DEPLOYMENT_CHECKLIST.md`  
🐛 Issues: Check Render logs in Dashboard

---

**Built by**: Meet Ratwani & Jaimin Pansal  
**Deployed on**: Render.com
