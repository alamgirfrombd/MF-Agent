"""Loads the master registry and referenced dataset definitions."""
import json
from pathlib import Path
from app.config import get_settings

class RegistryError(ValueError):
    pass

def load_registry(master_path: str | Path | None = None) -> dict:
    settings = get_settings()
    path = Path(master_path) if master_path else settings.resolve_path(settings.registry_path)
    if not path.is_absolute():
        path = settings.root_dir / path
    master = json.loads(path.read_text(encoding="utf-8"))
    datasets = {}
    for item in master.get("datasets", []):
        dataset_path = (path.parent / item["path"]).resolve()
        # Legacy master paths point to registries/; new paths resolve from registry/.
        if not dataset_path.exists():
            candidate = settings.root_dir / "registries" / Path(item["path"]).name
            if candidate.exists():
                dataset_path = candidate
        if not dataset_path.exists():
            raise RegistryError(f"Dataset registry not found: {item['dataset_id']}")
        datasets[item["dataset_id"]] = json.loads(dataset_path.read_text(encoding="utf-8"))
    master["_loaded_datasets"] = datasets
    return master
