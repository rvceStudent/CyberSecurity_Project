# CyberSecurity_Project
AI-Driven automated malecious traffic blocking 

# 🔐 AI-Driven Self-Healing Firewall

An intelligent, adaptive firewall system that uses **Machine Learning and Reinforcement Learning** to detect and mitigate network attacks (DDoS, brute force, abnormal traffic) in real time.

Unlike traditional static firewalls, this system **learns from traffic behavior** and automatically updates firewall rules without manual intervention.

---

## 📌 Features

- 📡 Real-time packet sniffing using Scapy  
- 🧠 AI-based attack detection trained on CICIDS2017 dataset  
- 🔁 Reinforcement Learning-based decision engine  
- 🔥 Automatic IP blocking and rate-limiting using iptables  
- 📊 Live dashboard for monitoring attacks and actions  
- 🔒 Runs as a background security service  

---

## 🏗️ System Architecture

Network Traffic
↓
Packet Sniffer (Scapy)
↓
Feature Extraction
↓
ML Attack Detection Model
↓
Reinforcement Learning Agent
↓
Firewall Controller (iptables)
↓
System Protection


---

## 🧪 Dataset Used

- **CICIDS2017** (Canadian Institute for Cybersecurity)
- Flow-based network intrusion dataset
- Attack types:
  - DDoS
  - Brute Force
  - Port Scan
  - Web Attacks

---

## 🛠️ Technology Stack

| Component | Technology |
|--------|-----------|
| OS | Ubuntu 22.04 |
| Language | Python 3 |
| Packet Capture | Scapy |
| ML Framework | PyTorch |
| Dataset | CICIDS2017 |
| Firewall | iptables |
| Dashboard | Flask + Chart.js |
| Deployment | systemd |

---

## 📁 Project Structure

self_healing_firewall/
├── src/
│ ├── main.py
│ ├── packet_sniffer.py
│ ├── feature_extractor.py
│ ├── ml_model.py
│ ├── rl_agent.py
│ ├── firewall.py
│
├── models/
│ ├── attack_model.pth
│ ├── scaler.save
│
├── dashboard/
│ ├── app.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ └── chart.js
│
├── logs/
│ └── firewall.log
│
├── deployment/
│ ├── install.sh
│ ├── firewall.service
│
├── README.md


---

## 🚀 Installation & Usage

### 1️⃣ Clone Repository
```bash
git clone <repository-url>
cd self_healing_firewall

