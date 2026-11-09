# 快速開始指南 - 農業水資源 RAG 問答系統

## ✅ 系統已準備好！

您的 RAG 系統已全部設置完成。以下是如何開始使用的步驟。

## 🚀 啟動應用

### 方法 1：使用批處理文件（推薦 Windows 用戶）

```bash
# 雙擊或在命令行運行
run.bat
```

### 方法 2：直接運行 Streamlit

```bash
streamlit run app.py
```

### 方法 3：使用 Shell 腳本（Linux/Mac）

```bash
bash run.sh
```

## 🌐 打開應用

運行以上任一命令後，您的瀏覽器會自動打開，或手動訪問：

```
http://localhost:8501
```

## 📖 使用步驟

### 第一次使用

1. **初始化向量存儲**
   - 打開應用後，點擊左側邊欄中的「Initialize/Reload Vector Store」按鈕
   - 系統會自動：
     - 加載所有 PDF 文件
     - 將文本分割成小塊
     - 生成向量並存儲在 Chroma 數據庫中
   - 首次運行可能需要 2-5 分鐘，請耐心等待

2. **提出問題**
   - 在文本框中輸入您的問題
   - 例如：
     - "農業水資源的主要應用是什麼？"
     - "項目報告中提到了哪些水利工程？"
     - "這個計畫的目標是什麼？"
   - 點擊「提交」按鈕

3. **查看答案和來源**
   - 系統會顯示 AI 生成的答案
   - 點擊「查看源文檔」可以看到答案參考的原始文本

### 後續使用

- **向量存儲已保存**：第二次及以後使用時，系統會直接加載已保存的向量存儲，啟動更快
- **清除歷史**：點擊「清除對話歷史」按鈕清空聊天記錄
- **重新索引**：如果更新了 PDF 文件，點擊「初始化/重新加載向量存儲」重新處理

## 🔧 系統配置

### 模型選擇

編輯 [qa_engine.py](qa_engine.py:5) 中的 `model_name` 來選擇 OpenAI 模型：

- `gpt-3.5-turbo`：快速且成本低（推薦）
- `gpt-4`：更準確但成本更高
- `gpt-4-turbo`：性能和成本的平衡

### 調整參數

#### 向量化參數（[document_processor.py](document_processor.py:25)）
- `chunk_size: 1000`：文本塊大小，值越小檢索越精準但速度越慢
- `chunk_overlap: 200`：塊之間的重疊，避免信息丟失

#### LLM 參數（[qa_engine.py](qa_engine.py:7)）
- `temperature: 0.7`：生成多樣性（0=確定性，1=隨機性）
- `max_tokens: 2048`：最大回答長度

#### 檢索參數（[qa_engine.py](qa_engine.py:31)）
- `search_kwargs={"k": 5}`：檢索相關文檔數量，更多 = 更多上下文但更慢

## 💰 成本估算

- **向量化**：使用 embedding-3-small 模型，成本很低
- **每次提問**：使用 gpt-3.5-turbo，約 $0.001-0.01 USD（取決於文本長度）
- **向量存儲**：本地存儲，無額外費用

## ❓ 常見問題

### Q：系統運行很慢怎麼辦？
A：
- 減小 `chunk_size` 的值（例如改為 500）
- 減少檢索的文檔數量 `k` 值（例如改為 3）
- 使用 gpt-3.5-turbo 而不是 gpt-4

### Q：答案不準確怎麼辦？
A：
- 增加檢索的文檔數量 `k` 值（例如改為 10）
- 提高 `temperature` 值（例如改為 0.9）
- 查看源文檔確認 PDF 中是否有相關信息

### Q：如何使用不同的 LLM？
A：編輯 [qa_engine.py](qa_engine.py) 中的 LLM 配置：
- 使用 Claude：改用 `ChatAnthropic`
- 使用本地模型：改用 `ChatOllama` 或其他本地模型

### Q：如何增加新的 PDF 文件？
A：
1. 將新 PDF 文件放在項目根目錄
2. 點擊「初始化/重新加載向量存儲」重新索引

### Q：向量存儲佔用多少空間？
A：根據 PDF 大小，通常為 10-100MB

## 🔒 隱私和安全

- **本地存儲**：所有向量和聊天歷史都存儲在本地
- **API 密鑰**：`.env` 文件不會被提交到版本控制
- **PDF 文檔**：不會被發送到 OpenAI，只有提取的文本被用於生成答案

## 📞 故障排除

### 無法連接到 OpenAI API
- 檢查 `.env` 文件中的 API 密鑰是否正確
- 檢查網絡連接
- 確認 API 配額未用完

### PDF 加載失敗
- 確保 PDF 文件未損壞
- 檢查 PDF 是否為文本格式（不是掃描圖像）
- 嘗試使用其他 PDF 查看器打開該文件

### Streamlit 無法啟動
- 刪除 `.streamlit` 目錄
- 運行 `pip install --upgrade streamlit`
- 重新啟動應用

### 向量存儲錯誤
- 刪除 `chroma_db` 目錄
- 運行 `streamlit run app.py` 重新創建

## 📚 更多資源

- [LangChain 文檔](https://python.langchain.com/)
- [Streamlit 文檔](https://docs.streamlit.io/)
- [Chroma 文檔](https://docs.trychroma.com/)
- [OpenAI API 文檔](https://platform.openai.com/docs/)

## 📝 項目結構

```
RAG/
├── app.py                      # Streamlit 主應用
├── document_processor.py       # PDF 加載和向量化
├── qa_engine.py               # QA 鏈和回答邏輯
├── config.py                  # 配置管理
├── check_setup.py            # 系統檢查腳本
├── requirements.txt          # Python 依賴
├── .env                       # 環境變量（不要提交）
├── .env.example              # 環境變量模板
├── .gitignore               # Git 忽略文件
├── run.bat                  # Windows 啟動腳本
├── run.sh                   # Linux/Mac 啟動腳本
├── README.md               # 項目文檔
├── QUICKSTART.md           # 本文件
├── chroma_db/              # 向量存儲（自動生成）
└── [PDF 文件]              # 您的 PDF 文檔
```

## 🎯 下一步

1. ✅ 已完成系統設置
2. ➡️ **現在**：運行 `streamlit run app.py` 或雙擊 `run.bat`
3. 📌 首次使用時，點擊「Initialize/Reload Vector Store」
4. 💬 開始提問！

祝您使用愉快！
