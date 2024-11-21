import sqlite3
from time import sleep


questions = [
    {"Qno": 1, "Question": "Stomach pain"},
    {"Qno": 2, "Question": "Back pain"},
    {"Qno": 3, "Question": "Pain in your arms, legs, or joints (knees, hips, etc.)"},
    {"Qno": 4, "Question": "Menstrual cramps or other problems with your periods (WOMEN ONLY)"},
    {"Qno": 5, "Question": "Headaches"},
    {"Qno": 6, "Question": "Chest pain"},
    {"Qno": 7, "Question": "Dizziness"},
    {"Qno": 8, "Question": "Fainting spells"},
    {"Qno": 9, "Question": "Feeling your heart pound or race"},
    {"Qno": 10, "Question": "Shortness of breath"},
    {"Qno": 11, "Question": "Pain or problems during sexual intercourse"},
    {"Qno": 12, "Question": "Constipation, loose bowels, or diarrhea"},
    {"Qno": 13, "Question": "Nausea, gas, or indigestion"},
    {"Qno": 14, "Question": "Feeling tired or having low energy"},
    {"Qno": 15, "Question": "Trouble sleeping"}
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_ADULT_SS (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not Bothered At All',
    Option2 TEXT DEFAULT 'Bothered A Little',
    Option3 TEXT DEFAULT 'Bothered A Lot'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_ADULT_SS (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
