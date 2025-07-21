  SELECT
      payment_method,
      status,
      SUM(amount) AS total_amount
  FROM
      orders
  GROUP BY
      payment_method, status
  ORDER BY
      payment_method, status;