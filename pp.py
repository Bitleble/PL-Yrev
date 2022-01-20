import requests
from bs4 import BeautifulSoup
import webbrowser

proxies= {
    'http': 'socks5h://127.0.0.1:9050',
    'https': 'socks5h://127.0.0.1:9050',
}

nm = input('Введите Login: ')
ps = input('Введите пароль: ')
search = input('Введите поисковый запрос: ')
v = int(input('Введите количество записей: '))
s = requests.Session()
inin = s.post('https://rutracker.org/forum/login.php', {
    'login_username': '{}'.format(nm),
    'login_password': '{}'.format(ps),
    'login': 'вход',
},proxies=proxies)

inin1 = s.get('https://rutracker.org/forum/tracker.php?nm={}'.format(search),proxies=proxies)
soup = BeautifulSoup(inin1.text, 'lxml')
quotes = soup.find_all('a', class_='med tLink ts-text hl-tags bold')
q = soup.find_all('div', class_='t-tags')
t = 0
t1 = 0
print('Теги отвечают за скачивание ищите t-tags соответстующий необходимому торренту')
for word1 in q:
    t1 += 1
    print(t1, q[t1-1])
    if t1 == v:
        break

for word in quotes:
    t += 1
    print(t,word.text)
    if t == v:
         break

dowl = input('Введите t-tag нужного торрента: ')
webbrowser.register('operaGX', None, webbrowser.BackgroundBrowser(r"C:\Users\VV\AppData\Local\Programs\Opera GX\launcher.exe"))
webbrowser.get(using='operaGX').open('https://rutracker.org/forum/dl.php?t={}'.format(dowl))