import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
import requests


class TestForWork(BaseCase):
    fields_to_delete = {
        ("email"),
        ("password"),
        ("username"),
        ("firstName"),
        ("lastName")
    }

    @pytest.mark.parametrize('field_to_delete', fields_to_delete)
    def test_check(self, field_to_delete):

        data = self.prepare_register_data_without_field_by_name(field_name_to_delete=field_to_delete)
        response = requests.post("https://playground.learnqa.ru/api/user", data=data)

        expected_status_code = 400
        Assertions.assert_code_status(response, expected_status_code)

        expected_error_text = f"The following required params are missed: {field_to_delete}"
        assert expected_error_text in response.text, f"{expected_error_text} != {response.text}"
        print(response.text + "\n")



