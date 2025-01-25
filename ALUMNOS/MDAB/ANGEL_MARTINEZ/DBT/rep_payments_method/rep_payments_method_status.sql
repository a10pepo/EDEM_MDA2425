SELECT 
    payments.paymentmethod,
    sum(case when status ='success' then 1 end) as success,
    sum(case when status ='fail' then 1 end) as failed
FROM 
    {{ref('payments')}}

GROUP BY 
    payments.paymentmethod 
