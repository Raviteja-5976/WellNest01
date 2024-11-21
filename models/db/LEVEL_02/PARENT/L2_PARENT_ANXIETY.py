import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "Felt like something awful might happen.",
},
{	
"Qno": 2,
"Question": "Felt nervous.",
},
{	
"Qno": 3,
"Question": "Felt scared.",
},
{	
"Qno": 4,
"Question": "Felt worried.",
},
{	
"Qno": 5,
"Question": "Worried about what could happen to me.",
},
{	
"Qno": 6,
"Question": "Worried when he/she went to bed at night.",
},
{	
"Qno": 7,
"Question": "Got scared really easy.",
},
{	
"Qno": 8,
"Question": "Was afraid of going to school.",
},
{	
"Qno": 9,
"Question": "Worried when he/she was at home. ",
},
{	
"Qno": 10,
"Question": "Worried when he/she was away from home. ",
}
]

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_ANXIETY (
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
    INSERT INTO L2_PARENT_ANXIETY (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



