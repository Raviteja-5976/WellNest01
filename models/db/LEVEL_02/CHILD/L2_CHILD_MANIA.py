import sqlite3
from time import sleep

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_CHILD_MANIA (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT,
    Option2 TEXT,
    Option3 TEXT,
    Option4 TEXT,
    Option5 TEXT
);
"""
cursor.execute(create_table_query)

questions = [
{	
"Qno": 1,
"Question": "Question 1",
"options": {
"0":" I do not feel happier or more cheerful than usual.",
"1":" I occasionally feel happier or more cheerful than usual.",
"2":" I often feel happier or more cheerful than usual.",
"3":" I feel happier or more cheerful than usual most of the time.",
"4":" I feel happier of more cheerful than usual all of the time.",
},
},
{	
"Qno": 2,
"Question": "Question 2",
"options": {
"0":" I do not feel more self-confident than usual.",
"1":" I occasionally feel more self-confident than usual.",
"2":" I often feel more self-confident than usual.",
"3":" I frequently feel more self-confident than usual.",
"4":" I feel extremely self-confident all of the time",
},
},
{	
"Qno": 3,
"Question": "Question 3",
"options": {
"0":"I do not need less sleep than usual.",
"1":"I occasionally need less sleep than usual.",
"2":"I often need less sleep than usual.",
"3":"I frequently need less sleep than usual.",
"4":"I can go all day and all night without any sleep and still not feel tired.",
},
},
{	
"Qno": 4,
"Question": "Question 4",
"options": {
"0":" I do not talk more than usual.",
"1":" I occasionally talk more than usual.",
"2":" I often talk more than usual.",
"3":" I frequently talk more than usual.",
"4":" I talk constantly and cannot be interrupted.",
},
},
{	
"Qno": 5,
"Question": "Question 5",
"options": {
"0":" I have not been more active (either socially, sexually, at work, home, or school) than usual.",
"1":" I have occasionally been more active than usual.",
"2":" I have often been more active than usual.",
"3":" I have frequently been more active than usual.",
"4":" I am constantly more active or on the go all the time.",
},
},
]

command = """
INSERT INTO L2_CHILD_MANIA (Qno, Question, Option1, Option2, Option3, Option4, Option5)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
for item in questions:
    options = item["options"]
    cursor.execute(command, (item["Qno"], item["Question"], options["0"], options["1"], options["2"], options["3"], options["4"]))
    sleep(0.01)


connection.commit()
connection.close()
