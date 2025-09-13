#!/usr/bin/env python3
import psutil
import os

def get_system_usage():
    # CPU usage in %
    cpu_usage = psutil.cpu_percent(interval=1)

    # RAM usage
    memory = psutil.virtual_memory()
    ram_total = round(memory.total / (1024**3), 2)  # in GB
    ram_used = round(memory.used / (1024**3), 2)
    ram_percent = memory.percent

    # Disk usage
    disk = psutil.disk_usage('/')
    disk_total = round(disk.total / (1024**3), 2)  # in GB
    disk_used = round(disk.used / (1024**3), 2)
    disk_percent = disk.percent

    return {
        "CPU Usage (%)": cpu_usage,
        "RAM (Used/Total GB)": f"{ram_used}/{ram_total} ({ram_percent}%)",
        "Disk (Used/Total GB)": f"{disk_used}/{disk_total} ({disk_percent}%)"
    }

if __name__ == "__main__":
    usage = get_system_usage()
    for k, v in usage.items():
        print(f"{k}: {v}")
