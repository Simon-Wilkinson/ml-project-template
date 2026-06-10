import mlflow
from sklearn.model_selection import cross_validate


def cv_score(pipeline, X, y, *, cv, scoring) -> dict:
    """Run cross-validation; return a dict with train + val scores."""
    return cross_validate(pipeline, X, y, cv=cv, scoring=scoring, return_train_score=True)


def log_metrics(metrics: dict, step: int | None = None) -> None:
    """Log a flat dict of metrics to the active MLflow run."""
    for key, value in metrics.items():
        mlflow.log_metric(key, float(value), step=step)


def log_params(params: dict) -> None:
    """Log a dict of params to the active MLflow run."""
    mlflow.log_params(params)
