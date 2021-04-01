from kafka import KafkaProducer
from json import dumps
import time


# dict(key,value) -> object
# str -> string

producer = KafkaProducer(acks=0, 
                compression_type='gzip',
                bootstrap_servers=['127.0.0.1:9092'],
                value_deserializer=lambda X : dumps(x).encode('utf-8'))

start = time.time()
for i in range(10):
    data = {'name': 'Dowon-' + str(i)}
    producer.send('my-topic-users', value=data)
    producer.flush()

print("Done. Elapsed time: ", (time.time() - start))