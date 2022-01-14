import requests
from lib.assertions import Assertions


class TestClassEx16(Assertions):
    def test_check_asas(self):

        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_method = response1.json()["user_id"]

        another_user_id = "2"
        response2 = requests.get(f"https://playground.learnqa.ru/api/user/{another_user_id}",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}
                                 )

        keys_for_owner = ["username", "id", "email", "firstName", "lastName"]
        for key in keys_for_owner:
            assert key in response2.json(), f"Key {key} is not in response: {response2.json()}"

        response3 = requests.get(
            "https://playground.learnqa.ru/api/user/1",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        keys_for_not_owner = ["id", "email", "firstName", "lastName"]
        for key in keys_for_not_owner:
            assert key not in response3.json(), f"Key {key} is still in response: {response3.json()}"

        Assertions.assert_json_has_not_keys(response3, keys_for_not_owner)
