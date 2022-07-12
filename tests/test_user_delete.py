import email

from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):
    def test_user_delete(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        user_id = 2
        response2 = MyRequests.delete(
            f"user/{user_id}",
            data=data,
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_check_user_by_id_number(
            response2,
            user_id_from_auth_method,
            2,
            f"You want to delete user with id {user_id_from_auth_method}, but not user with id 2"
        )


    def test_positiv_user_delete(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")

        response2 = MyRequests.delete(
            f"user/{user_id_from_auth_method}",
            data=data,
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        response3 = MyRequests.get(
            f"user/{user_id_from_auth_method}",
            data=data,
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response3, 404)


    def test_delete_user_by_another_user_auth(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = MyRequests.post("/user/login", data=data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        user_id_from_auth_method = self.get_json_value(response1, "user_id")


        data = {
            'email': 'alekseeva@example.com',
            'password': '1234'
        }
        response2 = MyRequests.delete(
            f"user/{user_id_from_auth_method}",
            data=data,
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_check_user_by_email(response2, data['email'], "vinkotov@example.com", "Wrong user email was sent")

