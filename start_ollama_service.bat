@echo off
REM 在背景執行 Ollama，不顯示終端
start "" /B ollama serve
REM 等待 Ollama 啟動
timeout /t 3 /nobreak
REM 啟動 Streamlit 應用
streamlit run app.py
pause
