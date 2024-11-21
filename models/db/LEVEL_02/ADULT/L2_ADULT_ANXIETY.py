import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "I felt fearful.",
},
{	
"Qno": 2,
"Question": "I felt anxious.",
},
{	
"Qno": 3,
"Question": "I felt worried.",
},
{	
"Qno": 4,
"Question": "I found it hard to focus on anything other than my anxiety.",
},
{	
"Qno": 5,
"Question": "I felt nervous.",
},
{	
"Qno": 6,
"Question": "I felt uneasy.",
},
{	
"Qno": 7,
"Question": "I felt tense.",
},
]

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_ADULT_ANXIETY (
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
    INSERT INTO L2_ADULT_ANXIETY (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



