BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

DELETE FROM Orders
WHERE order_date < '2024-01-20';

/* Update your query here */

-- DELETE c 
-- FROM Customers c
-- LEFT JOIN Orders o
-- on c.customer_id= o.customer_id
-- WHERE o.order_id IS NULL;

DELETE FROM Customers 
WHERE NOT EXISTS(
SELECT 1 
FROM Orders o 
WHERE o.customer_id=Customers.customer_id);

SELECT customer_id, name 
FROM Customers;