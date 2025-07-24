# Análisis Disney+ con PySpark - EDEM MDA 2324

Análisis simple y efectivo del catálogo de Disney+ usando PySpark para procesar datos de películas y series.

## 📁 Estructura
```
PYSPARK/
├── Docker/
│   └── docker-compose.yml
├── disney-plus-analysis.py
├── Data/
│   └── disney_plus_titles.csv
├── results/           # Resultados generados
└── README.md
```

## 🚀 Ejecución

1. **Levantar Spark:**
```bash
cd Docker/
docker-compose up -d
```

2. **Ejecutar análisis:**
```bash
docker exec -it spark-master bash /spark/bin/spark-submit \
  --master local[*] \
  /opt/project/disney-plus-analysis.py
```

## 📊 Análisis Realizados

- **Distribución de contenido**: Movies vs TV Shows
- **Top géneros**: Los 10 más populares  
- **Análisis temporal**: Contenido por década de lanzamiento
- **Geografía**: Top 10 países productores
- **Duración películas**: Estadísticas (min, max, promedio)
- **Directores**: Top 10 con más contenido
- **Audiencia**: Clasificación Kids, Family, Teen

## 🎯 Transformaciones PySpark

- **`split()`**: Separar géneros y países múltiples
- **`regexp_extract()`**: Extraer minutos de duración  
- **`when().otherwise()`**: Clasificar por audiencia
- **`groupBy().agg()`**: Agregaciones y estadísticas
- **`filter()`**: Filtrado de datos nulos
- **Casting**: Conversión de tipos de datos

## 📈 Resultados

Los análisis se guardan como CSV en `/results/`:
- `content_by_type/`
- `top_genres/` 
- `content_by_decade/`
- `top_countries/`
- `movie_duration_stats/`
- `top_directors/`
- `content_by_audience/`

## 🛠️ Tecnologías
- **PySpark 3.5**: Procesamiento distribuido
- **Docker**: Entorno de ejecución
- **Spark SQL**: Transformaciones y agregaciones

---
*Proyecto EDEM MDA 2324 - Análisis eficiente de big data con PySpark*