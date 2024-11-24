import sqlite3

questions = [
  { "Qno": 1, "Question": "felt moments of sudden terror, fear, or fright" },
  { "Qno": 2, "Question": "felt anxious, worried, or nervous" },
  { "Qno": 3, "Question": "had thoughts of bad things happening, such as family tragedy, ill health, loss of a job, or accidents" },
  { "Qno": 4, "Question": "felt a racing heart, sweaty, trouble breathing, faint, or shaky" },
  { "Qno": 5, "Question": "felt tense muscles, felt on edge or restless, or had trouble relaxing or trouble sleeping" },
  { "Qno": 6, "Question": "avoided, or did not approach or enter, situations about which I worry" },
  { "Qno": 7, "Question": "left situations early or participated only minimally due to worries" },
  { "Qno": 8, "Question": "spent lots of time making decisions, putting off making decisions, or preparing for situations, due to worries" },
  { "Qno": 9, "Question": "sought reassurance from others due to worries" },
  { "Qno": 10, "Question": "needed help to cope with anxiety (e.g., alcohol or medication, superstitious objects, or other people)" }
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_GENERALIZED_A_D(
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
    INSERT INTO SMD_GENERALIZED_A_D (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
