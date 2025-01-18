
  create view "dbt"."dev"."stg_orders__dbt_tmp"
    
    
  as (
    select
    id as order_id,
    user_id as customer_id,
    order_date,
    status
from 
    "dbt"."dev_data"."orders"
  );