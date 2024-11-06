# setup_db.py
import pyodbc
from config import Config

def run_sql(filename):
    conn = pyodbc.connect(Config.DATABASE_URI)
    cursor = conn.cursor()
    with open(filename, 'r', encoding='utf-8') as file:
        sql_script = file.read()
    for statement in sql_script.split(';'):
        statement = statement.strip()
        if statement:
            cursor.execute(statement)
            conn.commit()
    cursor.close()
    conn.close()
    print("Successfully!")

# Run this script to initialize the database
if __name__ == "__main__":
    run_sql('order_status.sql')
