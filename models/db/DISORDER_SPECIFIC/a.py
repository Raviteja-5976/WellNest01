import sqlite3 

db_name = "wellnest01.db"
connection = sqlite3.connect(db_name)
cursor = connection.cursor()


# drop L1_PARENT Table
command = """
DROP TABLE raviteja_4352_test_result;
"""
connection.execute(command)