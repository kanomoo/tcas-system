# TCAS System

TCAS System is a command-line application for managing TCAS-related student registration data, course information, and application fee reports. The program is organized around a simple text-based menu so users can register students, browse course details, and generate summary reports from the stored data files.

## Recommended GitHub Setup

- Repository name: `tcas-system`
- About: `A command-line TCAS management system for student registration, course information, and application fee reporting.`

## Features

- Register and manage student records
- Store and update TCAS application data
- Browse universities, faculties, and programs
- Generate applicant and fee summary reports
- Display formatted tables in the terminal for easier reading

## Requirements

- Python 3.10 or newer
- The `wcwidth` package for proper terminal alignment, especially for Thai text

## Installation

Install the required dependency with:

```bash
pip install wcwidth
```

If you are using a virtual environment, activate it first before installing packages.

## How to Run

Run the application from the project root with:

```bash
python main.py
```

After the program starts, choose the menu number shown on the screen.

## Main Menu

The application starts with these top-level options:

1. Student Menu - register students, edit student data, and view student reports
2. Course information - search and manage university, faculty, and program information
3. TCAS Applicant and Fee Statistics Report - generate statistics from the registration records
4. Exit Program - close the application

## Detailed Function Overview

### Student Menu

This menu is used to manage student-related information.

- Register a new student
- Register exam/application details for a student
- Edit student data
- Delete application or student data
- Print ID card and registration reports

### Course Information

This menu is used to browse and manage course-related information.

- Search by university, faculty, or program
- View all stored course information
- View total course counts

### Statistics Report

This report section summarizes applicant records and application fees.

- Counts applicants by university and program
- Summarizes fee totals
- Groups entries by TCAS round

## Data Files

The application reads and writes plain text data under `data_information/datas`.

- `data_student.txt` stores basic student records
- `data_register.txt` stores student registration/application data
- `data_course_info.txt` stores university, faculty, and program information

These files are part of the application state, so keep them with the project when moving or backing up the repository.

## Project Structure

```text
Tcas-System/
├── main.py
├── main.spec
├── README.md
├── data_information/
│   ├── course_info.py
│   ├── report_register.py
│   ├── student_tcas.py
│   └── datas/
│       ├── data_course_info.txt
│       ├── data_register.txt
│       └── data_student.txt
```

## Notes

- The project is a terminal application, not a web app or GUI app.
- The code uses `match` statements, so Python 3.10+ is required.
- The repository already includes `main.spec`, which can be used with PyInstaller to build an executable.

## Example Workflow

1. Start the program with `python main.py`.
2. Open the Student Menu to register or edit student data.
3. Open Course information to find the target university, faculty, and program.
4. Register the exam/application details.
5. Use the statistics report to review total applicants and total fees.

## Suggested Description for the README Header

If you want a short one-line intro for the top of the repository, use this:

> A terminal-based TCAS management system for student registration, course information, and applicant fee reporting.