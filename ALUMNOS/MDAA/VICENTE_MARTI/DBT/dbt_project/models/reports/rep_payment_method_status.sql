{{ config(materialized='table') }}

SELECT
    paymentmethod,    
    status,
    SUM(amount) AS total_amount
FROM public.payments
GROUP BY paymentmethod, status
ORDER BY paymentmethod, status
