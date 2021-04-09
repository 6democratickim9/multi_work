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
data = {"schema":{"type":"struct","fields":[{"type":"int32","field":"id"},{"type":"string","field":"user_id"},{"type":"string","field":"NAME"}],"name":"users"},"payload":{"id":114,"user_id":"6democratickim9","NAME":"minjju"}}
producer.send('minju_exam_topic_users', value=data)
producer.flush()

print("Done. Elapsed time: ", (time.time() - start))