"""Download competition data into data/raw/.  Usage: uv run python scripts/download_data.py [--force]"""

import sys

from airparis import download_data

if __name__ == "__main__":
    out = download_data(force="--force" in sys.argv)
    print(f"Data in {out}:")
    for f in sorted(out.iterdir()):
        print(f"  {f.name:40s} {f.stat().st_size / 1e6:8.2f} MB")
