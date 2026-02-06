# NiveshAI Startup Script
# This script starts both the backend API and frontend web server

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host " NIVESHAI - AI Stock Prediction System" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host ""

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✓ Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Python not found. Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Starting services..." -ForegroundColor Yellow
Write-Host ""

# Start backend API server in a new window
Write-Host "1. Starting Backend API (port 5000)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python server.py"
Start-Sleep -Seconds 3

# Start frontend web server in a new window
Write-Host "2. Starting Frontend App (port 8080)..." -ForegroundColor Cyan
Start-Process powershell -ArgumentList "-NoExit", "-Command", "python app.py"
Start-Sleep -Seconds 2

Write-Host ""
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host " Services Started Successfully!" -ForegroundColor Green
Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("="*69) -ForegroundColor Cyan
Write-Host ""
Write-Host "Backend API:  http://localhost:5000" -ForegroundColor Yellow
Write-Host "Frontend App: http://localhost:8080" -ForegroundColor Yellow
Write-Host ""
Write-Host "Your browser should open automatically." -ForegroundColor Gray
Write-Host "If not, navigate to: http://localhost:8080" -ForegroundColor Gray
Write-Host ""
Write-Host "Press Ctrl+C in each window to stop the servers." -ForegroundColor Gray
Write-Host ""
