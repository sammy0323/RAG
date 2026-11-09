"""
Test RAG System Script
Verify all components are correctly installed and configured
"""

import sys
import os
from pathlib import Path

print("=" * 60)
print("RAG System Check")
print("=" * 60)

# 1. Check environment variables
print("\n[1/5] Checking environment variables...")
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if api_key and api_key != "sk-your-api-key-here":
    print("OK: OPENAI_API_KEY is set")
else:
    print("FAILED: OPENAI_API_KEY not set or invalid")
    print("   Please edit .env file and set your OpenAI API Key")
    sys.exit(1)

# 2. Check PDF files
print("\n[2/5] Checking PDF files...")
pdf_files = list(Path(".").glob("*.pdf"))
if pdf_files:
    print(f"OK: Found {len(pdf_files)} PDF file(s):")
    for pdf in pdf_files:
        print(f"   - {pdf.name}")
else:
    print("FAILED: No PDF files found")
    print("   Please place PDF files in the project root directory")
    sys.exit(1)

# 3. Check required Python modules
print("\n[3/5] Checking Python modules...")
required_modules = [
    "streamlit",
    "langchain",
    "chromadb",
    "pypdf",
    "openai",
    "pydantic"
]

missing_modules = []
for module in required_modules:
    try:
        __import__(module)
        print(f"OK: {module}")
    except ImportError:
        print(f"FAILED: {module}")
        missing_modules.append(module)

if missing_modules:
    print(f"\nFAILED: Missing modules: {', '.join(missing_modules)}")
    print("Please run: pip install -r requirements.txt")
    sys.exit(1)

# 4. Check config file
print("\n[4/5] Checking configuration files...")
try:
    from config import OPENAI_API_KEY, CHROMA_DB_PATH, PDF_FOLDER_PATH
    print("OK: config.py imported successfully")
except Exception as e:
    print(f"FAILED: config.py import failed: {e}")
    sys.exit(1)

# 5. Check core modules
print("\n[5/5] Checking core modules...")
try:
    from document_processor import initialize_vector_store, load_pdfs, split_documents
    print("OK: document_processor.py imported successfully")
except Exception as e:
    print(f"FAILED: document_processor.py import failed: {e}")
    sys.exit(1)

try:
    from qa_engine import create_qa_chain, answer_question
    print("OK: qa_engine.py imported successfully")
except Exception as e:
    print(f"FAILED: qa_engine.py import failed: {e}")
    sys.exit(1)

print("\n" + "=" * 60)
print("OK: All checks passed! System is ready.")
print("=" * 60)
print("\nNext steps:")
print("1. Run: streamlit run app.py")
print("2. Or run: run.bat (Windows) or run.sh (Linux/Mac)")
print("3. Open browser: http://localhost:8501")
print("\nOn first run, click 'Initialize/Reload Vector Store'")
print("System will automatically process PDFs and create vector store.\n")
