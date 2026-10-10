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
