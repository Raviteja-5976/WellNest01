import sqlite3



questions = [
	{	
	"Qno": 1,
	"Question": " Often fails to give close attention to details or makes careless mistakes in schoolwork, work, or other activities.",
},

{	
	"Qno": 2,
	"Question": " Often has difficulty sustaining attention in tasks or play activities.",
},

{	
	"Qno": 3,
	"Question": " Often does not seem to listen when spoken to directly.",
},

{	
	"Qno": 4,
	"Question": " Often does not follow through on instructions and fails to finish schoolwork, chores, or duties.",
},

{	
	"Qno": 5,
	"Question": " Often has difficulty organizing tasks and activities.",
},

{	
	"Qno": 6,
	"Question": " Often avoids, dislikes, or is reluctant to engage in tasks that require sustained mental effort (e.g., schoolwork or homework).",
},

{	
	"Qno": 7,
	"Question": " Often loses things necessary for tasks or activities (e.g.,toys, school assignments, pencils, books, or tools.)",
},

{	
	"Qno": 8,
	"Question": "Often is distracted by extraneous stimuli.",
}
]






db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS L2_PARENT_INATTENTION (
    Qno INTEGER PRIMARY KEY,
    Question TEXT NOT NULL,
    Option1 TEXT DEFAULT 'Not At All',
    Option2 TEXT DEFAULT 'Just A Little',
    Option3 TEXT DEFAULT 'Quite A Bit',
    Option4 TEXT DEFAULT 'Very Much'
);
"""
cursor.execute(create_table_query)

for question in questions:
    Qno = question["Qno"]
    Question = question["Question"]
    insert_query = f"""
    INSERT INTO L2_PARENT_INATTENTION (Qno, Question) VALUES ({Qno}, '{Question}');
    """
    cursor.execute(insert_query)
    connection.commit()


connection.close()



