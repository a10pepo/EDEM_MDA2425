CREATE STREAM processed_orders_stream (
   order_id INT,
   product STRING,
   quantity INT,
   price DOUBLE,
   timestamp BIGINT,
   status STRING
) WITH (
   KAFKA_TOPIC='processed_orders',
   VALUE_FORMAT='JSON'
);
