# air-polluants-in-paris

Forecasting hourly air pollution in Paris over a 504-hour horizon
([X-HEC TS 2025 Kaggle challenge](https://www.kaggle.com/competitions/x-hec-ts-2025-predicting-air-quality-in-paris)).

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nicotranfr/air-polluants-in-paris/blob/main/notebooks/main.ipynb)

## Run in Colab (one click)

1. One-time: in Colab, open the 🔑 **Secrets** panel and add `KAGGLE_API_TOKEN` (your Kaggle API token).
2. Click the badge above, then Runtime → Change runtime type → **T4 GPU**.
3. Run all. The first cell installs dependencies and downloads the data.

## Run locally

```bash
uv sync                                    # create .venv
echo <token> > ~/.kaggle/access_token      # one-time Kaggle auth
```

Open `notebooks/main.ipynb` in VS Code with the `.venv` kernel.

Both setups require that you joined the competition on Kaggle.

## Layout

```
notebooks/main.ipynb   analysis, models, evaluation, submission
reports/               short report + figures
submissions/           generated submission CSVs (git-ignored)
```
