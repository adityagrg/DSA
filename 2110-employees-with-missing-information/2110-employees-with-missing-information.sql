# Write your MySQL query statement below
-- with u
-- as (select distinct e.employee_id 
-- from Employees e 
-- cross join Salaries s)
-- select e.employee_id
-- from Employees e
-- cross join Salaries
-- where e.employee_id not in (select employee_id from u);


SELECT e.employee_id
FROM Employees e
LEFT JOIN Salaries s ON e.employee_id = s.employee_id
WHERE SALARY IS NULL

UNION

SELECT s.employee_id
FROM Salaries s
LEFT JOIN EMPLOYEES e ON e.employee_id = s.employee_id
WHERE NAME IS NULL

ORDER BY employee_id;