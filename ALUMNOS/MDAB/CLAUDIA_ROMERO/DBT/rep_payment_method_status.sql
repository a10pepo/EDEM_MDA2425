WITH payment_status AS (
    SELECT
        payment_method,
        SUM(amount) AS total_amount,
        status
    FROM {{ ref('stg_payments') }}
    GROUP BY payment_method, status
)

SELECT
    payment_method,
    SUM(CASE WHEN status = 'success' THEN total_amount ELSE 0 END) AS success,
    SUM(CASE WHEN status = 'failed' THEN total_amount ELSE 0 END) AS failed
FROM payment_status
GROUP BY payment_method


