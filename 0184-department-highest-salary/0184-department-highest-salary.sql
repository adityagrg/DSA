# Write your MySQL query statement below

select e.Employee, e.salary, d.name as Department
from
(select departmentId, name as Employee, salary,
dense_rank() over (partition by departmentId order by salary desc) as rankd
from Employee) e
join Department d
on e.departmentId = d.id
where e.rankd = 1;