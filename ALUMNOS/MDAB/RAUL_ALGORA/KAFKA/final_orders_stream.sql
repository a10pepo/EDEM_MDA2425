CREATE STREAM final_orders_stream WITH (KAFKA_TOPIC='final_orders', VALUE_FORMAT='JSON') AS
SELECT order_id, product, quantity, price, status, TIMESTAMPTOSTRING(timestamp, 'yyyy-MM-dd HH:mm:ss') AS order_time
FROM processed_orders_stream
WHERE price > 100;
