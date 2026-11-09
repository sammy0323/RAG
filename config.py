import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CHROMA_DB_PATH = "./chroma_db"
PDF_FOLDER_PATH = "./"

# 如果未設置 API key，使用默認值
if not OPENAI_API_KEY:
    raise ValueError("請設置環境變量 OPENAI_API_KEY")
