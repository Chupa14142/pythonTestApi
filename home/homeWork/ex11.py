import requests

response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
print(response.cookies)

assert "HomeWork" in response.cookies
assert "hw_value" in response.cookies["HomeWork"]