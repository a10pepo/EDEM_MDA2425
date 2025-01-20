with orders_returned as (
   SELECT
      o.id AS order_id,
      c.id AS customer_id,
      o.order_date, 
      o.status,
      c.first_name,
      c.last_name,
      p.amount
   FROM {{ ref('orders') }} o
   JOIN {{ ref('customers') }} c ON o.user_id = c.id
   JOIN {{ ref('payments') }} p ON o.id = p.orderid
   WHERE o.status = 'returned'
)

select *
from orders_returned

