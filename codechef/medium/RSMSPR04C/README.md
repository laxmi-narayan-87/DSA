# RSMSPR04C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-4C Data Modification (Update and Alter)

Listen

Write queries for the following data modification operations based on the tables that we created and the data that we inserted.

### Task

Update the stock quantity of all products that has stock quantity of 10 to 0.
Then, retrieve all the details of all the products whose stock quantity is 0 from the Products table.

### Expected output

```
┌────────────┬─────────────────┬─────────────┬──────────┬────────────────┐
│ product_id │      name       │  category   │  price   │ stock_quantity │
├────────────┼─────────────────┼─────────────┼──────────┼────────────────┤
│ 101        │ Apple iPhone 15 │ Electronics │ 999.99   │ 0              │
└────────────┴─────────────────┴─────────────┴──────────┴────────────────┘

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
**Submitted:** 2026-08-26T13:43:03.533Z  

```sql
/* Update your query here*/

UPDATE Products
SET stock_quantity =0
WHERE stock_quantity=10;

SELECT * FROM Products 
WHERE stock_quantity=0;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR04C)