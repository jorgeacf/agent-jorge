.PHONY: help install install-dev test lint format typecheck check clean run

PYTHON ?= python3
PIP ?= $(PYTHON) -m pip

help:
	@echo "Available commands:"
	@echo "  make install       Install package"
	@echo "  make install-dev   Install package in editable mode with dev dependencies"
	@echo "  make test          Run tests with coverage"
	@echo "  make lint          Run ruff linter"
	@echo "  make format        Run ruff code formatter and fix issues"
	@echo "  make typecheck     Run mypy type checker"
	@echo "  make check         Run all checks (lint, format check, typecheck, test)"
	@echo "  make run           Run the CLI application"
	@echo "  make clean         Remove build artifacts and cache files"

install:
	$(PIP) install .

install-dev:
	$(PIP) install -e ".[dev]"

test:
	pytest

lint:
	ruff check .

format:
	ruff format .
	ruff check --fix .

typecheck:
	mypy src

check: lint typecheck test

run:
	$(PYTHON) -m agent_jorge.cli

clean:
	rm -rf build/ dist/ *.egg-info .coverage coverage.xml htmlcov/ .pytest_cache/ .mypy_cache/ .ruff_cache/
	find . -type d -name "__pycache__" -exec rm -rf {} +
