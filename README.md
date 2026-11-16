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


cd D:\MF-Agent

# Correct GitHub remote URL
                git remote set-url origin https://github.com/alamgirfrombd/MF-Agent.git

                # Verify remote
                git remote -v

                # Push project
                git push -u origin main

                git add .
                git commit -m "Update MF Agent"

                git pushgit add .
                git commit -m "Update MF Agent"
                git push




# অনুশীলন: Qwen Model-এর বাংলা বোঝার ক্ষমতা পরীক্ষা
    ১. প্রথমে Installed Model দেখুন
    PowerShell Terminal খুলে লিখুন: ollama list

# oollama list
    ollama run qwen2.5-coder:3b
    ২০২৫ সালে মোট ঋণ বিতরণ কত?

        উত্তর দেওয়ার আগে বলুন:
        ১. এই প্রশ্নের উত্তর দিতে কী কী তথ্য প্রয়োজন?
        ২. কোন Database Table প্রয়োজন হতে পারে?
        ৩. কোন Column প্রয়োজন?
        ৪. কীভাবে মোট ঋণ বিতরণের হিসাব করবেন?
        ৫. তথ্য না থাকলে অনুমান করে উত্তর দেবেন না।

