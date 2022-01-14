import pytest

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserRegister(BaseCase):

    def test_create_user_successfully(self):
        data = self.prepare_registration_data()

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")


    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)

        response = MyRequests.post("/user", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_without_symbol_at(self):
        invalid_email = "emailwithoutat"
        data = self.prepare_registration_data(invalid_email)

        response = MyRequests.post("/user", data=data)
        expected_error_text = "Invalid email format"
        expected_status_code = 400
        Assertions.assert_code_status(response, expected_status_code)
        assert expected_error_text in response.text, f"{expected_error_text} != {response.text}"


    fields_to_delete = {
        ("email"),
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName")
    }

    @pytest.mark.parametrize('field_to_delete', fields_to_delete)
    def test_check_create_user_without_one_field(self, field_to_delete):
        data = self.prepare_register_data_without_field_by_name(field_name_to_delete=field_to_delete)
        response = MyRequests.post("/user", data=data)

        expected_status_code = 400
        Assertions.assert_code_status(response, expected_status_code)

        expected_error_text = f"The following required params are missed: {field_to_delete}"
        assert expected_error_text in response.text, f"Expected error text: {expected_error_text} != Actual: {response.text}"

    def test_create_user_with_short_name(self):
        data = self.prepare_registration_data(username='a')

        response = MyRequests.post("/user", data=data)
        expected_error_text = "The value of 'username' field is too short"
        expected_status_code = 400

        Assertions.assert_code_status(response, expected_status_code)
        assert expected_error_text in response.text, f"{expected_error_text} != {response.text}"

    def test_create_user_with_long_name(self):
        data = self.prepare_registration_data(username='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')

        response = MyRequests.post("/user", data=data)
        expected_error_text = "The value of 'username' field is too long"
        expected_status_code = 400

        Assertions.assert_code_status(response, expected_status_code)
        assert expected_error_text in response.text, f"{expected_error_text} != {response.text}"
