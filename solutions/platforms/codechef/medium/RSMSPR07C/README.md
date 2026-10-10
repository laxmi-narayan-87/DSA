# RSMSPR07C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-7C Working with NULL values

Listen

Write queries for the following operations that deal with NULL values based on the tables that we created and the data that we inserted.

### Task

Update the Orders table by setting the Remarks_if_any field to NULL wherever it currently has the value "No Remarks".
After the update, retrieve the order_id and Remarks_if_any for all orders where Remarks_if_any is NULL.

**Hint: The `=` operator may not work for NULL.
Use an appropriate condition to check for NULL values.**

### Expected output

```
┌──────────┬────────────────┐
│ order_id │ Remarks_if_any │
├──────────┼────────────────┤
│ 1001     │ NULL           │
│ 1004     │ NULL           │
│ 1007     │ NULL           │
│ 1009     │ NULL           │
└──────────┴────────────────┘

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
**Submitted:** 2026-08-27T05:04:10.653Z  

```sql
/* Update your query here*/

UPDATE Orders 
SET Remarks_if_any = 'NULL'
WHERE Remarks_if_any='No Remarks';

SELECT order_id,Remarks_if_any
FROM Orders WHERE Remarks_if_any= 'NULL';
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR07C)