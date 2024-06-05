import sqlite3
from sqlite3 import Connection

def get_db_connection() -> Connection:
    conn = sqlite3.connect('data.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS sensor (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        created_at TEXT NOT NULL,
                        value REAL NOT NULL
                    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS automation (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        created_at TEXT NOT NULL,
                        state TEXT NOT NULL
                    )''')
    return conn
