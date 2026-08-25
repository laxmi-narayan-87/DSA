/*Write a query which does the following
- Delete the entire row of the customer with customer id 1.
- Output the entire table once the above action is performed. */

DELETE FROM customer 
WHERE Id=1;

SELECT * FROM customer;