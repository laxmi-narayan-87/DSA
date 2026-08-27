# RSMSPR06A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-6A Aggregations & Grouping

Listen

Write queries for the following Aggregations & Grouping operations based on the tables that we created and the data that we inserted.

🤔Remember, we deleted many records in the previous module. But let's say we want to perform the queries here before the deletion.
💡Fortunately, SAVEPOINT comes to our rescue here. Let's rollback the database to SAVEPOINT S1 and restore the previous state.

### Task

Find the total revenue generated and display it with the header total_revenue.

### Expected output

```
┌───────────────┐
│ total_revenue │
├───────────────┤
│ 4501.89       │
└───────────────┘

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
**Submitted:** 2026-08-27T04:37:54.154Z  

```sql
ROLLBACK TO S1;

/* Update your query below this line*/

SELECT SUM(total_amount) as total_revenue FROM Orders;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR06A)