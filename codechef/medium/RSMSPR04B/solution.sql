/* Update your query here*/

UPDATE Products
SET price=price+(0.1*price)
WHERE category= 'Electronics';

SELECT name,price,stock_quantity FROM products
WHERE category='Electronics'
LIMIT 1;