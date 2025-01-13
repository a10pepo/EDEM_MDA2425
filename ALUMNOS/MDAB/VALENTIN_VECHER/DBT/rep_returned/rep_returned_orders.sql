with orders_returned as (
    select
        o.id,
        o.user_id,
        o.order_date,
        o.status,
        c.first_name,
        c.last_name,
        p.amount/100 as amount 
    from {{ref("orders")}} o 
    left join {{ref("customers")}} c on o.user_id = c.id 
    left join {{ref("payments")}} p on o.id = p.orderid
    where o.status = 'returned'
)

select *
from orders_returned