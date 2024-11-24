import sqlite3

questions = [
  { "Qno": 1, "Question": "Having 'flashbacks,' that is, you suddenly acted or felt as if a stressful experience from the past was happening all over again (for example, you reexperienced parts of a stressful experience by seeing, hearing, smelling, or physically feeling parts of the experience)?" },
  { "Qno": 2, "Question": "Feeling very emotionally upset when something reminded you of a stressful experience?" },
  { "Qno": 3, "Question": "Feeling detached or distant from yourself, your body, your physical surroundings, or your memories?" },
  { "Qno": 4, "Question": "Trying to avoid thoughts, feelings, or physical sensations that reminded you of a stressful experience?" },
  { "Qno": 5, "Question": "Being 'super alert,' on guard, or constantly on the lookout for danger?" },
  { "Qno": 6, "Question": "Feeling jumpy or easily startled when you hear an unexpected noise?" },
  { "Qno": 7, "Question": "Being extremely irritable or angry to the point where you yelled at other people, got into fights, or destroyed things?" }
]


db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS SMD_ACUTE_S_S (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not At All',
    Option2 TEXT DEFAULT 'A Little Bit',
    Option3 TEXT DEFAULT 'Moderately',
    Option4 TEXT DEFAULT 'Quite A Bit',
    Option5 TEXT DEFAULT 'Extremely'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO SMD_ACUTE_S_S (Qno, Question) VALUES (?, ?);
    """
    cursor.execute(insert_query, (Qno, Question))
    connection.commit()


connection.close()
