import yfinance as yf
import pandas as pd
import numpy as np

def fetch_fundamentals(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    info = stock.info

    return {
        "Company": info.get("longName"),
        "Sector": info.get("sector"),
        "Market Cap": info.get("marketCap"),
        "PE Ratio": info.get("trailingPE"),
        "Revenue": info.get("totalRevenue"),
        "Profit Margin": info.get("profitMargins"),
        "EPS": info.get("trailingEps")
    }

def technical_analysis(ticker: str) -> dict:
    stock = yf.Ticker(ticker)
    hist = stock.history(period="6mo")

    hist["SMA_20"] = hist["Close"].rolling(20).mean()
    hist["SMA_50"] = hist["Close"].rolling(50).mean()

    latest = hist.iloc[-1]

    trend = "Bullish" if latest["SMA_20"] > latest["SMA_50"] else "Bearish"

    return {
        "Latest Close": float(latest["Close"]),
        "SMA 20": float(latest["SMA_20"]),
        "SMA 50": float(latest["SMA_50"]),
        "Trend": trend
    }
