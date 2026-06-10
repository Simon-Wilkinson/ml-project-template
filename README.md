# ml-project-template

Cookiecutter template for a reproducible ML project following the
**EDA → Feature Engineering → Model Selection → Validation** backbone.

## What you get

```
<project-slug>/
├── .github/workflows/ci.yml     conda env-free CI: lint + pytest on push
├── src/<package>/
│   ├── config.py                paths, params, MLflow tracking URI
│   ├── data.py                  acquisition / loading stub
│   ├── features.py              preprocessing pipeline (passthrough to start)
│   ├── model.py                 model pipeline + MLflow registry stub
│   └── evaluate.py              CV scoring + MLflow metric helpers
├── notebooks/
│   ├── 01-eda-fe.ipynb          explore → graduate transforms into src/
│   └── 02-modelling.ipynb       model selection → graduate model into src/
├── tests/test_features.py       canonical leakage-guard test (passes on skeleton)
├── data/{raw,processed}/        gitignored
├── models/                      gitignored
├── environment.yml              reproducible conda env
├── pyproject.toml               src/ importable via pip install -e .
├── .pre-commit-config.yaml      black + ruff
└── tasks.py                     cross-platform task runner (setup / test / lint / mlflow-ui)
```

## Usage

```bash
pip install cookiecutter
cookiecutter gh:Simon-Wilkinson/ml-project-template
```

Answer the prompts:

| Prompt | Example |
|---|---|
| `project_name` | My House Price Model |
| `project_slug` | _(auto: my-house-price-model)_ |
| `package_name` | _(auto: my_house_price_model)_ |
| `problem_type` | regression |
| `author` | Your Name |

Then:

```bash
cd my-house-price-model
python tasks.py setup   # creates conda env + installs package + pre-commit
python tasks.py test    # should be green on the empty skeleton
```

## Design principles

- **Graduation ratchet** — preprocessing is born in notebook 01 but *used* in notebook 02. Keeper transforms move into `src/features.py` at the 01→02 boundary; notebook 02 imports, never rebuilds.
- **Notebooks run top-to-bottom** before every commit — a notebook that only works out of order is lying.
- **One tested source of truth** — correctness-critical logic lives in `src/`, not scattered across cells.
- **Skeleton CI is green** — the template ships with a passthrough pipeline so tests and CI pass before you write a single line of real code.
