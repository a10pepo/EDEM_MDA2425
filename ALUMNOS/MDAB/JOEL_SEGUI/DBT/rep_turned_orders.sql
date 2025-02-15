--Create a report “rep_returned_orders” to show the orders returned, the report should include the following columns: order_id - customer_id - 
--order_date - status - first_name last_name - amount. 

WITH returned_orders AS (
    SELECT 
        o.id AS order_id,
        o.user_id AS customer_id,
        o.order_date,
        o.status
    FROM {{ ref('orders') }} o
    WHERE o.status = 'returned'
)
SELECT 
    ro.order_id,
    c.id AS customer_id,
    ro.order_date, 
    ro.status,
    c.first_name,
    c.last_name,
    p.amount
FROM returned_orders ro
JOIN {{ ref('customers') }} c ON ro.customer_id = c.id
JOIN {{ ref('payments') }} p ON ro.order_id = p.orderid;



