# {{ cookiecutter.project_name }}

> One-line problem statement: _what are you predicting / analysing, and on what data?_

**Problem type:** {{ cookiecutter.problem_type }}  
**Data source:** _file / database / API / cloud — link or path_  
**Status:** ☐ setup ☐ EDA+FE ☐ modelling ☐ tracked ☐ tested ☐ questions answered

---

## The workflow

```
notebooks/01-eda-fe.ipynb     explore, visualise, try transforms → arrive at a feature set
        │
        │  graduate keeper transforms → src/features.py (fittable, leak-safe pipeline)
        ▼
notebooks/02-modelling.ipynb  import the pipeline → model selection + evaluation → arrive at a model
        │
        │  graduate final model → src/model.py, metrics → src/evaluate.py
        ▼
both notebooks call src/ · run top-to-bottom · commit
```

**Two non-negotiable disciplines:**
1. Both notebooks **run top-to-bottom before every commit.**
2. Anything correctness-critical is **imported from `src/`, never inlined.**

---

## Structure

```
.
├── .github/workflows/ci.yml
├── src/{{ cookiecutter.package_name }}/
│   ├── config.py       paths, params, MLflow tracking URI
│   ├── data.py         acquisition / loading
│   ├── features.py     preprocessing pipeline — graduates from notebook 01
│   ├── model.py        model / full pipeline — graduates from notebook 02
│   └── evaluate.py     metric + validation functions
├── notebooks/
│   ├── 01-eda-fe.ipynb
│   └── 02-modelling.ipynb
├── tests/test_features.py
├── data/{raw,processed}/   gitignored
├── models/                 gitignored
├── mlruns/                 gitignored — MLflow local backend
├── environment.yml
├── pyproject.toml
├── .pre-commit-config.yaml
└── tasks.py                cross-platform task runner
```

---

## Tasks

```
python tasks.py setup      # conda env create + pip install -e . + pre-commit install
python tasks.py test       # pytest
python tasks.py lint       # ruff + black --check
python tasks.py mlflow-ui  # launch tracking UI against ./mlruns
```

---

## Conceptual questions

_Answer these in your own words once the project works._

1. _..._
2. _..._
3. _..._

---

## Notes & findings

_Key EDA observations, decisions made, and anything that surprised you._
