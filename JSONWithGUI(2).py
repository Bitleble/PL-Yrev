# -*- coding: utf-8 -*-
# В самом окне добавил виджет txt и scrolledtext
# Благодаря txt я получаю имя пользователя GitHub, в scrolledtext выводятся полученные данные
from tkinter import *
from tkinter import scrolledtext
import requests


def clickJSON():
    username = str(txt.get())
    url = f"https://api.github.com/users/{username}"
    user_data = (requests.get(url).json())
    txt1.insert(1.0, user_data)

def cleartext():
    txt1.delete(1.0,END)


window = Tk()
window.title("FindJSON")
window.geometry('1000x500')
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
txt1 = scrolledtext.ScrolledText(window, width=50, height=50)
txt1.grid(column=10, row=10)
'''--------------------------------------'''
window.mainloop()