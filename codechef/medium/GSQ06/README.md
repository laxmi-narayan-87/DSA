# GSQ06

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Debug this query

Listen

The Query written in the console is trying to insert data to the table employee.
 **Debug this query**  to output the entire table.

Your table is named 'employee' and has the following columns

- Id (INT)
- Name (TEXT),
- Age (INT),
- Address (TEXT)
### Expected output

```
┌────┬───────────────┬─────┬──────────────┐
│ Id │     Name      │ Age │   Address    │
├────┼───────────────┼─────┼──────────────┤
│ 1  │ John Smith    │ 25  │ 123 Main St  │
│ 2  │ Sarah Johnson │ 30  │ 456 Broadway │
└────┴───────────────┴─────┴──────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:20:57.435Z  

```sql
/* The Query written in the console is trying to insert data to the table employee.
Debug this query to output the entire table */

INSERT INTO employee (Id,Name,Age,Address)
VALUES  (1, 'John Smith', 25,  '123 Main St'),
        (2, 'Sarah Johnson', 30,'456 Broadway');

SELECT * FROM employee; 
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ06)