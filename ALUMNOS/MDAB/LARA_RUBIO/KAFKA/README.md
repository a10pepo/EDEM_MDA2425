# Kafka Workflow

## Introducción
Esta aplicación se enfoca en el procesamiento y análisis de datos en tiempo real utilizando Apache Kafka y KSQL. Para este proyecto, empleamos un dataset de Netflix que incluye información detallada sobre películas y programas de televisión.

---

## Pasos Realizados

### 1. Obtención de los Datos
El dataset de Netflix contiene diversos atributos sobre los títulos, entre ellos:
- **title**: Nombre del título.
- **type**: Categoría del contenido ("Movie" o "TV Show").
- **country**: País de origen.
- Otros datos como director, reparto, calificación, duración, etc.

El archivo en formato CSV fue convertido a mensajes JSON y enviado a un tema de Kafka para su posterior procesamiento.

---

### 2. Consumo y Clasificación de Datos
Un consumidor desarrollado en Python con la librería `confluent-kafka` realiza las siguientes tareas:
- **Lee los datos del tema Kafka llamado `netflix`**.
- **Clasifica los datos**:
  - Los títulos con `type = "Movie"` se envían al tema `movies`.
  - Los títulos con `type = "TV Show"` se envían al tema `tv_shows`.
- Escribe los datos clasificados en los temas correspondientes para etapas de procesamiento adicionales.

---

### 3. Creación de la Tabla en KSQL
Con KSQL, generamos un flujo y una tabla para realizar análisis sobre los datos del tema `tv_shows`.

#### Definición del Stream
Creamos un stream para estructurar los datos provenientes del tema `tv_shows`:
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
Creamos una tabla que agrupa los datos por país y calcula el número de títulos por país:
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

### 4. Consultas en KSQL
Finalmente, consultamos la tabla `shows_by_country` para obtener la cantidad de títulos agrupados por país:
```sql
SELECT * FROM shows_by_country EMIT CHANGES;
```

#### Ejemplo de Resultados
| País            | Número de Shows |
|-----------------|-----------------|
| United States   | 10              |
| India           | 5               |
| South Africa    | 3               |

---

## Conclusión
Este proyecto ilustra cómo usar Kafka y KSQL para procesar y analizar datos en tiempo real. A través de este flujo:
- Clasificamos un dataset en categorías específicas.
- Creamos tablas y streams en KSQL para realizar agregaciones.
- Generamos insights como el número de títulos por país.

El enfoque es escalable y adaptable a otros flujos de procesamiento de datos en tiempo real.
