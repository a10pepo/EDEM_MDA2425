SELECT
    payments.paymentmethod,
    SUM(CASE WHEN status = 'success' THEN amount ELSE 0 END) AS success,
    SUM(CASE WHEN status = 'failed' THEN amount ELSE 0 END) AS failed
FROM
    {{ref('payments')}}
GROUP BY
    payments.paymentmethod