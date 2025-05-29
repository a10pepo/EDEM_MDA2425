## 1. Create the architecture in GCP

### Compute Engine

-  Create the VM instances for `orders-app` and `delivery-app`:

<p align="center">
<img src="img/image.png" height="300">
<img src="img/image-1.png" height="200">
</p>

### Cloud SQL

- Create SQL instance:

<p align="center"> 
<img src="img/image-4.png" height="300">
</p>
<br>

- Create database named `ecommerce`:
  
<p align="center"> 
<img src="img/image-5.png" height="300">
</p>
<br>

- Run queries to create tables in database `ecommerce`:
  
<p align="center"> 
<img src="img/image-6.png" height="400">
<br>
<img src="img/image-11.png" height="400">


### BigQuery

- Create datasets `orders` and `delivery`:

<p align="center"> 
<img src="img/image-8.png" height="400">
</p>
<br>

-  Create tables by running queries:

<p align="center"> 
<img src="img/image-7.png" height="300">
<br>
<img src="img/image-9.png" height="300">
</p>

### Pub/Sub

- Create topics `delivery-events` and `topic-events`:

<p align="center"> 
<img src="img/image-2.png" height="300">
<br>
<img src="img/image-3.png" height="250">
</p>
<br>

- Configure subscription to BQ:

<p align="center"> 
<img src="img/image-10.png" height="450">
</p>

### Bucket

- Create bucket (.parquet available after step in section 2. Ejecution)

<p align="center"> 
<img src="img/image-14.png" height="300">
</p>

## 2. Ejectution

- Initiate and run (`nohup`) in both VM instances `orders-app` and `delivery-app` to send data to Postgres and the Bucket created previously:

<p align="center"> 
<img src="img/image-13.png" height="450">
</p>


### Analytical layer

- Definition of variables. Syncronization of Postgres with BigQuery:

<p align="center"> 
<img src="img/image-12.png" height="30">
<img src="img/image-15.png" height="350">
</p>


## 3. DBT

- Configuration of dbt files to match our project's information.

<br>

- dbt run `expanded_delivery_events`:

<p align="center">
<img src="img/image-16.png" height="300">
</p>
<br>

- Datasets created by DBT in BigQuery, as result of the previous step:

<p align="center">
<img src="img/image-17.png" height="350">
</p>
<br>


## 4. Visualization - Metabase

- Through a docker-compose, we access to Metabase and load our datasets.
<br>

- Sample of dashboard:

<p align="center">
<img src="img/image-20.png" height="300">
</p>





