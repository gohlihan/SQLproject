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


    INSERT INTO Agents(agent_id,agent_name,city_id) 
    VALUES
        (1,'Agent_Tokyo',1),
        (2,'Agent_Yokohama',2),
        (3,'Agent_Osaka',3),
        (4,'Agent_Nagoya',4),
        (5,'Agent_Sapporo',5);


    INSERT INTO Managers(manager_id,manager_name,agent_id)
    VALUES
        (1,'Sakurai Bunko',1),
        (2,'Miyahara Masaru',2),
        (3,'Hoga Tamotsu',3),
        (4,'Kinoshita Shiori',4),
        (5,'Uyeda Tomoko',5);


    INSERT INTO Workers (worker_id,worker_name,manager_id)
    VALUES
        (1,'Gima Masaru',1),
        (2,'Sakura Gen',2),
        (3,'Kite Jean',3),
        (4,'Yabi Osamatsu',4),
        (5,'Linda Armstrong',5);


    INSERT INTO Warehouses(warehouse_id,city_id,agent_id,item_id,item_name,stock_item_quantity)
    VALUES
        (1,1,1,1,'NewPhone',10),
        (2,2,2,2,'OldPhone',20),
        (3,3,3,1,'NewPhone',30),
        (4,4,4,2,'OldPhone',40),
        (5,5,5,1,'NewPhone',50),
        (1,1,1,1,'OldPhone',10),
        (2,2,2,2,'NewPhone',20),
        (3,3,3,1,'OldPhone',30),
        (4,4,4,2,'NewPhone',40),
        (5,5,5,1,'OldPhone',50);

    
    INSERT INTO Items(item_id,item_name,item_price)
    VALUES
        (1,'NewPhone',3000),
        (2,'OldPhone',2000);
    

    INSERT INTO Shopping_lists(shopping_list_id,item_id,item_quantity)
    VALUES
        (1,1,4),
        (2,2,3),
        (3,1,1),
        (4,2,2),
        (5,1,2),
        (6,1,4),
        (7,2,3),
        (8,1,1);
    

    INSERT INTO Customers(customer_name,city_id,invoice_id)
    VALUES
        ('Houa Gura',1,1),
        ('Wula Deana',2,2),
        ('Peter Tobby',3,3),
        ('Stark Onney',4,4),
        ('William Jhon',5,5);
    

    INSERT INTO Invoices(invoice_date,worker_id,customer_id,shopping_list_id,total_price,city_id,driver_id,shipping_status)
    VALUES
        ('2021/11/11',1,1,1,12000,1,1,2),
        ('2021/11/11',2,2,2,6000,2,2,2),
        ('2021/11/11',3,3,3,3000,3,3,2),
        ('2021/11/11',4,4,4,4000,4,4,1),
        ('2021/11/11',5,5,5,6000,5,5,0),
        ('2021/11/11',1,1,6,12000,1,1,2),
        ('2021/11/11',2,2,7,6000,2,2,2),
        ('2021/11/11',3,3,8,3000,3,3,2),
        ('2021/11/11',2,2,7,6000,2,2,2);
    

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