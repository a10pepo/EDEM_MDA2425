{{ config(materialized='ephemeral' )}}

SELECT
publish_time,
data,
message_id
FROM {{ source('delivery', 'raw_events_delivery') }}