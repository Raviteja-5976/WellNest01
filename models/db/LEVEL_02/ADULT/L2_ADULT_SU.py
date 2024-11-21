import sqlite3

questions = [
    {"Qno": 1, "Question": "Painkillers (like Vicodin)"},
    {"Qno": 2, "Question": "Stimulants (like Ritalin, Adderall)"},
    {"Qno": 3, "Question": "Sedatives or tranquilizers (like sleeping pills or Valium)"},
    {"Qno": 4, "Question": "Marijuana"},
    {"Qno": 5, "Question": "Cocaine or crack"},
    {"Qno": 6, "Question": "Club drugs (like ecstasy)"},
    {"Qno": 7, "Question": "Hallucinogens (like LSD)"},
    {"Qno": 8, "Question": "Heroin"},
    {"Qno": 9, "Question": "Inhalants or solvents (like glue)"},
    {"Qno": 10, "Question": "Methamphetamine (like speed)"}
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_SU (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not At All',
    Option2 TEXT DEFAULT 'Less Than a Day or Two',
    Option3 TEXT DEFAULT 'Several Days',
    Option4 TEXT DEFAULT 'More than half the days',
    Option5 TEXT DEFAULT 'Nearly Every Day'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_CHILD_SU (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
