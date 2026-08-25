# GSQ09

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:24:08.650Z  

```sql
/* Write a query to add a column 'Designation' to the table and set 'Null' as the default value. Output the entire table.*/

ALTER TABLE Employee
ADD COLUMN Designation TEXT default Null;

select * from employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ09)