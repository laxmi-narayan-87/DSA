/* Update your query here*/

UPDATE Orders 
SET Remarks_if_any = 'NULL'
WHERE Remarks_if_any='No Remarks';

SELECT order_id,Remarks_if_any
FROM Orders WHERE Remarks_if_any= 'NULL';