-- Querys usadas en KSQL

--Crear table

CREATE STREAM imdb_300_stream (
    titulo VARCHAR,
    rating DOUBLE,
    genero VARCHAR,
    director VARCHAR,
    actores ARRAY<VARCHAR>
) WITH (
    KAFKA_TOPIC='imdb',
    VALUE_FORMAT='JSON'
);

-- Querys
SELECT genero, COUNT(*) AS cantidad_peliculas
FROM imdb_300_stream
GROUP BY genero
EMIT CHANGES

SELECT genero, AVG(rating) AS promedio_rating
FROM imdb_300_stream
GROUP BY genero
EMIT CHANGES;

SELECT genero, director, AVG(rating) AS promedio_rating
FROM imdb_300_stream
GROUP BY genero, director
HAVING AVG(rating) > 8.0
EMIT CHANGES;
