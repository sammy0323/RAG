# OpenAI API 額度用完的解決方案

## ❌ 問題
您的 OpenAI API 額度已用完（credit_balance_exhausted）

## ✅ 解決方案

### 方案 1：為 OpenAI 帳戶充值（推薦，5-10 分鐘解決）

**步驟：**
1. 訪問：https://platform.openai.com/settings/organization/billing/overview
2. 登錄您的 OpenAI 帳戶
3. 點擊「Add to credit balance」或前往「Billing」
4. 添加信用卡信息
5. 充值金額（建議先充 $5-10 測試）
6. 等待 5-10 分鐘
7. 返回您的應用，點擊「刷新」或重新提問

**成本估算：**
- 向量化 PDF：~$0.03
- 每次提問：~$0.001-0.01
- 100 次提問：~$3-10

### 方案 2：使用免費本地模型（無需付費）

**需要：**
- Ollama（免費開源本地 LLM）
- ~8GB RAM
- ~5 分鐘安裝時間

**安裝步驟：**

1. **下載 Ollama**
   - 訪問：https://ollama.ai/
   - 下載 Windows 版本
   - 安裝並運行

2. **在命令行運行 Llama2 模型**
   ```bash
   ollama run llama2
   ```
   第一次運行會下載模型（~4GB，需要 10-15 分鐘）

3. **更新應用配置**
   
   編輯 `qa_engine.py` 文件，替換以下代碼：
   
   ```python
   # 改為使用本地模型
   from langchain_community.llms import Ollama
   
   llm = Ollama(
       model="llama2",
       base_url="http://localhost:11434"
   )
   ```

4. **重啟應用**
   ```bash
   streamlit run app.py
   ```

**優點：**
- ✅ 完全免費
- ✅ 本地運行，隱私有保障
- ✅ 無需網絡連接（除了首次下載模型）

**缺點：**
- ⚠️ 速度較慢（CPU 限制）
- ⚠️ 需要較多內存
- ⚠️ 模型質量略低於 GPT-4

### 方案 3：使用其他免費 LLM 服務

**Hugging Face 免費 API（Limited）：**
```python
from langchain_huggingface import HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-2-7b-chat-hf",
    task="text-generation",
    max_length=2048,
    temperature=0.7,
)
```

## 📊 成本比較

| 方案 | 成本 | 速度 | 質量 | 設置難度 |
|------|------|------|------|---------|
| OpenAI GPT-3.5 | $0.001-0.01/次 | 快（2-5s） | 高 | 容易 |
| Ollama Llama2 | 免費 | 慢（30-60s） | 中 | 中等 |
| Hugging Face | 免費 | 快（取決於網絡） | 中 | 中等 |

## 🔧 推薦方案排序

1. **最好**：為 OpenAI 充值 $5-10（最快最簡單）
2. **次好**：使用 Ollama 本地模型（完全免費）
3. **備選**：使用 Hugging Face API（有限制）

## ❓ 常見問題

**Q：需要花多少錢？**
A：取決於使用量。初期測試建議充 $5-10。

**Q：可以只充一點錢嗎？**
A：可以。建議先充 $5，夠用來初始化和做幾十次查詢測試。

**Q：向量化完成後還需要付費嗎？**
A：是的。每次生成答案時都要調用 LLM，都會產生費用。

**Q：本地模型會很慢嗎？**
A：會。Llama2 通常需要 30-60 秒生成答案，而 GPT-3.5 只需 2-5 秒。

**Q：可以同時使用多個模型嗎？**
A：可以。您可以在應用中添加模型選擇下拉菜單。

## 💡 建議

- 如果您有預算，**充值 OpenAI**（最好的體驗）
- 如果您想免費使用，**安裝 Ollama**（需要等待，但完全免費）
- 如果您只想快速測試，**充值 $5-10**（夠用一陣子）

---

需要幫助嗎？告訴我您選擇哪個方案，我會幫您配置！
