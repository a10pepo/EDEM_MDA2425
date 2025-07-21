  SELECT
      o.order_id,
      o.customer_id,
      o.order_date,
      o.status,
      c.first_name,
      c.last_name,
      o.amount
  FROM
      orders o
      JOIN customers c ON o.customer_id = c.customer_id
  WHERE
      o.status = 'returned'
  ORDER BY
      o.order_date DESC;