import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
size_dict = response.history

print(f"Количество редиректов: {len(size_dict)}")
print(f"Redirects: {response.history}")
print(f"Последний url:  {response.url}")



