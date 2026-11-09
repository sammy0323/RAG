import os
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from config import CHROMA_DB_PATH, PDF_FOLDER_PATH


def load_documents(folder_path: str):
    """Load all PDF and TXT files from specified folder"""
    documents = []
    
    # Load PDF files
    pdf_files = list(Path(folder_path).glob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files")
    
    for pdf_file in pdf_files:
        print(f"Loading: {pdf_file.name}")
        try:
            loader = PyPDFLoader(str(pdf_file))
            docs = loader.load()
            documents.extend(docs)
            print(f"  Loaded {len(docs)} pages")
        except Exception as e:
            print(f"  Error loading PDF: {e}")
    
    # Load TXT files from public_data folder
    public_data_path = Path(folder_path).parent / "public_data"
    if public_data_path.exists():
        txt_files = list(public_data_path.glob("*.txt"))
        print(f"Found {len(txt_files)} public TXT files")
        
        for txt_file in txt_files:
            print(f"Loading: {txt_file.name}")
            try:
                with open(txt_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                doc = Document(
                    page_content=content,
                    metadata={"source": txt_file.name}
                )
                documents.append(doc)
                print(f"  Loaded public data file")
            except Exception as e:
                print(f"  Error loading TXT: {e}")
    
    return documents


def split_documents(documents, chunk_size: int = 1000, chunk_overlap: int = 200):
    """Split documents into smaller chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""]
    )
    
    split_docs = text_splitter.split_documents(documents)
    print(f"Document splitting complete: {len(split_docs)} chunks")
    return split_docs


def create_vector_store(documents, persist_directory: str = CHROMA_DB_PATH):
    """Create vector store"""
    embeddings = OpenAIEmbeddings()
    
    # Create or load Chroma vector store
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
