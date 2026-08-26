/* Write a query to output the following
- Department and average payout on a single line
- Where total payout of the department is more than 40. */


SELECT Department, AVG(payout) as avg_payout
FROM employee
GROUP BY Department
HAVING SUM(payout)>40;