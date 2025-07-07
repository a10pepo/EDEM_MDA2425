ksql http://kafka-ksql-server-1:8088 <<EOF
CREATE STREAM retail_stream (
  invoice_no   VARCHAR,
  stock_code   VARCHAR,
  description  VARCHAR,
  quantity     INT,
  invoice_date VARCHAR,
  unit_price   DOUBLE,
  customer_id  INT,
  country      VARCHAR
) WITH (
  KAFKA_TOPIC='retail',
  VALUE_FORMAT='JSON'
);

SELECT
  country,
  COUNT(*) AS transaction_count
FROM retail_stream
GROUP BY country
EMIT CHANGES;

SELECT
  country,
  SUM(quantity * unit_price) AS total_revenue
FROM retail_stream
GROUP BY country
EMIT CHANGES;

SELECT
  country,
  AVG(unit_price) AS avg_unit_price
FROM retail_stream
GROUP BY country
EMIT CHANGES;

SELECT
  WINDOWSTART AS window_start,
  SUM(quantity * unit_price) AS daily_revenue
FROM retail_stream
WINDOW TUMBLING (SIZE 1 DAYS)
GROUP BY WINDOWSTART
EMIT CHANGES;

CREATE TABLE top_customers AS
  SELECT
    customer_id,
    SUM(quantity * unit_price) AS total_spent
  FROM retail_stream
  WHERE customer_id IS NOT NULL
  GROUP BY customer_id
  EMIT CHANGES;

SELECT * FROM top_customers
EMIT CHANGES;
EOF