# -*- coding: utf-8 -*-
# В самом окне добавил виджет txt и scrolledtext
# Благодаря txt я получаю имя пользователя GitHub, в scrolledtext выводятся полученные данные
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import requests
import json


def clickJSON():
    username = str(txt.get())
    url = f"https://api.github.com/users/{username}"
    user_data = (requests.get(url).json())
    txt1.insert(1.0, user_data)

def WriteJson():
    username = str(txt.get())
    response = requests.get(f"https://api.github.com/users/{username}")
    DataFind = json.loads(response.text)
    data = {
        'company': DataFind['company'],
        'created_at': DataFind['created_at'],
        'email': DataFind['email'],
        'id': DataFind['id'],
        'name': DataFind['name'],
        'url': DataFind['url'],
    }
    with open('data.json', 'a') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')
    outfile.close()
    messagebox.showinfo(title="data.json",message="В файл занесено искомое")

def cleartext():
    txt1.delete(1.0, END)


window = Tk()
window.title("FindJSON")
window.geometry('700x500')
window["bg"] = "blue"
txt = Entry(window, width=23, bg='yellow')
txt.grid(column=2, rows=2)
'''--------------------------------------'''
lbl = Label(window, text="<-Введите имя пользователя GitHub", bg="yellow")
lbl.grid(column=4, rows=2)
btn = Button(window, text="Получение JSON", bg="red", command=clickJSON)
btn.grid(column=2, rows=2)
btn = Button(window, text="Очистка поля", bg="red", command=cleartext)
btn.grid(column=2, rows=2)
btn = Button(window, text="Занести в файл искомое", bg = "red", command=WriteJson)
btn.grid(column=2,rows=2)
txt1 = scrolledtext.ScrolledText(window, width=30, height=25)
txt1.grid(column=10, row=10)
'''--------------------------------------'''
window.mainloop()