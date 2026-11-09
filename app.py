import streamlit as st
from document_processor import initialize_vector_store
from qa_engine import create_qa_chain, answer_question

# 頁面配置
st.set_page_config(
    page_title="農業水資源 RAG 問答系統",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌾 農業水資源 RAG 問答系統")
st.markdown("---")

# 初始化 session state
if "qa_chain" not in st.session_state:
    st.session_state.qa_chain = None
    st.session_state.vector_store = None
    st.session_state.chat_history = []

# 側邊欄
with st.sidebar:
    st.header("⚙️ 系統設置")
    
    if st.button("🔄 初始化/重新加載向量存儲", use_container_width=True):
        with st.spinner("正在處理 PDF 文件和創建向量存儲..."):
            try:
                st.session_state.vector_store = initialize_vector_store()
                st.session_state.qa_chain = create_qa_chain(st.session_state.vector_store)
                st.success("✅ 向量存儲初始化成功！")
            except Exception as e:
                st.error(f"❌ 初始化失敗: {str(e)}")
    
    if st.button("🗑️ 清除對話歷史", use_container_width=True):
        st.session_state.chat_history = []
        st.success("✅ 對話歷史已清除")
    
    st.markdown("---")
    st.markdown("""
    ### 📖 使用說明
    1. 點擊「初始化/重新加載向量存儲」
    2. 在下方輸入框提問
    3. 系統會檢索相關文檔並生成答案
    4. 可查看源文檔參考
    """)

# 主要內容區域
# 首先嘗試自動初始化
if st.session_state.qa_chain is None:
    with st.spinner("首次初始化向量存儲..."):
        try:
            st.session_state.vector_store = initialize_vector_store()
            st.session_state.qa_chain = create_qa_chain(st.session_state.vector_store)
            st.success("✅ 向量存儲已加載！")
        except Exception as e:
            st.error(f"❌ 無法初始化系統: {str(e)}")
            st.info("請確保已設置 OPENAI_API_KEY 環境變量")
            st.stop()

# 聊天介面
st.markdown("### 💬 提問")

# 顯示對話歷史
if st.session_state.chat_history:
    with st.container():
        for message in st.session_state.chat_history:
            if message["type"] == "user":
                st.markdown(f"👤 **用戶**: {message['content']}")
            else:
                st.markdown(f"🤖 **助手**: {message['content']}")
                if message.get("sources"):
                    with st.expander("📄 查看源文檔"):
                        for i, doc in enumerate(message["sources"], 1):
                            st.markdown(f"**文檔 {i}**")
                            st.markdown(f"- 來源: {doc.metadata.get('source', '未知')}")
                            st.markdown(f"- 頁碼: {doc.metadata.get('page', '未知')}")
                            st.markdown(f"- 內容: {doc.page_content[:200]}...")
            st.markdown("---")

# 輸入框
col1, col2 = st.columns([5, 1])

with col1:
    user_question = st.text_input(
        "請輸入您的問題",
        placeholder="例如：農業水資源的主要應用是什麼？",
        key="question_input"
    )

with col2:
    submit_button = st.button("提交", use_container_width=True, type="primary")

# 處理提交
if submit_button and user_question:
    # 添加用戶問題到歷史
    st.session_state.chat_history.append({
        "type": "user",
        "content": user_question
    })
    
    with st.spinner("🔍 正在檢索相關信息和生成回答..."):
        try:
            result = answer_question(st.session_state.qa_chain, user_question)
            
            # 添加助手回答到歷史
            st.session_state.chat_history.append({
                "type": "assistant",
                "content": result["answer"],
                "sources": result["source_documents"]
            })
            
            st.rerun()
        except Exception as e:
            st.error(f"❌ 處理問題時出錯: {str(e)}")

# 頁腳
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    農業水資源業務推動及基礎資料協作服務計畫 | 由 OpenAI GPT 驅動
</div>
""", unsafe_allow_html=True)
