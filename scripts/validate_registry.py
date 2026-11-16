import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from registry.loader import load_registry
from registry.validator import validate_master

if __name__ == "__main__":
    master = load_registry()
    errors = validate_master(master)
    if errors:
        print("Registry validation issues:")
        for error in errors: print(" -", error)
        raise SystemExit(1)
    print("Registry structure is valid. Note: this does not verify SQL schema or business rules.")
