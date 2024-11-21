import sqlite3



questions = [
    {"Qno": 1, "Question": "I could not stop feeling sad."},
    {"Qno": 2, "Question": "I felt alone."},
    {"Qno": 3, "Question": "I felt everything in my life went wrong."},
    {"Qno": 4, "Question": "I felt like I couldn’t do anything right."},
    {"Qno": 5, "Question": "I felt lonely."},
    {"Qno": 6, "Question": "I felt sad."},
    {"Qno": 7, "Question": "I felt unhappy."},
    {"Qno": 8, "Question": "I thought that my life was bad."},
    {"Qno": 9, "Question": "Being sad made it hard for me to do things with my friends."},
    {"Qno": 10, "Question": "I didn’t care about anything."},
    {"Qno": 11, "Question": "I felt stressed."},
    {"Qno": 12, "Question": "I felt too sad to eat."},
    {"Qno": 13, "Question": "I wanted to be by myself."},
    {"Qno": 14, "Question": "It was hard for me to have fun."}
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_DEPRESSION (
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
    INSERT INTO L2_CHILD_DEPRESSION (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



