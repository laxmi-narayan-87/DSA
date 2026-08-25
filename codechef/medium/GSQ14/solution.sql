/* Write a query which does the following
- Delete the row where the department is Client.
- Output the entire table.
*/

DELETE FROM employee 
WHERE Department='Client';

SELECT * FROM employee;