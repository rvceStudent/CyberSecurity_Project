from flask import Flask, render_template, jsonify
from collections import Counter
import re
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

LOG_FILE = "../logs/firewall.log"

def parse_logs():
    actions = []
    threat_scores = []

    if not os.path.exists(LOG_FILE):
        return actions, threat_scores

    with open(LOG_FILE, "r") as f:
        for line in f:
            if "RATE-LIMITED IP" in line:
                actions.append("rate_limited")
                match = re.search(r"score:\s*([0-9.]+)", line)
                if match:
                    threat_scores.append(float(match.group(1)))

            elif "BLOCKED IP" in line:
                actions.append("blocked")

    return actions, threat_scores


@app.route("/")
def dashboard():
    return render_template("index.html")


@app.route("/api/stats")
def stats():
    actions, threat_scores = parse_logs()
    counts = Counter(actions)

    return jsonify({
        "rate_limited": counts.get("rate_limited", 0),
        "blocked": counts.get("blocked", 0),
        "threat_scores": threat_scores[-20:]
    })


if __name__ == "__main__":
    app.run(debug=True)
