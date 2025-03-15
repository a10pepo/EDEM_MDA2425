CREATE STREAM processed_orders_stream (
    order_id VARCHAR,
    customer_id VARCHAR,
    restaurant VARCHAR,
    status VARCHAR,
    updated_time VARCHAR,
    driver VARCHAR
) WITH (KAFKA_TOPIC='processed_orders', VALUE_FORMAT='JSON');