import sqlite3 

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


# drop L1_PARENT Table
command = """
DROP TABLE SMD_ADULT_PTSD;
"""
connection.execute(command)