# RSMSPR06A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-5D Deleting Records

Listen

Write queries for the following deletion operations based on the tables that we created and the data that we inserted.

Before we proceed with our queries, since these involve deletion operations, let's create a  **SAVEPOINT called S1**  before executing them. In real-life databases, we do this to revert back to the savepoint in case we need to undo the changes.

### Task

Delete all orders from the Orders table that are less than Rs. 150.
Then, retrieve the order_id, customer_id and total_amount of all orders from the Orders table.

### Expected output

```
┌──────────┬─────────────┬──────────────┐
│ order_id │ customer_id │ total_amount │
├──────────┼─────────────┼──────────────┤
│ 1001     │ 1           │ 999.99       │
│ 1002     │ 2           │ 299.98       │
│ 1004     │ 4           │ 899.99       │
│ 1005     │ 5           │ 799.99       │
│ 1006     │ 6           │ 499.99       │
│ 1008     │ 8           │ 699.99       │
└──────────┴─────────────┴──────────────┘

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
**Submitted:** 2026-08-27T04:36:20.989Z  

```sql
BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

/* Update your query below this line*/

DELETE FROM Orders
WHERE total_amount< 150;

SELECT order_id,customer_id, total_amount
FROM Orders;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR06A)