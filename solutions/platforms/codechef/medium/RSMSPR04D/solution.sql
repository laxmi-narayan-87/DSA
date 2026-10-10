/* Update your query here*/

ALTER TABLE Customers
ADD COLUMN new_address
DEFAULT 'Unknown';

SELECT name,address,new_address
FROM Customers
LIMIT 1;