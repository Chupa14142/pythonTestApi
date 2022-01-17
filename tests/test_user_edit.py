from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        first_name = register_data['firstName']
        print("firstName = " + first_name)
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_name = "Changed Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        print(response4.text)

        Assertions.assert_json_value_by_name(
            response4,
            "firstName",
            new_name,
            "Wrong name of user after edit"
        )

    def test_try_to_edit_without_auth(self):
        user_id = "10"

        new_name = "Changed Name"

        response = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": "dfdfdfdfdfdf"},
            cookies={"auth_sid": "dfdfdfdfdfdfdf"},
            data={"firstName": new_name})

        Assertions.assert_code_status(response, 400)
        expected_error = "Auth token not supplied"
        assert expected_error in response.text, f"Expected error: {expected_error} != {response.text}"

    def test_try_to_edit_another_user(self):
        # LOGIN
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response = MyRequests.post("/user/login", data=data)
            # requests.post("https://playground.learnqa.ru/api/user/login", data=data)

        auth_sid = self.get_cookie(response, "auth_sid")
        token = self.get_header(response, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response, "user_id")

        # TRY TO EDIT ANOTHER USER
        another_user_id = 22
        new_name = "Changed Name"
        response1 = MyRequests.put(
            f"/user/{another_user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name})

        Assertions.assert_code_status(response1, 400)

        expected_error_text = "Please, do not edit test users with ID 1, 2, 3, 4 or 5."
        assert expected_error_text in response1.text, f"Expected error: {expected_error_text} != {response.text}"

    def test_try_to_edit_user_email_without_symbol_at(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_invalid_email = self.prepare_registration_data(email="chupa1414gmail.com")

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_invalid_email}
        )

        Assertions.assert_code_status(response3, 400)

        expected_error_text = "Invalid email format"
        assert expected_error_text in response3.text, f"Expected error: {expected_error_text} != {response3.text}"



    def test_try_to_set_firstname_with_one_symbol(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data['email']
        password = register_data['password']
        user_id = self.get_json_value(response1, "id")

        # LOGIN
        login_data = {
            'email': email,
            'password': password
        }

        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        # EDIT
        new_invalid_firstName = "A"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_invalid_firstName}
        )

        Assertions.assert_code_status(response3, 400)

        expected_error_text = "Too short value for field firstName"
        assert expected_error_text in response3.text, f"Expected error: {expected_error_text} != {response3.text}"