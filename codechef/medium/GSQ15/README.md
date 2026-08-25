# GSQ15

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Debug this query

Listen

The Query written in the console is trying to insert data to the table employee.
 **Debug this query**  to run the problem successfully.

- Don’t worry about the actual values as long as you get the query to run.

Your database is named 'employee' and has the following columns

- Id PRIMARY KEY(INT)
- Name (TEXT),
- Age (INT),
- Address UNIQUE (TEXT)

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:57:19.184Z  

```sql
/* Debug this query to run the problem successfully. 
- Don’t worry about the actual values as long as you get the query to run. */

INSERT INTO employee (Id,Name,Age,Address)
VALUES  (1, 'John Smith', 25,  '123 Main St'),
        (2, 'Sarah Johnson', 30,'456 Broadway'),
        (3, 'Michael Brown', 45,  '123 Main Str'),
        (4, 'Jessica Davis', 28,  '321 Elm St');
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ15)