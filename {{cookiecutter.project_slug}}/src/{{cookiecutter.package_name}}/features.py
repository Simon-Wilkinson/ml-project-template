from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer


def build_pipeline() -> Pipeline:
    """
    Preprocessing pipeline.  Starts as a passthrough — populate during notebook 01
    then graduate the keeper transforms here at the 01 → 02 boundary.

    The pipeline must be fittable on training data only so it can be safely
    wrapped inside a CV fold.  Never fit on the full dataset before splitting.
    """
    return Pipeline([("passthrough", FunctionTransformer())])
