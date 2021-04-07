from kafka import KafkaConsumer
import time
import json
import threading
from datetime import datetime
from flask_restful import Resource,reqparse,Api

import uuid
import flask_restful
#import mariadb
import json
import pymysql


app = Flask(__name__)

api = flask_restful.Api(app)

config = {
    'host':'172.17.0.2', #도커 내의 네트워크
    'port':3306, 
    'user':'root',
    'password':'', 
    'database':'mydb'
}


consumer = KafkaConsumer('new_orders',
                        bootstrap_servers=["localhost:16000"],
                        auto_offset_reset='earliest',
                        enable_auto_commit=True,
                        auto_commit_interval_ms=1000,
                        consumer_timeout_ms=1000
                        )


start = time.time()

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
            delivery_id = str(uuid.uuid4())

            status = 'COMPLETED'
            cursor.execute(sql,[delivery_id,value,status])
            conn.commit()
       
    threading.Timer(next_call_in - time.time(),
                    fetch_latest_orders,
                    [next_call_in]).start()


class Delivery(flask_restful.Resource):

    def get(self, delivery_id):
        return {'delivery_id': delivery_id}




class DeliveryDetail(flask_restful.Resource):

    def get(self, delivery_id):
        return {'delivery_id': delivery_id}

api.add_resource(DeliveryDetail,'/delivery-ms/orders')
api.add_resource(Delivery,'/delivery-ms/deliveries/<string:delivery_id>/status')


next_call_in = time.time()
fetch_latest_orders(next_call_in)

