import pandas as pd
from pathlib import Path
from . import config


def load_raw(path: Path | None = None) -> pd.DataFrame:
    """Load raw data from disk. Replace with your actual source (file / DB / API)."""
    raise NotImplementedError("Implement load_raw() for your data source.")


def save_processed(df: pd.DataFrame, path: Path = config.DATA_PROCESSED / "data.parquet") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)


def load_processed(path: Path = config.DATA_PROCESSED / "data.parquet") -> pd.DataFrame:
    return pd.read_parquet(path)
