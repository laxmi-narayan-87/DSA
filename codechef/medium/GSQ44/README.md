# GSQ44

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### AVG()

Listen

The AVG() function is used to calculate the  **Average**  of values within a specific column.
It takes the column name as argument and outputs the resulting average.

Below is the query to find the Average Age from the table customer.

```
SELECT AVG(Age)
FROM customer;

```

### Task

Write a query to find the Average of the column 'Payout' from the table 'employee'.
Rename the column header as 'avg_payout'.
Code it out in the IDE.

```
Expected output
┌─────────────┐
│ avg_payout  │
├─────────────┤
│ 15.5339     │
└─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:15:30.898Z  

```sql
/* Write a query to find the Average of the column 'Payout' from the table 'employee'. */

SELECT AVG(Payout) as avg_payout FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ44)