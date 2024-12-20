select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      with payments as (
    select
        *
    from
        "dbt"."dev"."stg_payments"
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
      
    ) dbt_internal_test