# GSQ59

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Problem-Group By & Having

Listen

Given a table  **employee**  which contains details of different employees, including their Department and their Payout, write an SQL query that performs the following:

- Calculate the average payout for each department.
- Only include departments where the total payout is greater than 40.
- Rename the column displaying the average payout as avg_payout.
- Display the results sorted by the department.

```
Expected output
┌────────────┬──────────────────┐
│ Department │   avg_payout     │
├────────────┼──────────────────┤
│ Hr         │ 23.9886666666667 │
│ Operations │ 11.227           │
│ Sales      │ 20.34625         │
└────────────┴──────────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:50:47.451Z  

```sql
/* Write a query to output the following
- Department and average payout on a single line
- Where total payout of the department is more than 40. */


SELECT Department, AVG(payout) as avg_payout
FROM employee
GROUP BY Department
HAVING SUM(payout)>40;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ59)