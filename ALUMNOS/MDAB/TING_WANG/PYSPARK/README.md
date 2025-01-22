## Datasets
Los datasets se pueden encontrar en la carpeta *resources*, donde hay subidos tres CSV. En total se han utilizado 4 datasets, sin embargo el número 3 no se ha podido subir a GitHub porque es demasiado grande. Dejo a continuación los enlaces de donde los he obtenido:
1. World Development Indicators (https://www.kaggle.com/datasets/kaggle/world-development-indicators?select=Country.csv)
2. Human Development Index (https://www.kaggle.com/datasets/elmartini/human-development-index-historical-data)
3. **Global Terrorism** (https://www.kaggle.com/datasets/START-UMD/gtd)
4. World Happiness Report (https://www.kaggle.com/datasets/unsdsn/world-happiness?select=2019.csv)

## Objetivo
El objetivo es identificar patrones que muestren si el nivel de desarrollo humano, económico y social influye en los niveles de felicidad de los ciudadanos y si los incidentes de terrorismo pueden afectar negativamente la percepción de bienestar en esos países. Cómo estas tres variables (felicidad, índice de desarrollo y terrorismo) están relacionadas.

## Transformaciones
En primer lugar, se ha realizado un análisis del dataset de terrorismo (países y regiones con más/menos casos; casos en Europa; evolución anual)y también del dataset de felicidad (correlación con las diferentes varaibles con el ranking).
</br>
En segundo lugar, haciendo un join de los DF de felicidad y terrorismo, se ha intentado buscar la correlación con diferentes variables medidas para la felicidad con el número de casos de terrorismo. Introduciendo el DF de "Country", se han agrupado por "income group", llegando a la conclusión que los países de ingresos medios son los que más incidencias han tenido. Aún así, no hay una relación directamente lineal entre ingresos y ataques terroristas.
</br>
Por último, se ha buscado la correlación de felicidad, eventos terroristas y el índice de desarrollo humano. Para saber si los países en donde más/menos ataques terroristas han habido están por encima/debajo de la media de felicidad y desarrollo.

## MySQL
Como último paso, se ha creado una base de datos en MySQL a partir de el trabajo realizado con PySpark. Se ha creado una copia del script de python donde omitimos algunas de las transformaciones, guardando solo algunos DF como tablas. Para ello, se ha definido una función llamada save_to_mysql.
</br>
Para conectar MySQL y PySpark, ha sido necesario añadir un nuevo fichero .jar (MySQL Connector/J). Con este comando, se han pasado los DF a MySQL:
```
docker exec -it spark-master /spark/bin/spark-submit --jars /opt/project/jar/mysql-connector-j-8.0.33.jar /opt/project/src/python/e_wach_e2eSpark-MYSQL.py
```
