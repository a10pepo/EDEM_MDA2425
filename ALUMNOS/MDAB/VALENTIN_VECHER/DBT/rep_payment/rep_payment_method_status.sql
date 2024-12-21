SELECT 
    payments.paymentmethod,
    SUM(case when status ='success' then amount else 0 end) as success,
    sum(case when status ='failed' then amount else 0 end) as failed
from 
    {{ref('payments')}}

group by 
    payments.paymentmethod 