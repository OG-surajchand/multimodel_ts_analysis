import os
import polars as pl
import yfinance as yf
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "ohlcv"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_ohlcv(ticker: str, start: str, end: str):
    df = yf.download(ticker, start=start, end=end, progress=False)
    df = df[["Open", "High", "Low", "Close", "Volume"]]
    return df


if __name__ == "__main__":
    ticker = "AAPL"
    start_date, end_date = "2015-01-01", "2024-12-31"
    df = fetch_ohlcv(ticker, start_date, end_date)
    out_path = os.path.join(DATA_DIR, f"{ticker}.csv")
    df.to_csv(out_path)
    print(f"Saved: {out_path}")
