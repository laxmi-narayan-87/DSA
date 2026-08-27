# RSMSPR05C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T04:04:23.866Z  

```sql
BEGIN TRANSACTION;
SAVEPOINT S1;
--Savepoint created incase any changes to the the database beyond this point has to be undone in the future.

/* Update your query here*/

DELETE FROM Orders 
WHERE order_date <'2024-01-20';

SELECT order_id, customer_id, order_date, total_amount
FROM Orders;
```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR05C)