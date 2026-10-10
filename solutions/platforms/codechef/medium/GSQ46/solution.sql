 /* Write a query to find out the average Payout across department which has more than 3 employees from the table employee.
The output table should have the name of the department and their respective average pay. */

SELECT Department, AVG(Payout) as avg_payout
FROM employee
GROUP BY Department
HAVING COUNT(*)>3;