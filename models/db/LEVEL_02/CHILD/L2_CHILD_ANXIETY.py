import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "I felt like something awful might happen.",
},
{	
"Qno": 2,
"Question": "I felt nervous.",
},
{	
"Qno": 3,
"Question": "I felt scared.",
},
{	
"Qno": 4,
"Question": "I felt worried.",
},
{	
"Qno": 5,
"Question": "I worried about what could happen to me.",
},
{	
"Qno": 6,
"Question": "I worried when I went to bed at night.",
},
{	
"Qno": 7,
"Question": "I got scared really easy.",
},
{	
"Qno": 8,
"Question": "I was afraid of going to school.",
},
{	
"Qno": 9,
"Question": "I was worried I might die.",
},
{	
"Qno": 10,
"Question": "I woke up at night scared.",
},
{	
"Qno": 11,
"Question": "I worried when I was at home.",
},
{	
"Qno": 12,
"Question": "I worried when I was away from home.",
},
{	
"Qno": 13,
"Question": "It was hard for me to relax.",
}
]

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_ANXIETY (
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
    INSERT INTO L2_CHILD_ANXIETY (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



