# GSQ15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice - Delete From

Listen

You are given a table -  **employee**  (mentioned below).

Write a query which does the following

- Delete the row where the department is Client.
- Output the entire table.
- Original table has the following rows

```
┌─────────────┬────────────────┬────────────┐
│ Employee_id │ Employee_Name  │ Department │
├─────────────┼────────────────┼────────────┤
│ 1           │ Kayla Thompson │ Sales      │
│ 2           │ Ethan Chen     │ Operations │
│ 3           │ Julia Lee      │ Client     │
│ 4           │ Marcus Garcia  │ Product    │
└─────────────┴────────────────┴────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:55:54.030Z  

```sql
/* Write a query which does the following
- Delete the row where the department is Client.
- Output the entire table.
*/

DELETE FROM employee 
WHERE Department='Client';

SELECT * FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ15)