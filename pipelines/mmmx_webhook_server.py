import http.server
import json
import os
import sys
import time

# Add parent directory to path so local adapters/pipelines import seamlessly
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from investment_engine import get_portfolio_summary
from adapters.cloud_sync import sync_with_cloud

PORT = 8080

class MMMXInvestmentHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        portfolio_data = get_portfolio_summary()
        sync_with_cloud(portfolio_data)
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(portfolio_data, indent=2).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        try:
            payload = json.loads(post_data.decode('utf-8'))
        except Exception:
            payload = {"raw_payload": post_data.decode('utf-8', errors='ignore')}
            
        current_portfolio = get_portfolio_summary()
        cloud_receipt = sync_with_cloud(current_portfolio)
        
        response_data = {
            "status": "ORDER_EXECUTED",
            "app": "MMMX",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "order_details": payload,
            "cloud_sync": cloud_receipt
        }
        
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data, indent=2).encode('utf-8'))

def run_server():
    server_address = ('0.0.0.0', PORT)
    httpd = http.server.HTTPServer(server_address, MMMXInvestmentHandler)
    print("==================================================")
    print(f" MMMX ROBINHOOD INVESTMENT APP LIVE ON PORT {PORT}")
    print("==================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[INFO] Shutting down server.")
        httpd.server_close()

if __name__ == "__main__":
    run_server()
