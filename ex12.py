import requests

class TestResponseHeaders:
    def test_headers(self):
        self.response = requests.get("https://playground.learnqa.ru/api/homework_header")
        print(self.response.headers)

        assert "Date" in self.response.headers, "There is no 'Date' header"
        assert "application/json" in self.response.headers['Content-Type'], "There is no application/json type in 'Content-Type' header"
        assert "15" in self.response.headers['Content-Length'], "Content length is not equal 15"
        assert "keep-alive" in self.response.headers['Connection'], "Connection is not keep-alive"
        assert "timeout=10" in self.response.headers['Keep-Alive'], "Timeout is not 10 seconds"
        assert "Apache" in self.response.headers['Server'],  "Server is not Apache"
        assert "Some secret value" in self.response.headers['x-secret-homework-header'], "Value of x-secret-homework-header is not 'Some secret value'"
        assert "max-age=0" in self.response.headers['Cache-Control'], "Cache control is not 'max-age=0'"
        assert "Expires" in self.response.headers, "There is no 'Expires' header"