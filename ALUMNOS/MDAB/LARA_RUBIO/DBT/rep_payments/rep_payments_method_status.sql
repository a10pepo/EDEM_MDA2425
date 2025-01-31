with orders_returned as (
SELECT 
    payments.paymentmethod,
    COUNT(case when status ='success' then 1 end) as success,
    COUNT(case when status ='fail' then 1 end) as failed
FROM 
    {{ref('payments')}}

GROUP BY 
    payments.paymentmethod 
)

select * from orders_returned