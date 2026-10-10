# GSQ41

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Problem-ROUND()

Listen

Write a query to output the following from the  **employee**  table:

- Round the column Payout to 2 decimal places. Rename the column header as 'payout'

```
Expected output
┌────────┐
│ payout │
├────────┤
│ 22.66  │
│ 6.55   │
│ 25.18  │
│ 0.71   │
│ 24.0   │
│ 5.48   │
│ 18.56  │
│ 13.65  │
│ 18.73  │
│ 19.82  │
└────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T07:04:59.512Z  

```sql
/* Write a query to output the following:
- Round the column **Payout** to 2 decimal places. */

SELECT ROUND(Payout,2) as Payout FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ41)