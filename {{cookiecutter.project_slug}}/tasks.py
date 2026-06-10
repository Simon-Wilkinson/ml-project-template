#!/usr/bin/env python3
"""Cross-platform task runner. Usage: python3 tasks.py <task>"""
import sys

if sys.version_info < (3, 8):
    sys.exit("Python 3.8+ required. Run with: python3 tasks.py <task>")

import subprocess

ENV = "{{ cookiecutter.project_slug }}"


def _run(cmd: str) -> None:
    subprocess.run(cmd, shell=True, check=True)


def setup() -> None:
    _run("conda env create -f environment.yml")
    _run(f"conda run -n {ENV} pip install -e .")
    _run("git init")
    _run(f"conda run -n {ENV} pre-commit install")


def update() -> None:
    _run(f"conda env update -n {ENV} -f environment.yml --prune")
    _run(f"conda run -n {ENV} pip install -e .")


def test() -> None:
    _run(f"conda run -n {ENV} pytest tests/ -v")


def lint() -> None:
    _run(f"conda run -n {ENV} ruff check src/ tests/")
    _run(f"conda run -n {ENV} black --check src/ tests/")


def mlflow_ui() -> None:
    _run("mlflow ui --backend-store-uri ./mlruns")


TASKS = {
    "setup": setup,
    "update": update,
    "test": test,
    "lint": lint,
    "mlflow-ui": mlflow_ui,
}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in TASKS:
        print(f"Usage: python tasks.py [{' | '.join(TASKS)}]")
        sys.exit(1)
    TASKS[sys.argv[1]]()
