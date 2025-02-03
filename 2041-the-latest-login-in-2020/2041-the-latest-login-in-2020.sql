# Write your MySQL query statement below
select user_id, last_stamp
from
(select user_id, time_stamp as last_stamp,
row_number() over (partition by user_id order by time_stamp desc) as rno
from
(select user_id, time_stamp
from Logins
having year(time_stamp) = 2020) e) f
where rno = 1;