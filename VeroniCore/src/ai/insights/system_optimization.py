# system_optimization.py
# This script analyzes system resources and suggests optimizations, such as memory management, CPU allocation, and energy efficiency.

import psutil

class SystemOptimizer:
    def __init__(self):
        self.system_status = {}

    def analyze_memory(self):
        memory_info = psutil.virtual_memory()
        self.system_status['memory'] = {
            'total': memory_info.total,
            'available': memory_info.available,
            'percent_used': memory_info.percent
        }
        return self.system_status['memory']

    def analyze_cpu(self):
        cpu_info = psutil.cpu_percent(interval=1, percpu=True)
        self.system_status['cpu'] = {
            'cpu_usage_per_core': cpu_info,
            'average_cpu_usage': sum(cpu_info) / len(cpu_info)
        }
        return self.system_status['cpu']

    def analyze_disk(self):
        disk_info = psutil.disk_usage('/')
        self.system_status['disk'] = {
            'total': disk_info.total,
            'used': disk_info.used,
            'percent_used': disk_info.percent
        }
        return self.system_status['disk']

    def suggest_optimizations(self):
        optimizations = []
        if self.system_status['memory']['percent_used'] > 80:
            optimizations.append('Consider closing unused applications to free up memory.')
        if self.system_status['cpu']['average_cpu_usage'] > 70:
            optimizations.append('Consider reducing the number of active processes or upgrading your CPU.')
        if self.system_status['disk']['percent_used'] > 85:
            optimizations.append('Consider cleaning up disk space or upgrading storage capacity.')
        return optimizations

if __name__ == "__main__":
    # Example usage of the SystemOptimizer
    optimizer = SystemOptimizer()

    memory_status = optimizer.analyze_memory()
    print(f"Memory Status: {memory_status}")

    cpu_status = optimizer.analyze_cpu()
    print(f"CPU Status: {cpu_status}")

    disk_status = optimizer.analyze_disk()
    print(f"Disk Status: {disk_status}")

    optimizations = optimizer.suggest_optimizations()
    print(f"Suggested Optimizations: {optimizations}")
    