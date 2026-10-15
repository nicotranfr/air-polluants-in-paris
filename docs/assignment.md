# Paris Air Quality Forecasting

## Assignment overview

In this practical assignment, you will forecast hourly air pollution in Paris for the next three weeks. You will compare simple baselines with a zero-shot time-series foundation model, then explain what works, what does not, and why.

### Expected deliverables

- **A notebook**: Analysis, modelling choices, figures, evaluation and final predictions
- **Short report**: Answers to theoretical questions, methodology, findings and limitations

### Rules on external information

You may use calendar information known in advance, such as hour, weekday and public holidays. You must not use pollutant values or weather observations from the validation or test period. Briefly cite any external source you use.

## 1. Data understanding and preparation

Start by understanding the dataset before choosing a model.

- **Work to complete:** Load the train and test files. Identify the timestamp column and the five pollutant columns. Check that dates are sorted and that there are no unexpected duplicates.
- **Points to discuss:** Why is this a time-series forecasting problem, not a standard regression problem?
- **Points to discuss:** Why would a random train-test split create a misleading evaluation?
- **Work to complete:** Check data quality: time range, missing values, duplicates, outliers and simple statistics for each pollutant.
- **Work to complete:** Plot the pollutant series and describe visible trends, daily or weekly patterns, peaks and relationships between pollutants.
- **Points to discuss:** Which patterns seem visible in the data: hourly, daily or weekly? Give evidence from your plots.
- **Points to discuss:** How will you handle missing values? Explain why you must not interpolate using future validation or test data.

## 2. Validation strategy and baselines

Before using a foundation model, build simple baselines. They are useful references and are often hard to beat on seasonal data.

- **Work to complete:** Create a time-based validation split with a 504-hour forecast horizon. Make sure no future information enters the training data.
- **Work to complete:** Implement at least two baselines: persistence and seasonal naive. For the seasonal naive model, test a 168-hour lag and justify it.
- **Points to discuss:** Why is a 168-hour lag useful for hourly urban pollution data?
- **Points to discuss:** Why should you report MAE for each pollutant, not only the average MAE?

## 3. Time-series foundation models

Use a pretrained time-series foundation model in zero-shot mode. This means the model produces forecasts from historical context without being trained again on this Paris dataset.

- **Points to discuss:** What is a time-series foundation model? How is it different from a model trained only on this dataset?
- **Points to discuss:** What does zero-shot forecasting mean in this context?
- **Points to discuss:** Why could forecasting all pollutants together help? Give one possible advantage and one possible risk.
- **Points to discuss:** Classify the following as target, past-only covariate or known-future covariate: pollutant history, historical weather, hour of day and future weather observations.

## 4. Zero-shot forecasting experiment

Run the experiment in Google Colab. Keep the setup simple and reproducible.

- **Work to complete:** Run the foundation model in zero-shot mode. Record the model name, version, hardware and main settings.
- **Work to complete:** Prepare the data in the format expected by the model. Use only information available before the validation period.
- **Work to complete:** Generate forecasts for the full 504-hour horizon.
- **Work to complete:** Align predictions with the validation timestamps and compute MAE for each pollutant and on average.
- **Points to discuss:** Why can the median forecast be a good choice when the metric is MAE?

## 5. Comparative experiments

In this section, do two simple comparisons using the same validation period and the same metric. The goal is not to test many ideas, but to understand the effect of the modelling choice.

- **Independent vs joint forecasting:** train or run one model per pollutant, then compare it with one joint model that predicts all pollutants together.
- **Foundation model vs neural network:** compare the foundation model with a simple LSTM or RNN trained on the dataset.

- **Points to discuss:** Which approach works best: one model per pollutant, one joint model, or the LSTM/RNN? Explain the result using the MAE per pollutant.

## 6. Results and discussion

- **Work to complete:** Compare all models using MAE per pollutant and average MAE. Highlight cases where the average hides important differences.
- **Work to complete:** Analyse whether performance changes between the beginning and the end of the 504-hour horizon.
- **Work to complete:** Plot observed vs predicted values. Comment on one clear success or failure.
- **Points to discuss:** Which model performs best overall? Is it also best for every pollutant?
- **Points to discuss:** Where does the foundation model fail compared with the seasonal naive baseline?
- **Points to discuss:** List three limitations of your work: one about the data, one about the evaluation and one about the model.

## 7. Final forecast and submission

- **Work to complete:** Select the final method using validation results only, then generate forecasts for the competition test period.
- **Work to complete:** Check that the final submission follows the required format and contains complete, correctly ordered predictions for all five pollutants.

## References and starting points

- Ansari et al., "Chronos-2: From Univariate to Universal Forecasting". Technical description of the model and its group-attention approach.
- Chronos-2 quick-start notebook
- Kaggle challenge description and data: https://www.kaggle.com/competitions/x-hec-ts-2025-predicting-air-quality-in-paris
