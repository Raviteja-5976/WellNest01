import sqlite3

import sqlite3
from time import sleep


def section_01():
    # Dictionary containing questions
    questions =[
        {"Qno": 1, "Question": "Complained of stomachaches, headaches, or other aches and pains?"},
        {"Qno": 2, "Question": "Said he/she was worried about his/her health or about getting sick?"},
        {"Qno": 3, "Question": "Had problems sleeping—that is, trouble falling asleep, staying asleep, or waking up too early?"},
        {"Qno": 4, "Question": "Had problems paying attention when he/she was in class or doing his/her homework or reading a book or playing a game?"},
        {"Qno": 5, "Question": "Had less fun doing things than he/she used to?"},
        {"Qno": 6, "Question": "Seemed sad or depressed for several hours?"},
        {"Qno": 7, "Question": "Seemed more irritated or easily annoyed than usual?"},
        {"Qno": 8, "Question": "Seemed angry or lost his/her temper?"},
        {"Qno": 9, "Question": "Started lots more projects than usual or did more risky things than usual?"},
        {"Qno": 10, "Question": "Slept less than usual for him/her, but still had lots of energy?"},
        {"Qno": 11, "Question": "Said he/she felt nervous, anxious, or scared?"},
        {"Qno": 12, "Question": "Not been able to stop worrying?"},
        {"Qno": 13, "Question": "Said he/she couldn’t do things he/she wanted to or should have done, because they made him/her feel nervous?"},
        {"Qno": 14, "Question": "Said that he/she heard voices—when there was no one there—speaking about him/her or telling him/her what to do or saying bad things to him/her?"},
        {"Qno": 15, "Question": "Said that he/she had a vision when he/she was completely awake—that is, saw something or someone that no one else could see?"},
        {"Qno": 16, "Question": "Said that he/she had thoughts that kept coming into his/her mind that he/she would do something bad or that something bad would happen to him/her or to someone else?"},
        {"Qno": 17, "Question": "Said he/she felt the need to check on certain things over and over again, like whether a door was locked or whether the stove was turned off?"},
        {"Qno": 18, "Question": "Seemed to worry a lot about things he/she touched being dirty or having germs or being poisoned?"},
        {"Qno": 19, "Question": "Said that he/she had to do things in a certain way, like counting or saying special things out loud, in order to keep something bad from happening?"}
    ]

    # Connect to the SQLite database (creates the file if it doesn't exist)
    db_name = "wellnest01.db"
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS L1_PARENT (
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
    INSERT INTO L1_PARENT (Qno, Question) VALUES (?, ?);
    """
    for item in questions:
        cursor.execute(insert_query, (item["Qno"], item["Question"]))
        sleep(0.01)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    return "Table created successfully" 

def section_02():

    db_name = "wellnest01.db"
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    questions = [
    {"Qno": 20, "Question": "Had an alcoholic beverage (beer, wine, liquor, etc.)?"},
    {"Qno": 21, "Question": "Smoked a cigarette, a cigar, or pipe, or used snuff or chewing tobacco?"},
    {"Qno": 22, "Question": "Used drugs like marijuana, cocaine or crack, club drugs (like ecstasy), hallucinogens (like LSD), heroin, inhalants or solvents (like glue), or methamphetamine (like speed)?"},
    {"Qno": 23, "Question": "Used any medicine without a doctor’s prescription (e.g., painkillers [like Vicodin], stimulants [like Ritalin or Adderall], sedatives or tranquilizers [like sleeping pills or Valium], or steroids)?"},
    {"Qno": 24, "Question": "In the past TWO (2) WEEKS, has he/she talked about wanting to kill himself/herself or about wanting to commit suicide?"},
    {"Qno": 25, "Question": "Has he/she EVER tried to kill himself/herself?"}
    ]
    command = """
    INSERT INTO L1_PARENT (Qno, Question, Option1, Option2, Option3, Option4, Option5)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    for item in questions:
        cursor.execute(command, (item["Qno"], item["Question"],"YES", "NO", "Don't Know", None, None))
        sleep(0.01)

    connection.commit()
    connection.close()

    return "Info Inserted"


def main():
    section_02()



if __name__ == "__main__":
    main()


# import sqlite3
# from time import sleep


# def section_01():
#     # Dictionary containing questions
#     questions = [
#         {"Qno": 1, "Question": "Complained of stomachaches, headaches, or other aches and pains?"},
#         {"Qno": 2, "Question": "Said he/she was worried about his/her health or about getting sick?"},
#         {"Qno": 3, "Question": "Had problems sleeping—that is, trouble falling asleep, staying asleep, or waking up too early?"},
#         {"Qno": 4, "Question": "Had problems paying attention when he/she was in class or doing his/her homework or reading a book or playing a game?"},
#         {"Qno": 5, "Question": "Had less fun doing things than he/she used to?"},
#         {"Qno": 6, "Question": "Seemed sad or depressed for several hours?"},
#         {"Qno": 7, "Question": "Seemed more irritated or easily annoyed than usual?"},
#         {"Qno": 8, "Question": "Seemed angry or lost his/her temper?"},
#         {"Qno": 9, "Question": "Started lots more projects than usual or did more risky things than usual?"},
#         {"Qno": 10, "Question": "Slept less than usual for him/her, but still had lots of energy?"},
#         {"Qno": 11, "Question": "Said he/she felt nervous, anxious, or scared?"},
#         {"Qno": 12, "Question": "Not been able to stop worrying?"},
#         {"Qno": 13, "Question": "Said he/she couldn’t do things he/she wanted to or should have done, because they made him/her feel nervous?"},
#         {"Qno": 14, "Question": "Said that he/she heard voices—when there was no one there—speaking about him/her or telling him/her what to do or saying bad things to him/her?"},
#         {"Qno": 15, "Question": "Said that he/she had a vision when he/she was completely awake—that is, saw something or someone that no one else could see?"},
#         {"Qno": 16, "Question": "Said that he/she had thoughts that kept coming into his/her mind that he/she would do something bad or that something bad would happen to him/her or to someone else?"},
#         {"Qno": 17, "Question": "Said he/she felt the need to check on certain things over and over again, like whether a door was locked or whether the stove was turned off?"},
#         {"Qno": 18, "Question": "Seemed to worry a lot about things he/she touched being dirty or having germs or being poisoned?"},
#         {"Qno": 19, "Question": "Said that he/she had to do things in a certain way, like counting or saying special things out loud, in order to keep something bad from happening?"}
#     ]

#     # Connect to the SQLite database (creates the file if it doesn't exist)
#     db_name = "wellnest01.db"
#     connection = sqlite3.connect(db_name)
#     cursor = connection.cursor()

#     # Create the table
#     create_table_query = """
#     CREATE TABLE IF NOT EXISTS L1_PARENT (
#         Qno INTEGER PRIMARY KEY,
#         Question TEXT NOT NULL,
#         Option1 TEXT,
#         Option2 TEXT,
#         Option3 TEXT,
#         Option4 TEXT,
#         Option5 TEXT
#     );
#     """
#     cursor.execute(create_table_query)

#     # Insert questions with options into the table
#     insert_query = """
#     INSERT INTO L1_PARENT (Qno, Question, Option1, Option2, Option3, Option4, Option5)
#     VALUES (?, ?, ?, ?, ?, ?, ?);
#     """
#     for item in questions:
#         cursor.execute(insert_query, (item["Qno"], item["Question"],
#                                       "Not at all", "Rare, less than a day or two", "Several days", 
#                                       "More than half the days", "Nearly every day"))
#         sleep(0.01)

#     # Commit changes and close the connection
#     connection.commit()
#     connection.close()

#     return "Table created and data inserted successfully"


# def main():
#     print(section_01())


# if __name__ == "__main__":
#     main()
