{{ config(materialized='ephemeral' )}}

SELECT
id,
customer_name,
email
FROM {{ source('orders_bronze', 'customers')}}