import sqlite3

questions = [
  { "Qno": 1, "Question": "felt moments of sudden terror, fear, or fright when separated" },
  { "Qno": 2, "Question": "felt anxious, worried, or nervous about being separated" },
  { "Qno": 3, "Question": "have had thoughts of bad things happening to people important to me or bad things happening to me when separated from them (e.g., getting lost, accidents)" },
  { "Qno": 4, "Question": "felt a racing heart, sweaty, trouble breathing, faint, or shaky when separated" },
  { "Qno": 5, "Question": "felt tense muscles, felt on edge or restless, or had trouble relaxing or trouble sleeping when separated" },
  { "Qno": 6, "Question": "avoided going places where I would be separated" },
  { "Qno": 7, "Question": "when separated, left places early to go home" },
  { "Qno": 8, "Question": "spent a lot of time preparing for how to deal with separation" },
  { "Qno": 9, "Question": "distracted myself to avoid thinking about being separated" },
  { "Qno": 10, "Question": "needed help to cope with separation (e.g., alcohol or medications, superstitious objects)" }
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_SEPARATION_A_D (
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
    INSERT INTO SMD_SEPARATION_A_D (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
