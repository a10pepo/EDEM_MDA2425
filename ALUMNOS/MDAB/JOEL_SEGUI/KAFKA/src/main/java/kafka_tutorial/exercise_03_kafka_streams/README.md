# Kafka Streams Lab,

## Objectives

 1) Run Zookeeper + Kafka
 2) Produce messages  
 3) Process messages with Kafka Streams DSL
 4) Output results

### Requirements

 * Docker for Windows
 * Docker Compose 

## Run
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
$ docker-compose up -d
```

Status: 

```sh
$ docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab1_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab1_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```
 
### Example Description

The example is a Maven project. You can import the project as Maven project with your IDE. 

* **Shakespeare Quotes Producer**: The producer will generate 1000 Shakespeare quotes messages, using the [Faker API](https://github.com/DiUS/java-faker), and send them to the `quotes-input`. 

 Quote Examples: 
  * `True is it that we have seen better days.`
  * `Can one desire too much of a good thing?.`

* **Word Count**: The WordCount, using the high-level [KStream DSL](https://docs.confluent.io/current/streams/developer-guide/dsl-api.html), will compute a simple word occurrence histogram from input quotes. In this example, the input stream reads from a topic named "quotes-input", where the values of messages represent lines of text; and the histogram output is written to topic "streams-wordcount-output", where each record is an updated count of a single word

* **Results Consumer**: The Consumer will output the "streams-wordcount-output" topic messages.

Example: 

```sh
     | think | 625
     | he | 625
     | is | 1852
     | wise | 1249
```

### Running

```sh
$ cd kafka-streams-example 
```

Compile: 

```sh
$ mvn clean compile
```

###  Producer

Execute the Producer:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Producer_01"
``` 

###  WordCount

Execute the processor:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.WordcountConsumer"
``` 

###  Consumer

Execute the Consumer:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.Consumer_03"
```
 

#### Exercises  

* Filter words - Example: Count only words with length > 3

* Filter results - Example: Count > 10000

 

 

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```


