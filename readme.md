Multi-Modal Stock Movement Prediction System
Introduction
This project presents a robust and advanced machine learning system designed to predict the directional movement of stock prices. Unlike traditional models that rely solely on historical price data, this system leverages a multi-modal approach by integrating quantitative time-series data with qualitative sentiment data derived from financial news headlines. The goal is to build a more comprehensive and resilient prediction model.

Problem Statement
The challenge in stock prediction is its inherent volatility and the multitude of influencing factors. This project frames the problem as a multi-class classification task rather than a regression one, aiming to predict whether a stock's price will move "up," "down," or "stay neutral" over a specified future period. This approach provides more actionable insights and addresses the non-linear nature of financial markets by capturing both technical and psychological drivers.

Key Features & Methodology
This project demonstrates a full-stack data science workflow, from data acquisition and feature engineering to advanced modeling and backtesting.

Data Acquisition: Utilizes multiple APIs to collect a diverse set of features, including:

Historical OHLCV Data: Daily Open, High, Low, Close, and Volume data for a portfolio of stocks.

Macroeconomic Data: Key indicators like inflation rates and interest rates to capture market-wide trends.

Financial News Headlines: Real-time and historical news articles to gauge market sentiment.

Feature Engineering:

Quantitative Features: Automated calculation of over 30 technical indicators (e.g., RSI, MACD, Bollinger Bands, Moving Averages) using pandas-ta to transform raw price data into meaningful signals.

Qualitative Features: Performed Natural Language Processing (NLP) on news headlines to extract sentiment scores. A fine-tuned BERT-based model was used to classify sentiment, providing a daily sentiment score as a feature.

Model Architecture: The system employs a hybrid ensemble approach to combine the predictive power of different models:

Deep Learning Model (LSTM): An LSTM (Long Short-Term Memory) network was trained on the time-series data and quantitative features to capture temporal dependencies.

Ensemble Classifier: The predictions from the LSTM were combined with the daily sentiment features using a final Gradient Boosting model (XGBoost) to make the ultimate directional prediction.

Evaluation & Backtesting:

The model's performance was evaluated using a time-based validation strategy to prevent look-ahead bias. Metrics such as Precision, Recall, and F1-score were used to assess classification performance.

A simulated backtesting framework was built to test a simple trading strategy based on the model's predictions. The strategy's performance was measured using a Sharpe Ratio and compared against a buy-and-hold benchmark.

Technical Stack
Programming Language: Python 3.8+

Core Libraries: pandas, numpy, scikit-learn

Deep Learning: TensorFlow or PyTorch, huggingface/transformers

Data Acquisition: yfinance, requests

Technical Analysis: pandas-ta or ta-lib

Visualization: matplotlib, seaborn

Containerization (Optional): Docker

Author
Suraj Chand
