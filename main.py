import json
import os

from fim import create_baseline, compare_baseline


BASELINE_FILE = "baseline.json"


def save_baseline(baseline):
    """Save the baseline to a JSON file."""
    with open(BASELINE_FILE, "w", encoding="utf-8") as file:
        json.dump(baseline, file, indent=4)


def load_baseline():
    """Load the baseline from a JSON file."""
    if not os.path.exists(BASELINE_FILE):
        return None

    with open(BASELINE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def show_results(results):
    """Display integrity check results."""

    print("\n========== FIM RESULTS ==========")

    if results["added"]:
        print("\n[+] ADDED FILES")
        for file in results["added"]:
            print(f"  + {file}")

    if results["modified"]:
        print("\n[!] MODIFIED FILES")
        for file in results["modified"]:
            print(f"  ! {file}")

    if results["deleted"]:
        print("\n[-] DELETED FILES")
        for file in results["deleted"]:
            print(f"  - {file}")

    if not any(results.values()):
        print("\n[OK] No changes detected.")

    print("=================================\n")


def create_new_baseline():
    directory = input("Directory to monitor: ").strip()

    if not os.path.isdir(directory):
        print("[ERROR] Directory does not exist.")
        return

    print("\n[*] Creating baseline...")

    baseline = create_baseline(directory)
    save_baseline(baseline)

    print(f"[OK] Baseline created.")
    print(f"[INFO] {len(baseline)} files recorded.")


def check_integrity():
    baseline = load_baseline()

    if baseline is None:
        print("[ERROR] No baseline found.")
        print("[INFO] Create a baseline first.")
        return

    directory = input("Directory to check: ").strip()

    if not os.path.isdir(directory):
        print("[ERROR] Directory does not exist.")
        return

    print("\n[*] Checking file integrity...")

    current_state = create_baseline(directory)
    results = compare_baseline(baseline, current_state)

    show_results(results)


def menu():
    while True:
        print("""
========================================
       FILE INTEGRITY MONITOR
========================================
1. Create baseline
2. Check integrity
3. Exit
========================================
""")

        choice = input("Select an option: ").strip()

        if choice == "1":
            create_new_baseline()

        elif choice == "2":
            check_integrity()

        elif choice == "3":
            print("[*] Exiting...")
            break

        else:
            print("[ERROR] Invalid option.")


if __name__ == "__main__":
    menu()
