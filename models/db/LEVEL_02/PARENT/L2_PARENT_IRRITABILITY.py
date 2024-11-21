import sqlite3
from time import sleep


questions = [
	{	
	"Qno": 1,
	"Question": " Is easily annoyed by others.",
},

{	
	"Qno": 2,
	"Question": " Often loses his/her temper.",
},

{	
	"Qno": 3,
	"Question": " Stays angry for a long time.",
},

{	
	"Qno": 4,
	"Question": " Is angry most of the time.",
},
{	
	"Qno": 5,
	"Question": " Gets angry frequently.",
},

{	
	"Qno": 6,
	"Question": " Loses temper easily.",
},

{	
	"Qno": 7,
	"Question": " Overall irritability causes him/her problems.",
},
]





db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_IRRITABILITY (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not True',
    Option2 TEXT DEFAULT 'Somewhat True',
    Option3 TEXT DEFAULT 'Certainley True'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_PARENT_IRRITABILITY (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
