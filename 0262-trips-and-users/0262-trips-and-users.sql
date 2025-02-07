# Write your MySQL query statement below
select request_at as Day,
ROUND(
        SUM(CASE WHEN status IN ('cancelled_by_driver', 'cancelled_by_client') THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS 'Cancellation Rate'
from
(
    with e as
    (
        select users_id from Users
        where banned = "Yes"
    )
    select *
    from Trips
    where 
    client_id not in (select users_id from e)
    and driver_id not in (select users_id from e)
) f
where request_at between '2013-10-01' AND '2013-10-03'
group by request_at