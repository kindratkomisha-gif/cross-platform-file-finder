cross-platform-file-finder
A lightweight, cross-platform Python CLI script to search for files across the system with directory exclusion and time-based filtering.

#Cross-Platform File Finder 

A simple yet powerful Python utility designed to search for files across different operating systems (Windows, Linux, macOS) with advanced filtering options.

Features
- Cross-Platform Support:** Automatically detects your operating system and sets the appropriate root search directory.
- Directory Exclusion:** Skips heavy system directories and restricted folders (e.g., `AppData`, `.ssh`) to optimize performance.
- Time-Based Filtering:** Search for files created within a specific timeframe (defined in hours).
- Case-Insensitive Search:** Finds files regardless of uppercase or lowercase characters.
- Safety Checks:** Ignores symbolic links to prevent infinite loops.

Requirements
- Python 3.x

## Usage

Run the script from your terminal:

```bash
python main.py
```

How it works:
1. Enter the name (or part of the name) of the file you are looking for.
2. Specify a time limit in hours (or press `Enter` to search through all files without time restrictions).
3. The script will output a list of matching full file paths.

Built With
- Python standard libraries: `os`, `sys`, `time`
