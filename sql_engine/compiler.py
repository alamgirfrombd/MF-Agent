"""SQL compilation is intentionally not enabled until verified registry plans exist."""
class SQLCompilationNotReady(RuntimeError):
    pass

def compile_plan(plan: dict, dataset: dict) -> str:
    if dataset.get("status") != "active":
        raise SQLCompilationNotReady("Dataset must be verified and active before SQL compilation")
    raise SQLCompilationNotReady("Deterministic plan-to-SQL compiler is pending registry schema finalization")
