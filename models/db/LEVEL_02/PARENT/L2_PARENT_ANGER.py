import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "My Child flet Mad",
},
{
"Qno": 2,
"Question": "My was so angry he/she felt like throwing something.",
},
{	
"Qno": 3,
"Question": "My was so angry he/she felt like yelling at somebody.",
},
{	
"Qno": 4,
"Question": "My child felt upset.",
},
{
"Qno": 5,
"Question": "When my child got mad, he/she stayed mad. ",
}
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_ANGER (
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
    INSERT INTO L2_PARENT_ANGER (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
