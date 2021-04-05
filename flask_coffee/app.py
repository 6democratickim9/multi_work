from flask import Flask,jsonify,request
from datetime import datetime
import uuid
from flaskext.mysql import MySQL
from flask_restful import Resource,api, reqparse

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'my_rest_db'
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
mysql.init_app(app)

app = Flask(__name__)

@app.route('/order-ms/<user_id>/orders')
def order_ms(user_id):
    return "** order list **"

@app.route('/order-ms/<user_id>/orders/<order_id>')
def orders(order_id):
    return "** orders specified **"

@app.route('/users/<user_id>') # 꺾쇠로 가변데이터 명시
def users_detail(user_id):
    return jsonify({"user_id":user_id})


@app.route('/users', methods = ['POST']) # 그냥 넣으면 겟이 되니 포스트 추가
def userAdd():
    user = request.get_json()
    user['user_id'] = uuid.uuid4() 
    user['created_at'] = datetime.today()
    return jsonify(user), 201 

@app.route('/users/<user_id>/orders', methods = ['POST'])
def orderadd():
    user = request.get_json()
    user['coffee_name'] = request.get_json()
    user['coffee_price'] = request.get_json()
    user['coffee_qty'] = request.get_json()
    return jsonify()



 
class CreateUser(Resource):
    def post(self):
            parser = reqparse.RequestParser()
            parser.add_argument('email', type=str)
            parser.add_argument('username', type=str)
            parser.add_argument('password', type=str)
            args = parser.parse_args()
 
            _userEmail = args['email']
            _userName = args['username']
            _userPassword = args['password']
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.callproc('sp_create_user', (_userEmail, _userName, _userPassword))
            data = cursor.fetchall()
 
            if len(data) is 0:
                conn.commit()
                return {'StatusCode': '200', 'Message': 'User creation success'}
            else:
                return {'StatusCode': '1000', 'Message': str(data[0])}
 
api.add_resource(CreateUser, '/user')


if __name__ == "__main__":

    app.run()