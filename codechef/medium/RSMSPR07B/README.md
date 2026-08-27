# RSMSPR07B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-7B Working with NULL values

Listen

Write queries for the following operations that deal with NULL values based on the tables that we created and the data that we inserted.

 **Note:**  In the previous problem - we replaced all occurrences of "Unknown" in the new_address column with NULL. Using this updated table - perform the following.

### Task

Check if the customer with customer_id = 10 and name = 'Henry Adams' has NULL in the new_address column.
If it is NULL, update it to  **"23 Walnut Lane"**.
Then, retrieve all details about that customer from the Customers table.

### Expected output

```
┌─────────────┬─────────────┬───────────────────┬────────────┬────────────────┬────────────────┐
│ customer_id │    name     │       email       │   phone    │    address     │  new_address   │
├─────────────┼─────────────┼───────────────────┼────────────┼────────────────┼────────────────┤
│ 10          │ Henry Adams │ henry.a@email.com │ 9312465789 │ 22 Walnut Lane │ 23 Walnut Lane │
└─────────────┴─────────────┴───────────────────┴────────────┴────────────────┴────────────────┘

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
**Submitted:** 2026-08-27T05:00:56.354Z  

```sql
UPDATE Customers
SET new_address = NULL
WHERE new_address = 'Unknown';

/* Update your query below this line*/

UPDATE Customers
SET new_address="23 Walnut Lane"
WHERE customer_id=10
AND name='Henry Adams'
AND new_address IS NULL;

SELECT * FROM Customers WHERE customer_id=10;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR07B)