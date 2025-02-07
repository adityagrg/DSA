# Write your MySQL query statement below
-- select distinct num as ConsecutiveNums
-- from
-- (select num,
--     sum(is_true) as summ
-- from
-- (select l1.num,
--     case
--         when num = lag_1
--         and num = lag_2
--     then 1
--     else 0
--     end as is_true
-- from
-- (select id, num, lag(num, 1) over (order by id) as lag_1, lag(num, 2) over (order by id) as lag_2
-- from Logs) l1) l2
-- having summ > 0) as l3
-- having count(distinct num) > 0



-- select num,
--     sum(is_true) as summ
-- from
-- (select l1.num,
--     case
--         when num = lag_1
--         and num = lag_2
--     then 1
--     else 0
--     end as is_true
-- from
-- (select id, num, lag(num, 1) over (order by id) as lag_1, lag(num, 2) over (order by id) as lag_2
-- from Logs) l1) l2
-- having summ > 0


-- select num,
--     sum(is_true) as summ
-- from
-- (select l1.num,
--     case
--         when num = lag_1
--         and num = lag_2
--     then 1
--     else 0
--     end as is_true
-- from
-- (select id, num, lag(num, 1) over (order by id) as lag_1, lag(num, 2) over (order by id) as lag_2
-- from Logs) l1) l2



-- select num,
--     sum(is_true) as summ
-- from
-- (select l1.num,
--     case
--         when num = lag_1
--         and num = lag_2
--     then 1
--     else 0
--     end as is_true
-- from
-- (select id, num, lag(num, 1) over (order by id) as lag_1, lag(num, 2) over (order by id) as lag_2
-- from Logs) l1) l2


-- select l1.num,
--     case
--         when num = lag_1
--         and num = lag_2
--     then 1
--     else 0
--     end as is_true
-- from
-- (select id, num, lag(num, 1) over (order by id) as lag_1, lag(num, 2) over (order by id) as lag_2
-- from Logs) l1

-- select num as ConsecutiveNums
-- from
-- (select l1.num
-- from
-- Logs l1
-- join Logs l2
-- on l1.num = l2.num
-- and l1.id <> l2.id) t1
-- group by num
-- having count(num) > 1;
select distinct ConsecutiveNums
from
(
select
case when num = lead1 and num = lead2 then num
end as ConsecutiveNums
from
(select id, num,
lead(num) over (order by id) as lead1,
lead(num, 2) over (order by id) as lead2
from Logs) e
) f
where ConsecutiveNums is not null;