with orders as (
    select * from {{ref('stg_orders')}}
),
payments as (
    select * from {{ref('stg_payments')}}
),
customers as (
    select * from {{ref('stg_customers')}}
),
orders_ret as (
    select *
    from orders
    where status='returned'
),
orders_payments as (
    select 
        orders_ret.order_id,
        orders_ret.customer_id,
        orders_ret.order_date,
        orders_ret.status,
        payments.amount
    from orders_ret
    left join payments using (order_id)

),
final as (
    select
        orders_payments.order_id,
        orders_payments.customer_id,
        orders_payments.order_date,
        orders_payments.status,
        orders_payments.amount,
        customers.first_name,
        customers.last_name
    from orders_payments
    left join customers using (customer_id)
)
select * from final
