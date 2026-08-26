# RSMSPR04A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-4A Data Modification (Update and Alter)

Listen

Write queries for the following data modification operations based on the tables that we created and the data that we inserted.

### Task

Increase the prices of all products in the 'Electronics' category by 10%.
Then, retrieve the name, price, and stock quantity of the first Electronics product from the Products table.

### Expected output

```
┌─────────────────┬──────────┬────────────────┐
│      name       │  price   │ stock_quantity │
├─────────────────┼──────────┼────────────────┤
│ Apple iPhone 15 │ 1099.989 │ 10             │
└─────────────────┴──────────┴────────────────┘

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
**Submitted:** 2026-08-26T13:38:00.374Z  

```sql
/* Update your query here*/

UPDATE Products
SET price=price+(0.1*price)
WHERE category= 'Electronics';

SELECT name,price,stock_quantity FROM products
WHERE category='Electronics'
LIMIT 1;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR04A)