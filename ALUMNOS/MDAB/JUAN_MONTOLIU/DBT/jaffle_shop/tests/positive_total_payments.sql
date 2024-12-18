with payments as (
    select
        *
    from
        {{ ref ('stg_payments') }}
),

test_data as (
    select
        order_id,
        sum(amount) as total_amount
    from payments
    group by order_id
)

select *
from
    test_data
where
    total_amount < 0
