import sqlite3

questions =[
  { "Qno": 1, "Question": "I find myself staring into space and thinking of nothing." },
  { "Qno": 2, "Question": "People, objects, or the world around me seem strange or unreal." },
  { "Qno": 3, "Question": "I find that I did things that I do not remember doing." },
  { "Qno": 4, "Question": "When I am alone, I talk out loud to myself." },
  { "Qno": 5, "Question": "I feel as though I were looking at the world through a fog so that people and things seem far away or unclear." },
  { "Qno": 6, "Question": "I am able to ignore pain." },
  { "Qno": 7, "Question": "I act so differently from one situation to another that it is almost as if I were two different people." },
  { "Qno": 8, "Question": "I can do things very easily that would usually be hard for me." }
]



db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_ADULT_DISSOCIATIVE_SYMPTOMS (
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
    INSERT INTO SMD_ADULT_DISSOCIATIVE_SYMPTOMS (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
