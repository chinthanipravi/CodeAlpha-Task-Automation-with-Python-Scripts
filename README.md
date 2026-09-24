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

#  Email Extractor Script 📧

A Python script that automatically scans text files and extracts all valid email addresses using Regular Expressions (Regex).

---

## 📌 Project Overview
The Email Extractor automates the task of finding and extracting email addresses from raw text or documents, removing duplicates, and saving them into a clean text file.

---

## ✨ Features
* **Regex Pattern Matching:** Uses regular expressions to accurately detect email formats.
* **Duplicate Removal:** Automatically removes duplicate email entries using Python sets.
* **File Export:** Saves all extracted emails line-by-line into `extracted_emails.txt`.
* **Error Handling:** Gracefully handles missing files or unreadable text formats.

---

## 🧠 Concepts Applied
* `re` module (Regular Expressions)
* File Handling (`open()`, `read()`, `write()`)
* Set & List Data Structures

---

## 🚀 How to Run

1. Make sure Python is installed on your system.
2. Open your terminal/command prompt in the directory where `email_extractor.py` is saved.
3. Run the following command:
   ```bash
   python email_extractor.py
