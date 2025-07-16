@echo off
echo ============================
echo Building Docker image...
echo ============================
docker build -t metaflow-pipeline .

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Error building Docker image.
    exit /b %ERRORLEVEL%
)

echo.
echo ============================
echo Running Metaflow pipeline...
echo ============================
docker run --rm metaflow-pipeline

IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Error running Metaflow pipeline.
    exit /b %ERRORLEVEL%
)

echo.
echo ✅ Pipeline executed successfully.
pause
