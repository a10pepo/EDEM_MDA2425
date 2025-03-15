# Exercise 4: Python App to Kakfa running in Docker

## Objectives

1) Run Zookeeper + Kafka
2) Produce messages from the command line
3) Consume/Read messages from the command line
4) Produce messages from a Python application.
5) Consume/Read messages from a Python application.
6) Modify the Python Producer and/or Consumer Python application.


## Run Kafka in your computer with Docker
Simple scenario: 1 zookeeper + 1 Kafka broker.

Start the ZooKeeper and Kafka container.
To execute below command, make sure you open the terminal under the folder "exercise4/"

```sh
docker-compose up -d
```


Using the terminal create the topic 'ventas'

```sh
docker-compose exec kafka kafka-topics --create --topic ventas --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092
```
<!-- 
kafka-topics => comando de kafka
--create --topic [nameTopic] => crear un topic = equivalente a ser una tabla en una base de datos
--partitions
--replication-factor [nº] => nº de copia(s) de seguridad
--bootstrap-server => indicar el servidor
localhost:9092 => conexión entre producer y kafka
 -->


## Command Line: Producer
Produce messsages from the command line
```sh
docker-compose exec kafka kafka-console-producer --topic ventas --broker-list localhost:9092
```
<!-- 
kafka-console-producer => crea el producer
--broker-list

 -->

Send messages from the terminal.

## Command Line: Consumer
**Open TWO new console** and Consume the  topic content, executing below command on each new console:

```sh
docker-compose exec kafka kafka-console-consumer --topic ventas --from-beginning --bootstrap-server localhost:9092
```
<!-- 
--from-beginning => de los mensajes
--bootstrap-server [puerto]=> para indicar el servidor
 -->
## Do this exercise on your own
**Now must have three consoles opened at the same time**, one to produce message and another to consume the messsages.

===> Then, produce messages from one console and read the messages from the other two consoles.
<!-- Una consola con producer y otras dos con consumer -->

## Run the Producer Python App from VisualStudio
Open VisualStudio and run the producer.py App
<!-- en una nueva consola, envía mensajes a consumers -->
## Run the Consumer Python App from VisualStudio
Open VisualStudio and run the consumer.py App
<!-- muestra los mensajes -->


#### More Exercises
##### Exercise 4.1 
Check that in the opened two consumer consoles, you are getting the messages produced by the Python Producer Application.

Produce messages from the Producer console, and check that 1 ) you are getting the messages produced by the Python Producer Application.
and 2) you are getting the messages from the Python Consumer Application.

##### Exercise 4.2
Create a new topic from the command line. Then modify the Producer App and the Consumer App to use the new topic.
<!-- 
docker-compose exec kafka kafka-topics --create --topic compras --partitions 1 --replication-factor 1 --if-not-exists --bootstrap-server localhost:9092

docker-compose exec kafka kafka-console-producer --topic compras --broker-list localhost:9092

 -->
##### Exercise 4.4
Read the messages also with the Kafka Admin screen at http://localhost:9021/clusters
Check that this admin web console is very similar to the one we used in Confluent Cloud.

### Clean up

Shut down Docker Compose

```sh
docker-compose down
```