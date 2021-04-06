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
from kafka import KafkaProducer



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
    return "Welcome to ORDER Microservice!"

class Order(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()
        # 1. KafkaProducer() -> 생성자에 추가
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
        


    def get(self, user_id):
        sql = "select * from mydb where user_id=? order by id desc"
        self.cursor.execute(sql,['user_id']) #최신 데이터를 가져와서 반환
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

    def post(self, user_id):
        json_data = request.get_json()
        json_data['user_id'] = user_id
        json_data['order_id'] = str(uuid.uuid4())
        json_data['ordered_at'] = str(datetime.today())

        #DB 삽입
        sql = '''INSERT INTO mydb(user_id, order_id, coffee_name, coffee_price, coffee_qty, ordered_at)
                    VALUES(?,?,?,?,?,?)
        '''
        self.cursor.execute(sql,[user_id,
                                json_data['order_id'],
                                json_data['coffee_name'],
                                json_data['coffee_price'],
                                json_data['coffee_qty'],
                                json_data['ordered_at']])
        self.conn.commit()
        # kafka message send
        
        # 2. producer 인스턴스의 send() 메소드로 json 데이터 전송
        
        self.producer.send('new_orders',value=json.dumps(json_data).encode())
        self.producer.flush()

        response = jsonify(json_data)
        response.status_code =201 #생성 성공 코드
        return response


class OrderDetail(flask_restful.Resource):
    def get(self, user_id,order_id):
        return {'user_id':user_id, 'order_id': order_id}


api.add_resource(Order,'/order-ms/<string:user_id>/orders') 
api.add_resource(OrderDetail,'/order-ms/<string:user_id>/orders/<string:order_id>')

if __name__ == "__main__":
    app.run()