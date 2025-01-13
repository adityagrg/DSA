# Write your MySQL query statement below

-- Both the below solutions work

-- select name
-- from SalesPerson
-- where sales_id not in
-- (select o.sales_id
-- from Orders o
-- join Company c
-- on c.com_id = o.com_id
-- where c.name = "RED")

-- OR

select name
from SalesPerson
where sales_id not in
(select sales_id from Orders
where com_id =
(select com_id from Company where name = "RED"))