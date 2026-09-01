import json
import sys
import hashlib
from pathlib import Path


BASELINE_DIR = Path("baselines")
BASELINE_DIR.mkdir(exist_ok=True)


def scan_files(folder):
    files = {}

    for file in folder.iterdir():
        if file.is_file():
            with open(file, "rb") as item:
                file_data = item.read()

            file_hash = hashlib.sha256(file_data).hexdigest()

            files[str(file)] = file_hash

    return files


def load_baseline(baseline_path):
    with open(baseline_path, "r") as file:
        baseline = json.load(file)

    return baseline


def create_baseline(files, baseline_path):
    with open(baseline_path, "w") as file:
        json.dump(files, file, indent=4)


def check_integrity(files, baseline):
    for file in files:
        if file not in baseline:
            print(f"NEW: {file}")
        elif files[file] != baseline[file]:
            print(f"MODIFIED: {file}")

    for file in baseline:
        if file not in files:
            print(f"DELETED: {file}")


if len(sys.argv) < 3:
    print("Usage: python fim.py [baseline|check] [folder]")
    sys.exit()


command = sys.argv[1]
folder = Path(sys.argv[2])

if not folder.is_dir():
    print(f"Folder not found: {folder}")
    sys.exit()


if command == "baseline":
    files = scan_files(folder)

    baseline_path = BASELINE_DIR / f"{folder.name}.json"

    create_baseline(files, baseline_path)

    print(f"Baseline created: {baseline_path}")


elif command == "check":
    files = scan_files(folder)

    baseline_path = BASELINE_DIR / f"{folder.name}.json"

    if not baseline_path.exists():
        print(f"No baseline found for: {folder}")
        print(f"Create one with: python fim.py baseline {folder}")
        sys.exit()

    baseline = load_baseline(baseline_path)

    check_integrity(files, baseline)


else:
    print(f"Unknown command: {command}")
    print("Usage: python fim.py [baseline|check] [folder]")
