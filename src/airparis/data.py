"""Data download and environment utilities. No modelling logic lives here."""

import random
import shutil
from pathlib import Path

import numpy as np

from airparis.config import COMPETITION, RAW_DIR


def download_data(force: bool = False) -> Path:
    """Download the Kaggle competition files into data/raw/ and return that folder.

    Auth: ~/.kaggle/kaggle.json, KAGGLE_USERNAME/KAGGLE_KEY env vars, or Colab secrets.
    You must also have accepted the competition rules on kaggle.com.
    """
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if not force and any(RAW_DIR.glob("*.csv")):
        return RAW_DIR

    import kagglehub

    cache_path = Path(kagglehub.competition_download(COMPETITION, force_download=force))
    for f in cache_path.rglob("*"):
        if f.is_file():
            shutil.copy2(f, RAW_DIR / f.name)
    return RAW_DIR


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:
        pass


def get_device() -> str:
    """Best available torch device: cuda (Colab GPU) > mps (Apple Silicon) > cpu."""
    import torch

    if torch.cuda.is_available():
        return "cuda"
    if torch.backends.mps.is_available():
        return "mps"
    return "cpu"
