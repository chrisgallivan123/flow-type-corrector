# Contributing

Thanks for your interest!

## Setup
- Use Python 3.10+
- `python -m venv .venv && source .venv/bin/activate`
- `pip install -r requirements.txt`
- `pre-commit install`

## Workflow
1. Create a feature branch.
2. Add/update tests in `tests/` when applicable.
3. Run `pre-commit run --all-files`.
4. Open a PR. The CI will run linters and tests.

## Commit style
- Conventional Commits are appreciated (e.g., `feat:`, `fix:`, `docs:`).

## Code of conduct
See `CODE_OF_CONDUCT.md`.
