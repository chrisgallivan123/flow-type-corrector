import json, pathlib

def test_workflow_json_exists():
    p = pathlib.Path("workflow/flow-type-corrector-prod.json")
    assert p.exists(), "Workflow JSON missing"

def test_workflow_json_parse():
    p = pathlib.Path("workflow/flow-type-corrector-prod.json")
    data = json.loads(p.read_text())
    assert isinstance(data, dict), "Workflow JSON must be a dict at top-level"
