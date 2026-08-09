## Features Integrity Monitor (FIM)

A simple Python-based File Integrity Monitoring (FIM) tool designed to detect unauthorized or unexpected changes to files.

The tool creates a SHA-256 baseline of a directory and compares the current state of the files against that baseliFFeatureseatureseaturesures

- SHA-256 file hashing
- Baseline creation
- File modification detection
- File creation detection
- File deletion detection
- Simple terminal interface
- JSON-based baseline storage
- Lightweight and easy to use
- No external dependencies

Project Structure

file-integrity-monitor/
├── main.py
├── fim.py
├── config.json
├── requirements.txt
├── .gitignore
└── README.md

Requirements

- Python 3.8 or newer

No external Python packages are required.

Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/file-integrity-monitor.git
cd file-integrity-monitor

Run the program:

python main.py

Usage

1. Create a baseline

Start the program:

python main.py

Select:

1. Create baseline

Enter the directory you want to monitor.

The tool calculates a SHA-256 hash for each file and stores the results in "baseline.json".

2. Check file integrity

Run the program again and select:

2. Check integrity

The tool compares the current files with the stored baseline.

It can detect:

[+] Added files
[!] Modified files
[-] Deleted files

If nothing has changed:

[OK] No changes detected.

Example

========================================
       FILE INTEGRITY MONITOR
========================================
1. Create baseline
2. Check integrity
3. Exit
========================================

Select an option: 2

[*] Checking file integrity...

========== FIM RESULTS ==========

[+] ADDED FILES
  + test_files/new_file.txt

[!] MODIFIED FILES
  ! test_files/config.txt

[-] DELETED FILES
  - test_files/old.txt

=================================

How It Works

The FIM follows a simple process:

Directory
    ↓
Calculate SHA-256 hashes
    ↓
Create baseline
    ↓
Store file information
    ↓
Scan directory again
    ↓
Compare hashes
    ↓
Detect changes

A changed file produces a different SHA-256 hash, allowing the tool to identify modifications.

Security Use Case

File Integrity Monitoring is commonly used in cybersecurity to detect unexpected changes to important files.

Potential use cases include:

- Detecting unauthorized file modifications
- Monitoring configuration files
- Detecting suspicious file creation
- Detecting deleted files
- Supporting SOC investigations
- Supporting system monitoring and hardening

Disclaimer

This project is intended for educational and defensive cybersecurity purposes.

Only monitor files and directories that you own or are authorized to monitor.

Future Improvements

Planned improvements may include:

- Real-time monitoring
- Alert logging
- Colored terminal output
- Automatic configuration loading
- Email or webhook alerts
- File exclusion rules
- Monitoring multiple directories
- Detailed security reports
- SOC-friendly alert severity levels

License

This project is released under the MIT License.
