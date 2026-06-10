from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_RAW = ROOT / "data" / "raw"
DATA_PROCESSED = ROOT / "data" / "processed"
MODELS_DIR = ROOT / "models"

MLFLOW_TRACKING_URI = str(ROOT / "mlruns")
EXPERIMENT_NAME = "{{ cookiecutter.project_slug }}"

# Add project-specific hyperparameter defaults here
PARAMS: dict = {}
