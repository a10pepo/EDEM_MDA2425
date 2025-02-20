# Configuración de Infraestructura en Google Cloud Platform

Este documento detalla el proceso de configuración de una infraestructura completa en GCP para una aplicación de pedidos y entregas.

## Índice
- [Configuración de Infraestructura en Google Cloud Platform](#configuración-de-infraestructura-en-google-cloud-platform)
  - [Índice](#índice)
  - [Configuración de Máquinas Virtuales](#configuración-de-máquinas-virtuales)
    - [Orders App VM](#orders-app-vm)
    - [Delivery App VM](#delivery-app-vm)
  - [Configuración de Pub/Sub](#configuración-de-pubsub)
  - [Configuración de Base de Datos](#configuración-de-base-de-datos)
  - [Configuración de Big Query](#configuración-de-big-query)
    - [Pruebas del Sistema](#pruebas-del-sistema)
    - [Conexión con Data Lake](#conexión-con-data-lake)
  - [Implementación de dbt](#implementación-de-dbt)
  - [Visualización con Metabase](#visualización-con-metabase)

## Configuración de Máquinas Virtuales

### Orders App VM
1. Creamos una máquina virtual `orders-app` en el servidor de Bélgica con las siguientes especificaciones:
   - Tipo de máquina: e2-micro
   - Tráfico HTTP y HTTPS habilitado

![Configuración inicial de VM](images/image1.png)

2. Instalación de dependencias:
   - Docker
   - Docker-compose
   - Python
   - Clonación del repositorio de trabajo

![Instalación de dependencias](images/image2.png)

3. Creación de imagen base:
   - Se crea una imagen de la máquina virtual configurada para automatizar el proceso
   - Nombre de la imagen: `image-e2e`

![Creación de imagen base](images/image3.png)

### Delivery App VM
1. Se crea una nueva máquina virtual utilizando la imagen base `image-e2e`

![Creación de VM delivery-app](images/image4.png)

## Configuración de Pub/Sub

1. Creación de tópicos:
   - Tópico para orders
   - Tópico para delivery

![Configuración de tópico orders](images/image5.png)
![Configuración de tópico delivery](images/image6.png)

## Configuración de Base de Datos

1. Creación de Cloud SQL:
   - Nombre de la base de datos: `ecommerce`

![Configuración de Cloud SQL](images/image7.png)

## Configuración de Big Query

1. Creación de datasets:
   - Se crean 2 datasets independientes
   - Configuración de tablas correspondientes

![Primer dataset](images/image8.png)
![Segundo dataset](images/image9.png)

2. Configuración de suscripciones Pub/Sub:
   - Integración con Big Query para ambos tópicos

![Primera suscripción](images/image10.png)
![Segunda suscripción](images/image11.png)

### Pruebas del Sistema

1. Creación y lectura de pedidos:
   - Verificación de funcionamiento del sistema de pedidos

![Prueba de pedidos](images/image12.png)

2. Visualización en Cloud SQL:
   - Confirmación de almacenamiento correcto de datos

![Visualización en Cloud SQL](images/image13.png)

### Conexión con Data Lake

1. Creación de tabla externa en Big Query:
   - Configuración de conexión con Data Lake

![Configuración de tabla externa](images/image14.png)

## Implementación de dbt

1. Sincronización entre BigQuery y PostgreSQL:
   - Configuración de conexión bidireccional

![Sincronización de bases de datos](images/image15.png)
![Verificación de conexión](images/image16.png)

2. Inicialización del proyecto dbt:
```bash
dbt init
```

![Inicialización de dbt](images/image17.png)

3. Creación de vistas:
   - Implementación de templates preparados
   - Configuración de vistas personalizadas

![Estructura de archivos](images/image18.png)
![Configuración de vistas](images/image19.png)
![Implementación de vistas](images/image20.png)

## Visualización con Metabase

1. Despliegue de Metabase:
   - Implementación mediante Docker
   - Configuración de dashboard

![Dashboard en Metabase](images/image21.jpg)

