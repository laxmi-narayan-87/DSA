/* Update your query here*/

ALTER TABLE Orders
ADD COLUMN discount
default 0.0;

SELECT order_id, total_amount, discount
FROM Orders
LIMIT 1;