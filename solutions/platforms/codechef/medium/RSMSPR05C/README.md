# RSMSPR05C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-5C Deleting Records

Listen

Write queries for the following deletion operations based on the tables that we created and the data that we inserted.

Before we proceed with our queries, since these involve deletion operations, let's create a  **SAVEPOINT called S1**  before executing them. In real-life databases, we do this to revert back to the savepoint in case we need to undo the changes.

### Task

We have deleted all orders that were placed before 2024-01-20.

You need to do the following

- Delete all Customers from the Customer table who have no records in the Orders table.
- Then, retrieve the customer_id and name of all Customers from the Customers table.
### Expected output

```
┌─────────────┬──────────────┐
│ customer_id │     name     │
├─────────────┼──────────────┤
│ 6           │ David White  │
│ 7           │ Emily Clark  │
│ 8           │ Frank Harris │
│ 9           │ Grace Kelly  │
│ 10          │ Henry Adams  │
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
**Submitted:** 2026-08-27T04:34:41.028Z  

```sql
BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

DELETE FROM Orders
WHERE order_date < '2024-01-20';

/* Update your query here */

-- DELETE c 
-- FROM Customers c
-- LEFT JOIN Orders o
-- on c.customer_id= o.customer_id
-- WHERE o.order_id IS NULL;

DELETE FROM Customers 
WHERE NOT EXISTS(
SELECT 1 
FROM Orders o 
WHERE o.customer_id=Customers.customer_id);

SELECT customer_id, name 
FROM Customers;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR05C)