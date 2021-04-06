import flask
from flask import jsonify,request
from datetime import datetime
from flask_restful import Resource,reqparse,Api
from flask import Flask

import uuid
import flask_restful
import mariadb
import json

# 1. KafkaProducer() -> 생성자에 추가




app = Flask(__name__)
app.config["DEBUG"] = True
api = flask_restful.Api(app)

config = {
    'host':'127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'database': 'mysql'
}

@app.route('/order-ms')
def index():
    return "Welcome to DELIVERY Microservice!"

class Delivery(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()
   
    def get(self):
        sql = "select delivery_id, order_json, status,created_at from delivery_status order by id desc"
        self.cursor.execute(sql)
        result_set = self.cursor.fetchall()

        json_data = []
        for result in result_set:
            json_data.append(result)
        
        return jsonify(json_data)


        sql = '''select user_id, order_id, coffee_name, coffee_price, coffee_qty, ordered_at
                from orders where user_id=? order by id desc '''
        
        self.cursor.execute(sql,[user_id])
        result_set = self.cursor.fetchall()

        row_headers = [x[0]for x in self.cursor.description]


        json_data =[]
        for result in result_set:
            json_data.append(dict(zip(result)))

        return jsonify(json_data)



class DeliveryStatus(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()

    def put(self, delivery_id):
        json_data = request.get_json()
        status = json_data['status']
        #DB 삽입
        sql = 'UPDATE delivery_status SET status=? WHERE delivery_id=?'
        self.cursor.execute(sql,[status,delivery_id])
        self.conn.commit()
        
        json_data['updated_at'] = str(datetime.today())
        response = jsonify(json_data)
        response.status_code =201 #생성 성공 코드

        return response



api.add_resource(Delivery,'/delivery-ms/deliveries') 
api.add_resource(DeliveryStatus,'/delivery-ms/deliveries/<string:delivery_id>') 

if __name__ == "__main__":
    app.run(port=6000)