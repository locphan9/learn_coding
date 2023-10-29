import sqlite3

try:
    sqliteConnection = sqlite3.connect('python2_db')
    cursor = sqliteConnection.cursor()
    print("Database created and connected to sqlite")

    with open("./database/data_query.sql",'r') as sql_file:
        sql_script = sql_file.read()

    cursor.executescript(sql_script)
    print("SQL script executed")
    cursor.close()

except sqlite3.Error as error:
    print(error)
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print("The SQLite connection is closed")