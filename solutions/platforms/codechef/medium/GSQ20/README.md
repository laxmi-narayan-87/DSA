# GSQ20

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Practice - Basic query with Where Clause

Listen

Let us combine what we have learnt from our 'SELECT', 'DISTINCT' and 'WHERE' queries.

From the 'Flights' table - let us find the following

- Where the origin of the flight is 'New York'
- Output the passenger_name and gender

```
Expected Output
┌────────────────┬────────┐
│ Passenger_name │ Gender │
├────────────────┼────────┤
│ Dia            │ Female │
│ Jackson        │ Male   │
└────────────────┴────────┘

```

Remember that the column details are as follows

- Passenger_id
- Passenger_name
- Gender
- Origin
- Destination

## Solution

**Language:** SQL  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-25T07:21:45.859Z  

```sql
/* Write a query that does the following
- Where the origin of the flight is 'New York'
- Output the passenger_name and gender */

SELECT passenger_name, gender 
FROM Flights 
WHERE origin='New York';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ20)