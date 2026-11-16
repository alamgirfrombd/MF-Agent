"""Build a simple report payload from already validated result data."""
def build_report(title: str, dataframe, metadata: dict | None = None) -> dict:
    return {"title": title, "row_count": len(dataframe),
            "columns": list(dataframe.columns), "metadata": metadata or {},
            "records": dataframe.to_dict(orient="records")}
