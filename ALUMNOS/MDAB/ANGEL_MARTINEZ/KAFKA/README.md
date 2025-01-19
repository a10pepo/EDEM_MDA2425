# Trabajo KAFKA

## Introducción
Esta aplicación consiste en el procesamiento de datos de Netflix donde en tiempo real cogemos un dataset de Netflix, lo sube a KAFKA a través del producer y el consumidor ejecutara su código para que se divida en dos topics distintos según sea película o serie.

---

## Pasos Realizados

### 1. **Obtención de los Datos**
Hemos utilizado el dataset de Netflix, que contiene información sobre títulos de películas y programas de TV, incluyendo atributos como:
- `title`: Nombre del título.
- `type`: Categoría ("Movie" o "TV Show").
- `country`: País de origen.
- Otros detalles como `director`, `cast`, `rating`, `duration`, etc.

El dataset fue procesado en formato CSV y luego enviado a Kafka como mensajes JSON.

---

### 2. **Consumo y Clasificación de Datos con un Consumidor**
Un script Python basado en la librería `confluent-kafka` actúa como consumidor de datos. Este script realiza las siguientes acciones:
- **Lee datos del tema Kafka `netflix`**.
- **Clasifica los datos**:
  - Los títulos con `type = "Movie"` se envían al tema `movies`.
  - Los títulos con `type = "TV Show"` se envían al tema `tv_shows`.
- Los datos clasificados se escriben en sus respectivos temas para procesamiento adicional.

---

### 3. **Creación de la Tabla en KSQL**
Usamos KSQL para crear un stream basado en el tema `tv_shows`. Posteriormente, creamos una tabla para realizar agregaciones sobre los datos.

#### Definición del Stream
```sql
CREATE STREAM tv_stream_shows (
    show_id STRING,
    type STRING,
    title STRING,
    director STRING,
    cast_members STRING,
    country STRING,
    date_added STRING,
    release_year INT,
    rating STRING,
    duration STRING,
    listed_in STRING
) WITH (
    KAFKA_TOPIC = 'tv_shows',
    VALUE_FORMAT = 'JSON'
);
```

#### Definición de la Tabla con Agregación por País
Creamos una tabla que agrupa los datos por país y cuenta el número de títulos por país. Además, cambiamos el nombre de la columna agregada a `numero_de_shows`:

```sql
CREATE TABLE shows_by_country AS
SELECT
    country,
    COUNT(*) AS numero_de_shows
FROM tv_stream_shows
GROUP BY country
EMIT CHANGES;
```

---

### 4. **Consultas en KSQL**
Finalmente, ejecutamos una consulta sobre la tabla creada para verificar los datos agrupados por país:

```sql
SELECT * FROM shows_by_country EMIT CHANGES;
```

