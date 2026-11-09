@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo  農業水資源 RAG 系統
echo  使用免費 Ollama 本地模型
echo ========================================
echo.

REM 檢查 Ollama 是否運行
echo 檢查 Ollama 服務狀態...
timeout /t 1 /nobreak >nul
curl -s http://localhost:11434/api/tags >nul 2>&1

if errorlevel 1 (
    echo.
    echo ERROR: Ollama 未運行！
    echo.
    echo 請先：
    echo 1. 打開 Ollama 應用
    echo 2. 在命令行運行：ollama run mistral
    echo 3. 等待模型加載完成
    echo 4. 然後重新運行此批處理文件
    echo.
    echo 無法連接到 http://localhost:11434
    echo.
    pause
    exit /b 1
)

echo OK: Ollama 已運行
echo.
echo 啟動 RAG 應用...
echo 應用地址：http://localhost:8501
echo.

streamlit run app.py

pause
