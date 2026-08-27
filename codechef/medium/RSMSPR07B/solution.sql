UPDATE Customers
SET new_address = NULL
WHERE new_address = 'Unknown';

/* Update your query below this line*/

UPDATE Customers
SET new_address="23 Walnut Lane"
WHERE customer_id=10;

SELECT * FROM Customers WHERE customer_id=10;