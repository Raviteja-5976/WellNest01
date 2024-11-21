import sqlite3

questions = [
 { "Qno": 1, "Question": "felt moments of sudden terror, fear or fright, sometimes out of the blue (i.e., apanic attack)" },
 { "Qno": 2, "Question": "felt anxious, worried, or nervous about having more panic attacks" },
 { "Qno": 3, "Question": "had thoughts of losing control, dying, going crazy, or other bad thingshappening because of panic attacks" },
 { "Qno": 4, "Question": "felt a racing heart, sweaty, trouble breathing, faint, or shaky" },
 { "Qno": 5, "Question": "felt tense muscles, felt on edge or restless, or had trouble relaxing or troublesleeping" },
 { "Qno": 6, "Question": "avoided, or did not approach or enter, situations in which panic attacks mightoccur" },
 { "Qno": 7, "Question": "left situations early, or participated only minimally, because of panic attacks" },
 { "Qno": 8, "Question": "spent a lot of time preparing for, or procrastinating about (putting off),situations in which panic attacks might occur" },
 { "Qno": 9, "Question": "distracted myself to avoid thinking about panic attacks" },
 { "Qno": 10, "Question": "needed help to cope with panic attacks (e.g., alcohol or medication,superstitious objects, other people)" }
 ]

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_ADULT_PANIC_D (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Never',
    Option2 TEXT DEFAULT 'Occasionally',
    Option3 TEXT DEFAULT 'Half of the time',
    Option4 TEXT DEFAULT 'Most of the time',
    Option5 TEXT DEFAULT 'All of the time'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO SMD_ADULT_PANIC_D (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
