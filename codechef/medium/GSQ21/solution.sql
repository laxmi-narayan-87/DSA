/* Write a query that does the following
- Where the origin of the flight is 'New York'
- Output the passenger_name and gender */

SELECT passenger_name, gender 
FROM Flights 
WHERE origin='New York';