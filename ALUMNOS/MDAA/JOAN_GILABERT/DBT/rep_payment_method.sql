with payments as(
    select  * from {{ref('stg_payments')}}
),

final as(
    select
        payment_method,
        count(case when status = 'success' then 1 end) as success,
        count(case when status = 'fail' then 1 end ) as fail
    from payments
    group by payment_method
    
)

select * from final
