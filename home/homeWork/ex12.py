import requests

response = requests.get("https://playground.learnqa.ru/api/homework_header")
print(response.headers)
headers = [
    'Content-Type',
    'Content-Length',
    'Connection',
    'Keep-Alive',
    'Server',
    'x-secret-homework-header',
    'Cache-Control',
]

headers_value = [
    'application/json',
    '15',
    'keep-alive',
    'timeout=10',
    'Apache',
    'Some secret value',
    'max-age=0'

]

i = 0
while i < len(headers):
    assert headers[i] in response.headers, f"Header {headers[i]} isn't in Headers"
    assert response.headers[headers[i]] == headers_value[i], f"Header value: {headers_value[i]} is invalid"
    i = i + 1













