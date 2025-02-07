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
-- select distinct ConsecutiveNums
-- from
-- (
-- select
-- case when num = lead1 and num = lead2 then num
-- end as ConsecutiveNums
-- from
-- (select id, num,
-- lead(num) over (order by id) as lead1,
-- lead(num, 2) over (order by id) as lead2
-- from Logs) e
-- ) f
-- where ConsecutiveNums is not null;

-- SELECT DISTINCT num AS ConsecutiveNums
-- FROM (
--     SELECT num,
--            LEAD(num, 1) OVER (ORDER BY id) AS lead1,
--            LEAD(num, 2) OVER (ORDER BY id) AS lead2
--     FROM Logs
-- ) e
-- WHERE num = lead1 AND num = lead2;


with e as
(select l1.id as id1, l1.num, l2.id as id2
from Logs l1
join logs l2
on l1.num = l2.num
and l2.id - l1.id = 1)
select distinct e1.num as ConsecutiveNums from e e1
join e e2 on e1.num = e2.num
and e2.id2 - e1.id1 = 2