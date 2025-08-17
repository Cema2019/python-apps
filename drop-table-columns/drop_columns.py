"""
SQLite Drop Columns Script
--------------------------

This script connects to a SQLite database and removes multiple columns from a specified table.

⚠️ WARNING: Dropping columns is permanent. Always make a backup of your database before running this script.

Usage:
    1. Edit the values of `database_file`, `target_table`, and `columns_to_remove`.
    2. Run the script with: python drop_columns.py
"""

import sqlite3

def drop_columns(db_path, table_name, columns_to_drop):
    """
    Connects to a SQLite database and removes multiple columns from a table.

    Args:
        db_path (str): The path to the SQLite database file.
        table_name (str): The name of the table to modify.
        columns_to_drop (list): A list of strings, where each string is the
                                name of a column to be removed.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        for column in columns_to_drop:
            sql_query = f"ALTER TABLE {table_name} DROP COLUMN {column};"
            print(f"Executing: {sql_query}")
            cursor.execute(sql_query)

        conn.commit()
        print("\n✅ All specified columns have been successfully removed.")

    except sqlite3.Error as e:
        print(f"⚠️ An error occurred: {e}")
        if conn:
            conn.rollback()
    finally:
        if conn:
            conn.close()


# Path to your SQLite database file
database_file = "path/to/your/database.db"

# Name of the table to modify
target_table = "your_table"

# List of columns to remove
# Example: removing sequential fields from field1 to field100
columns_to_remove = [f"field{i}" for i in range(1, 101)]

# Run the function
drop_columns(database_file, target_table, columns_to_remove)
