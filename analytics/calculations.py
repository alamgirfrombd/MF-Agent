"""Pure calculation helpers. Production financial definitions require business approval."""
def percentage(numerator: float, denominator: float) -> float | None:
    if denominator == 0:
        return None
    return (numerator / denominator) * 100
