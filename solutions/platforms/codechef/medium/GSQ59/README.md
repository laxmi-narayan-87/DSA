# GSQ59

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Debug this code

Listen

The Query written in the console is trying to do the following

- Find the average age of the employees
- The department of the employees (using the group by function)
- specifically for departments which have more than three employees.

 **Debug this query**  to get the correct output.

Your database is named 'employee' and has the following columns

- Id (INT)
- Name (VARCHAR),
- Age (INT),
- Department (VARCHAR)
### Expected output

```
┌────────────┬─────────┐
│ Department │ avg_age │
├────────────┼─────────┤
│ Operations │ 23.0    │
│ Sales      │ 20.5    │
└────────────┴─────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:58:47.699Z  

```sql
/* Debug the below query */

SELECT  Department,Avg(Age) as 'avg_age'
FROM employee
GROUP BY Department
HAVING Count(*) > 3;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ59)