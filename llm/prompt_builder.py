"""Build bounded prompts from question and verified metadata only."""
def build_planning_prompt(question: str, datasets: list[dict]) -> str:
    return ("Plan a data request using only the following dataset catalog. Do not invent schema.\n"
            f"Question: {question}\nCatalog: {datasets}")
