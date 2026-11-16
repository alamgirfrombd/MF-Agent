# MF Agent — Developer Instructions

## Create and activate the virtual environment (Windows PowerShell)

```powershell
cd D:\path\to\MF-Agent
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
```

If PowerShell blocks activation, use this temporary current-session setting only when permitted by your organization's policy:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Copy `.env.example` to `.env`, then edit the SQL Server settings. Never share `.env` or commit it to Git.

## Validation

```powershell
python scripts/validate_project.py
python -m pytest -q
python scripts/health_check.py
python scripts/discover_schema.py
```

The database checks require the Microsoft ODBC Driver configured in `.env` and a reachable SQL Server.
