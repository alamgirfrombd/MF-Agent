cd D:\MF-Agent

# Install dependencies
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# Validate project
.\.venv\Scripts\python.exe scripts\validate_project.py

# Run tests
.\.venv\Scripts\python.exe -m pytest -q

# Run application (যখন প্রস্তুত হবে)
.\.venv\Scripts\python.exe -m streamlit run ui\dashboard.py