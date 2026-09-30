# 🔐 File Integrity Monitor

A lightweight Python-based **File Integrity Monitoring (FIM)** tool that detects changes to files using **SHA-256 cryptographic hashes**.

---

## Features

* 🔎 Scan files in a selected directory
* 🔑 Calculate **SHA-256** hashes
* 💾 Create a trusted file baseline
* 🆕 Detect new files
* ✏️ Detect modified files
* 🗑️ Detect deleted files
* 📁 Monitor user-selected directories
* 💻 Simple command-line interface
* 📄 Store baselines as JSON

---

## How It Works

The tool creates a **baseline** containing the SHA-256 hash of every file it scans.

Later, you can scan the same directory again.

The new hashes are compared against the baseline:

```text
              📁 Target Directory
                      │
                      ▼
                 🔎 Scan Files
                      │
                      ▼
                🔑 SHA-256 Hash
                      │
                      ▼
               💾 Save Baseline
                      │
                      │
                 Later Scan
                      │
                      ▼
                🔑 SHA-256 Hash
                      │
                      ▼
                ⚖️ Compare
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
        🆕 NEW     ✏️ MODIFIED   🗑️ DELETED
```

Even a very small change to a file produces a completely different SHA-256 hash.

---

# Installation

## Requirements

You need:

* Python **3.8+**
* Git (optional, if cloning the repository)

No external Python packages are currently required.

### Check Python

```bash
python3 --version
```

or:

```bash
python --version
```

---

## 📥 Clone the Repository

Clone the project:

```bash
git clone https://github.com/arischatrus/file-integrity-monitor.git
```

Enter the project directory:

```bash
cd file-integrity-monitor
```

You can now run the tool.

---

# 🛠️ Usage

The basic command format is:

```bash
python fim.py [command] [folder]
```

There are currently two commands:

```text
baseline
check
```

---

## 1️⃣ Create a Baseline

Before monitoring a directory, create a baseline:

```bash
python fim.py baseline /path/to/folder
```

For example:

```bash
python fim.py baseline /home/user/Documents
```

The tool calculates a SHA-256 hash for each file and stores the results in the `baselines/` directory.

Example:

```text
Baseline created: baselines/Documents.json
```

---

## 2️⃣ Check File Integrity

After creating a baseline, check the directory:

```bash
python fim.py check /home/user/Documents
```

The tool compares the current file hashes against the saved baseline.

For example:

```text
MODIFIED: /home/user/Documents/report.txt
NEW: /home/user/Documents/suspicious.txt
DELETED: /home/user/Documents/old.txt
```

---

# Example

Suppose we have:

```text
protected/
├── file1.txt
├── file2.txt
└── secret.txt
```

Create the baseline:

```bash
python fim.py baseline protected
```

Now imagine someone modifies `file1.txt`, deletes `file2.txt`, and creates `malware.txt`.

Run:

```bash
python fim.py check protected
```

The result could be:

```text
MODIFIED: protected/file1.txt
NEW: protected/malware.txt
DELETED: protected/file2.txt
```
