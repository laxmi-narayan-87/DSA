BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

/* Update your query below this line*/

DELETE FROM Products 
WHERE stock_quantity=0;

SELECT product_id, name, stock_quantity
FROM Products;