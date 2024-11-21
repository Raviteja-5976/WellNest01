import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "I was irritated more than people knew.",
},
{
"Qno": 2,
"Question": "I felt angry.",
},
{	
"Qno": 3,
"Question": "I felt like I was ready to explode.",
},
{	
"Qno": 4,
"Question": "I was grouchy.",
},
{
"Qno": 5,
"Question": "I felt annoyed.",
},
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_ADULT_ANGER (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Never',
    Option2 TEXT DEFAULT 'Rarely',
    Option3 TEXT DEFAULT 'Sometimes',
    Option4 TEXT DEFAULT 'Often',
    Option5 TEXT DEFAULT 'Always'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_ADULT_ANGER (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
