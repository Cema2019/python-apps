# Convert Excel table to SQLite database

This Python script imports book inventory data from an Excel file with multiple sheets into a single SQLite database. It was designed to help a small public library in Nicaragua transition from managing book records in cumbersome Excel spreadsheets to a more efficient and queryable SQLite database.

## Features

- Reads all sheets from an Excel workbook containing book lists.
- Cleans data by removing rows with both missing title and author fields.
- Standardizes Spanish column names (e.g., "TITULO DEL LIBRO" to "title") for consistency.
- Adds a `category` field based on the sheet name (e.g., "Internacionales", "Religion").
- Converts quantity fields to integers, defaulting to 1 for missing or invalid values.
- Creates or updates a SQLite database with a consolidated `books` table.
- Provides console output to track progress and verify data import.

## Requirements

- Python 3.7 or higher
- `pandas` 
- `openpyxl` – required for reading Excel files
- `sqlite3` (included in Python’s standard library)

## Usage

1. Ensure the required Python packages are installed:
   ```bash
   pip install pandas openpyxl
   ```

2. Update the `excel_file` and `db_file` paths in the script to match your system:
   - `excel_file`: Path to the Excel file (e.g., `Book catalog.xlsx`).
   - `db_file`: Path to the output SQLite database (e.g., `BookInventory.db`).
   - Use raw strings (e.g., `r"C:\path\to\file.xlsx"`) for Windows paths to avoid issues with backslashes.

3. Run the script:
   ```bash
   python xl_to_sqlite.py
   ```

   The script will:
   - Read all sheets from the Excel file.
   - Process and clean the data.
   - Create or overwrite a SQLite database with the `books` table.
   - Insert the consolidated data and display progress messages.

4. Verify the database:
   - Open the `.db` file using a SQLite viewer (e.g., DB Browser for SQLite).
   - Run queries to check the data, e.g.:
     ```sql
     SELECT * FROM books WHERE category = 'Internacionales' LIMIT 10;
     ```

## Database Schema

The script creates a `books` table with the following columns:
- `id`: Auto-incrementing primary key (INTEGER)
- `title`: Book title (TEXT, nullable)
- `author`: Author name (TEXT, nullable)
- `publisher`: Publisher name (TEXT, nullable)
- `format`: Book format, e.g., "Physical" (TEXT, nullable)
- `condition`: Book condition, e.g., "Good" (TEXT, nullable)
- `quantity`: Number of copies (INTEGER, defaults to 1 if missing)
- `acquisition_method`: How the book was acquired, e.g., "Donation" (TEXT, nullable)
- `isbn`: ISBN number (TEXT, nullable)
- `location`: Physical location (TEXT, nullable)
- `content`: Content or genre, e.g., "Poetry" (TEXT, nullable)
- `available`: Availability status (TEXT, nullable)
- `category`: Sheet name from the Excel file, e.g., "International" (TEXT)

## Notes

- **Input Assumptions**: The script expects Excel sheets with columns like "TITULO DEL LIBRO", "AUTOR", "EDITORIAL", etc. It handles variations and maps them to the schema.
- **Data Cleaning**: Rows missing both title and author are excluded to avoid clutter. Other missing fields are stored as `NULL`.
- **Error Handling**: Ensure the Excel file is accessible and not open in another program. Check file paths if errors occur.
- **Post-Import**: Use the SQLite database for inventory management, such as searching books by category or author, or generating reports.

