@echo off
REM Deployment script for Market Classifier to Render (Windows)

echo ==========================================
echo Market Classifier - Render Deployment
echo ==========================================
echo.

REM Check if git is initialized
if not exist .git (
    echo Initializing git repository...
    git init
    echo Git initialized
) else (
    echo Git already initialized
)

REM Add all files
echo.
echo Adding files to git...
git add .
echo Files added

REM Commit
echo.
echo Committing changes...
git commit -m "Deploy to Render - %date%"
echo Changes committed

REM Add remote if not exists
echo.
echo Setting up remote repository...
git remote | findstr origin >nul
if errorlevel 1 (
    git remote add origin https://github.com/canvameet/marketclassifer.git
    echo Remote added
) else (
    echo Remote already exists
)

REM Push to GitHub
echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main
echo Pushed to GitHub

echo.
echo ==========================================
echo Deployment Preparation Complete!
echo ==========================================
echo.
echo Next Steps:
echo 1. Go to https://dashboard.render.com/
echo 2. Click 'New +' -^> 'Blueprint'
echo 3. Connect: https://github.com/canvameet/marketclassifer
echo 4. Click 'Apply'
echo.
echo Your app will be live in 3-5 minutes at:
echo https://market-classifier-api.onrender.com
echo.
echo ==========================================
pause
