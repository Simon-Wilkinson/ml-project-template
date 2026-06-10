from sklearn.pipeline import Pipeline


def build_model_pipeline(preprocessor, estimator) -> Pipeline:
    """Combine a preprocessor and an estimator into a single sklearn Pipeline."""
    return Pipeline([("preprocessor", preprocessor), ("model", estimator)])


# --- project 9+ stub ---
def register_model(run_id: str, model_name: str) -> None:
    """Register a trained model in the MLflow Model Registry (activate in project 9+)."""
    raise NotImplementedError("Activate for project 9+.")
