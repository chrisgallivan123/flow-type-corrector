# Flow Type Corrector (n8n)

![CI](https://img.shields.io/github/actions/workflow/status/USER/REPO/ci.yml?label=CI&style=flat)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Made with n8n](https://img.shields.io/badge/Made%20with-n8n-orange)
![Type: Agentic](https://img.shields.io/badge/Type-Agentic-blueviolet)

A production-ready **Flow Type Corrector** built on **n8n** that normalizes and corrects work item types (e.g., Feature / Defect / Risk / Debt) using an LLM-informed pipeline with guardrails. This repo includes the production workflow JSON, evaluation harness, GitHub Actions, issue/PR templates, and docs.

> **Why it’s useful**: Improves data hygiene and reporting quality by enforcing a consistent flow-type taxonomy with auditable corrections.

---

## Quick Start

### 1) Import into n8n
- In n8n: **Import** → choose [`workflow/flow-type-corrector-prod.json`](workflow/flow-type-corrector-prod.json)
- Wire up your credentials (LLM provider, vector DB, etc., if used).
- Confirm the webhook URL and any environment variables your instance uses.

### 2) Send a test request
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/send_sample.py --title "Fix 500 on SSO callback" --description "NPE on token refresh; add null check"
```
The script prints the normalized/corrected flow type and rationale.

### 3) Evaluate on a labeled sample
```
python scripts/batch_classify.py --in examples/sample.csv --out examples/predictions.csv --webhook $WEBHOOK_URL
python scripts/evaluate.py --gold examples/sample.csv --pred examples/predictions.csv
```

---

## Repo Layout

```
.
├─ workflow/
│  └─ flow-type-corrector-prod.json
├─ docs/
│  ├─ architecture.md
│  └─ screenshots/
├─ scripts/
│  ├─ send_sample.py
│  ├─ batch_classify.py
│  └─ evaluate.py
├─ examples/
│  ├─ sample.csv
│  └─ predictions.csv
├─ tests/
│  └─ test_schema.py
├─ .github/
│  ├─ ISSUE_TEMPLATE/
│  │  ├─ bug_report.md
│  │  └─ feature_request.md
│  ├─ PULL_REQUEST_TEMPLATE.md
│  └─ workflows/
│     └─ ci.yml
├─ .pre-commit-config.yaml
├─ CONTRIBUTING.md
├─ CODE_OF_CONDUCT.md
├─ SECURITY.md
├─ LICENSE
├─ requirements.txt
├─ Makefile
└─ README.md
```

---

## Configuration

- **WEBHOOK_URL**: The n8n webhook for this workflow (set in env or pass via CLI).
- **DEBUG**: You can enable verbose logs for the **dev** variant of this workflow by supplying `"DEBUG": "true"` in the request body or via environment. (Prod variant minimizes logs by default.)

---

## Architecture

See [`docs/architecture.md`](docs/architecture.md) for a diagram and detailed notes on the pipeline, guardrails, and extension points.

---

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md). Please run pre-commit hooks locally before opening a PR:

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

---

## License

MIT — see [`LICENSE`](LICENSE).

---

## Security

Report vulnerabilities via [`SECURITY.md`](SECURITY.md).

---

## Maintainers

- @your-handle — Maintainer
