from kafka import KafkaConsumer
from json import loads
import time

consumer = KafkaConsumer('my_topic_users',
            bootstrap_servers=['127.0.0.1:9092'],
            auto_offset_reset='earlist',
            enable_auto_commit=True,
            group_id='my-group',
            value_deserializer=lambda x: loads(x.decode('utf-8')),
            consumer_timeout_ms=1000)

start = time.time()

for message in consumer:
    topic = message.topic
    patition = message.partition
    offset = message.offset
    key = message.key
    value = message.value
    print("Topic:{},Partition:{},Offset:{},Key:{},Value:{}".format(topic,patition,offset,key,value))

    print("Elapsed: ", (time.time() - start))