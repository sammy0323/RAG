"""
Test RAG System - Check if vector store is working
"""
import os
from dotenv import load_dotenv

os.chdir(r"C:\Users\small12321\Desktop\RAG")
load_dotenv()

try:
    from document_processor import load_vector_store
    from qa_engine import create_qa_chain, answer_question
    
    print("Loading vector store...")
    vector_store = load_vector_store()
    
    # Test retrieval
    print("\nTesting retrieval with a simple query...")
    test_query = "water resources"
    docs = vector_store.similarity_search(test_query, k=3)
    
    print(f"\nFound {len(docs)} documents:")
    for i, doc in enumerate(docs, 1):
        print(f"\n[Document {i}]")
        print(f"Source: {doc.metadata.get('source', 'Unknown')}")
        print(f"Page: {doc.metadata.get('page', 'Unknown')}")
        print(f"Content preview: {doc.page_content[:150]}...")
    
    if len(docs) == 0:
        print("\nERROR: No documents found in vector store!")
        print("Possible causes:")
        print("1. PDF files not loaded correctly")
        print("2. Text chunking failed")
        print("3. Vector embedding failed")
    else:
        print("\nOK: Vector store is working")
        
        # Test QA chain
        print("\n\nTesting QA chain...")
        qa_chain = create_qa_chain(vector_store)
        
        test_question = "What is water resource?"
        result = answer_question(qa_chain, test_question)
        
        print(f"\nQuestion: {test_question}")
        print(f"Answer: {result['answer']}")
        print(f"\nUsed {len(result['source_documents'])} source documents")

except Exception as e:
    print(f"ERROR: {str(e)}")
    import traceback
    traceback.print_exc()
