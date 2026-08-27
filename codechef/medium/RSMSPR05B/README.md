# RSMSPR05B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T04:02:24.847Z  

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

[View on CodeChef](https://www.codechef.com/problems/RSMSPR05B)