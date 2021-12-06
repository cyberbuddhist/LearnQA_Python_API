import pytest
import requests
import json

class TestUserAgent:
    params = [
        ('"user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"'),
        ('"user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"'),
        ('"user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"'),
        ('"user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"'),
        ('"user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"')
    ]

    @pytest.mark.parametrize("parameter", params)
    def test_user_agent(self, parameter):
        self.response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={"User-Agent": parameter})

        expected_results = [
            {
                "user_agent": [
                    {
                        "user_agent": "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                        "platform": "Mobile",
                        "browser": "No",
                        "device": "Android"
                    }
                ]
            },
            {
                "user_agent":[
                    {
                        "user_agent": "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1",
                        "platform": "Mobile",
                        "browser": "Chrome",
                        "device": "iOS"
                    }
                ]
            },
            {
                "user_agent": [
                    {
                        "user_agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                        "platform": "Googlebot",
                        "browser": "Unknown",
                        "device": "Unknown"
                    }
                ]
            },
            {
                "user_agent": [
                    {
                        "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0",
                        "platform": "Web",
                        "browser": "Chrome",
                        "device": "No"
                    }
                ]
            },
            {
                "user_agent": [
                    {
                        "user_agent": "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
                        "platform": "Mobile",
                        "browser": "No",
                        "device": "iPhone"
                    }
                ]
            }
        ]

        platform_value = self.response.json()["platform"]
        browser_value = self.response.json()["browser"]
        device_value = self.response.json()["device"]
        assert self.response.json()["platform"] == expected_results[0]["user_agent"][0]["platform"], f"Actual value of 'Platform' is not 'Mobile'. Platform value is {platform_value}"
        assert self.response.json()["platform"] == expected_results[1]["user_agent"][0]["platform"], f"Actual value of 'Platform' is not 'Mobile'. Platform value is {platform_value}"
        assert self.response.json()["platform"] == expected_results[2]["user_agent"][0]["platform"], f"Actual value of 'Platform' is not 'Googlebot'. Platform value is {platform_value}"
        assert self.response.json()["platform"] == expected_results[3]["user_agent"][0]["platform"], f"Actual value of 'Platform' is not 'Web'. Platform value is {platform_value}"
        assert self.response.json()["platform"] == expected_results[4]["user_agent"][0]["platform"], f"Actual value of 'Platform' is not 'Mobile'. Platform value is {platform_value}"
        assert self.response.json()["browser"] == expected_results[0]["user_agent"][0]["browser"], f"Actual value of 'Browser' is not 'No'. Browser value is {browser_value}"
        assert self.response.json()["browser"] == expected_results[1]["user_agent"][0]["browser"], f"Actual value of 'Browser' is not 'Chrome'. Browser value is {browser_value}"
        assert self.response.json()["browser"] == expected_results[2]["user_agent"][0]["browser"], f"Actual value of 'Browser' is not 'Unknown'. Browser value is {browser_value}"
        assert self.response.json()["browser"] == expected_results[3]["user_agent"][0]["browser"], f"Actual value of 'Browser' is not 'Chrome'. Browser value is {browser_value}"
        assert self.response.json()["browser"] == expected_results[4]["user_agent"][0]["device"], f"Actual value of 'Browser' is not 'No'. Browser value is {browser_value}"
        assert self.response.json()["device"] == expected_results[0]["user_agent"][0]["device"], f"Actual value of 'Device' is not 'Android'. Device value is {device_value}"
        assert self.response.json()["device"] == expected_results[1]["user_agent"][0]["device"], f"Actual value of 'Device' is not 'iOS'. Device value is {device_value}"
        assert self.response.json()["device"] == expected_results[2]["user_agent"][0]["device"], f"Actual value of 'Device' is not 'Unknown'. Device value is {device_value}"
        assert self.response.json()["device"] == expected_results[3]["user_agent"][0]["device"], f"Actual value of 'Device' is not 'No'. Device value is {device_value}"
        assert self.response.json()["device"] == expected_results[4]["user_agent"][0]["device"], f"Actual value of 'Device' is not 'iPhone'. Device value is {device_value}"