
  create view "dbt"."dev"."stg_customers__dbt_tmp"
    
    
  as (
    select
   id as customer_id,
   first_name,
   last_name
from
   "dbt"."dev_data"."customers"
  );