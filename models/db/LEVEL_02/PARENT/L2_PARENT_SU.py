import sqlite3

questions = [
    {"Qno": 1, "Question": "Have an alcoholic beverage (beer, wine, liquor, etc.)?"},
    {"Qno": 2, "Question": "Have 4 or more drinks in a single day?"},
    {"Qno": 3, "Question": "Smoke a cigarette, a cigar, or pipe or use snuff or chewing tobacco?"},
    {"Qno": 4, "Question": "Painkillers (like Vicodin)"},
    {"Qno": 5, "Question": "Stimulants (like Ritalin, Adderall)"},
    {"Qno": 6, "Question": "Sedatives or tranquilizers (like sleeping pills or Valium)"},
    {"Qno": 7, "Question": "Steroids"},
    {"Qno": 8, "Question": "Other medicines"},
    {"Qno": 9, "Question": "Marijuana"},
    {"Qno": 10, "Question": "Cocaine or crack"},
    {"Qno": 11, "Question": "Club drugs (like ecstasy)"},
    {"Qno": 12, "Question": "Hallucinogens (like LSD)"},
    {"Qno": 13, "Question": "Heroin"},
    {"Qno": 14, "Question": "Inhalants or solvents (like glue)"},
    {"Qno": 15, "Question": "Methamphetamine (like speed)"}
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_SU (
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
    INSERT INTO L2_PARENT_SU (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
