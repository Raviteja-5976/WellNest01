import sqlite3



questions = [
    {"Qno": 1, "Question": "Could not stop feeling sad."},
    {"Qno": 2, "Question": "Felt alone."},
    {"Qno": 3, "Question": "Felt everything in my life went wrong."},
    {"Qno": 4, "Question": "Felt like I couldn’t do anything right."},
    {"Qno": 5, "Question": "Felt lonely."},
    {"Qno": 6, "Question": "Felt sad."},
    {"Qno": 7, "Question": "Felt unhappy."},
    {"Qno": 8, "Question": "Thought that his/her life was bad."},
    {"Qno": 9, "Question": "Didn’t care about anything."},
    {"Qno": 10, "Question": "Felt stressed."},
    {"Qno": 11, "Question": "Felt too sad to eat."},
    {"Qno": 12, "Question": "Wanted to be by myself."},
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_DEPRESSION (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Never',
    Option2 TEXT DEFAULT 'Almost Never',
    Option3 TEXT DEFAULT 'Sometimes',
    Option4 TEXT DEFAULT 'Often',
    Option5 TEXT DEFAULT 'Almost Always'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_PARENT_DEPRESSION (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



