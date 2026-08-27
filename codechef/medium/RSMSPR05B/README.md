# RSMSPR05B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-5B Deleting Records

Listen

Write queries for the following deletion operations based on the tables that we created and the data that we inserted.

Before we proceed with our queries, since these involve deletion operations, let's create a  **SAVEPOINT called S1**  before executing them.
In real-life databases, we do this to revert back to the savepoint in case we need to undo the changes.

### Task

Delete all orders that were placed before 2024-01-20.
Then, retrieve the order_id, customer_id, order_date, total_amount of all orders from the Orders table.

### Expected output

```
┌──────────┬─────────────┬────────────┬──────────────┐
│ order_id │ customer_id │ order_date │ total_amount │
├──────────┼─────────────┼────────────┼──────────────┤
│ 1006     │ 6           │ 2024-01-20 │ 499.99       │
│ 1007     │ 7           │ 2024-01-21 │ 129.99       │
│ 1008     │ 8           │ 2024-01-22 │ 699.99       │
│ 1009     │ 9           │ 2024-01-23 │ 25.99        │
│ 1010     │ 10          │ 2024-01-24 │ 15.99        │
└──────────┴─────────────┴────────────┴──────────────┘

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
**Submitted:** 2026-08-27T04:04:18.904Z  

```sql
BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

/* Update your query here*/

DELETE FROM Orders 
WHERE order_date <'2024-01-20';

SELECT order_id, customer_id, order_date, total_amount
FROM Orders;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR05B)