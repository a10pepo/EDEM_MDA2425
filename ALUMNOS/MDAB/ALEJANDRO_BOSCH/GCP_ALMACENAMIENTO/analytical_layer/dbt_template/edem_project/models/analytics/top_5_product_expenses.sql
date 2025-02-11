{{ config(materialized='table') }}


SELECT
    SUM(op.price*op.quantity) AS total_product_spent,
    product_name
    FROM
    {{ ref('base_orders') }} o
    LEFT JOIN
    {{ ref('base_order_products')}} op
    ON
    o.id = op.order_id
    LEFT JOIN
    {{ ref('base_products') }} p
    ON
    op.product_id = p.id
    GROUP BY
    product_name
    ORDER BY
    SUM(op.price*op.quantity) DESC
    LIMIT
    5