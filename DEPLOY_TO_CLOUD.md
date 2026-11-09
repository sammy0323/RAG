# 🚀 部署到 Streamlit Cloud 指南

## 前置準備

### 1️⃣ 創建 GitHub 帳號
- 訪問：https://github.com/signup
- 創建帳號

### 2️⃣ 安裝 Git
- Windows: https://git-scm.com/download/win
- 選擇默認選項安裝

### 3️⃣ 設置 Git 用戶信息
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## 部署步驟

### 步驟 1：初始化 Git 倉庫
```bash
cd C:\Users\small12321\Desktop\RAG
git init
git add .
git commit -m "Initial RAG System commit"
git branch -M main
```

### 步驟 2：在 GitHub 上創建新倉庫
1. 訪問：https://github.com/new
2. Repository name: `RAG` (或您喜歡的名稱)
3. 選擇 Public（讓其他人能訪問）
4. 點擊「Create repository」

### 步驟 3：推送代碼到 GitHub
```bash
git remote add origin https://github.com/YOUR_USERNAME/RAG
git push -u origin main
```
（將 `YOUR_USERNAME` 替換為您的 GitHub 用戶名）

### 步驟 4：部署到 Streamlit Cloud
1. 訪問：https://streamlit.io/cloud
2. 點擊「New app」
3. 選擇：
   - **GitHub repo**: 您的倉庫
   - **Branch**: main
   - **Main file path**: app.py
4. 點擊「Deploy」

## 設置環境變量

### 在 Streamlit Cloud 上設置 OpenAI API Key
1. 部署後，點擊右上角「Manage app」
2. 進入「Settings」→「Secrets」
3. 添加以下內容：
```
OPENAI_API_KEY=sk-proj-YOUR_API_KEY_HERE
```

## 完成！

應用將在以下網址訪問：
```
https://YOUR_USERNAME-rag.streamlit.app
```

您可以將此鏈接分享給任何人！

## 常見問題

### Q: 會收費嗎？
A: Streamlit Cloud 免費版本每月有使用限制，但對大多數用戶夠用了。

### Q: 數據會洩露嗎？
A: 不會。您的 PDF 只會在雲端服務器上，API Key 使用 Secrets 安全存儲。

### Q: 如何停止應用？
A: 在 Streamlit Cloud 儀表板上點擊「Apps」→ 您的應用 → 點擊更多選項 → 「Delete app」

## 需要幫助？
- Streamlit Cloud 文檔：https://docs.streamlit.io/streamlit-cloud
- GitHub 幫助：https://docs.github.com
