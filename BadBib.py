import requests
import telebot
from bs4 import BeautifulSoup

bot = telebot.TeleBot('5205867083:AAGG27PmKJJ2-uxNwh7QcsADzkR56ldckRg')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь )')
@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Напишите запрос для поиска рецепта ')

@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Поиск рецептов связанных с: ' + message.text)
    s = requests.Session()
    inin = s.get('https://povar.ru/xmlsearch?query={}'.format(message.text))
    soup = BeautifulSoup(inin.text, 'lxml')
    q = soup.find_all('a',class_='listRecipieTitle')
    i = 0
    i1 = 0
    for word in q:
        i += 1
        bot.send_message(message.chat.id, str(i) + ' ' + word.text)
    for link in soup.find_all('a',class_='listRecipieTitle'):
        if link.get('href') != None:
            i1 += 1
            bot.send_message(message.chat.id, str(i1)+' '+' https://povar.ru'+str(link.get('href')))



bot.polling(none_stop=True, interval=0)