# Kafka - Lab 2 

## Objectives

 1) Run Zookeeper + Kafka
 2) Produce messages from the command line
 3) Read topic content
 4) Compile Java Producer and Consumer Apps project
 5) Start the Java Consumer App
 6) Start the Java Producer App
 7) Exercise 1
 8) Exercise 2
 9) Exercise 3

### Requirements

 * Ensure all other Docker containers are stopped!!

## 1) Run Zookeeper + Kafka

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

## 2) Produce messages from the command line

Run the command line producer:

```sh
$ docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>hi
>dlp
>

```

## 3) Read topic content:

```sh
$ docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
hi
dlp
```

# Java Example

The example is a Maven project. You can import the project as Maven project with your IDE. 

* Producer: The producer will generate 100 messages and send them to the `myTopic`. 
* Consumer: Consume and log messages from `myTopic`.  


## 4) Compile Java Producer and Consumer App project (below actions can be done in IntelliJ IDE)
```sh
$ cd kafka-example 
```

Compile: 

```sh
$ mvn clean compile
```

## 5) Start the Consumer (below actions can be done in IntelliJ IDE)


Execute the Consumer:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.ConsumerCloud"
```
The consumer will listen and log new messages. Leave it running in the background. 



## 6) Start the Java Producer App (below actions can be done in IntelliJ IDE)

Execute the Producer:

```sh
$ mvn exec:java -Dexec.mainClass="com.gft.dlp.kafka.ProducerCloud"
``` 


## 7) Exercise 1
Send messages from console, and verify they are consumed by the Java Consumer app, and also from the console Consumer

## 8) Exercise 2
Send messages from the Java Producer app, and verify they are consumed by the Java Consumer app, and also from the console Consumer 

## 9) Exercise 3
Modify the Java Consumer App to show in also the key of the message, and its Kafka message's offset.

## 10) Exercise 4

* How can the Consumer list on start all the messagges from the topic?  Tip: look up in internet documentation about

### Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
