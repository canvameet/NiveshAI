# 🚀 Deploy Market Classifier to Render

## 📋 Quick Links

- **5-Minute Deploy**: [QUICK_DEPLOY.md](QUICK_DEPLOY.md)
- **Complete Guide**: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)
- **Checklist**: [DEPLOYMENT_CHECKLIST.md](DEPLOYMENT_CHECKLIST.md)
- **Summary**: [DEPLOYMENT_SUMMARY.md](DEPLOYMENT_SUMMARY.md)

---

## ⚡ Super Quick Deploy (3 Steps)

### 1. Push to GitHub
```bash
git init
git add .
git commit -m "Deploy to Render"
git remote add origin https://github.com/canvameet/marketclassifer.git
git push -u origin main
```

### 2. Deploy on Render
1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Blueprint"**
3. Connect your repository
4. Click **"Apply"**

### 3. Done! 🎉
Your app is live at: `https://market-classifier-api.onrender.com`

---

## 📦 What's Included

### ✅ Ready-to-Deploy Configuration
- `render.yaml` - Render Blueprint configuration
- `.renderignore` - Optimized deployment
- Auto-detecting API URLs (local + deployed)

### ✅ Complete Documentation
- **QUICK_DEPLOY.md** - 5-minute quick start
- **RENDER_DEPLOYMENT.md** - Full deployment guide
- **DEPLOYMENT_CHECKLIST.md** - Step-by-step checklist
- **DEPLOYMENT_SUMMARY.md** - Technical summary

### ✅ Production-Ready Features
- Flask API server (Python 3.11.14)
- XGBoost ML models
- Real-time stock data
- Interactive frontend
- Automatic HTTPS
- Model caching (1 hour)
- Data caching (10 minutes)
- Concurrent request handling

---

## 🎯 API Endpoints

Once deployed, your API will be available at:
`https://YOUR-APP.onrender.com/api`

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/predict` | Predict stock movements |
| POST | `/api/popular-stocks` | Get popular stocks |
| GET | `/api/macro-events` | Economic calendar |
| POST | `/api/visualizations` | Model charts |
| POST | `/api/download-report` | Download ZIP |
| GET | `/api/categories` | Stock categories |
| GET | `/api/health` | Health check |
| POST | `/api/clear-cache` | Clear cache |

---

## 🧪 Test Your Deployment

### Health Check
```bash
curl https://YOUR-APP.onrender.com/api/health
```

### Predict Stocks
```bash
curl -X POST https://YOUR-APP.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{"tickers": "AAPL,TSLA,GOOGL"}'
```

### Access Frontend
Open browser: `https://YOUR-APP.onrender.com/`

---

## 💰 Pricing

### Free Tier (Perfect for Testing)
- ✅ 750 hours/month
- ✅ Automatic HTTPS
- ✅ Auto-scaling
- ⚠️ Sleeps after 15 min inactivity
- ⚠️ 512 MB RAM

### Starter Plan ($7/month)
- ✅ Always-on (no cold starts)
- ✅ 512 MB RAM
- ✅ Perfect for production

### Standard Plan ($25/month)
- ✅ 2 GB RAM
- ✅ Better performance
- ✅ High traffic support

---

## 📊 Performance

### Free Tier
- **Cold Start**: 30-60 seconds (after 15 min inactivity)
- **First Prediction**: 2-5 seconds (model training)
- **Cached Prediction**: <1 second
- **Memory**: 512 MB (sufficient)

### Paid Tier
- **No Cold Starts**: Always-on
- **First Prediction**: 2-5 seconds
- **Cached Prediction**: <1 second
- **Memory**: 512 MB - 2 GB

---

## 🔧 Configuration

### render.yaml
```yaml
services:
  - type: web
    name: market-classifier-api
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python server.py
    pythonVersion: 3.11.14
    envVars:
      - key: FINANCIAL_NEWS_API_KEY
        value: demo
      - key: PYTHON_VERSION
        value: 3.11.14
```

