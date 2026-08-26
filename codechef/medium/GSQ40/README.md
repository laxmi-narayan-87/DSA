# GSQ40

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Problem - COUNT() MAX() and MIN()

Listen

You are given a table employee (mentioned below).

```
┌─────────────┬────────────────┬────────────┬────────────┐
│ Employee_id │ Employee_Name  │ Department │ Hourly_Pay │
├─────────────┼────────────────┼────────────┼────────────┤
│ 1           │ Kayla Thompson │ Sales      │ 44         │
│ 2           │ Ethan Chen     │ Operations │ 26         │
│ 3           │ Julia Lee      │ Hr         │ 66         │
│ 4           │ Marcus Garcia  │ Product    │ 34         │
│ 5           │ Samantha Park  │ Operations │ 43         │
│ 6           │ Brandon Kim    │ Operations │ 28         │
│ 7           │ Olivia Nguyen  │ Sales      │ 30         │
│ 8           │ Dylan Patel    │ Operations │ 35         │
│ 9           │ Chloe Davis    │ Hr         │ 31         │
│ 10          │ Brandon Adams  │ Product    │ 43         │
└─────────────┴────────────────┴────────────┴────────────┘

```

### Task

Write 3 separate queries to output the entries for the following:

- Count the number of employees in the department 'Sales'. Rename the column header as 'count_sales'
- Maximum Hourly pay for the department 'Operations'. Rename the column header as 'ops_max_pay'
- Minimum Hourly pay for the department 'Operations'. Rename the column header as 'ops_min_pay'

```
Expected output
┌─────────────┐
│ count_sales │
├─────────────┤
│ 2           │
└─────────────┘
┌─────────────┐
│ ops_max_pay │
├─────────────┤
│ 43          │
└─────────────┘
┌─────────────┐
│ ops_min_pay │
├─────────────┤
│ 26          │
└─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T07:02:21.826Z  

```sql
/*Write 3 separate queries to output the entries for the following
- Count the number of employees in the department 'Sales'.
- Maximum Hourly pay for the department 'Operations'.
- Minimum Hourly pay for the department 'Operations'.

Output the counts on separate lines */


SELECT COUNT(*) as count_sales FROM employee 
WHERE department='Sales';

SELECT MAX(Hourly_Pay) as ops_max_pay FROM employee 
WHERE department = 'Operations';

SELECT MIN(Hourly_Pay) as ops_min_pay FROM employee
WHERE department='Operations';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ40)