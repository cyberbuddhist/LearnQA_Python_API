import pytest
import requests
import json

class TestBrutePassword:
    def test_search_password(self):
        password_value=["password", "123456", "12345678", "qwerty", "abc123", "monkey", "1234567", "letmein",
                           "trustno1", "dragon", "baseball", "111111", "iloveyou", "master", "sunshine", "ashley",
                           "bailey", "passw0rd", "shadow", "123123", "654321", "superman", "qazwsx", "michael",
                        "Football", "1234567", "welcome", "ashley", "football", "jesus", "michael", "ninja", "mustang",
                        "password1", "123456789", "111111", "1234567", "adobe123", "123123", "admin", "1234567890",
                        "letmein", "photoshop", "1234", "12345", "princess", "azerty", "trustno1", "000000", "123456",
                        "access", "696969", "batman", "1qaz2wsx", "login", "qwertyuiop", "solo", "starwars", "121212",
                        "flower", "hottie", "loveme", "zaq1zaq1", "hello", "freedom", "whatever", "qazwsx", "666666",
                        "654321", "!@#$%^&*", "charlie", "aa123456", "donald", "qwerty123", "1q2w3e4r", "555555", "lovely",
                        "7777777", "888888", "123qwe"]

        for i in password_value:
            data = {
                'login': 'super_admin',
                'password': i
            }
            response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
            #print(response1.cookies)
            #print(response1.status_code)
            #print(response1.content)

            auth_from_response = response1.cookies
            auth_sid = auth_from_response.keys()
            auth_sid_value_not_string = auth_from_response.values()
            auth_sid_value = str(auth_sid_value_not_string)
            #print(auth_sid)
            #print(auth_sid_value)

            response2 = requests.get(
                "https://playground.learnqa.ru/ajax/api/check_auth_cookie",
                cookies={"auth_cookie":auth_sid_value})
            #print(response2.content)
            if response2.content != "You are NOT authorized":
                print(response2.content)
                print(i) #вывести правильный пароль
