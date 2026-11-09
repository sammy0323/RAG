import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from config import CHROMA_DB_PATH, PDF_FOLDER_PATH


def load_pdfs(folder_path: str):
    """從指定資料夾加載所有 PDF 文件"""
    documents = []
    pdf_files = list(Path(folder_path).glob("*.pdf"))
    
    print(f"找到 {len(pdf_files)} 個 PDF 文件")
    
    for pdf_file in pdf_files:
        print(f"正在加載: {pdf_file.name}")
        loader = PyPDFLoader(str(pdf_file))
        docs = loader.load()
        documents.extend(docs)
        print(f"  已加載 {len(docs)} 頁")
    
    return documents


def split_documents(documents, chunk_size: int = 1000, chunk_overlap: int = 200):
    """分割文檔為更小的塊"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    
    split_docs = text_splitter.split_documents(documents)
    print(f"文檔分割完成: {len(split_docs)} 個塊")
    return split_docs


def create_vector_store(documents, persist_directory: str = CHROMA_DB_PATH):
    """創建向量存儲"""
    embeddings = OpenAIEmbeddings()
    
    # 創建或加載 Chroma 向量存儲
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=persist_directory
    )
    
    return vector_store


def load_vector_store(persist_directory: str = CHROMA_DB_PATH):
    """加載現有的向量存儲"""
    if not os.path.exists(persist_directory):
        raise FileNotFoundError(f"向量存儲不存在於 {persist_directory}")
    
    embeddings = OpenAIEmbeddings()
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    return vector_store


def initialize_vector_store(folder_path: str = PDF_FOLDER_PATH):
    """初始化向量存儲的主函數"""
    # 檢查是否已存在向量存儲
    if os.path.exists(CHROMA_DB_PATH):
        print("向量存儲已存在，正在加載...")
        return load_vector_store()
    
    # 否則創建新的向量存儲
    print("創建新向量存儲...")
    documents = load_pdfs(folder_path)
    split_docs = split_documents(documents)
    vector_store = create_vector_store(split_docs)
    
    return vector_store
