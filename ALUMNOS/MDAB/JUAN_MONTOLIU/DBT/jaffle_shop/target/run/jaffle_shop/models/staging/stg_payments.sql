
  create view "dbt"."dev"."stg_payments__dbt_tmp"
    
    
  as (
    select
    id as payment_id,
    orderid as order_id,
    paymentmethod as payment_method,
    status,
    -- amount is stored in cents, convert it to dollars
    
    (amount / 100)::numeric(16, 2)
 as amount,
    created as created_at
from "dbt"."dev_data"."payments"
  );