# Write your MySQL query statement below
select u.name, t.balance
from
(select account, sum(amount) as balance
from Transactions
group by account
having balance > 10000) t
join Users u
on t.account = u.account;