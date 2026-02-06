# NiveshAI Deployment Guide

## 🚀 Quick Start (Local Development)

### Option 1: Double-Click Start (Windows)
Simply double-click `start.bat` to launch both servers automatically.

### Option 2: Manual Start

#### Terminal 1 - Backend API Server
```bash
python server.py
```
- Runs on: http://localhost:5000
- Provides: ML predictions, stock data, news, order book

#### Terminal 2 - Frontend Web App
```bash
python app.py
```
- Runs on: http://localhost:8080
- Provides: User interface, visualizations, interactions
- **Note**: Make sure backend is running first!

### Option 3: PowerShell Script
```powershell
powershell -ExecutionPolicy Bypass -File start.ps1
```

## 📋 Prerequisites

### Python Requirements
- Python 3.8 or higher
- pip package manager

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🌐 Accessing the Application

Once both servers are running:
1. Open your browser
2. Navigate to: **http://localhost:8080**
3. The frontend will automatically connect to the backend API

## 📁 Project Structure

```
niveshai/
├── src/                      # Python modules
│   ├── __init__.py          # Package initializer
│   ├── data_loader.py       # Data loading
│   ├── feature_engineering.py # Feature creation
│   ├── model_training.py    # Model training
│   ├── backtesting.py       # Backtesting framework
│   └── order_book.py        # Order book analysis
├── templates/               # HTML templates
│   └── index.html          # Main UI
├── static/                  # Static assets
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images
├── data/                    # Data files
├── models/                  # Trained models
├── results/                 # Output visualizations
├── main.py                  # Main prediction pipeline
├── server.py                # Backend API (Flask)
├── app.py                   # Frontend server (Flask)
├── demo.py                  # Demo script
├── start.bat               # Windows quick start
├── start.ps1               # PowerShell startup script
└── requirements.txt         # Python dependencies
```

## 🔧 Configuration

### Backend (server.py)
- **Port**: 5000
- **Host**: 0.0.0.0 (accessible from network)
- **Debug**: False (production-ready)
- **Threading**: Enabled

### Frontend (app.py)
- **Port**: 8080
- **Host**: 0.0.0.0 (accessible from network)
- **Debug**: True (development mode)
- **Auto-open browser**: Enabled

## 🌍 Production Deployment

### Render.com (Recommended)
See `RENDER_DEPLOYMENT.md` for detailed instructions.

### Heroku
See `deploy.sh` for Heroku deployment script.

### Docker (Coming Soon)
Docker configuration will be added soon.

## 🔍 API Endpoints

### Backend API (port 5000)
- `POST /api/predict` - Predict custom tickers
- `POST /api/popular-stocks` - Get popular stocks with real data
- `GET /api/macro-events` - Get macro calendar events
- `POST /api/visualizations` - Get model visualizations
- `GET /api/categories` - List all categories
- `GET /api/health` - Health check
- `POST /api/clear-cache` - Clear model cache

## 🐛 Troubleshooting

### Port Already in Use
If you get a "port already in use" error:

**Windows:**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000
# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F

# Find process using port 8080
netstat -ano | findstr :8080
taskkill /PID <PID> /F
```

### Dependencies Not Installing
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Then install requirements
pip install -r requirements.txt
```

### Backend Not Responding
- Check if server.py is running without errors
- Verify port 5000 is not blocked by firewall
- Check console output for error messages

### Frontend Can't Connect to Backend
- Ensure backend is running on port 5000
- Check browser console (F12) for connection errors
- Verify CORS is enabled in server.py

## 📊 Features

- ✅ Real-time stock predictions (UP/DOWN)
- ✅ 250+ technical indicators
- ✅ XGBoost ML model with 85%+ accuracy
- ✅ SHAP explainability
- ✅ Backtesting framework
- ✅ Order book analysis
- ✅ Financial news integration
- ✅ Interactive visualizations
- ✅ Multi-ticker support
- ✅ SDG alignment tracking

## 📝 Notes

- First prediction may take 30-60 seconds (model training)
- Subsequent predictions are cached for faster response
- Model is retrained daily with latest data
- News is fetched in real-time from multiple sources

## 🆘 Support

For issues or questions:
- Check existing documentation files
- Review console logs for error messages
- Ensure all dependencies are properly installed

## 📄 License

MIT License - See LICENSE file for details
