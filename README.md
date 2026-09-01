# 🔐 File Integrity Monitor

A lightweight Python-based **File Integrity Monitoring (FIM)** tool that detects changes to files using **SHA-256 cryptographic hashes**.

Built as a cybersecurity learning project to explore file integrity monitoring, cryptographic hashing, Python automation, command-line interfaces, and Git/GitHub.

---

## ✨ Features

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

## 🧠 How It Works

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

# 🚀 Installation

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

# 🧪 Example

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

This is the basic idea behind **File Integrity Monitoring**.

---

# 🔑 Why SHA-256?

A cryptographic hash produces a fixed-length value based on the contents of a file.

For example:

```text
File
 │
 ▼
SHA-256
 │
 ▼
e3b0c44298fc1c149afbf4c8996fb924...
```

If the file changes:

```text
Original file
     │
     ▼
  SHA-256
     │
     ▼
   Hash A


Modified file
     │
     ▼
  SHA-256
     │
     ▼
   Hash B
```

Hash A and Hash B will normally be different.

The FIM uses this property to detect changes without manually comparing the contents of every file.

---

# 📂 Project Structure

```text
file-integrity-monitor/
│
├── fim.py                 # Main application
├── README.md              # Documentation
├── .gitignore             # Files ignored by Git
│
├── baselines/
│   └── .gitkeep           # Keeps directory in Git
│
└── ...
```

Baseline JSON files are intentionally excluded from Git because they are generated locally for the directories being monitored.

---

# 🧰 Technologies

| Technology | Purpose                     |
| ---------- | --------------------------- |
| 🐍 Python  | Main programming language   |
| 🔐 SHA-256 | File integrity verification |
| 📄 JSON    | Baseline storage            |
| 📁 pathlib | File and directory handling |
| 💻 sys     | Command-line arguments      |
| 🌿 Git     | Version control             |
| 🐙 GitHub  | Project hosting             |

---

# 🎯 What I Learned

This project was built while learning cybersecurity and Python.

Through the project, I practiced:

* Python functions
* Dictionaries
* File I/O
* JSON
* `pathlib`
* SHA-256 hashing
* Command-line arguments
* Error handling
* File integrity monitoring concepts
* Git
* GitHub
* Version control
* Basic project documentation

---

# 🚧 Current Limitations

This is an **educational project** and is still under development.

Current limitations include:

* ❌ Directory scanning is not yet recursive
* ❌ Baseline naming can conflict when different directories have the same name
* ❌ No continuous monitoring mode
* ❌ No logging system
* ❌ Limited command-line argument handling
* ❌ No automated test suite yet

These limitations are intentionally documented as part of the project's development roadmap.

---

# 🗺️ Roadmap

### v0.1 — Initial Version ✅

* [x] SHA-256 hashing
* [x] File scanning
* [x] Baseline creation
* [x] New file detection
* [x] Modified file detection
* [x] Deleted file detection
* [x] Command-line interface
* [x] User-selected directories
* [x] GitHub repository

### v0.2 — Scanner Improvements 🔨

* [ ] Recursive directory scanning
* [ ] Better baseline storage
* [ ] Improved command-line interface
* [ ] Better error handling
* [ ] Cleaner terminal output

### v0.3 — Monitoring & Logging 🔭

* [ ] Continuous monitoring mode
* [ ] Event logging
* [ ] Timestamps
* [ ] Configurable monitoring

### v0.4 — Testing 🧪

* [ ] Unit tests
* [ ] Integration tests
* [ ] Automated testing

---

# 🔐 Security Note

This project is intended for **educational and defensive security purposes**.

It is not intended to replace production-grade File Integrity Monitoring solutions.

For real-world environments, additional security controls are required, including secure baseline storage, authentication, logging, alerting, access control, and protection against attackers who can modify both monitored files and their baselines.

---

# 👨‍💻 Author

Built as part of my cybersecurity learning journey.

The project is intentionally developed step-by-step to document the learning process and gradually improve the tool.

⭐ If you find the project useful or interesting, feel free to star the repository!
