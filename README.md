cd D:\MF-Agent

# Install dependencies
.\.venv\Scripts\python.exe -m pip install -r requirements.txt

# Validate project
.\.venv\Scripts\python.exe scripts\validate_project.py

# Run tests
.\.venv\Scripts\python.exe -m pytest -q

# Run application (যখন প্রস্তুত হবে)
.\.venv\Scripts\python.exe -m streamlit run ui\dashboard.py


cd D:\MF-Agent

git config --global user.name "alamgirfrombd"
git config --global user.email "alamgirfrombd@gmail.com"

git status
git add .
git commit -m "Update MF Agent infrastructure and project architecture"