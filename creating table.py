import sqlite3

con = sqlite3.connect("users.db")
cursor = con.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    telegram_username TEXT,
    second_name TEXT, 
    first_name TEXT,
    phone_number TEXT,
    status TEXT,
    mirea_group TEXT,
    mirea_institute TEXT,
    CONSTRAINT  check_group CHECK ( mirea_group LIKE '__БО-__-__' ), 
    CONSTRAINT  check_number CHECK ( phone_number LIKE '8__________' )
    );
""")
con.commit()

cursor.execute("""
INSERT OR IGNORE INTO Users VALUES (?, ?, ?, ?, ?, ?, ?, ?);
""", (None, "danya", "gusevskii", "Daniil", "13334442266", "active", "ЭФМО-09-23", "ИПТИП")
               )

con.commit()
