"""Streamlit application launcher."""
from pathlib import Path
import subprocess
import sys

if __name__ == "__main__":
    ui_file = Path(__file__).parent / "ui" / "dashboard.py"
    raise SystemExit(subprocess.call([sys.executable, "-m", "streamlit", "run", str(ui_file)]))
