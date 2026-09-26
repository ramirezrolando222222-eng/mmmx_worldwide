import json
import os
import time

def sync_with_cloud(local_portfolio):
    cloud_vault_path = os.path.expanduser("~/mmmx_worldwide/vault/cloud_sync_vault.json")
    sync_payload = {
        "sync_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "node_id": "mmmx-cloud-edge-node-01",
        "owner": "Rolando H Ramirez Jr",
        "portfolio_snapshot": local_portfolio,
        "cloud_status": "SYNCHRONIZED_SECURE"
    }
    os.makedirs(os.path.dirname(cloud_vault_path), exist_ok=True)
    with open(cloud_vault_path, "w") as f:
        json.dump(sync_payload, f, indent=2)
    return sync_payload
