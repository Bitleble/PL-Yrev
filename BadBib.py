from random import randint

import requests
import telebot
from bs4 import BeautifulSoup

f = open('Hihish.txt', 'r')
jokes = f.read().split('___')
f.close()

bot = telebot.TeleBot('5205867083:AAGG27PmKJJ2-uxNwh7QcsADzkR56ldckRg')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '/help для большей информации')
@bot.message_handler(commands=["help"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Доступные команды:'+'\n'+ '/hohma - авторские анекдоты '+'\n'+'/hohma1 - анекдоты с анекдоты.ру(официально самый артхаусный артхаус)'
                                +'\n'+'/recipe: Поиск рецептов по написанным ингридиентам')
@bot.message_handler(commands=['hohma'])
def hihi(message):
    i = randint(1,7)
    bot.send_message(message.chat.id, 'Партия держать меня в подвале, я работать за миска рис, посмейтесь, и я буду работать за два миска рис. ')
    bot.send_message(message.chat.id, jokes[i])

@bot.message_handler(commands=['hohma1'])
def haha(message):
    i = randint(1, 34)
    bot.send_message(message.chat.id, 'Гружу анекдот с анекдоты ру, боже зачем я должен это делать')
    s = requests.Session()
    inin = s.get('https://anekdoty.ru')
    soup = BeautifulSoup(inin.text, 'lxml')
    s = soup.find_all('p')
    bot.send_message(message.chat.id, s[i].text)

@bot.message_handler(commands=["recipe"])
def handle_text(message):
    send = bot.send_message(message.chat.id, 'Введите ингридиенты')
    bot.register_next_step_handler(send, recipe)


def recipe(message):
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