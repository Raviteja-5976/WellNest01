import sqlite3
from time import sleep

# Dictionary containing questions
questions =[
    {"Qno": 1, "Question": "Little interest or pleasure in doing things?"},
    {"Qno": 2, "Question": "Feeling down, depressed, or hopeless?"},
    {"Qno": 3, "Question": "Feeling more irritated, grouchy, or angry than usual?"},
    {"Qno": 4, "Question": "Sleeping less than usual, but still have a lot of energy?"},
    {"Qno": 5, "Question": "Starting lots more projects than usual or doing more risky things than usual?"},
    {"Qno": 6, "Question": "Feeling nervous, anxious, frightened, worried, or on edge?"},
    {"Qno": 7, "Question": "Feeling panic or being frightened?"},
    {"Qno": 8, "Question": "Avoiding situations that make you anxious?"},
    {"Qno": 9, "Question": "Unexplained aches and pains (e.g., head, back, joints, abdomen, legs)?"},
    {"Qno": 10, "Question": "Feeling that your illnesses are not being taken seriously enough?"},
    {"Qno": 11, "Question": "Thoughts of actually hurting yourself?"},
    {"Qno": 12, "Question": "Hearing things other people couldn’t hear, such as voices even when no one was around?"},
    {"Qno": 13, "Question": "Feeling that someone could hear your thoughts, or that you could hear what another person was thinking?"},
    {"Qno": 14, "Question": "Problems with sleep that affected your sleep quality overall?"},
    {"Qno": 15, "Question": "Problems with memory (e.g., learning new information) or with location (e.g., finding your way home)?"},
    {"Qno": 16, "Question": "Unpleasant thoughts, urges, or images that repeatedly enter your mind?"},
    {"Qno": 17, "Question": "Feeling driven to perform certain behaviors or mental acts over and over again?"},
    {"Qno": 18, "Question": "Feeling detached or distant from yourself, your body, your physical surroundings, or your memories?"},
    {"Qno": 19, "Question": "Not knowing who you really are or what you want out of life?"},
    {"Qno": 20, "Question": "Not feeling close to other people or enjoying your relationships with them?"},
    {"Qno": 21, "Question": "Drinking at least 4 drinks of any kind of alcohol in a single day?"},
    {"Qno": 22, "Question": "Smoking any cigarettes, a cigar, or pipe, or using snuff or chewing tobacco?"},
    {"Qno": 23, "Question": "Using any of the following medicines ON YOUR OWN, that is, without a doctor’s prescription, in greater amounts or longer than prescribed [e.g., painkillers (like Vicodin), stimulants (like Ritalin or Adderall), sedatives or tranquilizers (like sleeping pills or Valium), or drugs like marijuana, cocaine or crack, club drugs (like ecstasy), hallucinogens (like LSD), heroin, inhalants or solvents (like glue), or methamphetamine (like speed)]?"}
  ]



# Connect to the SQLite database (creates the file if it doesn't exist)
db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

# Create the table
create_table_query = """
CREATE TABLE IF NOT EXISTS L1_ADULT (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not at all',
    Option2 TEXT DEFAULT 'Rare, less than a day or two',
    Option3 TEXT DEFAULT 'Several days',
    Option4 TEXT DEFAULT 'More than half the days',
    Option5 TEXT DEFAULT 'Nearly every day'
);
"""
cursor.execute(create_table_query)

# Insert questions into the table
insert_query = """
INSERT INTO L1_ADULT (Qno, Question) VALUES (?, ?);
"""
for item in questions:
    cursor.execute(insert_query, (item["Qno"], item["Question"]))
    sleep(0.01)

# Commit changes and close the connection
connection.commit()
connection.close()

print("Table created and questions inserted successfully!")
