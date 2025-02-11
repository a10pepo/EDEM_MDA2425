{{ config(materialized='view' )}}

SELECT
publish_time,
message_id,
CAST(JSON_VALUE(data, '$.delivery_status') AS STRING) AS delivery_status,
CAST(JSON_VALUE(data, '$.event_at') AS TIMESTAMP) AS event_at,
CAST(JSON_VALUE(data, '$.order_id') AS INT64) AS order_id
FROM {{ ref('base_raw_events_delivery') }}



