import sqlite3
from time import sleep


questions = [
    {"Qno": 1, "Question": "Am easily annoyed by others."},
    {"Qno": 2, "Question": "Often lose my temper."},
    {"Qno": 3, "Question": "Stay angry for a long time."},
    {"Qno": 4, "Question": "Am angry most of the time."},
    {"Qno": 5, "Question": "Get angry frequently."},
    {"Qno": 6, "Question": "Lose temper easily."},
    {"Qno": 7, "Question": "Overall irritability causes me problems."}
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_IRRITABILITY (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not True',
    Option2 TEXT DEFAULT 'Somewhat True',
    Option3 TEXT DEFAULT 'Certainley True'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_CHILD_IRRITABILITY (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
