"""Consistent response envelope for UI/API callers."""
def success(data, message: str = "OK") -> dict:
    return {"status": "success", "message": message, "data": data}

def failure(message: str, code: str = "REQUEST_FAILED") -> dict:
    return {"status": "error", "code": code, "message": message, "data": None}
