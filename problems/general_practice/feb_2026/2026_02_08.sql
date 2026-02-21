/*

Your user registration system had a bug where users could sign up multiple times with the same email. 
Each signup created a new record with a new user_id. 
You need to identify the "canonical" user record for each email (the most recent one based on created_at).

users:

user_id | email              | username    | created_at          | last_login_at
--------|-------------------|-------------|---------------------|------------------
1       | alice@email.com   | alice_2020  | 2020-05-01 10:00:00 | 2020-05-15 14:00:00
2       | bob@email.com     | bob_main    | 2021-03-10 09:00:00 | 2024-01-20 08:30:00
3       | alice@email.com   | alice_new   | 2022-08-15 11:30:00 | 2024-02-01 16:45:00
4       | alice@email.com   | alice_2024  | 2024-01-01 08:00:00 | 2024-02-05 12:00:00
5       | carol@email.com   | carol       | 2023-06-20 14:00:00 | NULL

- So alice@email.com has 3 user id's. Find the latest created at for each email
- max(timestamp) for each user_id

*/

with cte as 
(select 
    email_id,
    user_id,
    username,
    created_at,
    row_number() over(partition by email order by created_at desc) as rnk
from users)
select 
    *
from cte 
where rnk = 1


/*
You have a daily snapshot of product prices. 
You need to identify which products had price changes between yesterday and today to send to a downstream system. 
Only return products where the price actually changed.

product_id | price  | snapshot_date
-----------|--------|---------------
101        | 29.99  | 2024-02-06
101        | 29.99  | 2024-02-07
102        | 49.99  | 2024-02-06
102        | 54.99  | 2024-02-07
103        | 19.99  | 2024-02-06
103        | 19.99  | 2024-02-07
104        | 99.99  | 2024-02-06
104        | NULL   | 2024-02-07

- Sort the table on snapshot_date
- use lag() to find if there is any difference in the prices for consecutive dates

*/

with cte as
(select 
    product_id,
    price as new_price,
    lag(price) over(partition by product_id by order by snapshot_date) as old_price
from product_prices
WHERE snapshot_date IN ('2024-02-06', '2024-02-07'))
select 
    *,
    new_price - old_price as change_amount
from cte
where new_price != old_price or (new_price is NULL AND old_price is not NULL) or (new_price is not NULL AND old_price is NULL)

/*
Given user activity events, identify distinct "sessions". 
A session ends when there's a gap of more than 30 minutes between consecutive events for the same user.

user_id | event_time          | event_type
--------|---------------------|------------
1       | 2024-02-08 10:00:00 | page_view
1       | 2024-02-08 10:05:00 | click
1       | 2024-02-08 10:15:00 | page_view
1       | 2024-02-08 11:00:00 | page_view   ← New session (45 min gap from 10:15)
1       | 2024-02-08 11:10:00 | click
2       | 2024-02-08 09:00:00 | page_view
2       | 2024-02-08 09:20:00 | click


- For each user, Calculate the session time by creating row numbers for same session.

          check if inside the session? curr_event_time - prev_event_time (using lag())
10:00 - 1 - 1
10:05 - 2 - 1
10:15 - 3 - 1

- Gap of 45 mins
11:00 - 1 - 2
11:10 - 2 - 2

1. Initial CTE
case when event_time - lag(event_time) over(partition by user_id order by event_time) > INTERVAL '30 minutes' then 1 else 0 end as is_session_start

2. Create Sessions
sum(is_session_start) over (partition by user_id order by event_time) 

3. Aggregate the sessions

*/


/*
You have a table of daily stock prices, but some days are missing (weekends, holidays). 
For each date in a complete calendar, fill in missing prices with the last known price (forward fill).

*/



/*
A fitness app tracks daily workouts. 
Find users who have workout streaks of 3+ consecutive days. Return the user, streak start date, streak end date, and streak length.

1 - 02-01 - 
1 - 02-02 - 1
1 - 02-03 - 1
1 - 02-04 - 1

1 - 02-06

2 - 02-03
2 - 02-04

3 - 02-01
3 - 02-07


- First check all the consecutive events by calculating the lag() - So, case when lag(event_date) over(partition by user_id order by event_date) is null then 1 
                                                                             when DATEDIFF(event_date, lag(event_date) over(partition by user_id order by event_date)) = 1 then 0
                                                                             else 1 end 
- Now use the constant to create session ids - sum(is_new_streak) over(partition by user_id order by event_date) as streak_id
- Now do the aggregations of min and max dates and count(*)


- Detect Streak Breaks with LAG() - So, case when lag(event_date) over(partition by user_id order by event_date) is null then 1 
                                                                             when DATEDIFF(event_date, lag(event_date) over(partition by user_id order by event_date)) = 1 then 0
                                                                             else 1 end 
- Create Streak IDs with Cumulative SUM - sum(is_new_streak) over(partition by user_id order by event_date) as streak_id
- Aggregate - min and max dates and count(*)

1 - 02-01 - 1
1 - 02-02 - 0
1 - 02-03 - 0
1 - 02-04 - 0

*/



/*
You're maintaining customer data with history tracking (SCD Type 2). 
When a customer's status changes, you insert a new row and close out the old row.

Write a query to:

- Find the current status for all customers
- Identify customers who changed status more than once

- To find out the current status for all customers, for each customer, rank the rows based on the event_time. Then extract the top 1

- To identify the customers who changed status more than once
- Calculate the case when lag(status) over(partition by usr_id order by event_time) is distinct from current then 1 else 0 end
- Now calculate the cumulative sum of the number of the events

*/

/*
Your event streaming pipeline sometimes receives events out of order. 
You have both an event_time (when the event actually happened) and ingestion_time (when it arrived in your system).

- Identify events that arrived more than 1 hour late
- Determine if any late events have changed daily aggregations

event_time | ingestion_time

*/


/*
You're analyzing an e-commerce funnel. 
Users go through: page_view → add_to_cart → checkout → purchase. 
Calculate the conversion rate at each step and identify users who dropped off at each stage.

*/



