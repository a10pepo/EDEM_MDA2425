## End2End Almacenamiento Cloud


 -Arrancamos las maquinas donde ejecutaremos los scripts que crean los datos de orders y delivery. 
 -Primero creamos orders y configuramos una imagen con docker y python, y la segunda máquina la creo por comandos añadiendo la imagen ya creada.
 -Conficuramos las maquinas por igual concretando como region europe-southwest1-c(Madrid) y europe-west1-c(Bélgica), con un tipo de maquina E2 micro ambas. En Firewall permitimos HTTP y HTTPS.

![Creción maquina orders](images/capt1.png)

![Configuración Firewall](images/capt2.png)

![Configuración imagen](images/capt3.png)

![Creación maquina delivery](images/capt4.png)


-Una vez arrancadas las maquinas, procedo a hacer la configuración de la instancia de postgreSQL.

![Instancia SQL](images/capt5.png)

![Configuración SQL](images/capt6.png)


-Creación datasets en BigQuery y tablas.

![Creación Datasets](images/capt7.png)

![Creación tablas BIGQUEY](images/capt8.png)

![Creación raw_delivery](images/capt9.png)

![BIGQUEY](images/capt10.png)


-Tablas postgreSQL.

![Tablas SQL](images/capt11.png)


-PUB/SUB: topics y subscripciones

![Topics](images/capt12.png)

![Subscripciones](images/capt13.png)


-El bucket para CLOUD Storage lo tengo creado del otro dia y se me olvidó hacerle captura.


-Arranco los scrits.

![Arranco script python delivery](images/captdelivery14.png)

![Arranco script python oeders](images/capt15.png)


-Compruebo q los datos se están cargando en las bases de datos.

![postgreSQL](images/capt16.png)

![BigQuery](images/capt17.png)

![Cloud Storage](images/capt18.png)

-Configuración parquet

![Parquet](images/capt19.png)


-Ejecuto Script Python en local (analytical_layer.el_orders.main)

![Script Local](images/capt20.png)


-DBT y BigQuery tablas

![DBT1](images/capt21.png)

![DBT2](images/capt22.png)

![DBT3](images/capt23.png)

![DBT4](images/capt24.png)

![DBT5](images/capt25.png)

![BIGQUEY todas las tablas](images/capt26.png)


-METABASE

![MB1](images/capt27.png)

![MB2](images/capt28.png)

![MB3](images/capt29.png)

![MB4](images/capt30.png)