# GSQ39

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### ROUND()

Listen

Let us introduce the  **ROUND()**  function as it is routinely used with aggregate functions.
Sql uses the ROUND() functions to display numeric values rounded to a specified precision.
The precision parameter indicates the number of decimal places to which the number should be rounded.

The ROUND() function requires two parameters enclosed in parentheses: a column name and an integer value.
Below is the query to display  **Total_Purchase**  rounded to 1 decimal place from the table customer

```
SELECT ROUND(Total_Purchase, 1)
FROM CUSTOMER; 

```

### Task

Write a query to display the values in the column `Taxable_Pay` rounded to 2 decimal places from the table `employee`.

- Rename the column header as 'taxable_pay'

Code it out in the IDE.

```
┌─────────────┐
│ taxable_pay │
├─────────────┤
│ 21.34       │
│ 19.45       │
│ 40.82       │
│ 33.29       │
│ 19.0        │
└─────────────┘

```

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T06:57:21.003Z  

```sql
/* Write a query to round the **Taxable_Pay** to 2 decimal place from the table employee. */

SELECT ROUND(Taxable_Pay,2) as Taxable_Pay FROM employee;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ39)