import requests
import time
import json

#1.создается задача
response1 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job')
r = json.loads(response1.text)
my_token = r['token']

#2.запрос с token ДО того, как задача готова, убедиться в правильности поля status
response2 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token": my_token})

#убедиться что статус Job is NOT ready
v = json.loads(response2.text)
my_status = v['status']
if my_status == "Job is NOT ready":
    time.sleep(5)
    response3 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token": my_token})
    k = json.loads(response3.text)
    status1 = k['status']
    result1 = k['result']
    print(status1)
    print(result1)
    if status1 == 'Job is ready' and result1 == '42':
        print('AllRightStatus: Job is ready and result is 42')
    else:
        print('Wrong status')
elif my_status != "Job is NOT ready":
    response4 = requests.get('https://playground.learnqa.ru/ajax/api/longtime_job', params={"token": my_token})
    p = json.loads(response4.text)
    status2 = p['status']
    result2 = p['result']
    print(status2)
    print(result2)
    if status2 == 'Job is ready' and result2 == '42':
        print('AllRightStatus: Job is ready and result is 42')
    else:
        print('Wrong status')
