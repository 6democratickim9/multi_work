import unittest #중요한 부분. 잘 만들었는지 판단할 수 있는 기준. 단위테스트를 위한 코드
import json
import rest1

class FlaskTest(unittest.TestCase):#사용자 요구사항을 위해 만든것
    def setUp(self): # db연동 등등의 작업
        rest1.app.testing = True
        self.client = rest1.app.test_client()
        
    #def tearDown(self): # 리소스 반환작업
    #/api/multiply?param1=3&param2=4
    # 결과로 12나와야됨


    def test_index(self): 
        #setup을 위한 준비작업. 티어다운을 통해 작업마무리(옵션임)
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)
        # self.assertEqual(call, 12) #실제 값이 12면 성공
        #self.assertEqual(response.content_type,"text/html; charset")
        self.assertIn("text/html",response.content_type)
        self.assertEqual(response.charset, 'utf-8')

        content = response.data
        # 반환 데이터 확인
        self.assertEqual(content.decode('utf-8'), 'Hello, Flask!')

    def test_multiply(self):
        response = self.client.get('/api/multiply?param1=3&param2=4')
        self.assertEqual(response.status_code, 200)
        self.assertIn('application/json',response.content_type )
        # TDD 테스트코드로 정상적으로 만들어졌나 실험
        json_result = json.loads(response.data)
        self.assertEqual(json_result.get('state'),1)
        self.assertEqual(json_result.get('response'),12)

if __name__ == '__main__':
    unittest.main()