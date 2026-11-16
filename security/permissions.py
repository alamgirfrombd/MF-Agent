"""Authorization policy interface. Deny by default until real identity integration exists."""
class AccessDenied(PermissionError):
    pass

def require_dataset_access(user_context: dict | None, dataset_id: str) -> None:
    if not user_context or not user_context.get("authenticated"):
        raise AccessDenied("Authenticated user context is required")
    allowed = user_context.get("allowed_datasets", [])
    if dataset_id not in allowed:
        raise AccessDenied("User is not authorized for this dataset")
