import sqlite3

# Adding tables
conn = sqlite3.connect('system.db')
c = conn.cursor()
c.executescript('''
    INSERT INTO Cities(city_id,city_name)
    VALUES
        (1,'Tokyo'),
        (2,'Yokohama'),
        (3,'Osaka'),
        (4,'Nagoya'),
        (5,'Sapporo');


    INSERT INTO Agents(agent_id,agent_name,city_id,total_sales) 
    VALUES
        (1,'Agent_Tokyo',1,9375104),
        (2,'Agent_Yokohama',2,3732616),
        (3,'Agent_Osaka',3,2691185),
        (4,'Agent_Nagoya',4,2327557),
        (5,'Agent_Sapporo',5,1976257);


    INSERT INTO Managers(manager_id,manager_name,agent_id)
    VALUES
        (1,'Sakurai Bunko',1),
        (2,'Miyahara Masaru',2),
        (3,'Hoga Tamotsu',3),
        (4,'Kinoshita Shiori',4),
        (5,'Uyeda Tomoko',5);


    INSERT INTO Workers (worker_id,worker_name,manager_id,total_sales)
    VALUES
        (1,'Gima Masaru',1,100),
        (2,'Sakura Gen',2,100),
        (3,'Kite Jean',3,100),
        (4,'Yabi Osamatsu',4,100),
        (5,'Linda Armstrong',5,100);


    INSERT INTO Warehouses(warehouse_id,city_id,agent_id,item_id,item_name,stock_item_quantity)
    VALUES
        (1,1,1,1,'NewPhone',10),
        (2,2,2,2,'OldPhone',20),
        (3,3,3,1,'NewPhone',30),
        (4,4,4,2,'OldPhone',40),
        (5,5,5,1,'NewPhone',50);

    
    INSERT INTO Items(item_id,item_name,item_price)
    VALUES
        (1,'NewPhone',100),
        (2,'OldPhone',100);
    

    INSERT INTO Shopping_lists(shopping_list_id,item_id,item_quantity)
    VALUES
        (1,1,1),
        (2,2,1),
        (3,1,1),
        (4,2,1),
        (5,1,1);
    

    INSERT INTO Customers(customer_id,customer_name,city_id,invoice_id)
    VALUES
        (1,'Houa Gura',1,1),
        (2,'Wula Deana',2,2),
        (3,'Peter Tobby',3,3),
        (4,'Stark Onney',4,4),
        (5,'William Jhon',5,5);
    

    INSERT INTO Invoices(invoice_id,invoice_date,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status)
    VALUES
        (1,'2021/11/11',1,1,100,1,1,2),
        (2,'2021/11/11',2,2,100,2,2,2),
        (3,'2021/11/11',3,3,100,3,3,2),
        (4,'2021/11/11',4,4,100,4,4,1),
        (5,'2021/11/11',5,5,100,5,5,0);
    

    INSERT INTO Drivers(driver_id,driver_name,city_id)
    VALUES
        (1,'Cathlin Kate',1),
        (2,'Obara Himi',2),
        (3,'Wukaze Khan',3),
        (4,'Shimta Izuku',4),
        (5,'Jeffson White',5);

''')


conn.commit()
conn.close()