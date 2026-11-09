# 🆓 免費本地 AI 模型設置 - 5 分鐘完成

## ✅ 您現在可以完全免費使用 RAG 系統！

### 📥 安裝步驟（總共 5 分鐘）

#### 1️⃣ 下載 Ollama（1 分鐘）
- 訪問：https://ollama.ai/download
- 選擇 Windows 版本下載
- 雙擊安裝，按默認選項安裝

#### 2️⃣ 啟動模型（3 分鐘下載）
打開 **命令提示符** 或 **PowerShell**，輸入：

```bash
ollama run mistral
```

或者，如果您想要更小的模型（更快但質量稍低）：

```bash
ollama run neural-chat
```

**第一次運行會下載模型（3-5 分鐘，約 4GB）**

#### 3️⃣ Streamlit 應用已經配置好了！

應用代碼已更新，現在使用 **免費的本地 Mistral 模型**。

只需：
```bash
streamlit run app.py
```

### 🎯 完整步驟

```
1. 打開 Ollama（https://ollama.ai/）
   ↓
2. 下載 Windows 版本
   ↓
3. 安裝並運行 Ollama
   ↓
4. 打開命令行，運行：ollama run mistral
   ↓
5. 等待 3-5 分鐘下載模型
   ↓
6. 運行 RAG 應用：streamlit run app.py
   ↓
7. 打開 http://localhost:8501
   ↓
8. 點擊「Initialize/Reload Vector Store」
   ↓
9. 開始提問！
```

### ⚡ 模型對比

| 模型 | 大小 | 速度 | 質量 | 推薦 |
|------|------|------|------|------|
| **mistral** | 4GB | 中 | 好 | ⭐⭐⭐⭐⭐ 推薦 |
| neural-chat | 3GB | 快 | 中 | ⭐⭐⭐⭐ |
| llama2 | 4GB | 慢 | 中 | ⭐⭐⭐ |

### 💰 成本對比

| 方案 | 成本 | 速度 | 質量 |
|------|------|------|------|
| OpenAI GPT-4o-mini | $付費 | 快（2-5s） | 很好 |
| Ollama Mistral | **免費** | 中等（10-30s） | 好 |
| 本地 Llama2 | 免費 | 慢（30-60s） | 中等 |

### ⚙️ 系統要求

- ✅ Windows 10 或更高版本
- ✅ 至少 8GB 內存
- ✅ 至少 10GB 硬盤空間
- ✅ 網絡連接（僅用於首次下載模型）

### 🆘 常見問題

**Q：模型下載會很慢嗎？**
A：取決於您的網速。通常 3-5 分鐘。

**Q：模型下載後需要一直連接網絡嗎？**
A：不需要。下載完成後，完全離線運行。

**Q：Ollama 會一直運行嗎？**
A：會。Ollama 在後台運行，您可以在系統托盤關閉它。

**Q：能同時使用多個模型嗎？**
A：可以。您可以用 `ollama run <model>` 切換模型。

**Q：回答速度會很慢嗎？**
A：會比 OpenAI 慢（10-30 秒），但完全免費且隱私有保障。

### 📋 快速命令參考

```bash
# 下載並運行 Mistral 模型
ollama run mistral

# 下載並運行 Neural-Chat 模型
ollama run neural-chat

# 查看已安裝的模型
ollama list

# 移除模型（釋放空間）
ollama rm mistral
```

### 🎬 現在開始

1. ✅ 下載 Ollama：https://ollama.ai/download
2. ✅ 運行：`ollama run mistral`
3. ✅ 等待模型下載完成
4. ✅ 運行：`streamlit run app.py`
5. ✅ 訪問：http://localhost:8501
6. ✅ 點擊「Initialize/Reload Vector Store」
7. ✅ 開始提問！

---

**完全免費，無需付費，無需 API key！** 🎉
