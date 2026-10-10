# GSQ58

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Debug this query

Listen

The Query written in the console is trying to find the minimum and maximum value of payout rounded to 2 decimal places in the table employee.
 **Debug this query**  to output the minimum and maximum value of payout, rounded to 2 decimal places.

Your database is named 'employee' and has the following columns

- Id (INT)
- Name (VARCHAR),
- Email (VARCHAR),
- Payout(INT)
### Expected output

```
┌─────────┬─────────┐
│ min_pay │ max_pay │
├─────────┼─────────┤
│ 123.54  │ 789.43  │
└─────────┴─────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T07:07:04.121Z  

```sql
/* **Debug this query** to output the minimum and maximum value of payout, round to 2 decimal places. */


select round(min(Payout),2) as 'min_pay',
    round(max(Payout),2) as 'max_pay'
from employee;


```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ58)