import json

def get_portfolio_summary():
    return {
        "app": "MMMX",
        "account": "Rolando H Ramirez Jr",
        "portfolio_value": "$142,850.40",
        "today_return": "+$3,420.15 (+2.45%)",
        "buying_power": "$25,400.00",
        "positions": [
            {"symbol": "MMMX", "shares": 5000, "price": "$12.80", "equity": "$64,000.00"},
            {"symbol": "NODE", "shares": 1, "price": "$35,000.00", "equity": "$35,000.00"},
            {"symbol": "SYNC", "shares": 1, "price": "$18,500.00", "equity": "$18,500.00"},
            {"symbol": "USD", "shares": 25400, "price": "$1.00", "equity": "$25,400.00"}
        ]
    }
