from scapy.all import sniff
from collections import defaultdict
import os

traffic = defaultdict(list)

def packet_handler(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        traffic[src_ip].append(1)

def start_sniffing():
    # 🔒 Safety: Only sniff if running as root
    if os.geteuid() != 0:
        print("⚠ Packet sniffing disabled (run as root to enable)")
        return

    sniff(prn=packet_handler, store=False)
