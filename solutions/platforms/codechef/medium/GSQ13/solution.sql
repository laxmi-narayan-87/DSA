/* Write a query to create a table employee with the mentioned constraints on the columns : 
employee_id - PRIMARY KEY, 
employee_Name -UNIQUE, 
department -NOT NULL CHECK (department IN ('Sales', 'Finance', 'Operations')) */

CREATE TABLE employee(
employee_id INT PRIMARY KEY,
employee_name TEXT UNIQUE,
department TEXT NOT NULL CHECK (department IN ('Sales', 'Finance', 'Operations'))
);