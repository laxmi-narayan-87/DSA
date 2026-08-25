# GSQ07

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Primary Key

Listen

## Primary Key

A  **Primary Key**  is a column (or a set of columns) in a database table that uniquely identifies each row. It enforces  **uniqueness**  and  **non-nullability**, meaning no two rows can have the same primary key value, and it cannot be NULL.

## Other Terms:
### Unique
- Ensures that all values in a column are distinct.
- Unlike a primary key, a column with a UNIQUE constraint can have NULL values (unless explicitly marked as NOT NULL). title VARCHAR(255) UNIQUE
### Not Null
- Prevents a column from having NULL values.
- Ensures that every row must have a valid (non-null) value for the specified column. id INT NOT NULL
### Default
- Assigns a default value to a column when no value is provided during an INSERT operation.
- Example: age INT DEFAULT 18
### Auto Increment
- Automatically generates a unique sequential value for a column (usually for primary keys).
- Commonly used with INTEGER primary keys.
- Example: CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,);
### Points to remember
- No two rows can have the same primary key—it must be unique.
- A primary key cannot contain null values (it can't be empty).
- Each table can have only one primary key.
### Here's a quick question for you: If you were making a table of movies, what would be a good primary key?

## Solution

**Language:** C++  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T06:17:52.460Z  

```cpp
/* Write a query to insert the below mentioned employee details to the table 'employee' */

INSERT INTO employee(employee_id,employee_name, department)
VALUES(4, 'Marcus Garcia', 'Product'),
(5, 'Samantha Park' , 'Hr');
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ07)