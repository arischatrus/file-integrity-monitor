# File Integrity Monitor

A simple Python-based File Integrity Monitoring (FIM) tool that detects unauthorized or unexpected changes to files using SHA-256 cryptographic hashes.

This project was built as a cybersecurity learning project to understand file integrity monitoring, cryptographic hashing, Python automation, and command-line tools.

## What does it do?

The tool creates a trusted baseline of files in a directory by calculating a SHA-256 hash for each file.

Later, the directory can be scanned again and compared against the baseline.

It can detect:

* **NEW** — a file was added
* **MODIFIED** — a file's contents changed
* **DELETED** — a file from the baseline is no longer present

### How it works

```text
                 Target directory
                        │
                        ▼
                  Scan files
                        │
                        ▼
                Calculate SHA-256
                        │
                        ▼
                  Save baseline
                        │
                        │
                  Later scan
                        │
                        ▼
                 Calculate hashes
                        │
                        ▼
                  Compare hashes
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
           NEW      MODIFIED    DELETED
```

## Requirements

* Python 3
* No external Python packages are currently required.

## Usage

### 1. Create a baseline

```bash
python fim.py baseline /path/to/folder
```

Example:

```bash
python fim.py baseline /home/user/Documents
```

This creates a baseline containing the SHA-256 hashes of the files in the selected directory.

### 2. Check file integrity

```bash
python fim.py check /path/to/folder
```

Example:

```bash
python fim.py check /home/user/Documents
```

If files have changed, the tool reports them:

```text
MODIFIED: /home/user/Documents/example.txt
NEW: /home/user/Documents/suspicious.txt
DELETED: /home/user/Documents/old.txt
```

## Example

Create a baseline:

```bash
python fim.py baseline protected
```

Modify a file and create a new file.

Then run:

```bash
python fim.py check protected
```

The tool will compare the current file hashes against the saved baseline.

## Why SHA-256?

A cryptographic hash produces a fixed-length value representing the contents of a file.

For example:

```text
file contents
      │
      ▼
   SHA-256
      │
      ▼
e3b0c44298fc1c149afbf4c8996fb924...
```

Even a small change to the file produces a different hash.

The tool uses this property to detect changes without needing to compare the entire contents of files manually.

## Current Features

* SHA-256 file hashing
* File discovery
* Baseline creation
* File modification detection
* New file detection
* Deleted file detection
* User-selected target directories
* Command-line interface
* Separate baseline files for monitored directories

## Current Limitations

This is an educational project and is still under development.

Current limitations include:

* File scanning is not yet recursive
* Baseline naming can have conflicts for directories with the same name
* No continuous monitoring mode
* No logging system
* No automated tests yet
* Limited command-line argument validation

## Roadmap

Planned improvements:

* [ ] Recursive directory scanning
* [ ] Better baseline storage
* [ ] Improved command-line interface
* [ ] Clear `[NEW]`, `[MODIFIED]`, `[DELETED]` output
* [ ] "No changes detected" status
* [ ] Error handling for missing/corrupted baselines
* [ ] Logging
* [ ] Continuous monitoring mode
* [ ] Automated tests
* [ ] Configuration options
* [ ] Documentation improvements

## What I Learned

Through this project I am practicing:

* Python functions
* File handling
* `pathlib`
* Dictionaries
* JSON
* SHA-256 hashing
* Command-line arguments
* File integrity monitoring concepts
* Basic cybersecurity automation
* Git and GitHub workflow

## Disclaimer

This project is intended for educational and defensive security purposes.

It is not intended to replace a production-grade File Integrity Monitoring solution.

## Author

Built as part of my cybersecurity learning journey.
