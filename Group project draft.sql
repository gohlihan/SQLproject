CREATE TABLE `Cities` (
  `city_id` int PRIMARY KEY,
  `city_name` varchar(255)
);

CREATE TABLE `Agents` (
  `agent_id` int PRIMARY KEY,
  `agent_name` varchar(255),
  `city_id` int,
  `total_sales` int
);

CREATE TABLE `Managers` (
  `manager_id` int PRIMARY KEY,
  `manager_name` varcahr,
  `belong_agent` int
);

CREATE TABLE `Workers` (
  `worker_id` int PRIMARY KEY,
  `worker_name` varchar(255),
  `belong_manager` int,
  `total_sales` int
);

CREATE TABLE `Warehouses` (
  `warehouse_id` int PRIMARY KEY,
  `city_id` int,
  `belong_agent` int,
  `stock_item_id` int,
  `stock_item_name` varchar(255),
  `stock_item_quantity` int
);

CREATE TABLE `Items` (
  `item_id` int PRIMARY KEY AUTO_INCREMENT,
  `item_name` varchar(255),
  `item_price` int
);

CREATE TABLE `Item_list` (
  `item_list_id` int,
  `item_id` int,
  `item_quantity` int DEFAULT 1
);

CREATE TABLE `Customers` (
  `customer_id` int PRIMARY KEY AUTO_INCREMENT,
  `customer_name` varchar(255),
  `city_id` int,
  `order_id` int
);

CREATE TABLE `Orders` (
  `order_id` int PRIMARY KEY,
  `customer_id` int,
  `purchase_item_list_id` int,
  `total_price` int,
  `delivery_city` int,
  `delivery_driver_id` int
);

CREATE TABLE `Drivers` (
  `driver_id` int PRIMARY KEY,
  `driver_name` varchar(255),
  `city_id` int,
  `total_delivery_count` int
);

ALTER TABLE `Cities` ADD FOREIGN KEY (`city_id`) REFERENCES `Agents` (`city_id`);

ALTER TABLE `Agents` ADD FOREIGN KEY (`agent_id`) REFERENCES `Managers` (`belong_agent`);

ALTER TABLE `Workers` ADD FOREIGN KEY (`belong_manager`) REFERENCES `Managers` (`manager_id`);

ALTER TABLE `Agents` ADD FOREIGN KEY (`agent_id`) REFERENCES `Warehouses` (`belong_agent`);

ALTER TABLE `Warehouses` ADD FOREIGN KEY (`stock_item_name`) REFERENCES `Items` (`item_name`);

ALTER TABLE `Item_list` ADD FOREIGN KEY (`item_id`) REFERENCES `Items` (`item_id`);

ALTER TABLE `Customers` ADD FOREIGN KEY (`city_id`) REFERENCES `Cities` (`city_id`);

ALTER TABLE `Customers` ADD FOREIGN KEY (`order_id`) REFERENCES `Orders` (`order_id`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`delivery_city`) REFERENCES `Cities` (`city_id`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`delivery_driver_id`) REFERENCES `Drivers` (`driver_id`);

ALTER TABLE `Item_list` ADD FOREIGN KEY (`item_list_id`) REFERENCES `Orders` (`purchase_item_list_id`);

ALTER TABLE `Cities` ADD FOREIGN KEY (`city_id`) REFERENCES `Drivers` (`city_id`);
