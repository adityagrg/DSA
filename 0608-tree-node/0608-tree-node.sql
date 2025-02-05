# Write your MySQL query statement below
select Tree.id,
case when Tree.p_id is null then "Root"
else coalesce(e.type, "Leaf") end as type
from
Tree
left join
(select distinct(p_id), "Inner" as type
from Tree) e
on Tree.id = e.p_id;