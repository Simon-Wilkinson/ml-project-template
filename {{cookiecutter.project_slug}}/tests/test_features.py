import numpy as np
from sklearn.model_selection import KFold

from {{ cookiecutter.package_name }}.features import build_pipeline


def test_preprocessing_fits_inside_fold():
    """Preprocessing pipeline must fit only on training rows — never the validation split."""
    rng = np.random.default_rng(42)
    X = rng.standard_normal((100, 4))
    y = rng.standard_normal(100)

    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    for train_idx, val_idx in kf.split(X):
        pipe = build_pipeline()
        pipe.fit(X[train_idx], y[train_idx])
        X_val_transformed = pipe.transform(X[val_idx])
        assert X_val_transformed.shape[0] == len(val_idx), (
            "Transformed validation set has wrong number of rows — "
            "check that transform() is not re-fitting on validation data."
        )
