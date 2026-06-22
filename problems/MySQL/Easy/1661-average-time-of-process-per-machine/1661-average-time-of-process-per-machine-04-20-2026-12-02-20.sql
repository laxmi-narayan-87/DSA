# Write your MySQL query statement below
SELECT  a.machine_id ,
ROUND(AVG(b.timestamp-a.timestamp),3) as Processing_time
FROM Activity a 
Join Activity b
ON a.machine_id = b.machine_id AND a.process_id= b.process_id
WHERE a.activity_type='start'
AND b.activity_type='end'
group by a.machine_id