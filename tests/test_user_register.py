import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("Register new user cases")
class TestUserRegister(BaseCase):
    @allure.description("This test registers user successfully")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.story
    @allure.description("This test creates new user using existing in database email")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = self.prepare_registration_data(email)
        response = MyRequests.post("/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {response.content}"

    @allure.description("This test creates user using incorrect email")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason='this test is expecting failure')
    def test_create_user_with_unexisting_email(self):
        email = 'vinkotovaexample.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }
        response = MyRequests.post("/user/", data=data)
        assert response.content.decode("utf-8") != f"Users with email '{email}' don't exist", f"Wrong {email} in {response.content}"
    

    params = [
        ("'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa'"),
        ("'password': '123', 'username': 'learnqa', 'firstName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'password': '123', 'username': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'password': '123', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'"),
        ("'username': 'learnqa', 'firstName': 'learnqa', 'lastName': 'learnqa', 'email': 'vinkotov@example.com'")
    ]

    @allure.description("This test registers user without necessary parameters")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.xfail(reason='this test is expecting failure')
    @pytest.mark.parametrize("parameter", params)
    def test_create_user_without_parameter(self, parameter):
        self.response = MyRequests.post("/user/", data=parameter)
        assert self.response.content.decode("utf-8") != f"The following required params are missed: email, password, username, firstName, lastName", f"User was not registered, because the request doesn't contain all needed parameters"

    @allure.description("This test registers user with short first name in one symbol")
    @pytest.mark.xfail(reason='this test is expecting failure')
    def test_create_user_with_short_firstName(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'l',
            'lastName': 'learnqa',
            'email': email
        }
        response = MyRequests.post("/user/", data=data)
        assert response.text != f"The value of 'firstName' field is too short", f"The value of 'firstName' field is too short"

    @allure.description("This test registers user with long first name more then 250 symbols")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.xfail(reason='this test is expecting failure')
    def test_create_user_with_long_firstName(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'Далеко-далеко за словесными горами в стране гласных и согласных живут рыбные тексты. Вдали от всех живут они в буквенных домах на берегу Семантика большого языкового океана. Маленький ручеек Даль журчит по всей стране и обеспечивает ее всеми необходимым',
            'lastName': 'learnqa',
            'email': email
        }
        response = MyRequests.post("/user/", data=data)
        assert response.text != f"The value of 'firstName' field is too long", f"The value of 'firstName' field is too long"
