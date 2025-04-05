# Análisis IMDB con Spark

En este repositorio se encuentra el código para realizar el análisis de películas de IMDB usando Spark. El proyecto consiste en analizar los datos del conjunto de IMDB y almacenar los resultados en una base de datos MySQL.

## Ejecución del Proyecto

Para levantar los contenedores de Spark, entra en la carpeta docker y lanza el siguiente comando:
```sh
docker-compose up -d
```

### Ejecución en Terminal
Existen dos scripts disponibles dependiendo de si deseas almacenar los resultados en MySQL o simplemente visualizarlos por pantalla.

#### Visualización en pantalla
Para ejecutar el script que muestra los resultados directamente en la terminal, usa el siguiente comando:
```sh
bash /spark/bin/spark-submit --master local /opt/project/src/python/peliculas_IMDB.py
```

#### Almacenamiento en MySQL
Para ejecutar el script que guarda los resultados en MySQL, utiliza el siguiente comando:
```sh
docker exec -it spark-master /spark/bin/spark-submit --jars /opt/project/jar/mysql-connector-j-8.0.33.jar /opt/project/src/python/peliculas_IMDB_SQL.py
```

Los resultados se pueden visualizar directamente en la terminal al ejecutar el script de Spark:
```sh
bash /spark/bin/spark-submit --master local /opt/project/src/python/peliculas_IMDB.py
```

### Ejecución con MySQL
Si prefieres almacenar los resultados en la base de datos para consultarlos posteriormente, asegúrate de que el contenedor MySQL esté en ejecución y accesible desde el contenedor Spark. Los parámetros de conexión están configurados de la siguiente manera:
- Host: mysql
- Puerto: 8080
- Base de datos: pysparkdb
- Usuario: EDEM2425
- Contraseña: EDEM2425

## Descripción del Proyecto

1. **Carga de Datos:**
   - El script carga el conjunto de datos IMDB usando PySpark y realiza el preprocesamiento para limpiar y estructurar la información.

2. **Análisis Realizados:**
   - Top 10 películas mejor calificadas
   - Top 10 películas con mayor recaudación
   - Top 10 películas con más votos
   - Géneros más comunes
   - Mejores calificaciones por género
   - Calificación media por década
   - Recaudación media por década
   - Directores con más películas

3. **Almacenamiento de Resultados:**
   - Los resultados se almacenan en una base de datos MySQL, con cada análisis guardado en una tabla separada.

## Gracias :)

