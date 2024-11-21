import sqlite3
from time import sleep

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_SD (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT,
    Option2 TEXT,
    Option3 TEXT,
    Option4 TEXT,
    Option5 TEXT
);
"""
cursor.execute(create_table_query)

questions = [
    {"Qno": 1, "Question": "His/her sleep was restless.", "Options": ["Not at all", "A little bit", "Somewhat", "Quite a bit", "Very much"]},
    {"Qno": 2, "Question": "He/she was satisfied with his/her sleep..", "Options": ["Not at all", "A little bit", "Somewhat", "Quite a bit", "Very much"]},
    {"Qno": 3, "Question": "His/her sleep was refreshing.", "Options": ["Not at all", "A little bit", "Somewhat", "Quite a bit", "Very much"]},
    {"Qno": 4, "Question": "He/she had difficulty falling asleep.", "Options": ["Not at all", "A little bit", "Somewhat", "Quite a bit", "Very much"]},
    {"Qno": 5, "Question": "He/she had trouble staying asleep.", "Options": ["Never", "Rarely", "Sometimes", "Often", "Always"]},
    {"Qno": 6, "Question": "He/she had trouble sleeping.", "Options": ["Never", "Rarely", "Sometimes", "Often", "Always"]},
    {"Qno": 7, "Question": "He/she got enough sleep.", "Options": ["Never", "Rarely", "Sometimes", "Often", "Always"]},
    {"Qno": 8, "Question": "His/her sleep quality was...", "Options": ["Very Poor", "Poor", "Fair", "Good", "Very Good"]}
]

# ]
command = """
INSERT INTO L2_PARENT_SD (Qno, Question, Option1, Option2, Option3, Option4, Option5)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
for item in questions:
    options = item["Options"]
    cursor.execute(command, (item["Qno"], item["Question"], options[0], options[1], options[2], options[3], options[4]))
    sleep(0.01)


connection.commit()
connection.close()




