"""
Windows Task Automation & System Monitoring Script
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path

from tools.pretty_process import pretty_processes
from tools.processes import list_processes
from tools.filesystem import scan_directory

# ================================
# CONFIGURATION
# ================================

SCAN_DIR = r"C:\Path\To\Scan"  # Replace with the directory you want to monitor
SNAPSHOT_DIR = Path("snapshots")
SNAPSHOT_DIR.mkdir(exist_ok=True)
INTERVAL_SECONDS = 6 * 60 * 60  # 6 hours

# ================================
# FUNCTIONS
# ================================

def take_snapshot():
    """Capture current system state and save as JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    snapshot_file = SNAPSHOT_DIR / f"snapshot_{timestamp}.json"

    print(f"[+] Taking snapshot at {timestamp}")

    # 1. List processes
    try:
        processes = list_processes()
        processes_pretty = pretty_processes(processes)
    except Exception as e:
        print(f"[!] Failed to list processes: {e}")
        processes_pretty = []

    # 2. Scan directory and hash files
    try:
        files_snapshot = scan_directory(SCAN_DIR)
    except Exception as e:
        print(f"[!] Failed to scan directory {SCAN_DIR}: {e}")
        files_snapshot = []

    snapshot_data = {
        "timestamp": timestamp,
        "processes": processes_pretty,
        "files": files_snapshot,
    }

    try:
        with open(snapshot_file, "w", encoding="utf-8") as f:
            json.dump(snapshot_data, f, indent=4)
        print(f"[+] Snapshot saved: {snapshot_file}")
    except Exception as e:
        print(f"[!] Failed to save snapshot: {e}")

# ================================
# MAIN
# ================================

if __name__ == "__main__":
    print("[*] Snapshot runner started")

    # If running via Task Scheduler, take one snapshot and exit
    if os.environ.get("TASK_SCHEDULER"):
        take_snapshot()
    else:
        while True:
            take_snapshot()
            print(f"[*] Sleeping for {INTERVAL_SECONDS / 3600} hours...")
            time.sleep(INTERVAL_SECONDS)
