/* write a query below that returns the rows which meet the following conditions
- Gender - Female
- Destination - Cairo */

select * from Flights
where Gender = 'Female' 
and destination = 'Cairo';