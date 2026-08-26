/* Write a query to output the following on separate lines
- Total Payout for the Product department.
- Average Payout for Operations department. */

SELECT SUM(Payout) as product_total_pay FROM employee
WHERE department='Product';

SELECT AVG(Payout) as ops_avg_pay FROM employee
WHERE department='Operations';