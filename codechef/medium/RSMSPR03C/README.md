# RSMSPR03C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-3C Data Retrieval Using Queries

Listen

Write queries for the following data retrieval operations based on the tables that we created and the data that we inserted.

### Task

Find the 2 most expensive products from the Products table.

### Expected output

```
┌────────────┬──────────────────┬─────────────┬────────┬────────────────┐
│ product_id │       name       │  category   │ price  │ stock_quantity │
├────────────┼──────────────────┼─────────────┼────────┼────────────────┤
│ 101        │ Apple iPhone 15  │ Electronics │ 999.99 │ 10             │
│ 109        │ Sofa Set (3+1+1) │ Furniture   │ 999.99 │ 4              │
└────────────┴──────────────────┴─────────────┴────────┴────────────────┘

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
**Submitted:** 2026-08-26T13:32:02.356Z  

```sql
/* Update your query here */

SELECT * FROM Products
-- GROUP BY price
ORDER BY price DESC
LIMIT 2;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR03C)