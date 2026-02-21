/*
- figure out a way to 


with cte as 
(select 
    user_id,
    date_trunc("DAY", timestamp) as curr_day,
    max(case when action = "page_load" then timestamp end) as load_time,
    min(case when action = "page_exit" then timestamp end) as exit_time
from facebook_web_log
group by user_id, curr_day)

select
    user_id,    
    avg(exit_time - load_time) as avg_session_time
from cte
where load_time < exit_time 
    and load_time is not null 
    and exit_time is not null
group by user_id

*/

/*
Acceptance Rate By Date

- Join
- Filter
- Group by
- Aggregate
- Ranking


- Need to find the requests which got accepted. That's it.
- User_id A sent request to User_id B. Check if B has accepted it.



*/

