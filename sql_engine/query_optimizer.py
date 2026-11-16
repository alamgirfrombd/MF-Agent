"""Optimization advisory checks; does not rewrite SQL automatically."""
def review_query(sql: str) -> list[str]:
    advice = []
    normalized = sql.upper()
    if "SELECT *" in normalized:
        advice.append("Select only required columns instead of SELECT *.")
    if "WHERE" not in normalized:
        advice.append("Consider a selective date/branch filter for large transaction tables.")
    return advice
