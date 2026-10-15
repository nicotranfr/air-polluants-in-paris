"""Project-wide constants and paths."""

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
SUBMISSIONS_DIR = PROJECT_ROOT / "submissions"
FIGURES_DIR = PROJECT_ROOT / "reports" / "figures"

COMPETITION = "x-hec-ts-2025-predicting-air-quality-in-paris"

HORIZON = 504  # 3 weeks of hourly forecasts
SEED = 42
