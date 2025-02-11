{{ config(materialized='ephemeral' )}}

SELECT
id,
product_name,
price
FROM {{ source('orders_bronze', 'products')}}