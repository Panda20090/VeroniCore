# mining_monitor.py
# This script monitors mining performance, such as hash rate, block rewards, and power consumption.
# It provides real-time feedback to the user regarding mining operations.

import time
import psutil

class MiningMonitor:
    def __init__(self):
        self.hash_rate = 0
        self.power_consumption = 0
        self.block_rewards = 0

    def update_metrics(self, hash_rate, power_consumption, block_rewards):
        self.hash_rate = hash_rate
        self.power_consumption = power_consumption
        self.block_rewards = block_rewards
        self.display_metrics()

    def display_metrics(self):
        print(f"Current Hash Rate: {self.hash_rate} H/s")
        print(f"Power Consumption: {self.power_consumption} W")
        print(f"Block Rewards: {self.block_rewards} BTC")

    def monitor_resources(self):
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            mem_usage = psutil.virtual_memory().percent
            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {mem_usage}%")
            time.sleep(5)

if __name__ == "__main__":
    monitor = MiningMonitor()
    monitor.monitor_resources()
    # Example usage: monitor.update_metrics(5000, 250, 0.01)
    