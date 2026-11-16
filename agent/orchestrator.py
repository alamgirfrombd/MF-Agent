"""Initial orchestration boundary; execution is disabled until a dataset is verified."""
from registry.loader import load_registry
from registry.validator import validate_dataset

def available_datasets() -> list[dict]:
    master = load_registry()
    result = []
    for item in master.get("datasets", []):
        ds = master["_loaded_datasets"].get(item["dataset_id"], {})
        result.append({"dataset_id": item["dataset_id"], "status": ds.get("status", item.get("status")),
                       "description": ds.get("description", ""),
                       "validation_errors": validate_dataset(ds)})
    return result

def ensure_dataset_executable(dataset: dict) -> None:
    errors = validate_dataset(dataset)
    if errors:
        raise ValueError("Registry validation failed: " + "; ".join(errors))
    if dataset.get("status") != "active":
        raise PermissionError("Dataset is not active; schema and business rules must be verified first")
