import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
"""Offline validation that does not require SQL Server or an LLM."""
import compileall
import re
from pathlib import Path
from registry.loader import load_registry
from registry.validator import validate_master

if __name__ == "__main__":
    ok = compileall.compile_dir(".", quiet=1, force=True, rx=re.compile(r"(^|[/\\])(\.venv|__pycache__)([/\\]|$)"))
    master = load_registry()
    errors = validate_master(master)
    print({"python_compile": ok, "registry_errors": errors,
           "dataset_count": len(master.get("_loaded_datasets", {})),
           "database_test": "not_run", "llm_test": "not_run"})
    if not ok or errors: raise SystemExit(1)
