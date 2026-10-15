# Paris Air Quality Forecasting — Short Report

## 1. Methodology

- Data: hourly NO2, CO, O3, PM10, PM2.5 in Paris, 2020-01-01 → 2024-09-03 (40,991 hours)
- Validation: last 504 hours of the training set
- Metric: MAE per pollutant and average MAE
- Models:

## 2. Theoretical questions

### Why is this a time-series forecasting problem, not a standard regression problem?

### Why would a random train-test split create a misleading evaluation?

### Which patterns are visible: hourly, daily or weekly?

### How are missing values handled, and why not interpolate using future data?

### Why is a 168-hour lag useful for hourly urban pollution data?

### Why report MAE per pollutant, not only the average?

### What is a time-series foundation model? How does it differ from a model trained only on this dataset?

### What does zero-shot forecasting mean here?

### Why could forecasting all pollutants together help? (one advantage, one risk)

### Classification: target / past-only covariate / known-future covariate

| Variable                   | Role |
|----------------------------|------|
| Pollutant history          |      |
| Historical weather         |      |
| Hour of day                |      |
| Future weather observations|      |

### Why can the median forecast be a good choice when the metric is MAE?

## 3. Findings

### MAE per pollutant (validation)

| Model | NO2 | CO | O3 | PM10 | PM2.5 | Average |
|-------|-----|----|----|------|-------|---------|
|       |     |    |    |      |       |         |

### Best model overall, and per pollutant

### Independent vs joint vs LSTM/RNN

### Where the foundation model fails vs seasonal naive

### Performance across the 504-hour horizon

## 4. Limitations

- **Data:**
- **Evaluation:**
- **Model:**

## 5. Final submission

- Selected method:
- Reason (validation only):

## References

- Ansari et al., "Chronos-2: From Univariate to Universal Forecasting"
- Kaggle: x-hec-ts-2025-predicting-air-quality-in-paris
