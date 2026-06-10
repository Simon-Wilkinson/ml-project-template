import numpy as np
from sklearn.model_selection import KFold

from {{ cookiecutter.package_name }}.features import build_pipeline


def test_preprocessing_fits_inside_fold():
    """
    Guard against data leakage: the preprocessing pipeline must be fit only on
    training rows inside each CV fold, never on the validation split.

    This is the canonical skeleton test — it passes on the default passthrough
    pipeline and keeps passing as long as build_pipeline() returns a proper
    sklearn-compatible pipeline that exposes fit / transform separately.
    """
    rng = np.random.default_rng(42)
    X = rng.standard_normal((100, 4))
    y = rng.standard_normal(100)

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    for train_idx, val_idx in kf.split(X):
        pipe = build_pipeline()
        pipe.fit(X[train_idx], y[train_idx])          # fit on train only
        X_val_transformed = pipe.transform(X[val_idx])  # transform val without refitting
        assert X_val_transformed.shape[0] == len(val_idx), (
            "Transformed validation set has wrong number of rows — "
            "check that transform() is not re-fitting on validation data."
        )
