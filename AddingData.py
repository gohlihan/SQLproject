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
        (1,'Gima Masaru',1,)






    CREATE TABLE Workers (
    worker_id integer PRIMARY KEY,
    worker_name text,
    manager_id integer,
    total_sales integer,
    FOREIGN KEY (manager_id) REFERENCES Managers (manager_id)
);

    CREATE TABLE Warehouses (
    warehouse_id integer PRIMARY KEY,
    city_id integer,
    agent_id integer,
    item_id integer,
    item_name text,
    stock_item_quantity integer,
    FOREIGN KEY (city_id) REFERENCES Cities (city_id),
    FOREIGN KEY (agent_id) REFERENCES Agents (agent_id),
    FOREIGN KEY (item_id) REFERENCES Items (item_id),
    FOREIGN KEY (item_name) REFERENCES Items (item_name)
);

    CREATE TABLE Items (
    item_id integer PRIMARY KEY ,
    item_name text,
    item_price integer
);

    CREATE TABLE Shopping_lists (
    shopping_list_id integer,
    item_id integer,
    item_quantity integer DEFAULT 1,
    FOREIGN KEY (item_id) REFERENCES Items (item_id)
);

    CREATE TABLE Customers (
    customer_id integer PRIMARY KEY ,
    customer_name text,
    city_id integer,
    invoice_id integer,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id),
    FOREIGN KEY (invoice_id) REFERENCES Invoices (invoice_id)
);

    CREATE TABLE Invoices (
    invoice_id integer PRIMARY KEY,
    invoice_date text,
    customer_id integer,
    shopping_list_id integer,
    total_price integer,
    city_id integer,
    driver_id integer,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (shopping_list_id) REFERENCES Shopping_lists (shopping_list_id),
    FOREIGN KEY (city_id) REFERENCES Cities(city_id),
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
);

    CREATE TABLE Drivers (
    driver_id integer PRIMARY KEY,
    driver_name text,
    city_id integer,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)




''')


conn.commit()
conn.close()