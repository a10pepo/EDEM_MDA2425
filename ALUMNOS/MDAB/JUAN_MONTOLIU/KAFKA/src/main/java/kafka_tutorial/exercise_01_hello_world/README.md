# Kafka - Lab 1 

## Objectives

 1) Run Kafka (and Zookeeper)
 2) Check Docker Kafka and Zookeeper status
 3) Create a Kafka topic 
 4) Produce messages from the command line 
 5) Read messages from the command line
 6) Produce Messages with keys
 7) Explore Kafka web UI
 8) Describe the Kafka topic

### Requirements

 * Ensure all other Docker containers are stopped!!

## 1) Run Kafka (and Zookeeper)
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.

```sh
docker-compose up -d
```

## 2) Check Docker Kafka and Zookeeper status
### Check Kafka
Status: 

```sh
docker-compose ps
      Name                  Command            State                     Ports
-------------------------------------------------------------------------------------------------
lab0_kafka_1       /etc/confluent/docker/run   Up      0.0.0.0:9092->9092/tcp
lab0_zookeeper_1   /etc/confluent/docker/run   Up      0.0.0.0:2181->2181/tcp, 2888/tcp, 3888/tcp
```

### Check Zookeeper 

Check the ZooKeeper logs to verify that ZooKeeper is healthy.

```sh
docker-compose logs zookeeper | Select-String binding    #for windows
docker-compose logs zookeeper | grep -i binding          #for linux
```

Sample output: 

```sh
zookeeper    | [2020-02-18 15:49:28,229] INFO binding to port 0.0.0.0/0.0.0.0:2181 (org.apache.zookeeper.server.NIOServerCnxnFactory)
```

### Check Kafka Broker 

Check the Kafka logs to verify that broker is healthy.

```sh
docker-compose logs kafka | Select-String started    #for windows
docker-compose logs kafka | grep -i started          #for linux
```

Sample output: 

```sh
kafka_1      | [2020-02-18 16:05:21,153] INFO [SocketServer brokerId=1] Started 2 acceptor threads for data-plane (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,646] DEBUG [ReplicaStateMachine controllerId=1] Started replica state machine with initial state -> Map() (kafka.controller.ZkReplicaStateMachine)
kafka_1      | [2020-02-18 16:05:21,663] DEBUG [PartitionStateMachine controllerId=1] Started partition state machine with initial state -> Map() (kafka.controller.ZkPartitionStateMachine)
kafka_1      | [2020-02-18 16:05:21,715] INFO [SocketServer brokerId=1] Started data-plane processors for 2 acceptors (kafka.network.SocketServer)
kafka_1      | [2020-02-18 16:05:21,727] INFO [KafkaServer id=1] started (kafka.server.KafkaServer)
```

## 3) Create a Kafka topic

Create a topic named `myTopic`, one partition and one replica.

```sh
docker-compose exec kafka kafka-topics --create --topic myTopic --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```

Output: 

```sh
Created topic myTopic.
```

## 4) Produce messages from the command line

Produce messages (It is very didactic to execute below command in more than once console at the same time):
```sh
docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092
>hi
>dlp
>

```

## 5) Read messages from the command line
Read topic content (It is very didactic to execute below command in more than once console at the same time):

```sh
docker-compose exec kafka kafka-console-consumer --topic myTopic --from-beginning --bootstrap-server localhost:9092
hi
dlp
```

## 6) Produce Messages with keys
Send KEY-VALUES:
```sh
docker-compose exec kafka kafka-console-producer --topic myTopic --broker-list localhost:9092 --property "parse.key=true" --property "key.separator=:"
spain:3
french:4
germany:2
italy:n/a
```

Open again the consumer to read the values (by default the keys are not visible)

## 7) Explore Kafka web UI
Open a browser at at http://localhost:8080/

## 8) Describe the Kafka topic

```sh
docker-compose exec kafka kafka-topics --describe --topic myTopic --bootstrap-server host.docker.internal:9092
```

Output:

```sh
Topic: myTopic  PartitionCount: 1       ReplicationFactor: 1    Configs:
        Topic: myTopic  Partition: 0    Leader: 1       Replicas: 1     Isr: 1
```


## Clean up

Shut down Docker Compose

```sh
$ docker-compose down
```
