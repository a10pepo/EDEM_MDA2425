# KSQL Lab

## Objectives

### Requirements

* Docker for Windows
* Docker Compose

## Quick theoretical Kafka intro
Streams vs Tables. Below link explains the difference. Thouh in next exercises we will use a different use case.
https://developer.confluent.io/courses/ksqldb/streams-and-tables/#:~:text=Streams%20are%20unbounded%20series%20of,want%20to%20use%20the%20data.

## Java App

Compile and execute the Producer Java App. That will create a topic, and send messages to it.

## Run

Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
docker-compose up -d
```

```sh
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
```

docker-compose exec ksql-cli bash -c 'echo -e "\n\n⏳ Waiting for KSQL to be available before launching CLI\n"; while [ $(curl -s -o /dev/null -w %{http_code} http://ksql-server:8088/) -eq 000 ] ; do echo -e $(date) "KSQL Server HTTP state: " $(curl -s -o /dev/null -w %{http_code} http://ksql-server:8088/) " (waiting for 200)" ; sleep 5 ; done; ksql http://ksql-server:8088'

⏳ Waiting for KSQL to be available before launching CLI

      ===========================================
      =        _  __ _____  ____  _             =
      =       | |/ // ____|/ __ \| |            =
      =       | ' /| (___ | |  | | |            =
      =       |  <  \___ \| |  | | |            =
      =       | . \ ____) | |__| | |____        =
      =       |_|\_\_____/ \___\_\______|       =
      =                                         =
      =  Streaming SQL Engine for Apache Kafka® =
      ===========================================
Copyright 2017-2019 Confluent Inc.

CLI v5.4.1, Server v<unknown> located at http://ksql-server:8088

https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html

```sql
ksql>  SET 'auto.offset.reset' = 'earliest';
```
```sql
ksql> SHOW TOPICS;
```
```
Kafka Topic  | Partitions | Partition Replicas
------------------------------------------------
 orders | 1          | 1
------------------------------------------------
```
```sql
ksql> PRINT 'orders' FROM BEGINNING;
```
```sql
ksql> CREATE STREAM orders_stream
  (orderedAt BIGINT,
   customerId BIGINT,
   amount BIGINT,
   price DOUBLE,
   product VARCHAR)
   WITH (KAFKA_TOPIC='orders',
        VALUE_FORMAT='JSON',
        TIMESTAMP='orderedAt');
```
```sh
 Message
----------------
 Stream created
----------------
```
```sql
ksql> SELECT * FROM orders_stream WHERE customerId = 1 EMIT CHANGES;
```
```sql
ksql> SELECT customerId,
         count(*)
  FROM orders_stream
  GROUP BY customerId
  EMIT CHANGES;
```
```
-------------------------------------------------------------------------------------
| CUSTOMERID                   |    KSQL_COL_1                                      |
-------------------------------------------------------------------------------------
| 2                            | 704                                                |
| 4                            | 1141                                               |
| 3                            | 788                                                |
| 1                            | 367                                          
```
```
 Message
----------------------------------------------------------
 Source `ORDERS_STREAM` (topic: orders) was dropped.
----------------------------------------------------------
```
```sql
ksql> CREATE TABLE orders_by_customer AS
  SELECT customerId,
         count(*)
  FROM orders_stream
  GROUP BY customerId
  EMIT CHANGES;
```
```
 Message
---------------------------------------------------------------------------------------------------------
 Table ORDERS_BY_CUSTOMER created and running. Created by query with query ID: CTAS_ORDERS_BY_CUSTOMER_1
---------------------------------------------------------------------------------------------------------


 Table Name         | Kafka Topic        | Format | Windowed
-------------------------------------------------------------
 ORDERS_BY_CUSTOMER | ORDERS_BY_CUSTOMER | JSON   | false
-------------------------------------------------------------

```
```sql
ksql> select * from orders_by_customer emit changes;
```
```
-----------------------------------------------------------------------------------------------------------------------------------------------------
|ROWTIME                             |ROWKEY                              |CUSTOMERID                          |KSQL_COL_1                          |
-----------------------------------------------------------------------------------------------------------------------------------------------------
|1584199961874                       |1                                   |1                                   |245                                 |
|1584209859996                       |2                                   |2                                   |477                                 |
|1584211766419                       |4                                   |4                                   |757                                 |
|1584211668855                       |3                                   |3                                   |521                                 |

Query terminated

```

### If you want to know more
https://ksqldb.io/examples.html

### Clean up

```sh
ksql> DROP STREAM ORDERS
```

Shut down Docker Compose

```sh
$ docker-compose down
```

