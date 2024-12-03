WITH orders_returned AS (
    SELECT
        o.id AS order_id,
        o.user_id AS customer_id,
        o.order_date,
        o.status,
        c.first_name,
        c.last_name,
        p.amount
    FROM {{ ref('orders') }} o
    LEFT JOIN {{ ref('customers') }} c ON o.user_id = c.id
    LEFT JOIN {{ ref('payments') }} p ON o.id = p.orderid
    WHERE o.status = 'returned'
)

SELECT *
FROM orders_returned
