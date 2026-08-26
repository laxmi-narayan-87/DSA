/* Update your query here */

ALTER TABLE Orders
ADD COLUMN discount DECIMAL(10,4)
DEFAULT 0.000;

UPDATE Orders 
-- SET discount= total_amount*0.5
SET discount= ROUND(total_amount*0.05,4)
WHERE total_amount>900;

SELECT order_id,total_amount,discount 
FROM Orders
WHERE discount>0;