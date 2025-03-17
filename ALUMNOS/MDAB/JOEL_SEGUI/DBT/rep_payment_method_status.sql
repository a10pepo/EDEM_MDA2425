--Create a report “rep_payment_method_status.sql”, to calculate the total amount failed and success per each payment_method.
--Hint (the table should look like this): 

SELECT
    payments.paymentmethod,
    SUM(CASE WHEN status = 'success' THEN amount ELSE 0 END) AS success,
    SUM(CASE WHEN status = 'failed' THEN amount ELSE 0 END) AS failed
FROM {{ ref('payments') }}
GROUP BY payments.paymentmethod
ORDER BY payments.paymentmethod