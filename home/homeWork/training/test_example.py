import pytest
import requests


class TestExample:
    passwords = [
        ("secret_pass"),
        ("asasasasasas")
    ]




    @pytest.mark.parametrize('password', passwords)
    def test_example_check(self, password):
        get_auth_cookie = "https://playground.learnqa.ru/api/get_auth_cookie"
        check_auth_cookie = "https://playground.learnqa.ru/api/check_auth_cookie"

        payload = {"login": "secret_login", "password": password}
        response = requests.post(get_auth_cookie, data=payload)
        cookie_value = response.cookies.get('auth_cookie')
        cookies = {}
        if cookie_value is not None:
            cookies.update({"auth_cookie": cookie_value})

        response1 = requests.post(check_auth_cookie, cookies=cookies)
        print(response1.text)
        autorized_user = "You are authorized"
        not_autorized_user = "You are NOT authorized"

        if cookie_value is not None:
            assert autorized_user == response1.text, f"{autorized_user} == {response1.text}"
        else:
            assert not_autorized_user == response1.text, f"{not_autorized_user} != {response1.text}"
