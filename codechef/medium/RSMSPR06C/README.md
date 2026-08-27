# RSMSPR06C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-6C Aggregations & Grouping

Listen

Write queries for the following Aggregations & Grouping operations based on the tables that we created and the data that we inserted.

### Task

Find the number of orders placed per month and display them with the headers order_month and total_orders.
To aggregate orders placed per month - you can use the following

```
SELECT strftime('%Y-%m', order_date) AS order_month

```

### Expected output

```
┌─────────────┬──────────────┐
│ order_month │ total_orders │
├─────────────┼──────────────┤
│ 2024-01     │ 10           │
└─────────────┴──────────────┘

```

### Tables
- Customers

```
┌─────────────┬─────────────┬──────────────────────┬────────────┬─────────────┐
│ customer_id │    name     │        email         │   phone    │   address   │
└─────────────┼─────────────┼──────────────────────┼────────────┼─────────────┘

```

- Products

```
┌────────────┬────────────────────┬─────────────┬────────┬────────────────┐
│ product_id │        name        │  category   │ price  │ stock_quantity │
└────────────┴────────────────────┴─────────────┴────────┴────────────────┘

```

- Orders

```
┌──────────┬─────────────┬────────────┬──────────────┬─────────────────┐
│ order_id │ customer_id │ order_date │ total_amount │ Remarks_if_any  │
└──────────┴─────────────┴────────────┴──────────────┴─────────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T04:46:25.554Z  

```sql
ROLLBACK TO S1;

/* Update your query below this line*/

SELECT strftime('%Y-%m', order_date) as order_month, COUNT(total_amount) as total_orders
FROM Orders
GROUP by Order_month;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR06C)