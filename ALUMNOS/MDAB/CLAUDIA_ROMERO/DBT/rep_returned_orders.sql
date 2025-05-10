WITH orders AS (
    SELECT 
        order_id,
        customer_id,
        order_date,
        status
    FROM {{ ref('stg_orders') }}
    WHERE status = 'returned'
),

customers AS (
    SELECT 
        customer_id,
        first_name,
        last_name
    FROM {{ ref('stg_customers') }}
),

payments AS (
    SELECT 
        order_id,
        SUM(CASE WHEN status = 'success' THEN amount END) AS amount
    FROM {{ ref('stg_payments') }}
    GROUP BY order_id
)

SELECT 
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    c.first_name,
    c.last_name,
    p.amount
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.customer_id
LEFT JOIN payments AS p ON o.order_id = p.order_id