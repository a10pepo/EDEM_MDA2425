# Exercise 5: KSQL

## Objectives

1) Produce messages from a Python application.
2) Use KSql to query the messages


## Run Kafka in your computer with Docker
Simple scenario: 1 zookeeper + 1 Kafka broker + 1 Ksql server + 1 Ksql CLI.

Start the ZooKeeper and Kafka container.

**To execute below command, make sure you open the terminal under the folder "exercise5/"**
```sh
$ docker-compose up -d
```

## Command Line , create a new Kafka topic

Run the command line producer:

```sh
docker-compose exec kafka kafka-topics --create --topic palabras --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

## Run the Producer Python App from VisualStudio
Execute the exercise5/producer.py Python Producer Application. Check that it shows El Quijote's phrases.

Then ensure the messages (each word of El Quijote's book) is being sent to the topic "palabras".

```sh
docker-compose exec kafka kafka-console-consumer --topic palabras --from-beginning --bootstrap-server localhost:9092
```

If the messages are arriving you are OK. Now Exit with Control-C. You are ready to start to query the messages with KSQL in next steps :)!!!

## Open KSql in a console
```sh
docker-compose exec ksql-cli ksql http://host.docker.internal:8088
````

Check you can see an output like the below one:

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


## Query the messages from a topic with KSQL

```sql
SET 'auto.offset.reset' = 'earliest';
```
```sql
SHOW TOPICS;
```
```
Kafka Topic  | Partitions | Partition Replicas
------------------------------------------------
 palabras | 1          | 1
------------------------------------------------
```
```sql
PRINT 'palabras' FROM BEGINNING;
```

Press Control-C some times to exit. Be patient, some times take time :)....If it does not stop, close the terminal and 
open a new one under the same folder "exercise5".

If you have data in an existing Apache Kafka topic, you can create a stream or a table backed by that topic and begin 
streaming the data into ksqlDB:
Any subsequent data produced to the topic will be streamed into ksqlDB, and any data inserted into the new stream will
be written to the Kafka topic automagically.
```sql
CREATE STREAM palabras_stream
  (palabra VARCHAR)
   WITH (KAFKA_TOPIC='palabras',
        VALUE_FORMAT='DELIMITED');
```

Select all the messages from the stream (topic), and show what is each word's length.
```sql
SELECT palabra, LEN(palabra) FROM palabras_stream emit changes;
```

Select the messages from the stream where the message size is major than 7
```sql
SELECT palabra AS mi_palabra, LEN(palabra) AS longitud FROM palabras_stream WHERE LEN(palabra) > 7 emit changes;
```

### Do this Exercise on your own
Select the messages from the stream where the message size is major than 10

### Keep going on
Filter words **starting** with the letter **"t"** in a stream named palabras_stream
```sql
SELECT palabra
FROM palabras_stream
WHERE palabra LIKE 't%' emit changes;
```

### Do this Exercise on your own
Filter words **ending** with the letters **"go"** in a stream named palabras_stream

### Keep going on
Create a KTable, to check out how many times a word has appeared in the El Quijote's book. Notice that while the words
are arriving to the topic, the KTable gets updated in real time!!!
```sql
CREATE TABLE mi_ktable AS
SELECT palabra,
count(*)
FROM palabras_stream
GROUP BY palabra
EMIT CHANGES;
```

Read the KTable
```sql
SELECT * FROM mi_ktable EMIT CHANGES;
```

#### More Exercises
##### Exercise 5.1
Find the words that starts with 'ca' **and** finishes with 'o' **and** the word is longer than 6 characters.

##### Exercise 5.2
Select all the words, but transformed in Uppercase. Hint: use a select and using the function UCASE(...)

##### Exercise 5.3 ADVANCED
**Note:** If you are interested in learning more on KSQL you can find developer info here: https://docs.confluent.io/current/ksql/docs/developer-guide/syntax-reference.html
And you can try from this doc to performe another KSQL with the 'palabras' topic.

