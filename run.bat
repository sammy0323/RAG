@echo off
REM RAG 應用啟動腳本 (Windows 批處理文件)

echo.
echo 🌾 農業水資源 RAG 問答系統 - 啟動中...
echo.

REM 檢查 .env 文件
if not exist ".env" (
    echo ⚠️  未找到 .env 文件
    echo 正在從 .env.example 創建 .env 文件...
    copy ".env.example" ".env"
    echo ✅ .env 文件已創建
    echo.
    echo ⚠️  請編輯 .env 文件，設置你的 OPENAI_API_KEY
    echo 然後重新運行此批處理文件
    pause
    exit /b 1
)

REM 檢查 API Key
findstr /M "sk-your-api-key-here" .env >nul
if %errorlevel% equ 0 (
    echo ❌ 錯誤: 請先設置 OPENAI_API_KEY
    echo 編輯 .env 文件，替換 sk-your-api-key-here 為你的實際 API Key
    pause
    exit /b 1
)

REM 啟動 Streamlit 應用
echo ✅ 正在啟動 Streamlit 應用...
echo 🌐 打開瀏覽器訪問: http://localhost:8501
echo.

streamlit run app.py
