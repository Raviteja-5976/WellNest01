import sqlite3

questions = [
  { "Qno": 1, "Question": "felt moments of sudden terror, fear, or fright in these situations" },
  { "Qno": 2, "Question": "felt anxious, worried, or nervous about these situations" },
  { "Qno": 3, "Question": "had thoughts about panic attacks, uncomfortable physical sensations, getting lost, or being overcome with fear in these situations" },
  { "Qno": 4, "Question": "felt a racing heart, sweaty, trouble breathing, faint, or shaky in these situations" },
  { "Qno": 5, "Question": "felt tense muscles, felt on edge or restless, or had trouble relaxing in these situations" },
  { "Qno": 6, "Question": "avoided, or did not approach or enter, these situations" },
  { "Qno": 7, "Question": "moved away from these situations, left them early, or remained close to the exits" },
  { "Qno": 8, "Question": "spent a lot of time preparing for, or procrastinating about (putting off), these situations" },
  { "Qno": 9, "Question": "distracted myself to avoid thinking about these situations" },
  { "Qno": 10, "Question": "needed help to cope with these situations (e.g., alcohol or medication, superstitious objects, other people)" }
]

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_SPECIFIC_PHOBIA (
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
    INSERT INTO SMD_SPECIFIC_PHOBIA (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()
