# RSMSPR06B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-6B Aggregations & Grouping

Listen

Write queries for the following Aggregations & Grouping operations based on the tables that we created and the data that we inserted.

### Task

Find the average spending per customer and display it with the header avg_spending_per_customer.

### Expected output

```
┌───────────────────────────┐
│ avg_spending_per_customer │
├───────────────────────────┤
│ 599.99                    │
└───────────────────────────┘

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
**Submitted:** 2026-08-27T04:39:05.305Z  

```sql
/* Update your query here*/

SELECT AVG(total_amount) as avg_spending_per_customer
FROM Orders;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR06B)