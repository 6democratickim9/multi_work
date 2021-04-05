from flask import jsonify,request
from datetime import datetime
from flask_restful import Resource,reqparse,Api
from flask import Flask
from flask_mysqldb import MySQL

import uuid
import flask_restful
import mariadb
import sys
import pymysql
import json




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
    def get(self, user_id):
        conn = mariadb.connect(**config)
        cursor = conn.cursor()
        sql = "select * from orders where user_id=? order by id desc"
        cursor.execute(sql,('user_id')) #최신 데이터를 가져와서 반환
        result_set = cursor.fetchall()

        json_data = []
        for result in result_set:
            json_data.append(result)
        
        return jsonify(json_data)

        #return {'payload': user_id}
        #return {'user_id': user_id}
    def post(self, user_id):
       # parser = reqparse.RequestParser()
      #  parser.add_argument('coffee_name')
       # parser.add_argument('coffee_price')
       # parser.add_argument('coffee_qty')
       # args = parser.parse.args()

        json_data = request.get_json()
        json_data['user_id'] = user_id
        json_data['order_id'] = str(uuid.uuid4())
        json_data['order_at'] = str(datetime.today())

        coffee_name = json_data['coffee_name']
        coffee_price = json_data['coffee_price']
        coffee_qty = json_data['coffee_qty'] # 얻어올 파라미터 3개
        return jsonify(json_data),201
        #{'coffee_name': coffee_name, 'coffee_price':coffee_price},201

class OrderDetail(flask_restful.Resource):
    def get(self, user_id,order_id):
        return {'user_id':user_id, 'order_id': order_id}


api.add_resource(Order,'/order-ms/<string:user_id>/orders')
api.add_resource(OrderDetail,'/order-ms/<string:user_id>/orders/<string:order_id>')

if __name__ == "__main__":
    app.run()