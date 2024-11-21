import sqlite3
from time import sleep

# Dictionary containing questions
test =[
    { "Qno": 1, "Question": "People would describe me as reckless." },
    { "Qno": 2, "Question": "I feel like I act totally on impulse." },
    { "Qno": 3, "Question": "Even though I know better, I can’t stop making rash decisions." },
    { "Qno": 4, "Question": "I often feel like nothing I do really matters." },
    { "Qno": 5, "Question": "Others see me as irresponsible." },
    { "Qno": 6, "Question": "I’m not good at planning ahead." },
    { "Qno": 7, "Question": "My thoughts often don’t make sense to others." },
    { "Qno": 8, "Question": "I worry about almost everything." },
    { "Qno": 9, "Question": "I get emotional easily, often for very little reason." },
    { "Qno": 10, "Question": "I fear being alone in life more than anything else." },
    { "Qno": 11, "Question": "I get stuck on one way of doing things, even when it’s clear it won’t work." },
    { "Qno": 12, "Question": "I have seen things that weren’t really there." },
    { "Qno": 13, "Question": "I steer clear of romantic relationships." },
    { "Qno": 14, "Question": "I’m not interested in making friends." },
    { "Qno": 15, "Question": "I get irritated easily by all sorts of things." },
    { "Qno": 16, "Question": "I don’t like to get too close to people." },
    { "Qno": 17, "Question": "It’s no big deal if I hurt other peoples’ feelings." },
    { "Qno": 18, "Question": "I rarely get enthusiastic about anything." },
    { "Qno": 19, "Question": "I crave attention." },
    { "Qno": 20, "Question": "I often have to deal with people who are less important than me." },
    { "Qno": 21, "Question": "I often have thoughts that make sense to me but that other people say are strange." },
    { "Qno": 22, "Question": "I use people to get what I want." },
    { "Qno": 23, "Question": "I often 'zone out' and then suddenly come to and realize that a lot of time has passed." },
    { "Qno": 24, "Question": "Things around me often feel unreal, or more real than usual." },
    { "Qno": 25, "Question": "It is easy for me to take advantage of others." }
]


# Connect to the SQLite database (creates the file if it doesn't exist)
db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS PID_BF (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Very False or Often False',
    Option2 TEXT DEFAULT 'Sometimes or Somewhat False',
    Option3 TEXT DEFAULT 'Sometimes or Somewhat True',
    Option4 TEXT DEFAULT 'Very True or Often True'
);
"""
cursor.execute(create_table_query)

# Insert questions into the table
insert_query = """
INSERT INTO PID_BF (Qno, Question) VALUES (?, ?);
"""
for item in test:
    cursor.execute(insert_query, (item["Qno"], item["Question"]))
    sleep(0.01)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Table created and questions inserted successfully!")
