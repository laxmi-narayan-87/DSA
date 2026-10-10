# RSMSPR05A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-5A Deleting Records

Listen

Write queries for the following deletion operations based on the tables that we created and the data that we inserted.

Before we proceed with our queries, since these involve deletion operations, let's create a  **SAVEPOINT called S1**  before executing them.
In real-life databases, we do this to revert back to the savepoint in case we need to undo the changes.

### Task

Remove all products that are out of stock.
Then, retrieve the product_id, name and stock_quantity of all products from the Product table.

### Expected output

```
┌────────────┬─────────────────────┬────────────────┐
│ product_id │        name         │ stock_quantity │
├────────────┼─────────────────────┼────────────────┤
│ 102        │ Samsung Galaxy S23  │ 15             │
│ 103        │ Leather Jacket      │ 25             │
│ 104        │ HP Laptop           │ 8              │
│ 105        │ Wooden Dining Table │ 5              │
│ 106        │ Nike Running Shoes  │ 20             │
│ 107        │ LED TV 55"          │ 12             │
│ 108        │ Rice 10kg           │ 50             │
│ 109        │ Sofa Set (3+1+1)    │ 4              │
│ 110        │ Organic Honey 500ml │ 30             │
└────────────┴─────────────────────┴────────────────┘

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
**Submitted:** 2026-08-27T04:02:23.437Z  

```sql
BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

/* Update your query below this line*/

DELETE FROM Products 
WHERE stock_quantity=0;

SELECT product_id, name, stock_quantity
FROM Products;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR05A)