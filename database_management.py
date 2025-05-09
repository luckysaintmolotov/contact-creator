import sqlite3 as sql3
import pathlib

default_path_to_database = pathlib.Path("contact-creator/database/default.db")

def create_new_database():
    conn = sql3.connect(str(default_path_to_database))
    c = conn.cursor()
    
    c.execute("""

        CREATE TABLE IF NOT EXISTS contacts
        (firstname TEXT, lastname TEXT)


""")
    conn.close()

def insert(new_contact):
    firstname = new_contact[0]
    lastname = new_contact[1]
    conn = sql3.connect(str(default_path_to_database))
    
    c = conn.cursor()
    
    c.execute(
        "INSERT INTO contacts (firstname, lastname) VALUES (?, ?)",
        (firstname, lastname)
    )