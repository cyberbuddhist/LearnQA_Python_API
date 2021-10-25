import requests

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.history)
print(response.status_code)
print(response.text)

response = requests.post('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.history)
print(response.status_code)
print(response.text)

response = requests.put('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.history)
print(response.status_code)
print(response.text)

response = requests.delete('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.history)
print(response.status_code)
print(response.text)

#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response = requests.head('https://playground.learnqa.ru/ajax/api/compare_query_type')
print(response.history)
print(response.status_code)
print(response.text)

#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
response = requests.get('https://playground.learnqa.ru/ajax/api/compare_query_type', params={'method': 'GET'})
print(response.history)
print(response.status_code)
print(response.text)

'''4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. 
Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. 
И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, 
но сервер отвечает так, словно все ок. 
Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
'''
requested_methods = ['GET', 'POST', 'PUT', 'DELETE']
for i in requested_methods:
    for z in requested_methods:
        response = requests.request(i, 'https://playground.learnqa.ru/ajax/api/compare_query_type',
                                    params={'method': z})
        if i != z and response.status_code == 200:
            print("Method != Param, реальный тип запроса не совпадает со значением параметра")
            print(response.status_code)
            print(i)
            print(z)
        elif i == z and response.status_code == 400:
            print("Method == Param, типы запросов совпадают, но сервер отдает ошибку")
            print(response.status_code)
            print(i)
            print(z)
        elif i == z and response.status_code == 500:
            print("Method == Param, типы запросов совпадают, но сервер отдает ошибку")
            print(response.status_code)
            print(i)
            print(z)



