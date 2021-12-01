# -*- coding: utf-8 -*-
# Последняя цифра зачётки-5,нужен репозиторий языка Rust
# Для простого получения информации больше подойдёт уже следующая задача
# Тут я не стал заморачиватся и давать пользователю выбор, программа выводит только данные по репозиторию Rust
import requests
from pprint import pprint
username = "rust-lang"
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()
pprint(user_data)