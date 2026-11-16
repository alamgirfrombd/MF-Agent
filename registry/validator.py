"""Structural validation. This does not certify database mappings or business logic."""
REQUIRED_DATASET_FIELDS = {"dataset_id", "status", "tables", "business_rules", "approved_metrics"}

def validate_dataset(dataset: dict) -> list[str]:
    errors = []
    missing = REQUIRED_DATASET_FIELDS - dataset.keys()
    if missing:
        errors.append(f"Missing fields: {', '.join(sorted(missing))}")
    if dataset.get("status") not in {"draft", "review", "active", "disabled"}:
        errors.append("Invalid status")
    if not isinstance(dataset.get("tables", []), list):
        errors.append("tables must be a list")
    for table in dataset.get("tables", []):
        if not table.get("logical_name"):
            errors.append("Each table requires logical_name")
        if dataset.get("status") == "active" and not table.get("sql_table"):
            errors.append(f"Active dataset has an unmapped table: {table.get('logical_name')}")
        if table.get("verification_status") != "verified" and dataset.get("status") == "active":
            errors.append(f"Active dataset contains unverified table: {table.get('sql_table') or table.get('logical_name')}")
    return errors

def validate_master(master: dict) -> list[str]:
    errors = []
    seen = set()
    for item in master.get("datasets", []):
        dataset_id = item.get("dataset_id")
        if not dataset_id or dataset_id in seen:
            errors.append(f"Missing or duplicate dataset_id: {dataset_id}")
        seen.add(dataset_id)
        dataset = master.get("_loaded_datasets", {}).get(dataset_id)
        if dataset:
            errors.extend(f"{dataset_id}: {e}" for e in validate_dataset(dataset))
    if master.get("default_dataset") not in seen:
        errors.append("default_dataset is not listed")
    return errors
