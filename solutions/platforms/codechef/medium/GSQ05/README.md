# GSQ05

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Inserting Data into a Table

Listen

Rows are added to a table using the  **INSERT INTO**  statement. Below is an example query to add the details of 'Abel George' to the existing table named `student`:

```
INSERT INTO student (student_id, student_name, contact_number)
VALUES (34, 'Abel George', 910023432);

```

- The INSERT INTO clause is used to add one or more rows to a table.
- student is the name of the table where the row will be added.
- (student_id, student_name, contact_number) specifies the columns into which the data will be inserted.
- VALUES is used to define the data being inserted.
- (34, 'Abel George', 910023432) represents the values to be inserted: 34: An integer to be added to the student_id column. 'Abel George': A text value to be added to the student_name column. Text values must always be enclosed in single quotes. 910023432: A number to be added to the contact_number column.

 **Multiple rows can be inserted in a single query by separating each set of values with a comma `','`.**  For example

```
INSERT INTO student (student_id, student_name, contact_number)
VALUES (34, 'Abel George', 910023432),
       (34, 'George Abel', 123456789);

```

### Task

Write a query to insert the following employee details into the `employee` table.
 **Note - both rows need to be inserted together by separating each set of values.** 

- Employee 1: employee_id: 4 employee_name: 'Marcus Garcia' department: 'Product'
- Employee 2: employee_id: 5 employee_name: 'Samantha Park' department: 'Hr'

Code the solution in the IDE.

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:16:27.458Z  

```sql
/* Write a query to insert the below mentioned employee details to the table 'employee' */

INSERT INTO employee(employee_id,employee_name, department)
VALUES(4, 'Marcus Garcia', 'Product'),
(5, 'Samantha Park' , 'Hr');
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ05)