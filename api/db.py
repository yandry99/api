import sqlite3

def create_connection():
    connection = None
    try:
        connection = sqlite3.connect('../database/datebase.db')
    except sqlite3.Error as err:
        print(f"Error at create_connection function: {err.msg}" )
    return connection
