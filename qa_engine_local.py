# 本地模型配置（免費替代方案）
# 用此配置替換 qa_engine.py 中的 LLM 配置

# 選項 1：使用 Ollama（推薦）
# 需要先安裝 Ollama：https://ollama.ai/
# 然後在命令行運行：ollama run llama2

from langchain_community.llms import Ollama

def create_qa_chain_local(vector_store):
    """Create QA chain using local Ollama model (free)"""
    
    # 使用本地 Llama2 模型
    llm = Ollama(
        model="llama2",
        base_url="http://localhost:11434"  # Ollama 默認端口
    )
    
    from langchain_core.prompts import PromptTemplate
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.runnables import RunnablePassthrough
    
    template = """Use the following retrieved information to answer the question.
    If you don't know the answer, say "I don't know", don't make up an answer.
    Answer in Traditional Chinese.

    Document excerpts:
    {context}

    Question: {question}
    
    Detailed answer:"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    retriever = vector_store.as_retriever(search_kwargs={"k": 5})
    
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)
    
    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    
    # Store retriever
    class LocalRAGChain:
        def __init__(self, chain, retriever):
            self.chain = chain
            self.retriever = retriever
        
        def invoke(self, question: str) -> str:
            return self.chain.invoke(question)
    
    return LocalRAGChain(chain, retriever)
