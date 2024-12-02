WITH customer_details AS (
    SELECT
        id as customer_id,
        first_name,
        last_name
    FROM {{ source('jaffle_shop', 'customers') }}
),

stg_orders as (SELECT
        id as order_id,
        user_id as customer_id,
        order_date,
        status
    FROM {{ source('jaffle_shop', 'orders') }}
),

stg_payments as (
    SELECT
        id as payment_id,
        orderid as order_id,
        paymentmethod as payment_method,
        status,
        {{ cents_to_dollars('amount') }} as amount,
        created as created_at
    FROM {{ source('jaffle_shop', 'payments') }}
),

returned_orders as (SELECT
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status,
        c.first_name,
        c.last_name,
        p.amount
    from stg_orders o
    join customer_details c on o.customer_id = c.customer_id
    join stg_payments p on o.order_id = p.order_id
    where o.status = 'returned'
)

SELECT order_id, customer_id, order_date, status, first_name, last_name, amount
FROM returned_orders
