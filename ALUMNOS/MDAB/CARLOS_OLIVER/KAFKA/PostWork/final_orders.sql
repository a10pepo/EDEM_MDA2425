CREATE STREAM final_orders_stream AS 
SELECT 
    order_id, 
    restaurant, 
    'Delivered' AS status, 
    TIMESTAMPTOSTRING(ROWTIME, 'yyyy-MM-dd HH:mm:ss') AS delivery_time 
FROM processed_orders_stream 
WHERE status = 'Out for Delivery';