# SQLite Drop Columns Script

A simple Python script to remove multiple columns from a SQLite database table in bulk.

## ⚠️ Warning
Dropping columns is **permanent**. Always make a backup of your database file before using this script.

## Features
- Remove one or many columns from a SQLite table.
- Works with sequentially named columns (e.g., `field1` to `field100`).
- Minimal dependencies (only `sqlite3`, included in Python).

## Usage

1. Clone this repository (or download the single script if you only need this one):
2. Edit the script to set:
   - `database_file`: Path to your SQLite database file.
   - `target_table`: Name of the table you want to modify.
   - `columns_to_remove`: List of columns to delete.

Example inside the script:

```python
# Path to your SQLite database file
database_file = "path/to/your/database.db"

# Name of the table to modify
target_table = "your_table"

# List of columns to remove (sequentially named fields)
columns_to_remove = [f"field{i}" for i in range(1, 101)]
```

3. Run the script with:

```bash
python drop_columns.py
```

4. The script will execute `ALTER TABLE ... DROP COLUMN ...` for each column in the list.

## Example Output
```
Executing: ALTER TABLE your_table DROP COLUMN field1;
Executing: ALTER TABLE your_table DROP COLUMN field2;
...
✅ All specified columns have been successfully removed.
```

## Requirements
- Python 3.x
- SQLite3 (comes preinstalled with Python)

---

### License
MIT License
