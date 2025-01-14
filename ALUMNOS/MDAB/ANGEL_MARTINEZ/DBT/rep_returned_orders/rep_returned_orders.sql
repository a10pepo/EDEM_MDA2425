select
    orders.id as order_id,
    orders.user_id as customer_id,
    orders.order_date,
    orders.status,
    customers.first_name,
    customers.last_name,
    ROUND(payments.amount / 100.0) as payments_amount 
from {{ ref('orders') }} as orders
left join {{ ref('customers') }} as customers
    on orders.user_id = customers.id
left join {{ ref('payments') }} as payments
    on orders.id = payments.orderid
where orders.status = 'returned'
