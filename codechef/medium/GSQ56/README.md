# GSQ56

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice - Delete Single Record

Listen

Write a query which does the following

- Delete the entire row of the table 'customer' with customer id 1.
- Output the entire table once the above action is performed.
- Original table - 'customer' has the following rows

```
┌────┬───────────────┬─────┬──────────────┬───────────────────────────┐
│ Id │     Name      │ Age │   Address    │           email           │
├────┼───────────────┼─────┼──────────────┼───────────────────────────┤
│ 1  │ John Smith    │ 25  │ 123 Main St  │ john@example.com          │
│ 2  │ Sarah Johnson │ 30  │ 456 Broadway │ sarah@example.com         │
│ 3  │ Michael Brown │ 45  │ 789 5th Ave  │ michael.brown@example.com │
│ 4  │ Jessica Davis │ 28  │ 321 Elm St   │ jessica.davis@example.com │
└────┴───────────────┴─────┴──────────────┴───────────────────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T07:08:45.540Z  

```sql
/*Write a query which does the following
- Delete the entire row of the customer with customer id 1.
- Output the entire table once the above action is performed. */

DELETE FROM customer 
WHERE Id=1;

SELECT * FROM customer;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ56)