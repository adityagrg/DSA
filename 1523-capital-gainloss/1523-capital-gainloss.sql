# Write your MySQL query statement below
select stock_name, sum(total) as capital_gain_loss
from
(select stock_name,
case when operation = "Buy" then (0-total)
else total
end
as total
from
(select stock_name, operation, sum(price) as total
from Stocks
group by stock_name, operation) e) f
group by stock_name;