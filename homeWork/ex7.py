import requests

response1 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response1.text)

value = {"method": "put"}
response2 = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data=value)
print(response2.text)

value = {"method": "PUT"}
response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=value)
print(response3.text)
print("_____________________________")
