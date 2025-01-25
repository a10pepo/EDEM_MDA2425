WITH returned_orders AS (
    SELECT 
        o.order_id,
        o.customer_id,
        o.order_date,
        o.status AS order_status,
        p.payment_method,
        p.amount  
    FROM 
        {{ ref('stg_orders') }} o
    JOIN 
        {{ ref('stg_payments') }} p ON o.order_id = p.order_id
    WHERE 
        o.status = 'returned'  
)

SELECT
    ro.order_id,
    ro.customer_id,
    ro.order_date,
    ro.payment_method,
    ro.order_status,
    ro.amount,  
    c.first_name, 
    c.last_name  
FROM 
    returned_orders ro
JOIN 
    {{ ref('stg_customers') }} c ON ro.customer_id = c.customer_id 
ORDER BY 
    ro.order_date DESC