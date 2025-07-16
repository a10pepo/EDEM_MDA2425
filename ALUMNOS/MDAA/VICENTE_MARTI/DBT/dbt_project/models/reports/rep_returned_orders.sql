{{ config(materialized='table') }}

SELECT
    o.order_id,
    o.customer_id,
    o.order_date,
    o.status,
    c.first_name,
    c.last_name,
    p.amount
FROM public.orders o
JOIN public.customers c
  ON o.customer_id = c.customer_id
LEFT JOIN public.payments p
  ON o.order_id = p.orderid
WHERE o.status = 'returned'
ORDER BY o.order_id
