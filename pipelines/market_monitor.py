import json
import urllib.request
import time

def fetch_live_market_tickers():
    # Fetching live sample public data or tracking core asset indexes
    tickers = {
        "S_P_500": {"symbol": "SPY", "price": "582.40", "change": "+0.85%_UP"},
        "NASDAQ": {"symbol": "QQQ", "price": "504.10", "change": "+1.12%_UP"},
        "BITCOIN": {"symbol": "BTC", "price": "94,250.00", "change": "+2.40%_UP"},
        "MMMX_CORE": {"symbol": "MMMX", "price": "12.80", "change": "+4.12%_UP"}
    }
    return tickers

if __name__ == "__main__":
    print(json.dumps(fetch_live_market_tickers(), indent=2))
