# Write your MySQL query statement below

select event_day as day, emp_id, sum(time_col) as total_time
from
(select emp_id, event_day, (out_time - in_time) as time_col
from Employees) e
group by event_day, emp_id