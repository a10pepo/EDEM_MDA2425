with payment_status as (

    select
        payment_method,
        -- Calcula el total de pagos exitosos
        sum(case when status = 'success' then amount else 0 end) as success,
        -- Calcula el total de pagos fallidos
        sum(case when status = 'failed' then amount else 0 end) as failed
    from {{ ref('stg_payments') }}  -- Hace referencia a la tabla de pagos en staging
    group by payment_method

)

select * from payment_status
