SHELL := /bin/bash

.PHONY: setup lint test eval

setup:
	python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

lint:
	pre-commit run --all-files || true

test:
	pytest -q

eval:
	python scripts/evaluate.py --gold examples/sample.csv --pred examples/predictions.csv
