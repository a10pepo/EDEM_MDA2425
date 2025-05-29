# 🎬 Kafka Streaming con Filmaffinity + ksqlDB

Este proyecto implementa un **pipeline de streaming con Apache Kafka** utilizando **Python** para la ingesta y filtrado de datos de películas obtenidos de un CSV público de **Filmaffinity**. Posteriormente, utilizamos **ksqlDB** para realizar consultas en tiempo real sobre los datos.

---

## 📌 **Flujo del Proyecto**

1️⃣ **Obtención de datos:** Se utiliza un CSV con información de películas de Filmaffinity (scrappeado desde un repo público).
2️⃣ **Producción de datos:** Un script en Python (producer) lee el CSV y envía cada película a un **topic Kafka llamado `films`**.
3️⃣ **Consumo y filtrado:** Un script en Python (consumer) lee el topic `films`, filtra las películas por **nota media > 5** y las reenvía al topic **`films-filtered`**.
4️⃣ **Análisis con ksqlDB:** Se ejecutan consultas en ksqlDB para obtener estadísticas en tiempo real.

---

## 📂 **Estructura del Proyecto**
```plaintext
📁 kafka-filmaffinity
│── 📄 producer.py      # Envía datos del CSV a Kafka (topic: films)
│── 📄 consumer.py      # Filtra y reenvía datos (topic: filter)
│── 📄 docker-compose.yml # Entorno Kafka + ksqlDB
│── 📄 SOLUCION.md        # Documentación del proyecto
```

---

## 🚀 **1️⃣ Configuración del Entorno Kafka**

Este proyecto utiliza Docker para levantar un entorno con **Kafka, Zookeeper y ksqlDB**.
Asegúrate de tener **Docker** y **Docker Compose** instalados.

### 🔹 **Levantar Kafka y ksqlDB**
```bash
docker-compose up -d
```
🔍 **Servicios incluidos:**
- Kafka (puerto `9092`)
- Zookeeper (puerto `2181`)
- ksqlDB Server (puerto `8088`)

📌 **Verifica que los contenedores estén corriendo:**
```bash
docker ps
```

---

## 🏗 **2️⃣ Producer: Enviar datos del CSV a Kafka**

📌 **Script: `producer.py`**

El producer **lee el CSV y envía cada película al topic `films`**.

### 🔹 **Ejecutar el Producer:**
```bash
python producer.py
```

## 🏗 **3️⃣ Consumer: Filtrar y reenviar datos a Kafka**

📌 **Script: `consumer.py`**

El consumer **lee `films`, filtra las películas con nota > 5 y más de 500 votos, y las reenvía a `filter`**.

### 🔹 **Ejecutar el Consumer:**
```bash
python consumer.py
```

📜 **Ejemplo de mensaje filtrado en `filter`:**
```json
{"id": 916990.0, "titulo": "Love's Christmas Journey (TV)", "año": 2011.0, "duracion (min)": 172.0, "pais": "Estados Unidos", "direccion": "['David S. Cass Sr.']", "guion": "['George Tierney', 'Janette Oke']", "musica": "['Nathan Furst']", "fotografia": "['Maximo Munzi']", "productora": "['RHI Entertainment / Larry Levinson Productions']", "reparto": "['Natalie Hall', 'JoBeth Williams', 'Greg Vaughan', 'Dylan Bruce', 'Bobby Campo', 'Charles Shaughnessy', 'Sean Astin', 'Ryan Wynott', 'Jada Facer', 'Ernest Borgnine', 'Amanda Foreman', 'Annika Noelle']", "genero": "[['Romance'], ['Drama']]", "sinopsis": "Tras la pérdida de su marido y su hija, la viuda Ellie King visita a su hermano Aaron y a sus sobrinos por Navidad. Se esfuerza por disfrutar de la festividad y procura hacer nuevos amigos. Cuando Aaron tiene que hacer un viaje, Ellie accede a cuidar de los niños. (FILMAFFINITY)", "nota": "4,3", "votaciones": 42.0, "web": "https://www.filmaffinity.com/es/film916990.html"}
```

---

## 🔍 **4️⃣ Consultas con ksqlDB**

### 🔹 **Abrir KSQL Consol:**
```bash
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
```

### 🔹 **Crear un stream desde el topic `films`:**
```sql
CREATE STREAM films (
  id DOUBLE,
  titulo VARCHAR,
  anos DOUBLE,
  duracion DOUBLE,
  pais VARCHAR,
  direccion VARCHAR,
  guion VARCHAR,
  musica VARCHAR,
  fotografia VARCHAR,
  productora VARCHAR,
  reparto VARCHAR,
  genero VARCHAR,
  sinopsis VARCHAR,
  nota VARCHAR,
  votaciones DOUBLE,
  web VARCHAR
) WITH (
  KAFKA_TOPIC = 'films_filtered',
  VALUE_FORMAT = 'JSON'
);



