# GSQ38

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### MAX() and MIN()

Listen

The MAX() and MIN() functions retrieve the maximum and minimum values from a column, correspondingly.

Below is the query to find the highest and lowest age of the customers from the table customer

```
SELECT MAX(Age)
FROM customer;

```

```
SELECT MIN(Age)
FROM customer;

```

### Task

Write a query to find the highest and lowest 'Hourly_pay' of the employees from the table 'employee'.

- Rename the column header for highest pay as 'max_pay'
- Rename the column header for lowest pay as 'min_pay'

```
Expected output
┌─────────┐
│ max_pay │
├─────────┤
│ 55      │
└─────────┘
┌─────────┐
│ min_pay │
├─────────┤
│ 28      │
└─────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T06:54:30.168Z  

```sql
/*Write a query to find the highest and lowest 'Hourly_pay' of the employees from the table 'employee'*/

SELECT MAX(Hourly_pay) as max_pay FROM employee;
SELECT MIN(Hourly_pay) as min_pay FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ38)