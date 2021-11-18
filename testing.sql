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
    belong_agent integer,
    FOREIGN KEY (belong_agent) REFERENCES Agents (agent_id)
);

    CREATE TABLE Workers (
    worker_id integer PRIMARY KEY,
    worker_name text,
    belong_manager integer,
    total_sales integer,
    FOREIGN KEY (belong_manager) REFERENCES Managers (manager_id)
);

    CREATE TABLE Warehouses (
    warehouse_id integer PRIMARY KEY,
    city_id integer,
    belong_agent integer,
    stock_item_id integer,
    stock_item_name text,
    stock_item_quantity integer,
    FOREIGN KEY (city_id) REFERENCES Cities (city_id),
    FOREIGN KEY (belong_agent) REFERENCES Agents (agent_id)
);

    CREATE TABLE Items (
    item_id integer PRIMARY KEY AUTO_INCREMENT,
    item_name text,
    item_price integer
);

    CREATE TABLE Purchase_list (
    purchase_list_id integer,
    item_id integer,
    item_quantity integer DEFAULT 1,
    FOREIGN KEY (item_id) REFERENCES Items (item_id)
);

    CREATE TABLE Customers (
    customer_id integer PRIMARY KEY AUTO_INCREMENT,
    customer_name text,
    city_id integer,
    order_id integer,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id),
    FOREIGN KEY (order_id) REFERENCES Order(order_id)
);

    CREATE TABLE Orders (
    order_id integer PRIMARY KEY,
    customer_id integer,
    purchase_item_list_id integer,
    total_price integer,
    delivery_city integer,
    delivery_driver_id integer,
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (purchase_item_list_id) REFERENCES Purchase_list(purchase_item_list_id),
    FOREIGN KEY (delivery_city) REFERENCES Cities(city_id),
    FOREIGN KEY (delivery_driver_id) REFERENCES Drivers(driver_id)
);

    CREATE TABLE Drivers (
    driver_id integer PRIMARY KEY,
    driver_name text,
    city_id integer,
    total_delivery_count integer,
    FOREIGN KEY (city_id) REFERENCES Cities(city_id)
);
