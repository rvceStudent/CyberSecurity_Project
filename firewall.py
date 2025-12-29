from firewall_state import firewall_state
import subprocess

def block_ip(ip):
    print(f"[FIREWALL] Blocking IP: {ip}")
    firewall_state["blocked"] += 1

    # Optional real firewall command (Linux)
    # subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

def rate_limit_ip(ip):
    print(f"[FIREWALL] Rate limiting IP: {ip}")
    firewall_state["rate_limited"] += 1

    # Optional real rate limit logic