### Environment Variables
- `FINANCIAL_NEWS_API_KEY`: Your API key (optional, defaults to 'demo')
- `PYTHON_VERSION`: 3.11.14 (auto-set)

---

## 🐛 Troubleshooting

### Build Fails
1. Check Python version (3.11.14)
2. Verify requirements.txt
3. Check Render build logs

### App Crashes
1. Check Render logs (Dashboard → Logs)
2. Verify environment variables
3. Check memory usage

### Slow Response
1. Expected on first request (cold start)
2. Use health endpoint to keep warm
3. Consider upgrading to paid plan

---

## 📚 Documentation Structure

```
market-classifier-main/
├── QUICK_DEPLOY.md           # 5-minute quick start
├── RENDER_DEPLOYMENT.md      # Complete deployment guide
├── DEPLOYMENT_CHECKLIST.md   # Step-by-step checklist
├── DEPLOYMENT_SUMMARY.md     # Technical summary
├── RENDER_README.md          # This file
├── render.yaml               # Render configuration
├── .renderignore             # Deployment optimization
├── requirements.txt          # Python dependencies
├── server.py                 # Flask API server
├── app.py                    # Frontend server
└── templates/index.html      # Frontend UI
```

---

## 🎓 Learning Resources

- **Render Docs**: https://render.com/docs/web-services
- **Render Community**: https://community.render.com
- **Python on Render**: https://render.com/docs/deploy-flask
- **Flask Docs**: https://flask.palletsprojects.com/

---

## ✅ Deployment Checklist

- [x] `render.yaml` configured
- [x] Frontend auto-detects API URL
- [x] Server runs on 0.0.0.0:5000
- [x] All dependencies in requirements.txt
- [x] Python 3.11.14 specified
- [x] Environment variables set
- [x] Documentation complete
- [ ] Pushed to GitHub
- [ ] Deployed on Render
- [ ] Tested all endpoints
- [ ] Shared with users

---

## 🚀 Next Steps

1. **Deploy**: Follow [QUICK_DEPLOY.md](QUICK_DEPLOY.md)
2. **Test**: Verify all endpoints work
3. **Monitor**: Check logs and metrics
4. **Share**: Share your app URL!
5. **Upgrade**: Consider paid plan for production

---

## 💡 Pro Tips

### Keep Service Warm (Free Tier)
Use a cron job service to ping your health endpoint every 10 minutes:
- [UptimeRobot](https://uptimerobot.com/) (Free)
- [Cron-job.org](https://cron-job.org/) (Free)

### Monitor Performance
```bash
# Health check
curl https://YOUR-APP.onrender.com/api/health

# Check response time
time curl https://YOUR-APP.onrender.com/api/health
```

### View Logs
```
Dashboard → Your Service → Logs
```

### Redeploy
```bash
# Auto-deploy on push
git push origin main

# Manual deploy
Dashboard → Your Service → Manual Deploy
```

---

## 🎉 Success!

Your Market Classifier is now:
- ✅ Deployed on Render
- ✅ Accessible worldwide
- ✅ Secured with HTTPS
- ✅ Auto-scaling
- ✅ Production-ready

**Your App URL**: `https://market-classifier-api.onrender.com`

---

## 📞 Support

Need help? Check these resources:

1. **Documentation**: See guides in this folder
2. **Render Docs**: https://render.com/docs
3. **Community**: https://community.render.com
4. **GitHub Issues**: Create an issue in your repository

---

## 👥 Credits

**Built with ❤️ by**: Meet Ratwani & Jaimin Pansal  
**Deployment Platform**: Render.com  
**Date**: January 29, 2025  
**Version**: 1.0.0

---

## 📄 License

MIT License - See LICENSE file for details

---

**Ready to deploy? Start with [QUICK_DEPLOY.md](QUICK_DEPLOY.md)!** 🚀
