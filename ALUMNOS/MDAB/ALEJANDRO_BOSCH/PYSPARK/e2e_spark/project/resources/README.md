# Proyecto PySpark y MySQL

Este proyecto combina el uso de **PySpark** para procesamiento de datos y **MySQL** para la persistencia de resultados. El objetivo es analizar patrones y relaciones en un conjunto de datos que incluye información sobre autobuses y rutas.

---

## **Datasets**

Los datasets utilizados se encuentran en la carpeta `resources`, donde se han subido los archivos necesarios para este proyecto. A continuación, se listan los datasets empleados:

- **Buses Dataset**: Contiene información sobre autobuses, sus capacidades y estados.
- **Routes Dataset**: Incluye detalles de las rutas asociadas a los autobuses.

Ambos datasets han sido utilizados para realizar análisis de datos y se encuentran en la carpeta mencionada.

---

## **Objetivo**

El objetivo principal de este proyecto es demostrar cómo PySpark puede integrarse con MySQL para realizar análisis de datos y almacenar resultados procesados. Algunas metas incluyen:

1. Identificar patrones en la capacidad y estados de los autobuses.
2. Relacionar rutas con las capacidades de los autobuses asignados.
3. Demostrar cómo los resultados pueden persistirse en MySQL para futuros análisis.

---

## **Transformaciones**

### 1. Análisis inicial:
   - Se cargaron los datasets de `buses` y `routes` en PySpark.
   - Se exploraron los datos para identificar distribuciones y patrones básicos.

### 2. Transformaciones realizadas:
   - **Join entre datasets**: Se combinaron los datasets de `buses` y `routes` usando la columna `route_id`.
   - **Cálculo de promedios**: Se calculó el promedio de capacidad agrupado por el estado del autobús y la ruta.
   - **Filtrado de rutas**: Se analizaron las rutas con menos de 3 autobuses asignados para identificar patrones.

### 3. Resultados agrupados:
   - Agrupación por `status` y `route_name` para encontrar tendencias.
   - Búsqueda de correlaciones entre rutas y capacidad media de los autobuses asignados.

---

## **Integración con MySQL**

Los resultados procesados en PySpark se almacenaron en MySQL para facilitar futuros análisis. Se definió una función `save_to_mysql` para simplificar la escritura de DataFrames.

### **Pasos realizados:**

1. **Conexión PySpark-MySQL**  
   Para conectar PySpark con MySQL, se incluyó el archivo `.jar` del conector JDBC de MySQL:
   ```bash
   /opt/project/jar/mysql-connector-j-8.0.33.jar
   


Comando para ejecutar el script spark_exercise_mysql.py en un entorno Docker:
   ```bash
   docker exec -it spark-master /spark/bin/spark-submit \
    --jars /opt/project/jar/mysql-connector-j-8.0.33.jar \
    /opt/project/src/python/spark_exercise_mysql.py