import pandas as pd
import sqlite3

# Define the path to the Excel file and SQLite database using raw strings for Windows paths
excel_file = r"C:\Users\pc\Downloads\file-name.xlsx"
db_file = r"C:\Users\pc\Documents\dbName.db"

# Read all sheets from the Excel file
print("\nLeyendo archivo Excel y convirtiendo a DataFrame...\n")
excel_data = pd.read_excel(excel_file, sheet_name=None)

# Initialize an empty list to store DataFrames
all_dfs = []

# Process each sheet
for sheet_name, df in excel_data.items():
    print(f"Procesando hoja: {sheet_name}")
    
    # Clean the DataFrame: remove rows where both title and author are empty
    df = df.dropna(subset=['TITULO DEL LIBRO', 'AUTOR'], how='all')
    
    # Standardize column names to match the SQLite schema
    column_mapping = {
        'TITULO DEL LIBRO': 'titulo',
        'AUTOR': 'autor',
        'EDITORIAL': 'editorial',
        'FORMATO': 'formato',
        'ESTADO DEL LIBRO': 'estado',
        'CANTIDAD': 'cantidad',
        'CANTIDAD DE EJEMPLARES': 'cantidad',  # Map Nicaragüense sheet's column
        'FORMA DE ADQUISICION': 'forma_adquisicion',
        'ISBN': 'isbn',
        'UBICACIÓN': 'ubicacion',
        'CONTENIDO': 'contenido',
        'DISPONIBLE': 'disponible'
    }
    df = df.rename(columns=column_mapping)
    
    # Add the category column based on the sheet name
    df['categoria'] = sheet_name
    
    # Ensure quantity is integer, default to 1 if missing or invalid
    if 'cantidad' in df.columns:
        df['cantidad'] = pd.to_numeric(df['cantidad'], errors='coerce').fillna(1).astype('Int64')
    
    # Append to the list of DataFrames
    all_dfs.append(df)

# Concatenate all DataFrames
print("\nConsolidando datos de todas las hojas...\n")
consolidated_df = pd.concat(all_dfs, ignore_index=True)

# Print the consolidated DataFrame for verification
print(consolidated_df)

# Create or connect to the SQLite database
print("\nConectando a la base de datos SQLite...\n")
connection = sqlite3.connect(db_file)

# Create the libros table if it doesn't exist
print("\nCreando tabla libros...\n")
connection.execute("""
CREATE TABLE IF NOT EXISTS libros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    autor TEXT,
    editorial TEXT,
    formato TEXT,
    estado TEXT,
    cantidad INTEGER,
    forma_adquisicion TEXT,
    isbn TEXT,
    ubicacion TEXT,
    contenido TEXT,
    disponible TEXT,
    categoria TEXT
)
""")

# Insert the consolidated DataFrame into the SQLite table
print("\nInsertando datos en la base de datos SQLite...\n")
consolidated_df.to_sql(
    name='libros',
    con=connection,
    if_exists='replace',
    index=False,
    dtype={
        'titulo': 'TEXT',
        'autor': 'TEXT',
        'editorial': 'TEXT',
        'formato': 'TEXT',
        'estado': 'TEXT',
        'cantidad': 'INTEGER',
        'forma_adquisicion': 'TEXT',
        'isbn': 'TEXT',
        'ubicacion': 'TEXT',
        'contenido': 'TEXT',
        'disponible': 'TEXT',
        'categoria': 'TEXT'
    }
)

# Commit and close the connection
connection.commit()
connection.close()
print("\nDatos insertados exitosamente en la base de datos SQLite.\n")
