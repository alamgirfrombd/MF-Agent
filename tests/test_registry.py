from registry.loader import load_registry
from registry.validator import validate_dataset

def test_all_seven_registries_load():
    master = load_registry()
    assert len(master["_loaded_datasets"]) == 7
    assert master["default_dataset"] == "loan_disbursement"

def test_registries_remain_draft_until_verified():
    master = load_registry()
    assert all(ds["status"] == "draft" for ds in master["_loaded_datasets"].values())
