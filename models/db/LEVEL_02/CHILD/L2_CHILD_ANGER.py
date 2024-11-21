import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "I flet Mad",
},
{
"Qno": 2,
"Question": "I was so angry I felt like throwing something.",
},
{	
"Qno": 3,
"Question": "I was so angry I felt like yelling at somebody.",
},
{	
"Qno": 4,
"Question": "When I got mad, I stayed mad.",
},
{
"Qno": 5,
"Question": "I felt fed up.",
},
{
"Qno": 6,
"Question": "I felt upset.",
},
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_ANGER (
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
    INSERT INTO L2_CHILD_ANGER (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
