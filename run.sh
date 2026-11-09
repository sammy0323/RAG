#!/bin/bash
# RAG 應用啟動腳本

echo "🌾 農業水資源 RAG 問答系統 - 啟動中..."
echo ""

# 檢查 .env 文件
if [ ! -f .env ]; then
    echo "⚠️  未找到 .env 文件"
    echo "正在從 .env.example 創建 .env 文件..."
    cp .env.example .env
    echo "✅ .env 文件已創建"
    echo ""
    echo "⚠️  請編輯 .env 文件，設置你的 OPENAI_API_KEY"
    echo "然後重新運行此腳本"
    exit 1
fi

# 檢查 API Key
if grep -q "sk-your-api-key-here" .env; then
    echo "❌ 錯誤: 請先設置 OPENAI_API_KEY"
    echo "編輯 .env 文件，替換 sk-your-api-key-here 為你的實際 API Key"
    exit 1
fi

# 啟動 Streamlit 應用
echo "✅ 正在啟動 Streamlit 應用..."
echo "🌐 打開瀏覽器訪問: http://localhost:8501"
echo ""

streamlit run app.py
