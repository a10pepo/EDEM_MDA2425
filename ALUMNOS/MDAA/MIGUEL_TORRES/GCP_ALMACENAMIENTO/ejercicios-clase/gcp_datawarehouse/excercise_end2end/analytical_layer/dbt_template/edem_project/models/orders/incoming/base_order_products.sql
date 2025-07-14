{{ config(materialized='ephemeral' )}}

SELECT
order_id,
product_id,
quantity,
price
FROM {{ source('orders', 'order_products')}}