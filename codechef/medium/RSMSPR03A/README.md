# RSMSPR03A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-3 Data Retrieval Using Queries

Listen

Write queries for the following data retrieval operations based on the tables that we created and the data that we inserted.

### Task

Fetch all  **distinct**  product categories.

### Expected output

```
┌─────────────┐
│  category   │
├─────────────┤
│ Electronics │
│ Clothing    │
│ Furniture   │
│ Grocery     │
└─────────────┘

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
**Submitted:** 2026-08-26T13:25:37.618Z  

```sql
/* Update your query below*/

SELECT DISTINCT category  FROM Products;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR03A)