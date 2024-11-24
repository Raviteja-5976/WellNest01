import sqlite3

questions = [
  { "Qno": 1, "Question": "Felt moments of sudden terror, fear, or fright in social situations" },
  { "Qno": 2, "Question": "Felt anxious, worried, or nervous about social situations" },
  { "Qno": 3, "Question": "Had thoughts of being rejected, humiliated, embarrassed, ridiculed, or offending others" },
  { "Qno": 4, "Question": "Felt a racing heart, sweaty, trouble breathing, faint, or shaky in social situations" },
  { "Qno": 5, "Question": "Felt tense muscles, felt on edge or restless, or had trouble relaxing in social situations" },
  { "Qno": 6, "Question": "Avoided, or did not approach or enter, social situations" },
  { "Qno": 7, "Question": "Left social situations early or participated only minimally (e.g., said little, avoided eye contact)" },
  { "Qno": 8, "Question": "Spent a lot of time preparing what to say or how to act in social situations" },
  { "Qno": 9, "Question": "Distracted myself to avoid thinking about social situations" },
  { "Qno": 10, "Question": "Needed help to cope with social situations (e.g., alcohol or medications, superstitious objects)" }
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_SOCIAL_A_D (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Never',
    Option2 TEXT DEFAULT 'Occasionally',
    Option3 TEXT DEFAULT 'Half of the time',
    Option4 TEXT DEFAULT 'Most of the time',
    Option5 TEXT DEFAULT 'All of the time'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO SMD_SOCIAL_A_D (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
