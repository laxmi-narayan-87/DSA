# GSQ04

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Create table

Listen

Using a  **CREATE TABLE**  statement in SQL enables the creation of a new table in the database.
This statement can be used whenever a new table needs to be created, starting with a blank slate.
The example statement below demonstrates the creation of a new table called  **student**.

```
    CREATE TABLE student (
       Student_id INT,
       Student_Name  TEXT,
       Department  TEXT
   ); 

```

The above query will create an empty table 'student' as mentioned below:

 **Student_id** 	 **Student_Name** 	 **Department** 
		
		
### Task

Let us now try and build the table that we saw earlier, starting from scratch.
Write a query to create a table 'employee', with columns employee_id, employee_Name and Department.
Code it out in the IDE.

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:12:02.983Z  

```sql
/* Write a query to create a table 'employee', with columns employee_id, employee_Name and Department. 
Update the blanks below to solve this problem */

CREATE TABLE employee
(
    Employee_id int , /* Integer Data type assigned to the variable */
    Employee_Name   text, /* TEXT Data type assigned to the variable */
    Department  text/* TEXT Data type assigned to the variable */
);
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ04)