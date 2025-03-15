from kafka import KafkaConsumer
from json import loads

from confluent_kafka import Consumer


def read_ccloud_config(config_file):
    conf = {}
    with open(config_file) as fh:
        for line in fh:
            line = line.strip()
            if len(line) != 0 and line[0] != "#":
                parameter, value = line.strip().split('=', 1)
                conf[parameter] = value.strip()
    return conf


props = read_ccloud_config("exercise3/client.properties")
props["group.id"] = "python-group-1"
props["auto.offset.reset"] = "earliest"

consumer = Consumer(props)
consumer.subscribe(["ARBOLES"])

try:
    while True:
        msg = consumer.poll(1.0)
        if msg is not None and msg.error() is None:
            print("key = {key:12} value = {value:12}".format(key=msg.key().decode('utf-8'), value=msg.value().decode('utf-8')))
except KeyboardInterrupt:
    pass
finally:
    consumer.close()