{{ config(materialized='table') }}

SELECT
    SUM(total_price) AS total_price,
    c.customer_name
    FROM
    {{ ref('base_orders') }} o
    LEFT JOIN
    {{ ref('base_customers') }} c
    ON
    c.id = o.customer_id
    GROUP BY
    customer_name
    ORDER BY
    total_price desc