import requests

class TestResponse:
    def test_sending_response(self):
        self.response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        print(self.response.cookies)

        assert "HomeWork" in self.response.cookies, "There is no homework cookie in response"
        assert "hw_value" in self.response.cookies.values(), "There is another value of cookie"