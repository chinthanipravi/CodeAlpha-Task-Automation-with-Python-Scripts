# Task 3: Task Automation Script ⚙️

A Python automation script that automatically categorizes and organizes files in a directory based on their file extensions, developed for the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
The File Organizer Script cleans up cluttered directories by automatically scanning all files and sorting them into categorized subfolders (such as `Images`, `Documents`, and `Python_Files`).

---

## ✨ Features
* **Automated File Sorting:** Automatically sorts files (`.jpg`, `.png`, `.pdf`, `.txt`, `.py`, etc.) into dedicated folders.
* **Dynamic Folder Creation:** Creates missing category folders automatically if they do not already exist.
* **Safe File Management:** Ignores existing directories to prevent accidental nested file transfers or errors.
* **Custom Directory Path:** Allows users to specify any folder path or automatically clean the current directory.

---

## 🧠 Concepts Applied
* `os` module (directory scanning, path manipulation, and folder creation)
* `shutil` module (safe file moving operations)
* File Extension Parsing (`os.path.splitext`)
* Loops and conditional dictionary mapping

---

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Open your terminal/command prompt in the directory where `file_organizer.py` is saved.
3. Run the following command:
   ```bash
   python file_organizer.py
