# Write your MySQL query statement below

select e.user_id as buyer_id, e.join_date, coalesce(f.orders_in_2019, 0) as orders_in_2019
from Users e
left join
(select buyer_id, count(*) as orders_in_2019
from Orders
where year(order_date) = 2019
group by buyer_id) f
on e.user_id = f.buyer_id;