# RSMSPR06D

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-6D Aggregations & Grouping

Listen

Write queries for the following Aggregations & Grouping operations based on the tables that we created and the data that we inserted.

### Task

Find the highest-priced product along with its name.

### Expected output

```
┌─────────────────┬──────────┐
│      name       │  price   │
├─────────────────┼──────────┤
│ Apple iPhone 15 │ 1099.989 │
└─────────────────┴──────────┘

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
**Submitted:** 2026-08-27T04:48:12.674Z  

```sql
ROLLBACK TO S1;

/* Update your query below this line*/

SELECT name, MAX(price) as price
FROM Products; 
-- WHERE MAX

```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR06D)