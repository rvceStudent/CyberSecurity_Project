import time

def extract_features(ip, timestamps):
    duration = max(timestamps) - min(timestamps)
    packet_count = len(timestamps)
    packets_per_sec = packet_count / duration if duration > 0 else 0

    return [
        duration,
        packet_count,
        packet_count / 2,
        packets_per_sec,
        packets_per_sec * 100
    ]
