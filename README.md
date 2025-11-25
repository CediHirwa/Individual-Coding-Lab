Student Grade Generator & Organizer

This repository contains the solution for the ALU Individual Coding Lab 1. It consists of a Python application for calculating student grades and a Bash shell script for archiving data files.

**Project Structure:**

grade-generator.py: The main Python application.
organizer.sh: A shell script to archive CSV files.
grades.csv: (Generated) The output file containing student data.
archive/: (Generated) Directory where old CSV files are stored.
organizer.log: (Generated) Log file tracking archival operations.

Breakdown:

**Python Application**

1.Interactive Input: Accepts student name,ID(3 Digits), assignment Name, Category (FA/SA), Grade, and Weight.
2.Validation: Ensures grades are 0-100, weights are positive, and categories are correct.
3.Calculation:
  *Calculates weighted averages.
  *Computes GPA based on the 5.0 scale.
  *Determines Pass/Fail status (Requires >= 50% in both FA and SA categories).
4.Export: Saves all data to `grades.csv`with the student's name and ID included in every row.

**Bash Organizer**

1.Automated Archiving: Detects `.csv` files.
2.Timestamping: Renames files with the current timestamp (e.g., `grades-20251105.csv`).
3.Logging: Records the operation and the content of the file in `organizer.log`.
