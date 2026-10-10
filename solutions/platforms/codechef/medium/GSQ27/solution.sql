/* Debug this query to meet the following conditons
- Passenger gender - Female AND
- Flight destination - Delhi
*/

select * from flights
where gender like '%female%'
and destination like '%Delhi%';