from kafka import KafkaProducer
from json import dumps
import time


# dict(key,value) -> object
# str -> string

producer = KafkaProducer(acks=0, 
                compression_type='gzip',
                bootstrap_servers=['127.0.0.1:9092'],
                value_serializer=lambda x : dumps(x).encode('utf-8'))

start = time.time()
for i in range(10):
    data = {'schema':{"type":"struct","fields":[{"type":"int32","field":"id"},{"type":"string","field":"user_id"},{"type":"string","field":"pwd"},{"type":"string","field":"NAME"},{"type":"int64","name":"org.apache.kafka.connect.data.Timestamp","version":1,"field":"created_at"}],"name":"users"},"payload":{"id":10,"user_id":"new_test10","pwd":"new_pwd10","NAME":"NEW TEST USER10","created_at":161834903813}}
    producer.send('my_topic_users', value=data)
    producer.flush()

print("Done. Elapsed time: ", (time.time() - start))