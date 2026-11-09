"""
Manually reinitialize vector store
"""
import os
from dotenv import load_dotenv

os.chdir(r"C:\Users\small12321\Desktop\RAG")
load_dotenv()

try:
    from document_processor import load_documents, split_documents, create_vector_store
    
    print("Step 1: Loading documents (PDF and TXT files)...")
    documents = load_documents(".")
    print(f"Loaded {len(documents)} documents")
    
    if len(documents) == 0:
        print("ERROR: No documents loaded!")
        exit(1)
    
    print("\nStep 2: Splitting documents into chunks...")
    split_docs = split_documents(documents)
    print(f"Created {len(split_docs)} text chunks")
    
    print("\nStep 3: Creating vector store...")
    vector_store = create_vector_store(split_docs)
    print("Vector store created successfully")
    
    print("\nStep 4: Testing vector store...")
    test_docs = vector_store.similarity_search("water", k=3)
    print(f"Found {len(test_docs)} documents in vector store")
    
    if len(test_docs) > 0:
        print("\nSample document:")
        print(f"Content: {test_docs[0].page_content[:200]}...")
        print("\nSUCCESS: Vector store is ready!")
    else:
        print("WARNING: Vector store is empty")

except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
