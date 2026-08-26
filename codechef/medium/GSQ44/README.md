# GSQ44

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Problem - SUM() and AVG()

Listen

Write a query to output the following on separate lines from the table 'employee'

- Total Payout for the Product department. Rename the column header as 'product_total_pay'
- Average Payout for Operations department. Rename the column header as 'ops_avg_pay'

employee table has following columns:
| **Employee_id**  |  **Employee_Name**  |  **Department**  |  **Payout**  |

```
Expected output
┌───────────────────┐
│ product_total_pay │
├───────────────────┤
│ 20.528            │
└───────────────────┘
┌─────────────┐
│ ops_avg_pay │
├─────────────┤
│ 12.41975    │
└─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T12:17:41.263Z  

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

[View on CodeChef](https://www.codechef.com/problems/GSQ44)