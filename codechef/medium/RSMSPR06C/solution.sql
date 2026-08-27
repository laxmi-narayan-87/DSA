ROLLBACK TO S1;

/* Update your query below this line*/

SELECT strftime('%Y-%m', order_date) as order_month, COUNT(total_amount) as total_orders
FROM Orders
GROUP by Order_month;