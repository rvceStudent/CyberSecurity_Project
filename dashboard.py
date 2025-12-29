from flask import Flask, jsonify, render_template, request
from firewall_state import firewall_state
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/stats")
def stats():
    return jsonify({
        "status": "RUNNING" if firewall_state["running"] else "STOPPED",
        "blocked": firewall_state["blocked"],
        "rate_limited": firewall_state["rate_limited"],
        "threat_scores": firewall_state["threat_scores"]
    })

@app.route("/api/start", methods=["POST"])
def start_firewall():
    firewall_state["running"] = True
    return jsonify({"message": "Firewall started"})

@app.route("/api/stop", methods=["POST"])
def stop_firewall():
    firewall_state["running"] = False
    return jsonify({"message": "Firewall stopped"})
