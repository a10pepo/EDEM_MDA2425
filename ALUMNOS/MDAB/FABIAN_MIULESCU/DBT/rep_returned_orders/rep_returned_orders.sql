with orders_returned AS (
    SELECT
        o.id,
        o.user_id,
        o.order_date,
        o.status,
        c.first_name,
        c.last_name,
        p.amount/100 AS amount
    FROM {{ref("orders")}} o
    LEFT JOIN {{ref("customers")}} c ON o.user_id = c.id
    LEFT JOIN {{ref("payments")}} p ON o.id = p.orderid
    WHERE o.status = 'returned'  
)

SELECT *
FROM orders_returned
