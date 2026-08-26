# GSQ45

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:17:43.706Z  

```sql
/* Write a query to output the following on separate lines
- Total Payout for the Product department.
- Average Payout for Operations department. */

SELECT SUM(Payout) as product_total_pay FROM employee
WHERE department='Product';

SELECT AVG(Payout) as ops_avg_pay FROM employee
WHERE department='Operations';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ45)