# GSQ37A

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Rename columns using As

Listen

Before we begin aggregate functions, a useful concept to know is renaming of columns during output.

In SQL, the keyword 'AS' allows you to rename a column or table using an alias.
Sample syntax:

```
SELECT employee_id AS 'Serial'
FROM employee;

```

### Task

Write a query to output all from the following columns in the table 'employee'

- Rename employee_id as 'Serial'
- Rename employee_name as 'Name'
- Rename department as 'Dept'
### Expected output

```
┌────────┬────────────────┬────────────┐
│ Serial │      Name      │    Dept    │
├────────┼────────────────┼────────────┤
│ 1      │ Kayla Thompson │ Sales      │
│ 2      │ Ethan Chen     │ Operations │
│ 3      │ Julia Lee      │ Hr         │
│ 4      │ Marcus Garcia  │ Product    │
│ 5      │ Samantha Park  │ Operations │
└────────┴────────────────┴────────────┘

```

#### Video Explanation:

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T06:49:12.491Z  

```sql
/* Write a query to output all from the following columns in the table 'employee'
- Rename employee_id as 'Serial'
- Rename employee_name as 'Name'
- Rename department as 'Dept' */

SELECT employee_id as Serial, employee_name as Name, department as Dept
FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ37A)