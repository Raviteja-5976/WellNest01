import sqlite3
from time import sleep


questions = [
{	
"Qno": 1,
"Question": "On average, how much time is occupied by these thoughts or behaviors each day?",
},
{	
"Qno": 2,
"Question": "How much distress do these thoughts or behaviors cause you?",
},
{	
"Qno": 3,
"Question": "How hard is it for you to control these thoughts or behaviors?",
},
{	
"Qno": 4,
"Question": "How much do these thoughts or behaviors cause you to avoid doing anything, going anyplace, or being with anyone?",
},
{	
"Qno": 5,
"Question": "How much do these thoughts or behaviors interfere with school, work, or your social or family life?",
},
]




db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_ADULT_RT_B (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'None',
    Option2 TEXT DEFAULT 'Less than an hour a day',
    Option3 TEXT DEFAULT '1 to 3 hours a day',
    Option4 TEXT DEFAULT '3 to 8 hours a day',
    Option5 TEXT DEFAULT 'more than 8 hours a day'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_ADULT_RT_B (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



