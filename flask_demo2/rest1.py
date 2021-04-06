import flask
import flask_restful
from flask_restful import reqparse
from flask import Flask,jsonify, request

app = Flask(__name__)
#app.config["DEBUG"] = True #디버깅모드 켜기 -> 안됨
#실행 파일을 변경하려면 설정변수에 FLASK_APP=new_file.py로 설정하면됨
# 디버그로 하려면 CMD창에서 set FLASK_DEBUG=True -> auto refresh 
# 디버깅 모드는 개발자 모드에서만 사용!

api = flask_restful.Api(app)


@app.route('/')  #위의 api를 가져오는것
def index():
    return "Hello, Flask!"

def multiply(param1, param2): # 상태값을 갖는 것이 아니라 단순연산이기때문에 클래스 필요없음
    return param1 * param2



class HelloWorld(flask_restful.Resource): # 클래스 생성 시 레스트풀의 리소스 상속받아서 정의하면 됨
    def get(self): # 플라스크 안의 인스턴스는 반드시 셀프를 가짐/일반적 펑션이 아니라 method라고 부른다
        #전달하는 방법을 쿼리 스트링이라고 부른다. &가 들어오면 여러가지 파라미터를 넣을 수 있음
        # 많은 클래스가 해당 메소드 안으로만 들어간다
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


# 얘를 포스트 방식으로 호출하ㅏ면 에러남(포스트방식으로 만들지 않았기때문)
api.add_resource(HelloWorld,'/api/multiply') #수동으로 리소스 추가

if __name__ =='__main__':
    app.run()