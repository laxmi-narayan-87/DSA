# RSMSPR03B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-3B Data Retrieval Using Queries

Listen

Write queries for the following data retrieval operations based on the tables that we created and the data that we inserted.

### Task

Get orders of customers who have spent more than ₹900.

### Expected output

```
┌──────────┬─────────────┬────────────┬──────────────┬────────────────┐
│ order_id │ customer_id │ order_date │ total_amount │ Remarks_if_any │
├──────────┼─────────────┼────────────┼──────────────┼────────────────┤
│ 1001     │ 1           │ 2024-01-15 │ 999.99       │ No Remarks     │
└──────────┴─────────────┴────────────┴──────────────┴────────────────┘

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
**Submitted:** 2026-08-26T13:26:49.484Z  

```sql
/* Update your query below*/

SELECT * FROM Orders 
WHERE total_amount>900;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR03B)