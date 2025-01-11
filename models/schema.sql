CREATE TABLE Region (
    region_id INT PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL
);

CREATE TABLE Customer (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES Region(region_id)
);

CREATE TABLE Product (
    product_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    release_date DATE NOT NULL
);

CREATE TABLE Feedback (
    feedback_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    rating INT,
    comments TEXT,
    feedback_date DATE, 
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);


CREATE TABLE Audit_Log (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    action_type VARCHAR(10),
    action_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified_by VARCHAR(100),
    old_value VARCHAR(255),
    new_value VARCHAR(255),
    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id)
);
