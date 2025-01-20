WITH payment_status AS (
    SELECT 
        p.payment_method,
        COUNT(o.order_id) AS total_orders, 
        SUM(p.amount) AS total_amount 
    FROM 
        {{ ref('stg_orders') }} o
    JOIN 
        {{ ref('stg_payments') }} p ON o.order_id = p.order_id
    WHERE 
        o.status = 'completed' 
    GROUP BY 
        p.payment_method
)

SELECT 
    payment_method,
    total_orders,
    total_amount
FROM 
    payment_status
ORDER BY 
    total_amount DESC