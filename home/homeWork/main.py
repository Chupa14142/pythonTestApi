import requests
import simplejson

payload = {"name": "EUGENE"}
response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)

try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except simplejson.errors.JSONDecodeError:
    print("Response is not a JSON format")