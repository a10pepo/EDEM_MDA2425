with orders_returned as (
    select
        orders.id as order_id,
        orders.user_id as customer_id,
        orders.order_date,
        orders.status as order_status,
        customers.first_name as customer_first_name,
        customers.last_name as customer_last_name,
        payments.amount / 100.0 as payment_amount
    from {{ ref('orders') }} as orders
    left join {{ ref('customers') }} as customers
        on orders.user_id = customers.id
    left join {{ ref('payments') }} as payments
        on orders.id = payments.orderid
    where orders.status = 'returned'
)

select *
from orders_returned