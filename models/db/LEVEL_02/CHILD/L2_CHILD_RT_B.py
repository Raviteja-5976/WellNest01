import sqlite3
from time import sleep

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_RT_B (
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
    {
        "Qno": 1,
        "Question": "On average, how much time is occupied by these thoughts or behaviors each day?",
        "Options": ["None", "Less than an hour a day", "1 to 3 hours a day", "3 to 8 hours a day", "more than 8 hours a day"]
    },
    {
        "Qno": 2,
        "Question": "How much do they bother you?",
        "Options": ["None", "slightly upsetting", "upsetting but still manageable", "very upsetting", "overwhelming distress"]
    },
    {
        "Qno": 3,
        "Question": "How hard is it for you to control them?",
        "Options": ["Complete control", "Much control (usually able to control thoughts or behaviors)", "Moderate control (sometimes able to control thoughts or behaviors)", "Little control (not usually able to control thoughts or behaviors)", "No control (unable to control thoughts or behaviors)"]
    },
    {
        "Qno": 4,
        "Question": "How much do they cause you to avoid doing things, going places, or being with people?",
        "Options": ["No avoidance", "occasionally avoids things", "regularly avoids doing these things", "frequently avoids these things", "nearly complete avoidance; can’t leave the house"]
    },
    {
        "Qno": 5,
        "Question": "How much do they interfere with school, your social or family life, or your job?",
        "Options": ["None", "slight interference", "definite interference with functioning, but can still manage", "substantial interference", "near-total interference"]
    }
]


# ]
command = """
INSERT INTO L2_CHILD_RT_B (Qno, Question, Option1, Option2, Option3, Option4, Option5)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
for item in questions:
    options = item["Options"]
    cursor.execute(command, (item["Qno"], item["Question"], options[0], options[1], options[2], options[3], options[4]))
    sleep(0.01)


connection.commit()
connection.close()




