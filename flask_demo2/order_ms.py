import flask
from flask import jsonify,request
import flask_restful
from datetime import datetime
from flask_restful import Resource,reqparse,Api
from flask import Flask

import uuid

import mariadb
import json


app = Flask(__name__)
app.config["DEBUG"] = True
api = flask_restful.Api(app)

config = {
    'host':'127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'database': 'mydb'
}

@app.route('/order-ms')
def index():
    return "Welcome to ORDER Microservice!"

class Order(flask_restful.Resource):
    def __init__(self):
        self.conn = mariadb.connect(**config)
        self.cursor = self.conn.cursor()

    def get(self, user_id):
        sql = "select * from orders where user_id=? order by id desc"
        self.cursor.execute(sql,['user_id']) #최신 데이터를 가져와서 반환
        result_set = self.cursor.fetchall()

        json_data = []
        for result in result_set:
            json_data.append(result)
        
        return jsonify(json_data)

        #return {'payload': user_id}
        #return {'user_id': user_id}

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
        sql = '''INSERT INTO orders(user_id, order_id, coffee_name, coffee_price, coffee_qty, ordered_at)
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

        response = jsonify(json_data)
        response.status_code =201 #생성 성공 코드
        return response

        #coffee_name = json_data['coffee_name']
        #coffee_price = json_data['coffee_price']
        #coffee_qty = json_data['coffee_qty'] # 얻어올 파라미터 3개
        
        #return jsonify(json_data),201
        #{'coffee_name': coffee_name, 'coffee_price':coffee_price},201

class OrderDetail(flask_restful.Resource):
    def get(self, user_id,order_id):
        return {'user_id':user_id, 'order_id': order_id}


api.add_resource(Order,'/order-ms/<string:user_id>/orders') #주소값은 하나지만 GET과 POST 모두 가능
#GET 방식에는 사용자 아이디 검색 가능한지 json으로 반환 가능한지 확인/POST에서는 유저네임 읽어들인 후에 주문날짜와 오더네임 추가 후 201번 출력
#201번 코드를 통해 정상작동 여부 판단 가능
api.add_resource(OrderDetail,'/order-ms/<string:user_id>/orders/<string:order_id>')

if __name__ == "__main__":
    app.run()