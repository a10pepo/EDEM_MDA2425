with returned_orders as (
    select
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status
    from "dbt"."dev"."stg_orders" o
    where o.status = 'returned'  -- Filtra solo las órdenes devueltas
),

payment_details as (
    select
        p.order_id,
        sum(case when p.status = 'success' then p.amount else 0 end) as amount
    from "dbt"."dev"."stg_payments" p
    group by p.order_id
),

final_report as (
    select
        ro.order_id,
        ro.customer_id,
        ro.order_date,
        ro.status,
        c.first_name,
        c.last_name,
        pd.amount
    from returned_orders ro
    left join "dbt"."dev"."stg_customers" c
        on ro.customer_id = c.customer_id
    left join payment_details pd
        on ro.order_id = pd.order_id
)

select * from final_report