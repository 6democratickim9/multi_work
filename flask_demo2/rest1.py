import flask
import flask_restful
from flask_restful import reqparse
from flask import Flask,jsonify, request

app = Flask(__name__)
app.config["DEBUG"] = True #디버깅모드 켜기
api = flask_restful.Api(app)


@app.route('/')
def index():
    return "Hello, Flask!"

def multiply(param1, param2): # 상태값을 갖는 것이 아니라 단순연산이기때문에 클래스 필요없음
    return param1 * param2



class HelloWorld(flask_restful.Resource):
    def get(self):
        parser = reqparse.RequestParser()

        parser.add_argument('param1')
        parser.add_argument('param2')
        args = parser.parse_args()
        # 주소값의 파라미터들 추가

        param1 = args['param1']
        param2 = args['param2']

        if (not param1) or (not param2):
            return {
                'state': 0,
                'response': None
            }

        param1 = int(param1)
        param2 = int(param2)

        result = multiply(param1,param2)

        return{
            'state':1,
            'response': result
        }

# api/multiply => GET지원, POST도 지원
# 하나의 클래스로 만들고 그 안에 리소스 넣는것도 괜찮음
# 주문 목록 /orders ( GET)
# 주문하기 / orders(POST)
# 주문 상세보기 /orders/ID (GET)
# 주문 수정하기 /orders/ID (PUT)
# 주문 삭제하기 /orders/ID (DELETE)

api.add_resource(HelloWorld,'/api/multiply') #수동으로 리소스 추가

if __name__ =='__main__':
    app.run()