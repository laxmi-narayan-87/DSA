/* Update your query here*/

UPDATE Customers
SET new_address="NULL"
WHERE new_Address="Unknown";

SELECT customer_id,name,new_address
FROm Customers
LIMIT 3;