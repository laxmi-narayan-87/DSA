# GSQ21

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Debug this query

Listen

Let us combine what we have learnt from our 'SELECT', 'DISTINCT' and 'WHERE' queries.

The Query written in the console is trying to do the following.

- Where the origin of the flight is 'Mumbai'
- Output the 'Distinct' names of 'Male' passengers

 **Debug this query**  to get the correct output!

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
**Submitted:** 2026-08-26T06:19:15.854Z  

```sql
/* Debug this query to get the correct output */

select distinct passenger_name
from flights
where gender = 'Male'
and origin = 'Mumbai';
```

---

[View on CodeChef](https://www.codechef.com/problems/GSQ21)