/* Write a query which does the following
- Add a new column 'Hourly_Pay' to the table employee and set the value as 100 by default.
- Output the entire table
*/

ALTER table employee 
Add COLUMN Hourly_Pay TEXT default 100;

select * from employee;