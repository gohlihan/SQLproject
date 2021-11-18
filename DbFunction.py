import sqlite3

def add_many(list):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    c.execute("insert into")


    conn.commit()
    conn.disconnect()