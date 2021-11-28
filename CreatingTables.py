import sqlite3

# Adding tables
conn = sqlite3.connect('system.db')
c = conn.cursor()
c.executescript('''
    CREATE TABLE Cities(
    city_id integer PRIMARY KEY,
    city_name text
);

    CREATE TABLE Agents (
    agent_id integer PRIMARY KEY,
    agent_name text,
    city_id integer,
    total_sales integer,
    FOREIGN KEY (city_id) REFERENCES Cities (city_id)
);

    CREATE TABLE Managers (
    manager_id integer PRIMARY KEY,
    manager_name text,
    agent_id integer,
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
);

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
    shipping_status integer,
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
);

''')


conn.commit()
conn.close()