# Write your MySQL query statement below
select case when count(salary) >= 1
then salary
else null
end as SecondHighestSalary
from
(select distinct salary
from Employee
order by salary desc
limit 1 offset 1) e;