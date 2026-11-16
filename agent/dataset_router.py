"""Conservative dataset routing; ambiguous questions should be clarified by the planner."""
from registry.loader import load_registry

def get_dataset_catalog() -> list[dict]:
    master = load_registry()
    return [{"dataset_id": item["dataset_id"],
             "description": master["_loaded_datasets"].get(item["dataset_id"], {}).get("description", ""),
             "status": master["_loaded_datasets"].get(item["dataset_id"], {}).get("status", item.get("status", "draft"))}
            for item in master.get("datasets", [])]
