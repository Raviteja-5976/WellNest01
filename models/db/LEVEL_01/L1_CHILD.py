import sqlite3
from time import sleep


def section_01():
    # Dictionary containing questions
    questions = [
        {"Qno": 1, "Question": "Been bothered by stomachaches, headaches, or other aches and pains?"},
        {"Qno": 2, "Question": "Worried about your health or about getting sick?"},
        {"Qno": 3, "Question": "Been bothered by not being able to fall asleep or stay asleep, or by waking up too early?"},
        {"Qno": 4, "Question": "Been bothered by not being able to pay attention when you were in class or doing homework or reading a book or playing a game?"},
        {"Qno": 5, "Question": "Had less fun doing things than you used to?"},
        {"Qno": 6, "Question": "Felt sad or depressed for several hours?"},
        {"Qno": 7, "Question": "Felt more irritated or easily annoyed than usual?"},
        {"Qno": 8, "Question": "Felt angry or lost your temper?"},
        {"Qno": 9, "Question": "Started lots more projects than usual or done more risky things than usual?"},
        {"Qno": 10, "Question": "Slept less than usual but still had a lot of energy?"},
        {"Qno": 11, "Question": "Felt nervous, anxious, or scared?"},
        {"Qno": 12, "Question": "Not been able to stop worrying?"},
        {"Qno": 13, "Question": "Not been able to do things you wanted to or should have done, because they made you feel nervous?"},
        {"Qno": 14, "Question": "Heard voices—when there was no one there—speaking about you or telling you what to do or saying bad things to you?"},
        {"Qno": 15, "Question": "Had visions when you were completely awake—that is, seen something or someone that no one else could see?"},
        {"Qno": 16, "Question": "Had thoughts that kept coming into your mind that you would do something bad or that something bad would happen to you or to someone else?"},
        {"Qno": 17, "Question": "Felt the need to check on certain things over and over again, like whether a door was locked or whether the stove was turned off?"},
        {"Qno": 18, "Question": "Worried a lot about things you touched being dirty or having germs or being poisoned?"},
        {"Qno": 19, "Question": "Felt you had to do things in a certain way, like counting or saying special things, to keep something bad from happening?"}
    ]


    # Connect to the SQLite database (creates the file if it doesn't exist)
    db_name = "wellnest01.db"
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create the table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS L1_CHILD (
        Qno INTEGER PRIMARY KEY,
        Question TEXT NOT NULL,
        Option1 TEXT,
        Option2 TEXT,
        Option3 TEXT,
        Option4 TEXT,
        Option5 TEXT
    );
    """
    cursor.execute(create_table_query)

    # Insert questions with options into the table
    insert_query = """
    INSERT INTO L1_CHILD (Qno, Question, Option1, Option2, Option3, Option4, Option5)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    for item in questions:
        cursor.execute(insert_query, (item["Qno"], item["Question"],
                                      "Not at all", "Rare, less than a day or two", "Several days", 
                                      "More than half the days", "Nearly every day"))
        sleep(0.01)

    # Commit changes and close the connection
    connection.commit()
    connection.close()

    return "Table created and data inserted successfully"

def section_02():

    db_name = "wellnest01.db"
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    questions = [
        {"Qno": 20, "Question": "Had an alcoholic beverage (beer, wine, liquor, etc.)?"},
        {"Qno": 21, "Question": "Smoked a cigarette, a cigar, or pipe, or used snuff or chewing tobacco?"},
        {"Qno": 22, "Question": "Used drugs like marijuana, cocaine or crack, club drugs (like Ecstasy), hallucinogens (like LSD), heroin, inhalants or solvents (like glue), or methamphetamine (like speed)?"},
        {"Qno": 23, "Question": "Used any medicine without a doctor’s prescription to get high or change the way you feel (e.g., painkillers [like Vicodin], stimulants [like Ritalin or Adderall], sedatives or tranquilizers [like sleeping pills or Valium], or steroids)?"},
        {"Qno": 24, "Question": "In the last 2 weeks, have you thought about killing yourself or committing suicide?"},
        {"Qno": 25, "Question": "Have you EVER tried to kill yourself?"}
    ]
    command = """
    INSERT INTO L1_CHILD (Qno, Question, Option1, Option2, Option3, Option4, Option5)
    VALUES (?, ?, ?, ?, ?, ?, ?);
    """
    for item in questions:
        cursor.execute(command, (item["Qno"], item["Question"],"YES", "NO", "Don't Know", None, None))
        sleep(0.01)

    connection.commit()
    connection.close()

    return "Info Inserted"


def main():
    section_01()
    sleep(1.00)
    section_02()



if __name__ == "__main__":
    main()


# import sqlite3
# from time import sleep





# def main():
#     print(section_01())


# if __name__ == "__main__":
#     main()
