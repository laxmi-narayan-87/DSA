/* Write a query which does the following
- Update the age to 52 for the customer with customer id 3.
- Output all the entires of the table. */

UPDATE customer
SET Age=52 
WHERE Id=3;

SELECT * FROM customer;