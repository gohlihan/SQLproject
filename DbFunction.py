import sqlite3


def show_all_warehouse_inv():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql = '''
    SELECT warehouse_id, item_name, stock_item_quantity 
    FROM Warehouses  
    GROUP BY warehouse_id
    '''
    c.execute(sql)
    items = c.fetchall()
    print(items)

    conn.commit()
    conn.close()


def show_warehouse_inv(ware_id):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql = '''
    SELECT item_name, stock_item_quantity 
    FROM Warehouses 
    WHERE warehouse_id = (?) 
    GROUP BY item_id
    '''
    c.execute(sql,(ware_id,))
    items = c.fetchall()
    print("Warehouse id "+ str(ware_id) + " Stocks: "+ str(items))

    conn.commit()
    conn.close()


def change_warehouse_inv(stock,ware_id):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql = '''
    UPDATE Warehouses 
    SET stock_item_quantity = ?
    WHERE warehouse_id = ?
    '''
    c.execute(sql,(stock,ware_id,))
    print("Done changing warehouse_inv")

    conn.commit()
    conn.close()

def change_invoice_city(city,invoice_num):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql = '''
    UPDATE Invoices 
    SET city_id = ?
    WHERE invoice_id = ?
    '''
    c.execute(sql,(city,invoice_num,))
    print("Done changing invoice_city")

    conn.commit()
    conn.close()


def create_invoice(invoice_id,invoice_date,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status):
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql = '''
    INSERT INTO Invoices 
    VALUES (?,?,?,?,?,?,?,?)
    '''
    c.execute(sql,(invoice_id,invoice_date,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status,))
    print("Done creating new invoice, invoice id: "+str(invoice_id))

    conn.commit()
    conn.close()


def show_customer_totalbuy(): 
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT id, Sum
    FROM 
    (SELECT Customers.customer_id AS id, SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    GROUP BY Customers.customer_id) AS t
    ORDER BY Sum DESC;
    '''
    c.execute(sql)
    item = c.fetchall()
    print(item)
    conn.commit()
    conn.close()
    

def show_newphone_customer(): 
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT id, Sum
    FROM 
    (SELECT Customers.customer_id AS id, SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    AND Shopping_lists.item_id = 1
    GROUP BY Customers.customer_id) AS t
    ORDER BY Sum DESC;
    '''
    c.execute(sql)
    item = c.fetchall()
    print(item)
    conn.commit()
    conn.close()