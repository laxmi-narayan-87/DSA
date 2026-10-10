/* Write a query to add a column 'Designation' to the table and set 'Null' as the default value. Output the entire table.*/

ALTER TABLE Employee
ADD COLUMN Designation TEXT default Null;

select * from employee;