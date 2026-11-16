"""Metric catalogue boundary. Do not add MRA/PKSF formulas without signed-off definitions."""
class MetricNotApprovedError(ValueError):
    pass

def get_approved_metric(dataset: dict, metric_id: str) -> dict:
    matches = [m for m in dataset.get("approved_metrics", []) if m.get("metric_id") == metric_id]
    if len(matches) != 1:
        raise MetricNotApprovedError(f"Metric is not uniquely approved: {metric_id}")
    return matches[0]
