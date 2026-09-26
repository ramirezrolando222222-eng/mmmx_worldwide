import json
import os
import sys
import time

def run_mmmx_mission(raw_input):
    print("==================================================")
    print(" MMMX: MONEY MAKING MISSION EXPLOSIVE (GLOBAL)   ")
    print("==================================================")
    
    vault_path = os.path.expanduser("~/mmmx_worldwide/vault/vault.json")
    with open(vault_path, "r") as f:
        vault = json.load(f)
        
    print(f" -> App: {vault['app_meta']['app_name']}")
    print(f" -> Owner: {vault['app_meta']['owner']}")
    print(f" -> Processing Inbound Mission: '{raw_input}'")
    
    # Simple classification logic for the worldwide pipelines
    lower_input = raw_input.lower()
    if "lead" in lower_input or "client" in lower_input or "budget" in lower_input:
        domain = "LEAD_SCORE"
        action = "High-ticket speed-to-lead qualification & CRM sync."
    elif "invoice" in lower_input or "receipt" in lower_input or "ledger" in lower_input:
        domain = "INVOICE_PARSER"
        action = "Automated financial extraction & accounting ledger sync."
    elif "content" in lower_input or "post" in lower_input or "syndicate" in lower_input:
        domain = "CONTENT_ENGINE"
        action = "Multi-platform worldwide content syndication."
    else:
        domain = "SYSTEM_EXECUTION"
        action = "Automated digital execution & script routing."
        
    result = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "app": vault['app_meta']['app_name'],
        "status": "SUCCESS",
        "classified_domain": domain,
        "executed_action": action,
        "active_regions": vault['global_config']['supported_regions']
    }
    
    print("\n[GLOBAL MISSION REPORT]")
    print(json.dumps(result, indent=2))
    print("==================================================")

if __name__ == "__main__":
    test_input = "Capture incoming high-ticket client lead and dispatch across global nodes."
    if len(sys.argv) > 1:
        test_input = " ".join(sys.argv[1:])
    run_mmmx_mission(test_input)
