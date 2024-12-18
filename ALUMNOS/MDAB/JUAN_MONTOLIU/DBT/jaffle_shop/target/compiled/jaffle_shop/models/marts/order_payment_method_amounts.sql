

select
    order_id,
    
    sum(case when payment_method = 'bank_transfer' then amount end) as bank_transfer_amount,
    
    sum(case when payment_method = 'credit_card' then amount end) as credit_card_amount,
    
    sum(case when payment_method = 'gift_card' then amount end) as gift_card_amount,
    
    sum(amount) as total_amount
from "dbt"."dev"."stg_payments"
group by order_id