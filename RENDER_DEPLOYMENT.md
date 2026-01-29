# Render Deployment Guide

## Quick Deploy to Render

### Option 1: Deploy via Render Dashboard (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin https://github.com/YOUR_USERNAME/market-classifier.git
   git push -u origin main
   ```

2. **Create a new Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Render will auto-detect the `render.yaml` configuration

3. **Configure Environment Variables** (Optional)
   - `FINANCIAL_NEWS_API_KEY`: Your Financial Modeling Prep API key (defaults to 'demo')
   - `PYTHON_VERSION`: 3.11.14 (already set)

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Your API will be available at: `https://market-classifier-api.onrender.com`

### Option 2: Deploy via Render Blueprint (render.yaml)

Your `render.yaml` is already configured. Just:

1. Push to GitHub
2. In Render Dashboard, click "New +" → "Blueprint"
3. Select your repository
4. Render will read `render.yaml` and create the service automatically

---

## Configuration Details

### Current render.yaml Configuration

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

### What Gets Deployed

- **Service Type**: Web Service (HTTP server)
- **Runtime**: Python 3.11.14
- **Build**: Installs all dependencies from `requirements.txt`
- **Start Command**: Runs `python server.py` (Flask API on port 5000)
- **Port**: Render automatically maps port 5000 to HTTPS

---

## API Endpoints

Once deployed, your API will be available at:
`https://YOUR-APP-NAME.onrender.com/api`

### Available Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/predict` | Predict stock movements for custom tickers |
| POST | `/api/popular-stocks` | Get popular stocks with real-time data |
| GET | `/api/macro-events` | Get macro calendar events |
| POST | `/api/visualizations` | Get model visualizations |
| POST | `/api/download-report` | Download predictions + charts as ZIP |
| GET | `/api/categories` | List all stock categories |
| GET | `/api/health` | Health check endpoint |
| POST | `/api/clear-cache` | Clear model cache |

### Example API Call

```bash
curl -X POST https://YOUR-APP-NAME.onrender.com/api/predict \
  -H "Content-Type: application/json" \
  -d '{"tickers": "AAPL,TSLA,GOOGL"}'
```

---

## Frontend Deployment (Optional)

If you want to deploy the frontend separately:

### Option A: Deploy Frontend on Render

1. Create a new Static Site on Render
2. Build Command: `echo "No build needed"`
3. Publish Directory: `templates`
4. Update `templates/index.html` to point to your API:
   ```javascript
   const API_BASE = "https://YOUR-APP-NAME.onrender.com/api";
   ```

### Option B: Use the Backend to Serve Frontend

Your `server.py` already serves the frontend! Just access:
`https://YOUR-APP-NAME.onrender.com/`

But you'll need to update the API URL in `templates/index.html`:

```javascript
// Change from:
const API_BASE = "http://localhost:5000/api";

// To:
const API_BASE = window.location.origin + "/api";
```

---

## Important Notes

### Free Tier Limitations

- **Cold Starts**: Free tier services spin down after 15 minutes of inactivity
- **First Request**: May take 30-60 seconds to wake up
- **Build Time**: Initial deployment takes 3-5 minutes
- **Memory**: 512 MB RAM (sufficient for this app)

### Performance Optimization

1. **Model Caching**: Models are cached in memory for 1 hour
2. **Concurrent Requests**: Flask runs with `threaded=True`
3. **Data Caching**: Macro events cached for 10 minutes

### Troubleshooting

**Build Fails**
- Check Python version compatibility (3.11.14)
- Verify all dependencies in `requirements.txt`
- Check Render build logs

**App Crashes**
- Check Render logs: Dashboard → Your Service → Logs
- Verify environment variables are set
- Check memory usage (may need to upgrade plan)

**Slow Response**
- First request after cold start is slow (expected)
- Consider upgrading to paid plan to avoid cold starts
- Use `/api/health` endpoint to keep service warm

---

## Monitoring & Logs

### View Logs
1. Go to Render Dashboard
2. Select your service
3. Click "Logs" tab
4. Real-time logs show all API requests and errors

### Health Check
Use the health endpoint to monitor service status:
```bash
curl https://YOUR-APP-NAME.onrender.com/api/health
```

Response:
```json
{
  "status": "healthy",
  "timestamp": "2025-01-29T12:00:00Z",
  "models_cached": 3
}
```

---

## Upgrading to Paid Plan

For production use, consider upgrading to:
- **Starter Plan ($7/month)**: No cold starts, always-on
- **Standard Plan ($25/month)**: More resources, better performance

Benefits:
- No cold starts (instant response)
- More memory and CPU
- Better for high-traffic applications

---

## Environment Variables (Optional)

Add these in Render Dashboard → Environment:

| Variable | Description | Default |
|----------|-------------|---------|
| `FINANCIAL_NEWS_API_KEY` | Financial Modeling Prep API key | `demo` |
| `PYTHON_VERSION` | Python version | `3.11.14` |

---

## Next Steps

1. ✅ Push code to GitHub
2. ✅ Create Render account
3. ✅ Deploy via Dashboard or Blueprint
4. ✅ Test API endpoints
5. ✅ Update frontend API URL (if needed)
6. ✅ Share your deployed app!

---

## Support

- **Render Docs**: https://render.com/docs
- **Render Community**: https://community.render.com
- **GitHub Issues**: Create an issue in your repository

---

Built with ❤️ by Meet Ratwani & Jaimin Pansal
