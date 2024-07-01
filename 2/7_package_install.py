import requests

response = requests.get('https://api.github.com')
print(response.status_code)  # 응답 코드 출력
print(response.json())  # JSON 형식의 응답 출력
