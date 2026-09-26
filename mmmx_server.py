import http.server
import json
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from pipelines.investment_engine import get_portfolio_summary
from pipelines.market_monitor import fetch_live_market_tickers
from adapters.cloud_sync import sync_with_cloud

PORT = 8080

class MMMXTerminalHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        portfolio_data = get_portfolio_summary()
        market_data = fetch_live_market_tickers()
        
        # Combine portfolio state with Wall Street market monitors
        terminal_feed = {
            "terminal_status": "ONLINE_LIVE_MONITOR",
            "market_overview": market_data,
            "portfolio": portfolio_data
        }
        
        sync_with_cloud(terminal_feed)
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(terminal_feed, indent=2).encode('utf-8'))

def run_server():
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.HTTPServer(server_address, MMMXTerminalHandler)
    print("==================================================")
    print(f" MMMX WALL STREET TERMINAL LIVE ON PORT {PORT}   ")
    print("==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down terminal.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
