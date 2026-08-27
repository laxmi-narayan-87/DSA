/* Write all the 5 queries here and RUN/SUBMIT them all at once*/

SELECT order_id,customer_id,order_date
FROM Orders 
WHERE order_date BETWEEN '2024-01-01' AND '2024-01-31';

SELECT max(order_date) as most_recent_order
FROM Orders;

SELECT order_date, COUNT(*) as order_count 
FROM Orders
WHERE order_date BETWEEN '2024-01-15' AND '2024-01-17'
GROUP BY order_date;


SELECT JULIANDAY(MAX(order_date)) - JULIANDAY(MIN(order_date)) as days_between
FROM Orders;



SELECT order_id,customer_id,order_date, total_amount
FROM Orders 
WHERE order_date BETWEEN DATE('2024-01-24', '-5 days')
                     AND DATE('2024-01-24', '-1 day');