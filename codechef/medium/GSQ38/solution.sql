/*Write a query to find the highest and lowest 'Hourly_pay' of the employees from the table 'employee'*/

SELECT MAX(Hourly_pay) as max_pay FROM employee;
SELECT MIN(Hourly_pay) as min_pay FROM employee;