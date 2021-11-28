import sqlite3

def show_warehouse_inv(ware_id):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    c.execute("insert into")


    conn.commit()
    conn.disconnect()