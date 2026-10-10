/* Debug the below query */

SELECT  Department,Avg(Age) as 'avg_age'
FROM employee
GROUP BY Department
HAVING Count(*) > 3;