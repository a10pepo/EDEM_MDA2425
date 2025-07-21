{{ config(materialized='ephemeral' )}}

SELECT
id,
customer_id,
created_at,
total_price
FROM {{ source('orders', 'orders')}}