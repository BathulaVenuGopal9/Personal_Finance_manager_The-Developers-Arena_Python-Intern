# Personal Finance Manager (Python CLI)

A simple command-line based Personal Finance Manager built using Python.  
This project allows users to track expenses, generate reports, and manage backups using CSV file storage.

---

##  Features

- Add Expense (Amount, Category, Date, Description)
- View All Expenses
- Category-wise Expense Summary
- Monthly Expense Report
- Backup Expense Data
- Restore from Backup
- CSV File Storage
- Input Validation
- Simple CLI Menu Interface

---

##  Tech Stack

- Python 3
- CSV File Handling
- File System Operations (os, shutil)
- Datetime Module

---

## Project Structure

finance_manager/
│── main.py
│── requirements.txt
│── README.md
│
├── src/
│ ├── expense.py
│ ├── file_manager.py
│ ├── menu.py
│ ├── reports.py
│ ├── utils.py
│
├── data/
│ └── expenses.csv
│
├── backups/
│ └── (auto generated backup files)

## Sample Features

Category Summary → Shows total expense per category

Monthly Report → Shows total expense per month

Backup → Creates timestamped backup file

Restore → Recovers previous backup

## Project Purpose

This project was built as part of an internship to demonstrate:

Python Programming

File Handling

Modular Code Structure

CLI Application Development

Data Processing & Reporting

# Author

BATHULA VENU GOPAL | INTERN AT THE DEVELOPERS ARENA.

