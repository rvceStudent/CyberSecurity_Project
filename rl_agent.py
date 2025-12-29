import random

class FirewallAgent:
    def __init__(self):
        self.epsilon = 0.1

    def choose_action(self, threat_score):
        if threat_score < 0.5:
            return "ALLOW"
        elif threat_score < 0.8:
            return "LIMIT"
        else:
            return "BLOCK"
