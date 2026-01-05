# 1️⃣ Structure

Here’s a **generalized structure** you can use:

```
windows-task-automation/
│
├── .gitignore
├── README.md
├── requirements.txt
├── snapshot_runner.py          # Main automation script
├── tools/
│   ├── __init__.py
│   ├── processes.py            # Process listing, kill, suspend
│   ├── filesystem.py           # Directory scanning + SHA256 hashing
│   └── pretty_process.py       # Helper for nicely formatted process lists
└── snapshots/                  # JSON snapshots created by the script
```

**Notes:**

* No personal paths in repo — just placeholder paths.
* `snapshots/` can be `.gitignore`d if you don’t want to commit output files.
* `requirements.txt` should include:

```
psutil
pydantic
yara-python
```

---

# 2️⃣(Walkthrough for users)

````markdown
# Windows Task Automation and System Monitoring

A lightweight Python-based system to automate Windows system monitoring tasks. 
The script can:

- Capture running processes
- Scan directories and hash files
- Save snapshots as JSON for later review
- Be scheduled to run periodically using Task Scheduler

## Features

- Easy setup with a virtual environment
- Portable tools in the `tools/` folder
- Safe JSON output that can be used for analysis
- Fully automated snapshots for Windows

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/windows-task-automation.git
cd windows-task-automation
````

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

Edit `snapshot_runner.py` to set the directory you want to monitor:

```python
SCAN_DIR = r"C:\Path\To\Scan"
```

All snapshots will be saved under:

```text
snapshots/
```

---

## Running the Script

You can run manually:

```bash
python snapshot_runner.py
```

Or schedule it in **Windows Task Scheduler** to run automatically at intervals.

### Task Scheduler Setup

1. Open Task Scheduler → Create Task
2. Name: `Windows Task Automation`
3. Trigger: Daily, repeat every X hours (e.g., ?? hours you choose :))
4. Action:

   * Program/script: `C:\Path\To\Python\python.exe` (your venv python)
   * Arguments: `snapshot_runner.py`
   * Start in: Project folder
5. Save task and test with **Run**. Check `snapshots/` for JSON output.

---

## Using Snapshots

The snapshots are stored in JSON format and include:

* Running processes
* Filesystem hash info
* Timestamp

You can load them with Python:

```python
import json

with open("snapshots/snapshot_YYYYMMDD_HHMMSS.json") as f:
    data = json.load(f)
    print(data["processes"])
```

---

# 3️⃣ .gitignore

```gitignore
.venv/
__pycache__/
snapshots/
*.pyc
````
