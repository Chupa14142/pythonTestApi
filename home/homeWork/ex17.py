import requests

user_id = "1"
edit_url = f"https://playground.learnqa.ru/api/user/{user_id}"

response = requests.put(edit_url)

new_name = "Changed Name"

response3 = requests.put(edit_url,
            headers={"x-csrf-token": "dfdfdfdfdfdf"},
            cookies={"auth_sid": "dfdfdfdfdfdfdf"},
            data={"firstName": new_name})

expected_error = "Auth token not supplied"
assert expected_error in response3.text, f"Expected error: {expected_error} != {response3.text}"
