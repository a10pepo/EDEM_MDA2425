CREATE STREAM cultivos_valencia (id INT, ano INT, cultivo STRING, superficie_cultivada_hectareas INT) 
WITH (KAFKA_TOPIC='cultivos', VALUE_FORMAT='JSON');

SELECT cultivo
FROM cultivos_valencia
WHERE cultivo LIKE 'p%' emit changes;