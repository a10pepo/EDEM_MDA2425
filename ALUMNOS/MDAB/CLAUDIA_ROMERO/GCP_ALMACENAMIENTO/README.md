
## GCP ENTREGABLE

### Compute Engine

- Creación de las máquinas virtuales `orders-app` y `delivery-app`:

<p align="center">
<img src="img/1.png" height="250">
</p>

---


### Cloud SQL

- Creación de la instancia Cloud SQL con PostgreSQL:

<p align="center"> 
<img src="img/4.png" height="300">
</p>

- Creación de la base de datos `ecommerce`:

<p align="center"> 
<img src="img/5.png" height="250">
</p>

<p align="center"> 
<img src="img/7.png" height="250">
</p>

- Ejecución de queries para crear tablas en la base de datos:

<p align="center"> 
<img src="img/6.png" height="400">
</p>

---

### BigQuery

- Creación de los datasets `orders`, `delivery` y creación de tablas:

<p align="center"> 
<img src="img/8.png" height="350">
</p>


---

### Pub/Sub

- Creación de topicos:

<p align="center"> 
<img src="img/2.png" height="300">


- Creación de suscripciones:

<p align="center"> 
<img src="img/3.png" height="400">
</p>

---

### Bucket de Cloud Storage

- Creación del bucket para almacenar archivos `.parquet`:

<p align="center"> 
<img src="img/12.png" height="300">
</p>

---

## 2. Ejecución del sistema

<p align="center"> 
<img src="img/10.png" height="100">
</p>

<p align="center"> 
<img src="img/11.png" height="350">
</p>

---

## 3. Sincronización con BigQuery (Analytical Layer)

- Configuración de variables y ejecución del script para sincronizar PostgreSQL con BigQuery:

<p align="center"> 
<img src="img/13.png" height="300">
</p>

---

## 4. DBT

- Configuración y ejecución de dbt para transformar datos en BigQuery:

<p align="center">
<img src="img/14.png" height="300">
</p>


---

## 5. Visualización en Metabase

- Uso de docker-compose para levantar Metabase y conectar los datasets:

<p align="center">
<img src="img/15.png" height="350">
</p>

- Ejemplos de dashboards:

<p align="center">
<img src="img/16.png" height="300">
<img src="img/17.png" height="300">
</p>
