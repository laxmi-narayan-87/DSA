# RSMSPR07A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-7A Working with NULL values

Listen

Write queries for the following operations that deal with NULL values based on the tables that we created and the data that we inserted.

### Task

Update the Customers table to replace all occurrences of "Unknown" in the new_address column with NULL.
Ensure that no records are deleted, only modified.
Then, retrieve the customer_id, name and new_address of the first 3 customers from the Customer table.

### Expected output

```
┌─────────────┬─────────────┬─────────────┐
│ customer_id │    name     │ new_address │
├─────────────┼─────────────┼─────────────┤
│ 1           │ John Doe    │ NULL        │
│ 2           │ Jane Smith  │ NULL        │
│ 3           │ Alice Brown │ NULL        │
└─────────────┴─────────────┴─────────────┘

```

### Tables
- Customers

```
┌─────────────┬─────────────┬──────────────────────┬────────────┬─────────────┬──────────────┐
│ customer_id │    name     │        email         │   phone    │   address   │ new_address  │
├─────────────┼─────────────┼──────────────────────┼────────────┼─────────────┼──────────────┤

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
**Submitted:** 2026-08-27T04:56:00.030Z  

```sql
/* Update your query here*/

UPDATE Customers
SET new_address="NULL"
WHERE new_Address="Unknown";

SELECT customer_id,name,new_address
FROm Customers
LIMIT 3;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR07A)