# config.py

class Config:
    DEBUG = True
    DATABASE_URI = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=DESKTOP-HQ4AVAA\SQLEXPRESS;"  # Replace with your server name
        "DATABASE=ORDER_STATUS;"
        "Trusted_Connection=yes;"# Replace with the database name from order_Status.sql
        # Replace with your SQL Server password
        
    )
