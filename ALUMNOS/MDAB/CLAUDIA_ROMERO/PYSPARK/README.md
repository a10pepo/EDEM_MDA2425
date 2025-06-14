# 🎧 Spotify Wrapped - PySpark Analysis

Este proyecto es una versión inspirada en **Spotify Wrapped**, donde se realiza un análisis de datos musicales reales utilizando **Apache Spark** y se almacenan los resultados en **MySQL** mediante Docker.

## 🚀 ¿Qué se analiza?

He analizado más de **27.000 canciones** para responder preguntas como:

- 🎶 ¿Qué género musical es el más popular?
- 🌟 ¿Cuántas canciones fueron super hits?
- 🎤 ¿Quién es tu artista más repetido?
- 🏆 ¿Cuáles son las canciones con más popularidad?
- ⏱️ ¿Cuántos minutos de música hay en total?

## 🔍 Resultados almacenados en MySQL

Estas son las tablas generadas:

| Tabla                  | Descripción                                         |
|------------------------|-----------------------------------------------------|
| `popularidad_generos`  | Popularidad media por grupo de género               |
| `nivel_exito_summary`  | Número de canciones clasificadas por éxito          |
| `top_canciones`        | Las canciones más populares                         |
| `top_artistas`         | Artistas con más canciones                          |
| `total_duracion`       | Total de minutos de música disponibles              |


## 💾 Cómo ejecutar

1. Levanta los contenedores:
```bash
docker-compose up --build -d
```

2. Ejecuta el script desde Spark:
```bash
docker exec -it spark-master bash
cd /opt/project/src
/spark/bin/spark-submit spotify_analysis_ext.py
```

3. Accede a Adminer en [http://localhost:8080](http://localhost:8080) con:
```
Servidor: mysql
Usuario: spark
Contraseña: password
Base de datos: pysparkdb
```


