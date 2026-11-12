# Python Schedule Manager

A simple command-line schedule management application built with Python and Pandas.

Python Schedule Manager allows users to create, view, edit, and delete daily schedules using CSV files for data storage.

## Features

- **Daily Scheduling:** Create schedules for individual days of the week.
- **Today's Schedule:** Automatically select the current day.
- **Add Entries:** Add time slots and their corresponding activities.
- **Edit Entries:** Modify existing times and activities.
- **View Schedules:** Display saved schedules in a tabular format.
- **Remove Entries:** Delete unwanted schedule entries.
- **CSV Storage:** Store each day's schedule in a separate CSV file.

## Tech Stack

- Python
- Pandas
- CSV

## Project Structure

```text
pythonScheduleManager/
│
├── main.py
├── requirements.txt
├── README.md
│
└── schedule/
    ├── monday.csv
    ├── tuesday.csv
    ├── wednesday.csv
    └── ...
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Abhishekrauniyarr/pythonScheduleManager.git
```

### 2. Navigate to the project directory

```bash
cd pythonScheduleManager
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python main.py
```

## How to Use

1. Run the application.
2. Select a day from the menu.
3. Choose an operation:
   - Add Data
   - Edit Data
   - View Data
   - Remove Data
   - Back to Day Selection
4. Follow the terminal instructions.

To finish adding schedule entries, type `stop` when prompted for the time.

## Data Storage

Schedules are stored as individual CSV files inside the `schedule/` directory.

Each file contains two columns:

| Time | Activities |
|---|---|
| 05:00 AM | Study |
| 07:00 AM | Breakfast |
| 09:00 AM | College |

## Current Version

**Version 1.0**

This is the initial version of the project. Future versions may introduce improved data management, a more flexible architecture, and additional scheduling functionality.

## Author

**Abhishek Rauniyar**

GitHub: [@Abhishekrauniyarr](https://github.com/Abhishekrauniyarr)

---

*Built as a Python learning project.*

