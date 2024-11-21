import sqlite3



questions = [
{	
"Qno": 1,
"Question": "I felt worthless.",
},
{	
"Qno": 2,
"Question": "I felt that I had nothing to look forward to.",
},
{	
"Qno": 3,
"Question": "I felt helpless.",
},
{	
"Qno": 4,
"Question": "I felt sad.",
},
{	
"Qno": 5,
"Question": "I felt like a failure.",
},
{	
"Qno": 6,
"Question": "I felt depressed.",
},
{	
"Qno": 7,
"Question": "I felt unhappy.",
},
{	
"Qno": 8,
"Question": "I felt hopeless.",
},
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_ADULT_DEPRESSION (
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
    INSERT INTO L2_ADULT_DEPRESSION (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



