CREATE TABLE IF NOT EXISTS analytics_db.customers (
    id UInt32,
    customer_name String,
    email String
) ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE IF NOT EXISTS analytics_db.products (
    id UInt32,
    product_name String,
    price Float32
) ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE IF NOT EXISTS analytics_db.orders (
    id UInt32,
    customer_id UInt32,
    created_at DateTime,
    total_price Float32
) ENGINE = MergeTree()
ORDER BY id;

CREATE TABLE IF NOT EXISTS analytics_db.order_products (
    order_id UInt32,
    product_id UInt32,
    quantity UInt32,
    price Float32
) ENGINE = MergeTree()
ORDER BY (order_id, product_id);

CREATE TABLE IF NOT EXISTS analytics_db.delivery_events (
    order_id UInt32,
    delivery_status String,
    event_at DateTime,
) ENGINE = MergeTree()
ORDER BY order_id;
