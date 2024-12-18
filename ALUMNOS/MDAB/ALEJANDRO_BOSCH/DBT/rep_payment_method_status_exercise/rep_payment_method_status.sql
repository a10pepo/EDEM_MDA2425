WITH payments_status AS (
    SELECT
        payments.paymentmethod,
        COUNT(CASE WHEN status = 'success' THEN 1 END) AS success,
        COUNT(CASE WHEN status = 'fail' THEN 1 END) AS failed
    FROM {{ ref('payments') }}

    GROUP BY payments.paymentmethod
)

SELECT * 
FROM payments_status