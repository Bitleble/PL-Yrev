# -*- coding: utf-8 -*-
import requests
import json

# В задании чётко сказано какие элементы нам нужны, компания ,айди, имя и тд, значит для решения задачи
# достаточно просто доставать значения по очереди
# из DataFind достаю значения нужных мне полей
username = str(input('Введите имя пользователя: '))
response = requests.get(f"https://api.github.com/users/{username}")
DataFind = json.loads(response.text)
data = {
    'company': DataFind['company'],
    'created_at': DataFind['created_at'],
    'email': DataFind['email'],
    'id' : DataFind['id'],
    'name': DataFind['name'],
    'url': DataFind['url'],
}
# Создам json файл если такого нет и занесу туда необходимый словарь
with open('data.json', 'a') as outfile:
    json.dump(data, outfile)
outfile.close()