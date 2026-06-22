-- # Write your MySQL query statement below
-- Select a.machine_id,
-- Round(avg(b.timestamp- a.timestamp),3) as processing_time
-- from activity a 
-- join activity b
-- on a.machine_id= b.machine_id and a.process_id =b.process_id
-- where a.activity_type ="Start"
-- and b.activity_type ='END'
-- group by a.machine_id 

Select machine_id,
round(avg(process_time),3 ) as processing_time
from (
    select machine_id,process_id,
    sum(
        CASE when activity_type= "start" then -timestamp
        when activity_type="end" then timestamp
    end 
    )as process_time
    from activity 
    group by machine_id ,process_id
) t
group by machine_id;
