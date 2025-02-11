{{ config(materialized='ephemeral' )}}

SELECT
order_id,
product_id,
quantity,
price
FROM {{ source('orders_bronze', 'order_products')}}