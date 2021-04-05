from flask import Flask,jsonify, request
from datetime import datetime
import uuid
# unique한 아이디를 만들어줌
app = Flask(__name__)


@app.route('/') 
#데코레이터 사용 -> 엔드포인트는 슬러쉬: 인덱스라 불리는 애가 호출되어 헬로월드가 반환될것

def index():
    return "Hello, World!"

@app.route('/health-check') # 엔드포인트 이름 등록
def health_check():
    return "Server is running on 5000 port"

#@app.route('/health-check/<portId>') 
#def health_checkid(portId):
#    return "Server is running on {} port".format(portId)

@app.route('/users') 
def users():
    return "** Users List"


@app.route('/users/<userId>') # 꺾쇠로 가변데이터 명시
def users_detail(userId):
    #return "{\"name\":%s}"% (userId) #%s를 사용해서 전달하고자 하는 값이 동적임을 명시
    return jsonify({"user_id":userId})

#반환하고자 하는 파일을 훨씬 직관적으로 표현 가능

@app.route('/users', methods = ['POST']) # 그냥 넣으면 겟이 되니 포스트 추가
def userAdd():
    user = request.get_json()
    user['user_id'] = uuid.uuid4() #uuid1번부터 5번까지 만들 수 있음
    # post 에서 변수가 유저로 전달됨 -> 전달된 값은 나중에 데베에 추가하거나 카프카 서버에 전송하는 등의 작업 추가로 가능
    user['created_at'] = datetime.today()
    return jsonify(user), 201 # 성공 코드 추가



if __name__ == "__main__":

    app.run()
    # 플라스크를 기동하면 필요한 어플리케이션 실행