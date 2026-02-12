# Budget Tracker CLI (Python)

This is a simple command-line budget tracker that lets you add, edit, and delete expenses, update your budget, and generate a receipt in both TXT and JSON format.

## Features

- Add expenses with name + cost
- Edit an expense name or price
- Delete an expense
- Update initial budget
- View budget summary (total spent + remaining budget)
- Saves a receipt as:
  - `Receipt.txt`
  - `Receipt.json` (structured data)

## Tech Stack

- Python (standard library only)
- JSON file storage
- Pathlib for file handling

## How to Run

```bash
python expense_app.py
```

Sample Output

See: sample_output/run-demo.txt

Sample Saved JSON

See: sample_output/Receipt.sample.json

Notes
On exit, the app writes receipt files to a local folder path (based on the code's getFileDir() function).

## Demo

🎥 Demo video: https://github.com/Emmanuel-Awe/budget-tracker-cli/releases/tag/v1.0-demo

On exit, the app writes receipt files to a local folder path (based on the code's get_File_Dir() function).

- Currently optimized for Windows because it uses `msvcrt.getch()` for “press any key” prompts.
