# {{ project_name }}

> One-line problem statement: _what are you predicting / analysing, and on what data?_

/ **Workflow stage(s) reviewed:** _e.g. 03-modelling/regression, 00-fundamentals/cross-validation_
**Data source:** _file / database / API / cloud — link or path_
**Status:** ☐ setup ☐ EDA+FE ☐ modelling ☐ tracked ☐ tested ☐ questions answered

---

## The workflow

This project follows the standard backbone — **EDA → Feature Engineering → Model Selection → Validation & Evaluation** — across two notebooks, with correctness-critical logic graduating into `src/` as it stabilises.

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

**The graduation ratchet:** preprocessing is born in notebook 01 but *used* in notebook 02, where cross-validation happens and where leakage bites. So the keeper transforms move into `src/features.py` as a fittable pipeline **at the 01→02 boundary** — notebook 02 imports that pipeline, it never rebuilds it. Model selection runs CV over imported, leak-safe preprocessing, not loose notebook cells.

**Two non-negotiable disciplines:**
1. Both notebooks **run top-to-bottom before every commit.** A notebook that only works out of order is lying to you.
2. Anything correctness-critical is **imported from `src/`, never inlined** — one tested source of truth, no drift between notebooks.

---

## Structure

```
.
├── .github/workflows/ci.yml     # conda env + lint + pytest on push (present from day 1)
├── src/<package>/
│   ├── config.py                # paths, params, MLflow tracking URI
│   ├── data.py                  # acquisition / loading
│   ├── features.py              # preprocessing pipeline — graduates from notebook 01
│   ├── model.py                 # model / full pipeline — graduates from notebook 02
│   └── evaluate.py              # metric + validation functions — called by notebook 02
├── notebooks/
│   ├── 01-eda-fe.ipynb
│   └── 02-modelling.ipynb
├── tests/test_features.py       # canonical first test: preprocessing fits only inside the fold
├── data/{raw,processed}/        # gitignored
├── models/                      # gitignored — local artifacts
├── mlruns/                      # gitignored — MLflow local backend
├── environment.yml
├── pyproject.toml               # makes src/ importable + installable
├── .pre-commit-config.yaml      # black, ruff
└── tasks.py                     # cross-platform task runner
```

`src/` modules start near-empty and fill as logic graduates out of the notebooks. The notebook is the narrative and the visuals; `src/` is the load-bearing logic.

---

## Always-on baseline

Every project ships with the same ambient tooling, so it becomes something you reach for automatically rather than learn on top:

- **Conda env** — `environment.yml`, reproducible.
- **Git** from the first commit — real `.gitignore`, meaningful messages.
- **`src/` package** — `pyproject.toml`, `import <package>` works. Notebooks call the package.
- **pytest** — at least one *real* test (see below).
- **MLflow tracking** — local `mlruns/` backend, zero setup; log params, metrics, artifacts.
- **CI** — `ci.yml` present from day 1, runs green on the empty skeleton; starts verifying real tests once they exist.

### Make targets

```
python tasks.py setup      # conda env create + pip install -e . + pre-commit install
python tasks.py test       # pytest
python tasks.py lint       # ruff + black --check
python tasks.py mlflow-ui  # launch tracking UI against ./mlruns
```

---

## The canonical first test

`tests/test_features.py` asserts the preprocessing pipeline **fits only on training data inside each CV fold** — never on the validation split. This guards the single thing most likely to silently break (data leakage), and it's only possible *because* the preprocessing lives in `src/features.py` as an importable object rather than scattered across notebook cells.

Later projects add tests for their own logic (e.g. temporal-order preservation for time series, resampling-stays-inside-fold for imbalanced classification).

---

## Setup steps (the rote nine)

1. **Generate** from the cookiecutter; answer prompts (slug, package name, problem type).
2. **Environment** — `python tasks.py setup`.
3. **Repo** — `git init`, commit skeleton, create + push GitHub repo. CI should run green on the empty skeleton — that confirms the plumbing before you write real code.
4. **Acquire** — write `data.py`; raw data lands in `data/raw/` (gitignored).
5. **Explore (01-eda-fe)** — visualise, try transforms; findings to README notes, keeper transforms → `src/features.py`.
6. **Build (02-modelling)** — import the pipeline; model selection + evaluation matching the problem (right CV splitter, right metric); graduate model → `model.py`, metrics → `evaluate.py`.
7. **Track** — wrap training in an MLflow run.
8. **Test** — write the project's real test(s); `python tasks.py test`; push so CI verifies.
9. **Answer the questions** (below) — these become flashcard seeds.

Steps 1–3 are pure plumbing and should take minutes. If they ever start eating real time, the baseline has grown too heavy — trim the template. The data and the concepts stay the centre of gravity.

---

## Staged tooling (inert stubs until their project)

- **MLflow registry / packaging** — `register_model()` stub in `model.py` (activated project 9).
- **Docker + FastAPI deployment** — `deployment/` stubs; deliberate, not universal (projects 10 + 1–2 others).
- **Drift monitoring** — Evidently report stub (project 11).

---

## Conceptual questions

_Answer these in your own words once the project works. Each is a flashcard seed for the spaced-repetition layer._

1. _..._
2. _..._
3. _..._

---

## Notes & findings

_Key EDA observations, decisions made, and anything that surprised you._
