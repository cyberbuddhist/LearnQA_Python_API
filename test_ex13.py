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

    #expected_results = dict(results)

    @pytest.mark.parametrize("parameter", params)
    @pytest.mark.parametrize("expected", expected_results)
    def test_user_agent(self, parameter, expected):
        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check",
                                headers={"User-Agent": parameter})
        response_parsed = response.json()

        assert response.json()["platform"] == expected["user_agent"][0]["platform"]
        assert response.json()["browser"] == expected["user_agent"][0]["browser"]
        assert response.json()["device"] == expected["user_agent"][0]["device"]





