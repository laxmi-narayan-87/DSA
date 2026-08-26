# RSMSPR01

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Task-1 Design the Database Schema- Tables & Fields

Listen

### Create and Define the tables with proper constraints:

 ***Note: Use the exact table and field names mentioned here. Ensure that each field's datatype and constraints are defined exactly as specified.** *

There should be 3 tables in this database.

- Products - Stores information about items sold in the retail store.
- Customers - Stores customer details, ensuring unique emails and phone numbers.
- Orders - Tracks purchases, linking customers to their orders.

 **CREATE the tables with the following fields and constraints:** 

### Products
 **Field** 	 **Datatype** 	 **Constraint** 
product_id	INTEGER	PRIMARY KEY
name	TEXT	NOT NULL
category	TEXT	CHECK (category IN ('Electronics', 'Clothing', 'Grocery', 'Furniture'))
price	REAL	NOT NULL CHECK (price > 0)
stock_quantity	INTEGER	CHECK (stock_quantity >= 0)
### Customers
 **Field** 	 **Datatype** 	 **Constraint** 
customer_id	INTEGER	PRIMARY KEY
name	TEXT	NOT NULL
email	TEXT	UNIQUE NOT NULL
phone	TEXT	UNIQUE NOT NULL
address	TEXT	DEFAULT 'Not Provided'
### Orders
 **Field** 	 **Datatype** 	 **Constraint** 
order_id	INTEGER	PRIMARY KEY
customer_id	INTEGER	NOT NULL
order_date	DATE	DEFAULT CURRENT_DATE
total_amount	REAL	CHECK (total_amount > 0)
Remarks_if_any	TEXT	DEFAULT 'No Remarks'

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T13:17:15.158Z  

```sql
/* Update the '_' in the code below */

CREATE TABLE Products (
    product_id INT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT CHECK (category IN ('Electronics', 'Clothing', 'Grocery', 'Furniture')),
    price REAL NOT NULL CHECK(price > 0),
    stock_quantity INT CHECK (stock_quantity >=0)
);

CREATE TABLE Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    phone TEXT UNIQUE NOT NULL,
    address TEXT DEFAULT 'Not Provided'
);

CREATE TABLE Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date DATE DEFAULT CURRENT_DATE,
    total_amount REAL CHECK (total_amount > 0),
    Remarks_if_any TEXT DEFAULT 'No Remarks'
);

```

---

[View on CodeChef](https://www.codechef.com/problems/RSMSPR01)