WITH payment_status AS (
    select
        payment_method,
        status,
        sum(amount) as total_amount
    FROM {{ ref('stg_payments') }}
    GROUP BY
        payment_method,
        status
)


SELECT
    payment_method,
    sum(CASE WHEN status = 'success' THEN total_amount ELSE 0 END) AS success,
    sum(CASE WHEN status = 'failed' THEN total_amount ELSE 0 END) AS failed
FROM payment_status
GROUP BY payment_method
