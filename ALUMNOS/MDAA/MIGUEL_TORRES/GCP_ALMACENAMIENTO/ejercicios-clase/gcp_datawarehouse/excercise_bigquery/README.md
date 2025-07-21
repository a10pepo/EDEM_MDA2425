# GCP BIGQUERY EXERCISE

## Introduction

In this excercise, we will use the `public datasets` of bigquery to test the different capabilities of the tool.

You can check the public datasets available in BigQuery [here](https://console.cloud.google.com/marketplace/browse?filter=solution-type:dataset&hl=es-419&inv=1&invt=AbnQ3w).

In particular, we will check:

- **Table partitioning**: We will query a partitioned table to see how we can save costs by querying only the partitions we need.

- **Table clustering**: We will query a clustered table to see how we can save costs by querying only the columns we need.

- **Slots used**: We will check how many slots are used by a query and how we can optimize the query to use less slots.


## Etherium dataset

We will focus in the [ethereum dataset](https://console.cloud.google.com/marketplace/product/bigquery-public-data/blockchain-analytics-ethereum-mainnet-us). This dataset contains the historical data of the Ethereum blockchain. We will make a few queries to test the capabilities of BigQuery.


### Table partitioning + aggregation

The first query will show you how we can save costs by querying only the partitions we need.

```sql
SELECT 
    DATE(block_timestamp) AS transaction_date, 
    COUNT(*) AS transaction_count
FROM `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions`
WHERE block_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY) -- Partitioned table by block_timestamp show only the last 7 days
GROUP BY transaction_date
ORDER BY transaction_date DESC;
```

## Query with JOIN of two tables

The second query will show you how to join two tables to get the information you need.

The initial query that we will use is the following:

```sql
SELECT
  t.block_hash AS transaction_hash,
  t.block_number,
  b.miner,
  b.difficulty,
  t.from_address,
  t.to_address,
  t.value,
  t.block_timestamp
FROM
  `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions` AS t
JOIN
  `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks` AS b
USING
  (block_number)
WHERE
  DATE(t.block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 DAY)
ORDER BY
  t.block_timestamp DESC
```

However, this query can be further optimized by filtering the data of the tables before joining them. This can be used by encapsulating both tables with CTEs (Common Table Expression) and then joining them.

```sql
WITH
  base_transactions AS (
  SELECT
    block_hash,
    block_number,
    from_address,
    to_address,
    value,
    block_timestamp
  FROM
    `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions`
  WHERE
    DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 day) ),
  base_blocks AS(
  SELECT
    miner,
    difficulty,
    block_number,
    block_timestamp
  FROM
    `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks`
  WHERE
    DATE(block_timestamp) >= DATE_SUB(CURRENT_DATE(), INTERVAL 3 day) )
SELECT
  t.block_hash AS transaction_hash,
  t.block_number,
  b.miner,
  b.difficulty,
  t.from_address,
  t.to_address,
  t.value
FROM
  base_transactions AS t
JOIN
  base_blocks AS b
USING
  (block_number)
ORDER BY
  b.block_timestamp desc
```

If we now check both execution details, we will see that the second query uses less slots than the first one.


### Query with JOIN + aggregation

The third query will show you how to join two tables and then aggregate the data.

```sql
SELECT
  b.miner AS miner_address,
  COUNT(t.block_hash) AS total_transactions,
  SUM(t.value) / 1e18 AS total_eth_transacted
FROM
  `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.transactions` AS t
JOIN
  `bigquery-public-data.goog_blockchain_ethereum_mainnet_us.blocks` AS b
USING
  (block_number)
WHERE
  t.block_timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 7 DAY)
GROUP BY
  miner_address
ORDER BY
  total_eth_transacted DESC
LIMIT
  10;
```

Can you try to optimize this query by filtering the data of the tables before joining them?