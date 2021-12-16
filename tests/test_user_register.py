import pytest
import requests
import json
from lib.base_case import BaseCase
from datetime import datetime
from lib.assertions import Assertions

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_create_user_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        print(response.content)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    def test_create_user_with_unexisting_email(self):
        email = 'vinkotovaexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.content.decode("utf-8") != f"Users with email '{email}' don't exist", f"Wrong {email} in {response.content}"
    

    params = [
        ("'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'"),
        ("'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'")
    ]

    @pytest.mark.parametrize("parameter", params)
    def test_create_user_without_parameter(self, parameter):
        self.response = requests.post("https://playground.learnqa.ru/api/user/", data=parameter)
        assert self.response.content.decode("utf-8") != f"The following required params are missed: email, password, username, firstName, lastName", f"User was not registered, because the request doesn't contain all needed parameters"

    def test_create_user_with_short_firstName(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.text != f"The value of 'firstName' field is too short", f"The value of 'firstName' field is too short"


    def test_create_user_with_long_firstName(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. Вдали от всех живут они в буквенных домах на берегу Семантика большого языкового океана. Маленький ручеек Даль журчит по всей стране и обеспечивает ее всеми необходимым',
            'lastName': 'learnqa',
            'email': email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        assert response.text != f"The value of 'firstName' field is too long", f"The value of 'firstName' field is too long"
