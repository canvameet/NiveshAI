# Render Deployment Checklist ✅

## Pre-Deployment

- [x] `render.yaml` configured
- [x] `requirements.txt` includes all dependencies
- [x] Frontend API URL auto-detects environment
- [x] Server runs on `0.0.0.0:5000` (Render compatible)
- [x] Python version specified (3.11.14)

## Step-by-Step Deployment

### 1. Prepare Your Repository

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Ready for Render deployment"

# Create GitHub repository and push
git remote add origin https://github.com/canvameet/marketclassifer.git
git branch -M main
git push -u origin main
```

### 2. Deploy on Render

**Option A: Auto-Deploy with render.yaml**
1. Go to https://dashboard.render.com/
2. Click "New +" → "Blueprint"
3. Connect your GitHub repository
4. Render will detect `render.yaml` and configure automatically
5. Click "Apply" to deploy

**Option B: Manual Setup**
1. Go to https://dashboard.render.com/
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `market-classifier-api`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python server.py`
   - **Python Version**: `3.11.14`
5. Click "Create Web Service"

### 3. Wait for Build

- Initial build takes 3-5 minutes
- Watch the logs for any errors
- Service will be live at: `https://market-classifier-api.onrender.com`

### 4. Test Your Deployment

```bash
# Health check
curl https://YOUR-APP-NAME.onrender.com/api/health

# Test prediction
curl -X POST https://YOUR-APP-NAME.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{"tickers": "AAPL"}'
```

### 5. Access Your App

- **API**: `https://YOUR-APP-NAME.onrender.com/api`
- **Frontend**: `https://YOUR-APP-NAME.onrender.com/`

## Post-Deployment

### Monitor Your App

1. **View Logs**: Dashboard → Your Service → Logs
2. **Check Metrics**: Dashboard → Your Service → Metrics
3. **Health Check**: Visit `/api/health` endpoint

### Keep Service Warm (Free Tier)

Free tier services sleep after 15 minutes of inactivity. To keep it warm:

**Option 1: Use a Cron Job Service**
- [UptimeRobot](https://uptimerobot.com/) (Free)
- [Cron-job.org](https://cron-job.org/) (Free)
- Ping your `/api/health` endpoint every 10 minutes

**Option 2: Upgrade to Paid Plan**
- Starter Plan ($7/month) - No cold starts

### Update Frontend URL (If Needed)

The frontend now auto-detects the API URL, but you can manually set it:

```javascript
// In templates/index.html
const API_BASE = 'https://YOUR-APP-NAME.onrender.com/api';
```

## Troubleshooting

### Build Fails

**Check Python Version**
```yaml
# In render.yaml
pythonVersion: 3.11.14
```

**Check Dependencies**
```bash
# Test locally
pip install -r requirements.txt
python server.py
```

### App Crashes

**Check Logs**
- Dashboard → Your Service → Logs
- Look for Python errors or missing dependencies

**Memory Issues**
- Free tier has 512 MB RAM
- Consider upgrading if you see memory errors

### Slow Response

**First Request After Sleep**
- Expected on free tier (30-60 seconds)
- Subsequent requests are fast

**Solution**
- Upgrade to paid plan
- Use cron job to keep service warm

## Environment Variables

Add in Render Dashboard → Environment:

| Variable | Value | Required |
|----------|-------|----------|
| `FINANCIAL_NEWS_API_KEY` | Your API key | No (defaults to 'demo') |
| `PYTHON_VERSION` | 3.11.14 | Yes (auto-set) |

## Useful Commands

```bash
# View logs (if using Render CLI)
render logs -s market-classifier-api

# Redeploy
git push origin main  # Auto-deploys if connected

# Manual redeploy
# Dashboard → Your Service → Manual Deploy → Deploy latest commit
```

## Cost Estimate

### Free Tier
- ✅ 750 hours/month free
- ✅ Automatic HTTPS
- ⚠️ Sleeps after 15 min inactivity
- ⚠️ 512 MB RAM

### Starter Plan ($7/month)
- ✅ Always-on (no cold starts)
- ✅ 512 MB RAM
- ✅ Better for production

### Standard Plan ($25/month)
- ✅ 2 GB RAM
- ✅ Better performance
- ✅ Recommended for high traffic

## Success Criteria

- [ ] Build completes without errors
- [ ] `/api/health` returns 200 OK
- [ ] `/api/predict` accepts POST requests
- [ ] Frontend loads and displays UI
- [ ] Stock predictions work end-to-end
- [ ] Visualizations generate correctly

## Next Steps

1. ✅ Deploy to Render
2. ✅ Test all endpoints
3. ✅ Share your app URL
4. ✅ Monitor performance
5. ✅ Consider upgrading for production

## Support Resources

- **Render Docs**: https://render.com/docs/web-services
- **Render Community**: https://community.render.com
- **Python on Render**: https://render.com/docs/deploy-flask

---

**Your App URL**: `https://market-classifier-api.onrender.com`

Built with ❤️ by Meet Ratwani & Jaimin Pansal
