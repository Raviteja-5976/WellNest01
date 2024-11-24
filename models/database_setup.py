
import sqlite3

def init_db():
    conn = sqlite3.connect('wellnest01.db')
    c = conn.cursor()
    
    # Create test_results table if it doesn't exist
    c.execute('''CREATE TABLE IF NOT EXISTS test_results
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT NOT NULL,
                  test_id TEXT NOT NULL,
                  raw_score INTEGER,
                  t_score FLOAT,
                  result TEXT,
                  date DATETIME,
                  FOREIGN KEY (username) REFERENCES users(username))''')
    
    conn.commit()
    conn.close()