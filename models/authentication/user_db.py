import sqlite3
from contextlib import contextmanager

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect('wellnest01.db')
        yield conn
    finally:
        if conn:
            conn.commit()
            conn.close()

def user_test_info(username, conn):
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {username}_test_info (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id TEXT NOT NULL,
            test_question TEXT NOT NULL,
            test_answer TEXT NOT NULL,
            date TEXT NOT NULL
        );
    ''')

def user_test_result(username, conn):
    cursor = conn.cursor()
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {username}_test_result (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_id TEXT NOT NULL,
            test_result TEXT NOT NULL,
            date TEXT NOT NULL
        );
    ''')