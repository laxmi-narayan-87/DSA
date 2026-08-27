# RSMSPR07C

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-27T05:01:00.041Z  

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

[View on CodeChef](https://www.codechef.com/problems/RSMSPR07C)