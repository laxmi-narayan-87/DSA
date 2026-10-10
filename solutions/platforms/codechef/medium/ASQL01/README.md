# ASQL01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Right Joins

We've seen how `LEFT JOIN` keeps all rows from the left table, filling in `NULL`s where there's no match in the right table. `RIGHT JOIN` does the opposite.

A  **RIGHT JOIN**  keeps all rows from the  *right*  table (the second table listed in the `JOIN` clause) and includes matching rows from the  *left*  table (the first table listed).

If a row in the right table doesn't have a corresponding match in the left table:

- All columns from the right table will be included.
- Columns from the left table will be filled with NULL values.

Essentially, `RIGHT JOIN` ensures every row from the second (right) table appears in the result, regardless of whether a match exists in the first (left) table.

Here's the general structure:

```
SELECT *
FROM customer
RIGHT JOIN order
ON customer.cust_id = order.cust_id;

```

### Task

Write the queries to do the following:

- JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table.
- RIGHT JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table.

 **Expected outputs** 
 ***After JOIN** *

St_id	St_Name	Department	Course_id	Course_id	Course_Name	Credits	Prof_id
1001	John Smith	Computer Science	CS101	CS101	Introduction to Computer Science	3	2001
1002	Emily Brown	History	HIS102	HIS102	World History II	3	2004
1003	David Lee	Mathematics	MAT202	MAT202	Linear Algebra	2	2002
1004	Sarah Johnson	English	ENG201	ENG201	Advanced Writing	4	2003

 ***After RIGHT JOIN** *

St_id	St_Name	Department	Course_id	Course_id	Course_Name	Credits	Prof_id
1001	John Smith	Computer Science	CS101	CS101	Introduction to Computer Science	3	2001
1002	Emily Brown	History	HIS102	HIS102	World History II	3	2004
1003	David Lee	Mathematics	MAT202	MAT202	Linear Algebra	2	2002
1004	Sarah Johnson	English	ENG201	ENG201	Advanced Writing	4	2003
NULL	NULL	NULL	NULL	BIO104	Principles of Bio-technology	4	2006

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-31T05:36:29.714Z  

```sql
/* Write the queries to do the following:
 - JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table.
 - RIGHT JOIN the tables 'student' and 'course' using 'Course_id' to match both the tables and output the joined table. */
 
 
 
 SELECT * FROM student s JOIN course c on s.Course_id=c.Course_id;
 
 SELECT * FROM student s RIGHT JOIN course c on s.Course_id=c.Course_id;
```

---

[View on CodeChef](https://www.codechef.com/problems/ASQL01)