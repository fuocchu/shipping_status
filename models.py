import pyodbc
from config import Config

def db_connection():
    conn = pyodbc.connect(Config.DATABASE_URI)
    return conn

def get_status(ID):
    conn = db_connection()
    cursor = conn.cursor()
    query = "SELECT ORDER_STATUS FROM ORDERS WHERE ID = ? "
    cursor.execute(query,(ID,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result else None