import time
import threading
import torch
import joblib
import random

from firewall_state import firewall_state
from dashboard import app
from rl_agent import FirewallAgent
from ml_model import AttackDetector

# Load ML model
model = AttackDetector()
model.load_state_dict(torch.load("models/attack_model.pth"))
model.eval()

scaler = joblib.load("models/scaler.save")
agent = FirewallAgent()

# -------------------------------
# 🔥 SIMULATED TRAFFIC GENERATOR
# -------------------------------
def simulate_traffic():
    while True:
        time.sleep(5)

        if not firewall_state["running"]:
            continue

        # Generate fake threat score
        threat = random.uniform(0.1, 0.95)
        firewall_state["threat_scores"].append(threat)
        firewall_state["threat_scores"] = firewall_state["threat_scores"][-20:]

        action = agent.choose_action(threat)

        if action == "BLOCK":
            firewall_state["blocked"] += 1
        elif action == "LIMIT":
            firewall_state["rate_limited"] += 1

# -------------------------------
# 🔁 Background Threads
# -------------------------------
threading.Thread(target=simulate_traffic, daemon=True).start()

# -------------------------------
# 🚀 Start Flask App
# -------------------------------
if __name__ == "__main__":
    app.run(debug=False, threaded=True)
