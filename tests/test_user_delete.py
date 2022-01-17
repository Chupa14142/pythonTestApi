from lib.my_requests import MyRequests
from lib.assertions import Assertions
from lib.base_case import BaseCase
import allure


@allure.epic("Delete cases")
@allure.description("This is for Ex19: Теги Allure")
@allure.severity(allure.severity_level.CRITICAL)
class TestUserDelete(BaseCase):
    def test_try_to_delete_hardcore_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        user_id = "2"

        # LOGIN
        response = MyRequests.post("/user/login", data=data)
        auth_sid = response.cookies.get("auth_sid")
        token = response.headers.get("x-csrf-token")

        # DELETE USER
        response1 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid})

        Assertions.assert_code_status(response1, 400)

        expected_error_text = "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        assert expected_error_text in response1.text


    def test_delete_user_after_create(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        print("\n --- Created user data ---")
        print("User id: " + user_id)
        print("User email: " + email)
        print("User firstName: " + first_name)
        print("User password: " + password)
        print("-----------")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # GET
        response3 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response3, 200)
        Assertions.assert_json_value_by_name(response3, "id", user_id, f"Can't GET USER by expected id {user_id}. Actual id {response3.json()['id']}")

        print(f"\n Get user by id: {user_id}.\n Response DATA: " + response3.text)

        # DELETE
        response4 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response4, 200)

        # TRY To GET deleted USER
        response5 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response5, 404)

        expected_error_text = "User not found"
        assert expected_error_text in response5.text, f"expected_error_text != {response5.text}"


    def test_try_to_delete_another_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user", data=register_data)

        email = register_data['email']
        first_name = register_data['firstName']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        print("\n --- Created user data ---")
        print("User id: " + user_id)
        print("User email: " + email)
        print("User firstName: " + first_name)
        print("User password: " + password)
        print("-----------")

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)
        Assertions.assert_code_status(response2, 200)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # DELETE
        response4 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )
        Assertions.assert_code_status(response4, 400)
        expected_error_text = "Please, do not delete test users with ID 1, 2, 3, 4 or 5."
        assert expected_error_text in response4.text, f"{expected_error_text} != {response4.text}"