@echo off
REM RAG 應用啟動腳本 - 使用本地免費模型

echo.
echo ========================================
echo 農業水資源 RAG 問答系統
echo 使用免費本地 AI 模型
echo ========================================
echo.

REM 檢查 Ollama 是否運行
echo 檢查 Ollama 服務...
curl -s http://localhost:11434/api/tags >nul 2>&1

if errorlevel 1 (
    echo.
    echo ❌ 錯誤：Ollama 未運行！
    echo.
    echo 請先：
    echo 1. 下載 Ollama：https://ollama.ai/download
    echo 2. 安裝並打開 Ollama
    echo 3. 在命令行運行：ollama run mistral
    echo 4. 等待模型下載完成（3-5 分鐘）
    echo 5. 然後重新運行此腳本
    echo.
    pause
    exit /b 1
)

echo ✅ Ollama 已運行
echo.
echo 正在啟動 RAG 應用...
echo 🌐 應用地址：http://localhost:8501
echo.

streamlit run app.py
