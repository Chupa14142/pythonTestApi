import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
response_to_json = response.json()
token = response_to_json['token']
value = {"token": token}
wait_seconds = response_to_json['seconds']


response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=value)
response1_to_json = response1.json()
valid_status = "Job is NOT ready"
if valid_status in response1_to_json['status']:
    print(response1.text)
else:
    print("Status is incorrect")

time.sleep(wait_seconds)
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=value)
response2_to_json = response2.json()
valid_status = "Job is ready"
if valid_status in response2_to_json['status']:
    print(response2.text)
else:
    print("Status is incorrect")

