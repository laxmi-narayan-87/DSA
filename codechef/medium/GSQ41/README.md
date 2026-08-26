# GSQ41

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T07:02:24.471Z  

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

[View on CodeChef](https://www.codechef.com/problems/GSQ41)