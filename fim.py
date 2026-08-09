import hashlib
import os


def calculate_hash(file_path):
    """Calculate the SHA-256 hash of a file."""
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while chunk := file.read(4096):
                sha256.update(chunk)

        return sha256.hexdigest()

    except (PermissionError, OSError):
        return None


def create_baseline(directory):
    """Create a baseline of all files in a directory."""
    baseline = {}

    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            file_hash = calculate_hash(file_path)

            if file_hash:
                baseline[file_path] = file_hash

    return baseline


def compare_baseline(old_baseline, new_baseline):
    """Compare two baselines and detect file changes."""

    old_files = set(old_baseline.keys())
    new_files = set(new_baseline.keys())

    added = new_files - old_files
    deleted = old_files - new_files

    modified = {
        file_path
        for file_path in old_files & new_files
        if old_baseline[file_path] != new_baseline[file_path]
    }

    return {
        "added": sorted(added),
        "modified": sorted(modified),
        "deleted": sorted(deleted),
              }
