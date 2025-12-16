import pandas as pd
import numpy as np
import os


def analyze_stock():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, 'data', 'stock_data.csv')

    df = pd.read_csv(csv_path)

    df['MA_5'] = df['Close'].rolling(window=5).mean()
    df['MA_10'] = df['Close'].rolling(window=10).mean()

    df['Daily_Return'] = df['Close'].pct_change()
    volatility = float(np.std(df['Daily_Return'].dropna()))

    buy_price = float(df['Close'].iloc[0])
    sell_price = float(df['Close'].iloc[-1])
    profit_loss = float(sell_price - buy_price)

    if volatility > 0.02:
        risk = "High"
    elif volatility > 0.01:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "dates": df["Date"].astype(str).tolist(),
        "close_prices": [float(x) for x in df["Close"].tolist()],
        "ma_5": [float(x) if not pd.isna(x) else 0 for x in df["MA_5"].tolist()],
        "ma_10": [float(x) if not pd.isna(x) else 0 for x in df["MA_10"].tolist()],
        "volatility": volatility,
        "profit_loss": profit_loss,
        "risk_level": risk
    }
