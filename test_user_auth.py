import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        login_url = "https://playground.learnqa.ru/api/user/login"
        get_id_url = "https://playground.learnqa.ru/api/user/auth"

        response = requests.post(login_url, data=data)

        assert "auth_sid" in response.cookies, "There is no auth_sid in the response"
        assert "x-csrf-token" in response.headers, "There is no x-csrf-token in the headers"
        assert "user_id" in response.json(), "There is no user_id in the response"

        auth_sid = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")
        user_id_from_auth_method = response.json()["user_id"]

        response2 = requests.get(get_id_url, headers={"x-csrf-token": token}, cookies={"auth_sid": auth_sid})

        assert "user_id" in response2.json(), "There is no user_id in the response"
        user_id_from_check_method = response2.json()["user_id"]

        assert user_id_from_auth_method == user_id_from_check_method,\
            "User id from auth method is not equal to user id from check method"



