# RAG 系統 - 農業水資源問答助手

這是一個基於 **LangChain + Streamlit + Chroma + OpenAI** 的 RAG（檢索增強生成）問答系統。

## 📋 系統架構

```
PDF 文檔
   ↓
[文檔加載] → [分割文本] → [生成向量] → [存儲 Chroma]
                                          ↓
                                    [向量檢索]
                                          ↓
用戶問題 → [檢索相關文檔] → [LLM 生成回答] → 答案 + 源文檔
```

## 🚀 快速開始

### 1. 安裝依賴
```bash
pip install -r requirements.txt
```

### 2. 設置環境變量
在專案根目錄創建 `.env` 文件：
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. 運行應用
```bash
streamlit run app.py
```

應用會在 `http://localhost:8501` 開啟。

## 📁 項目結構

```
.
├── requirements.txt           # Python 依賴
├── config.py                 # 配置文件
├── document_processor.py      # PDF 加載和向量化
├── qa_engine.py              # QA 鏈和回答邏輯
├── app.py                    # Streamlit 前端
├── chroma_db/                # Chroma 向量存儲（自動生成）
└── README.md                 # 本文件
```

## 🔧 核心模組說明

### `config.py`
- 管理環境變量和配置參數
- OpenAI API Key 設置

### `document_processor.py`
- `load_pdfs()`: 加載 PDF 文件
- `split_documents()`: 將文本分割為可管理的塊
- `create_vector_store()`: 創建 Chroma 向量存儲
- `initialize_vector_store()`: 主初始化函數

### `qa_engine.py`
- `create_qa_chain()`: 創建 RetrievalQA 鏈
- `answer_question()`: 處理用戶問題並返回答案

### `app.py`
- Streamlit UI 實現
- 聊天介面
- 對話歷史管理
- 源文檔查看功能

## 💡 使用示例

1. 首次運行時，點擊側邊欄的「初始化/重新加載向量存儲」
2. 等待系統處理 PDF 文件
3. 在文本框輸入問題，例如：
   - "農業水資源的主要應用是什麼？"
   - "項目的期末報告中提到了哪些內容？"
   - "水資源管理的重點工作有哪些？"

## ⚙️ 調整參數

### 向量化參數 (document_processor.py)
- `chunk_size`: 文本塊大小（默認 1000 字符）
- `chunk_overlap`: 塊之間的重疊（默認 200 字符）

### LLM 參數 (qa_engine.py)
- `model_name`: 使用的模型（默認 gpt-3.5-turbo）
- `temperature`: 生成多樣性（0-1，默認 0.7）
- `max_tokens`: 最大輸出 token（默認 2048）

### 檢索參數 (qa_engine.py)
- `search_kwargs={"k": 5}`: 檢索的相關文檔數量

## 📝 注意事項

1. **API 成本**: 此系統使用 OpenAI API，每次查詢都會產生費用
2. **首次加載**: 首次運行需要時間處理 PDF 和創建向量存儲
3. **PDF 格式**: 確保 PDF 文件為可讀取的文本格式
4. **中文支持**: 系統完全支持繁體中文

## 🔍 故障排除

### 問題：OpenAI API 錯誤
- 檢查 `.env` 文件中的 API Key 是否正確

### 問題：PDF 加載失敗
- 確保 PDF 文件在正確的目錄中
- 檢查 PDF 文件是否損壞

### 問題：向量存儲錯誤
- 刪除 `chroma_db` 資料夾，重新初始化

## 📚 技術棧

- **LangChain**: LLM 應用框架
- **Streamlit**: 快速構建 Web UI
- **Chroma**: 向量數據庫
- **OpenAI**: LLM 引擎
- **PyPDF**: PDF 解析

## 📄 許可證

MIT License
