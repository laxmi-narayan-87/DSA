# RSMSPR04E

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-4 Data Modification (Update and Alter)

Listen

Write queries for the following data modification operations based on the tables that we created and the data that we inserted.

### Task

Add a new column "discount" to the Orders table.
Set its default value to 0.
Set a 5% discount for all orders above ₹900.
Then, retrieve the order_id, total_amount, discount of all orders that has at least some discount from the Orders table.

### Expected output

```
┌──────────┬──────────────┬──────────┐
│ order_id │ total_amount │ discount │
├──────────┼──────────────┼──────────┤
│ 1001     │ 999.99       │ 49.9995  │
└──────────┴──────────────┴──────────┘

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
**Submitted:** 2026-08-26T13:53:47.927Z  

```sql
/* Update your query here */

ALTER TABLE Orders
ADD COLUMN discount DECIMAL(10,4)
DEFAULT 0.000;

UPDATE Orders 
-- SET discount= total_amount*0.5
SET discount= ROUND(total_amount*0.05,4)
WHERE total_amount>900;

SELECT order_id,total_amount,discount 
FROM Orders
WHERE discount>0;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR04E)