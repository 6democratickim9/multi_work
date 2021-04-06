from kafka import KafkaConsumer
import time
import json
import threading
from datetime import datetime


import uuid
import flask_restful
import mariadb
import json
import mariadb



config = {
    'host':'127.0.0.1',
    'port':3306, 
    'user':'root',
    'password':'1234', 
    'database':'mysql'
}


consumer = KafkaConsumer('new_orders',
                        bootstrap_servers=["localhost:9092"],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        auto_commit_interval_ms=1000,
                        consumer_timeout_ms=1000
                        )

# kafka-client로 작업했었음

start = time.time()

#for message in consumer:
#    topic = message.topic
#    partition = message.partition
 #   offset = message.offset
  #  value = message.value
   # print("Topic:{},Partition:{}, Offset:{}, Value:{}".format(topic,partition,
    #offset,value))


conn = mariadb.connect(**config)
cursor = conn.cursor()

sql = '''INSERT INTO delivery_status(delivery_id, order_json, status)
        VALUES(?,?,?)'''

def fetch_latest_orders(next_call_in):

    next_call_in += 5
    batch = consumer.poll(timeout_ms=100)
    if len(batch) > 0:
        for message in list(batch.values())[0]:
            value = message.value.decode()
            #order_dict=json.loads(value) #json데이터를 dict로 바꿔주는 함수 :loads
            #print(order_dict["ordered_at"])
            delivery_id = str(uuid.uuid4())

            status = 'CONFIRMED'
            cursor.execute(sql,[delivery_id,value,status])
            conn.commit()
       
    threading.Timer(next_call_in - time.time(),
                    fetch_latest_orders,
                    [next_call_in]).start()



next_call_in = time.time()
fetch_latest_orders(next_call_in)

