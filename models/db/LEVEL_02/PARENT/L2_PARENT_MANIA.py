import sqlite3
from time import sleep

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_MANIA (
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
"Question": " Question 1",
"options": {
"0":" He/she does not feel happier or more cheerful than usual.",
"1":" He/she occasionally feels happier or more cheerful than usual.",
"2":" He/she often feels happier or more cheerful than usual.",
"3":" He/she feels happier or more cheerful than usual most of the time.",
"4":" He/she feels happier of more cheerful than usual all of the time.",
},
},
{	
"Qno": 2,
"Question": " Question 2",
"options": {
"0":" He/she does not feel more self-confident than usual.",
"1":" He/she occasionally feels more self-confident than usual.",
"2":" He/she often feels more self-confident than usual.",
"3":" He/she frequently feels more self-confident than usual.",
"4":" He/she feels extremely self-confident all of the time.",
},
},
{	
"Qno": 3,
"Question": " Question 3",
"options": {
"0":" He/she does not need less sleep than usual.",
"1":" He/she occasionally needs less sleep than usual.",
"2":" He/she often needs less sleep than usual.",
"3":" He/she frequently needs less sleep than usual.",
"4":" He/she can go all day and all night without any sleep and still not feel tired.",
},
},
{	
"Qno": 4,
"Question": " Question 4",
"options": {
"0":" He/she does not talk more than usual.",
"1":" He/she occasionally talks more than usual.",
"2":" He/she often talks more than usual.",
"3":" He/she frequently talks more than usual.",
"4":" He/she talks constantly and cannot be interrupted.",
},
},
{	
"Qno": 5,
"Question": "Question 5",
"options": {
"0":" He/she has not been more active (either socially, sexually, at work, home, or school) than usual.",
"1":" He/she has occasionally been more active than usual.",
"2":" He/she has often been more active than usual.",
"3":" He/she has frequently been more active than usual.",
"4":" He/she is constantly more active or on the go all the time.",
},
}
]
 



command = """
INSERT INTO L2_PARENT_MANIA (Qno, Question, Option1, Option2, Option3, Option4, Option5)
VALUES (?, ?, ?, ?, ?, ?, ?);
"""
for item in questions:
    options = item["options"]
    cursor.execute(command, (item["Qno"], item["Question"], options["0"], options["1"], options["2"], options["3"], options["4"]))
    sleep(0.01)


connection.commit()
connection.close()
