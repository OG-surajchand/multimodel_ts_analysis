import pandas as pd
import numpy as np
import pandas_ta as ta
from pathlib import Path


def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # Basic indicators
    df["rsi_14"] = ta.rsi(df["close"], length=14)
    macd = ta.macd(df["close"])
    df["macd"] = macd["MACD_12_26_9"]
    df["macd_signal"] = macd["MACDs_12_26_9"]
    bb = ta.bbands(df["close"], length=20)
    df["bb_upper"] = bb["BBU_20_2.0"]
    df["bb_lower"] = bb["BBL_20_2.0"]

    # Returns and vol
    df["log_ret"] = np.log(df["close"]).diff()
    df["vol_20"] = df["log_ret"].rolling(20).std()

    # Momentum / rate of change
    df["roc_10"] = ta.roc(df["close"], length=10)

    return df.dropna()


if __name__ == "__main__":

    data_path = (
        Path(__file__).resolve().parents[1] / "data" / "ohlcv" / "AAPL_labeled.csv"
    )
    df = pd.read_csv(data_path)
    print(df.head(5))
    df_feat = add_technical_indicators(df)
    out = data_path.parent / "AAPL_features.csv"
    df_feat.to_csv(out, index=False)
    print(f"Saved features CSV: {out}")
