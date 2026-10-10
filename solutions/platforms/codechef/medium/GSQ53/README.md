# GSQ53

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Project - Customer Database

Listen

Welcome to the Project to help you practice everything that you learnt about data manipulations.
Imagine you are hired by a Supermarket chain as a database analyst. Your initial task is to create a database of customers.

## Task
- Create a table 'customer'.
- Add the below mentioned data to the table 'customer'.
- Output the entire table.
 **Id** 	 **Name** 	 **Age** 	 **address** 
1	John Smith	25	123 Main St
2	Sarah Johnson	30	456 Broadway
3	Michael Brown	45	789 5th Ave
4	Jessica Davis	28	321 Elm St
5	David Lee	35	555 Park Ave

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T07:02:31.482Z  

```sql
/* Write a query which does the following */

-- Create a table 'customer'
CREATE TABLE customer(
id INT ,
Name TEXT,
Age INT,
address TEXT );






-- Insert data into the table 
INSERT INTO customer(id,Name, Age, address)
VALUES(1, 'John Smith', 25,  '123 Main St'),
(2, 'Sarah Johnson', 30,'456 Broadway'),
(3, 'Michael Brown', 45, '789 5th Ave'),
(4, 'Jessica Davis', 28, '321 Elm St'),
(5, 'David Lee', 35,  '555 Park Ave');

-- Output the entire table

SELECT * FROM customer;
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ53)