/* Write a query to do the following
- Set hourly_pay to 150 for HR employees
- Output the entire table
*/

-- UPDATE employee
-- SET Hourly_Pay = 150 
-- WHERE Department='HR';
-- select * from employee;

UPDATE employee
SET Hourly_Pay = 150
WHERE Department = 'Hr';

SELECT * FROM employee;