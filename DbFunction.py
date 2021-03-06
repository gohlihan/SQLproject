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
    SELECT id,name, Sum
    FROM 
    (SELECT Customers.customer_id AS id,Customers.customer_name AS name,SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    GROUP BY Customers.customer_id) AS t
    ORDER BY Sum DESC;
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show Customer purchases: "+str(item))
    conn.commit()
    conn.close()
    

def show_newphone_customer(): 
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT id, name, MAX(Sum)
    FROM 
    (SELECT Customers.customer_id AS id, Customers.customer_name AS name, SUM(item_quantity) AS Sum
    FROM Customers, Invoices, Shopping_lists
    WHERE Customers.customer_id = Invoices.customer_id 
    AND Invoices.shopping_list_id = Shopping_lists.shopping_list_id 
    AND Shopping_lists.item_id = 1
    GROUP BY Customers.customer_id)
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show New Phone Customer: "+str(item))
    conn.commit()
    conn.close()

def show_worker_sales():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT w.worker_id, w.worker_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i
    WHERE i.worker_id = w.worker_id
    GROUP BY w.worker_id, w.worker_name
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show Worker Sales: "+str(item))
    conn.commit()
    conn.close()


def show_the_best_worker():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT worker_id,worker_name,MAX(totalsale)
    FROM (SELECT w.worker_id, w.worker_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i
    WHERE i.worker_id = w.worker_id
    GROUP BY w.worker_id, w.worker_name)
    '''
    c.execute(sql)
    item = c.fetchall()
    print("The Best Worker is: "+str(item))
    conn.commit()
    conn.close()


def show_agent_sales():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT a.agent_id, a.agent_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i, Agents a, Managers m
    WHERE i.worker_id = w.worker_id AND w.manager_id = m.manager_id AND m.agent_id = a.agent_id
    GROUP BY a.agent_id, a.agent_name
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show Agent Sales: "+str(item))
    conn.commit()
    conn.close()


def show_the_best_agent():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT agent_id,agent_name,MAX(totalsale)
    FROM (SELECT a.agent_id, a.agent_name, SUM(i.total_price) AS totalsale
    FROM Workers w, Invoices i, Agents a, Managers m
    WHERE i.worker_id = w.worker_id AND w.manager_id = m.manager_id AND m.agent_id = a.agent_id
    GROUP BY a.agent_id, a.agent_name)
    '''
    c.execute(sql)
    item = c.fetchall()
    print("The Best Agent is: "+str(item))
    conn.commit()
    conn.close()

def show_driver_count():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT d.driver_id, d.driver_name, COUNT(i.city_id) AS count
    FROM Drivers d, Invoices i
    WHERE d.driver_id = i.driver_id
    GROUP BY d.driver_id, d.driver_name
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show Most active Driver: "+str(item))
    conn.commit()
    conn.close()

def show_active_driver():
    conn = sqlite3.connect("system.db")
    c=conn.cursor()
    sql='''
    SELECT driver_id, driver_name, MAX(count)
    FROM (SELECT d.driver_id, d.driver_name, COUNT(i.city_id) AS count
    FROM Drivers d, Invoices i
    WHERE d.driver_id = i.driver_id
    GROUP BY d.driver_id, d.driver_name)
    '''
    c.execute(sql)
    item = c.fetchall()
    print("Show Most active Driver: "+str(item))
    conn.commit()
    conn.close()

#----------Main functions--------------------

#show_warehouse_inv(1)

#show_all_warehouse_inv()

#change_warehouse_inv(99,1)

#change_invoice_city(5,3)

#create_invoice(invoice_id,invoice_date,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status)

#show_customer_totalbuy()

#show_newphone_customer()

#show_the_best_agent()

#show_the_best_worker()

#show_worker_sales()

#show_agent_sales()

#show_driver_count()

#show_active_driver()