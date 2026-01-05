import os
import hashlib
from pathlib import Path

def hash_file(path):
    """Compute SHA256 hash of a file"""
    sha256 = hashlib.sha256()
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception:
        return None

def scan_directory(directory):
    """Recursively scan directory and return list of file hashes"""
    files_data = []
    base = Path(directory)
    for path in base.rglob("*"):
        if path.is_file():
            files_data.append({
                "path": str(path),
                "sha256": hash_file(path)
            })
    return files_data
