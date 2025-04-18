# Análisis de Fútbol con Spark

En este repositorio se encuentra el código para realizar el análisis de datos de fútbol usando Apache Spark. El proyecto consiste en analizar los datos del conjunto de fútbol y almacenar los resultados en una base de datos MySQL.

## Ejecución del Proyecto
Para levantar los contenedores de Spark y MySQL, entra en la carpeta docker y lanza el siguiente comando:

```
docker-compose up -d
```

### Ejecución en Terminal
Existen dos análisis principales realizados en el proyecto:

#### Top 10 equipos con más goles a favor y Top 10 equipos con más goles en contra
Para ejecutar el script que muestra los resultados directamente en la terminal, usa el siguiente comando:

```
docker exec -it spark-master /spark/bin/spark-submit --jars /opt/project/jar/mysql-connector-j-8.0.33.jar /opt/project/src/analysisfootball.py

```
El script también genera el análisis de los equipos que más goles han recibido. Ambos resultados se almacenan en la base de datos MySQL.

### Ejecución con MySQL
Si prefieres almacenar los resultados en la base de datos para consultarlos posteriormente, asegúrate de que el contenedor MySQL esté en ejecución y accesible desde el contenedor Spark. Los parámetros de conexión están configurados de la siguiente manera:

- Host: mysql
- Puerto: 3306
- Base de datos: pysparkdb
- Usuario: spark
- Contraseña: password

## Descripción del Proyecto
### Carga de Datos:
El script carga el conjunto de datos de fútbol usando PySpark y realiza el análisis para obtener los equipos con más goles a favor y en contra.

### Análisis Realizados:
- Top 10 equipos con más goles a favor
- Top 10 equipos con más goles en contra

### Almacenamiento de Resultados:
Los resultados se almacenan en una base de datos MySQL, cada análisis en una tabla separada:
- Tabla: top_scoring_teams
- Tabla: top_conceding_teams


