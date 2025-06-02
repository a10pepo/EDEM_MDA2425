CREATE STREAM temperature_readings (
    sensor_id VARCHAR,
    location VARCHAR,
    temperature DOUBLE,
    timestamp VARCHAR,
    status VARCHAR
) WITH (
    kafka_topic = 'processed_temperatures',
    value_format = 'JSON'
);

CREATE STREAM temperature_analytics AS
SELECT 
    location,
    COUNT(*) as reading_count,
    AVG(temperature) as avg_temperature,
    MIN(temperature) as min_temperature,
    MAX(temperature) as max_temperature,
    LATEST_BY_OFFSET(timestamp) as last_reading_time
FROM temperature_readings 
WINDOW TUMBLING (SIZE 1 MINUTE)
GROUP BY location
EMIT CHANGES;

-- querys
SELECT * FROM TEMPERATURE_ANALYTICS EMIT CHANGES;