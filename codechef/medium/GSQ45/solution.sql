 /* Write a query to find the Average of the column 'Payout' across 'Department' from the table 'employee'. The output table should have the average payout of each department.*/

SELECT Department, AVG(payout) as avg_payout 
FROM employee 
GROUP BY Department;