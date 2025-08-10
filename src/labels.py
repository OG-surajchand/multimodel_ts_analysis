import numpy as np
import pandas as pd
from pathlib import Path


def create_labels(
    df: pd.DataFrame, horizon: int = 1, up_th: float = 0.005, down_th: float = -0.005
):
    df = df.copy()
    df["fwd_ret"] = df["close"].shift(-horizon) / df["close"] - 1
    df["label"] = np.where(
        df["fwd_ret"] > up_th, 1, np.where(df["fwd_ret"] < down_th, -1, 0)
    )
    return df


if __name__ == "__main__":

    data_path = Path(__file__).resolve().parents[1] / "data" / "ohlcv" / "AAPL.csv"
    df = pd.read_csv(data_path, skiprows=2)
    df.columns = ["date", "open", "high", "low", "close", "volume"]

    df_l = create_labels(df)
    out = data_path.parent / "AAPL_labeled.csv"
    df_l.to_csv(out, index=False)
    print(f"Saved labeled CSV: {out}")
