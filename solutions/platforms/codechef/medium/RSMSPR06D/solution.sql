ROLLBACK TO S1;

/* Update your query below this line*/

SELECT name, MAX(price) as price
FROM Products; 
-- WHERE MAX
