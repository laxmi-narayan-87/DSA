/* Write a query which does the following */

-- Create a table 'customer'
CREATE TABLE customer(
id INT ,
Name TEXT,
Age INT,
address TEXT );






-- Insert data into the table 
INSERT INTO customer(id,Name, Age, address)
VALUES(1, 'John Smith', 25,  '123 Main St'),
(2, 'Sarah Johnson', 30,'456 Broadway'),
(3, 'Michael Brown', 45, '789 5th Ave'),
(4, 'Jessica Davis', 28, '321 Elm St'),
(5, 'David Lee', 35,  '555 Park Ave');

-- Output the entire table

SELECT * FROM customer;