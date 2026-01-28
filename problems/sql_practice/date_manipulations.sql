with cte as
(select 
    appointment_type,
    EXTRACT(EPOCH FROM (appointment_end - appointment_start)) / 60 as duration_in_seconds
from appointments
 WHERE 
    status = 'completed' AND appointment_end IS NOT NULL)
select
    appointment_type,
    avg(duration_in_seconds) as avg_duration_minutes
from cte
group by appointment_type
order by avg_duration_minutes desc
