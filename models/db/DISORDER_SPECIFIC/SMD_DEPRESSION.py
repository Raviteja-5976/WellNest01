import sqlite3

questions =[
  { "Qno": 1, "Question": "Little interest or pleasure in doing things" },
  { "Qno": 2, "Question": "Feeling down, depressed, or hopeless" },
  { "Qno": 3, "Question": "Trouble falling or staying asleep, or sleeping too much" },
  { "Qno": 4, "Question": "Feeling tired or having little energy" },
  { "Qno": 5, "Question": "Poor appetite or overeating" },
  { "Qno": 6, "Question": "Feeling bad about yourself—or that you are a failure or have let yourself or your family down" },
  { "Qno": 7, "Question": "Trouble concentrating on things, such as reading the newspaper or watching television" },
  { "Qno": 8, "Question": "Moving or speaking so slowly that other people could have noticed? Or the opposite—being so fidgety or restless that you have been moving around a lot more than usual" },
  { "Qno": 9, "Question": "Thoughts that you would be better off dead or of hurting yourself in some way" }
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_DEPRESSION (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not At All',
    Option2 TEXT DEFAULT 'Several Days',
    Option3 TEXT DEFAULT 'More Than Half the Days',
    Option4 TEXT DEFAULT 'Nearly Every Day'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO SMD_DEPRESSION (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
