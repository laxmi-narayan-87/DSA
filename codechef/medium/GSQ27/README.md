# GSQ27

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T06:31:20.902Z  

```sql
/* write a query with the following conditions
- Destination city end in 'o' AND
- Origin city starts with 'M' 
*/

SELECT * FROM Flights
WHERE Destination like '%o'
AND Origin like 'M%';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ27)