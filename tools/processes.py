import psutil

def list_processes():
    """Return a list of running processes with pid, name, exe, cmdline"""
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
        try:
            info = proc.info
            processes.append(info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return processes

def kill_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.kill()
    except Exception as e:
        raise RuntimeError(f"Failed to kill process {pid}: {e}")

def suspend_process(pid):
    try:
        proc = psutil.Process(pid)
        proc.suspend()
    except Exception as e:
        raise RuntimeError(f"Failed to suspend process {pid}: {e}")
