import requests


response = requests.get("https://blog.naver.com/vega2k")
print("응답코드 : ",response.status_code)
#
# if response.status_code ==requests.codes.ok:
#     print("정상")
# else:
#     print("문제- 에러코드 ",response.status_code)

response.raise_for_status()

