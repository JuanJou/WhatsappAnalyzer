import sqlite3 as sql

def get_db_connection():
    db_connection = sql.connect("user")
    cursor = db_connection.cursor()
    return cursor


cursor = get_db_connection()

cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, user_name STRING REQUIRED, hash_password BINARY REQUIRED)")
