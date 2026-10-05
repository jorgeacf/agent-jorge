# agent-jorge

A modern Python project built with standard PEP 621 packaging, strict type checking, and automated CI workflows.

---

## Features

- **PEP 621 compliant packaging** with `hatchling` and `pyproject.toml`.
- **`src/` layout** to avoid implicit import bugs and ensure clean builds.
- **Fast Linting & Formatting** with [Ruff](https://github.com/astral-sh/ruff).
- **Strict Static Typing** with [Mypy](https://mypy.readthedocs.io/).
- **Testing & Coverage** with [Pytest](https://docs.pytest.org/) and `pytest-cov`.
- **Multi-OS / Multi-Python CI matrix** with GitHub Actions (Python 3.10 - 3.13 on Linux, macOS, Windows).
- **Makefile** for quick developer workflows.

---

## Project Structure

```text
agent-jorge/
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI matrix
├── src/
│   └── agent_jorge/
│       ├── __init__.py            # Package initialization & exports
│       ├── core.py                # Core application logic
│       ├── cli.py                 # Command-line interface
│       └── py.typed               # PEP 561 marker
├── tests/
│   ├── __init__.py
│   ├── conftest.py                # Pytest fixtures
│   ├── test_cli.py                # CLI tests
│   └── test_core.py               # Core unit tests
├── .editorconfig                  # Formatting standards
├── .env.example                   # Environment variable template
├── .gitignore                     # Git ignore rules
├── Makefile                       # Development task runner
├── pyproject.toml                 # Centralized configuration
└── README.md                      # Project documentation
```

---

## Quickstart

### 1. Create and Activate a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2. Install in Development Mode

```bash
make install-dev
# Or directly with pip:
pip install -e ".[dev]"
```

### 3. Run the CLI

```bash
agent-jorge --name "Developer"
# Or:
python -m agent_jorge.cli --name "Developer"
```

---

## Development & Quality Assurance

All common tasks are available via `make`:

```bash
# Run tests with coverage
make test

# Run linter
make lint

# Auto-format and fix lint issues
make format

# Run static type checker
make typecheck

# Run full QA suite (lint + typecheck + test)
make check

# Clean build artifacts & cache
make clean
```

---

## License

This project is licensed under the MIT License.