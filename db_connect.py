import math
import sqlite3
from tkinter import *
from tkinter import ttk, scrolledtext
from textwrap import wrap
from matplotlib import pyplot as plt
# В день может быть совершена одна покупка товара из одной категории , всего дне 365 ,
conn = sqlite3.connect('Build0.6.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS groups(
   kod INT,
   Den INT,
   kategor TEXT,
   tovar TEXT,
   zatrati INT);
""")
conn.commit()
b = []
c = []
summall = []
summcode = []
summkat = []
def gruppchange():
    dannie = (int(txt.get()), int(txt1.get()), txt2.get(),txt3.get(),int(txt4.get()))
    cur.execute("insert into groups VALUES(?,?,?,?,?);", dannie)
    conn.commit()

def info():
    tovt = txtt.get()
    vetv1 = Tk()
    vetv1.geometry('400x400')
    vibort = """select * from groups where tovar = ?"""
    cur.execute(vibort, (tovt,))
    records = cur.fetchall()
    textt = scrolledtext.ScrolledText(vetv1, width=30, height=50)
    textt.grid(column=10, row=10)
    for row in records:
        res = "Код: {}".format(row[0]) + '\n' + "Категория:{}".format(row[2])+'\n' + '\n'
        textt.insert(1.0, res)
        break
    vetv1.mainloop()

def vivodlingr():
    den = int(txtk.get())
    den1 = int(txtk1.get())
    tov = txtk2.get()
    root = Tk()
    root.geometry('400x400')
    vibor = """select * from groups where Den = ? and kategor = ?"""
    text = scrolledtext.ScrolledText(root, width=30, height=50)
    text.grid(column=10, row=10)
    for i in range(den,den1+1):
      cur.execute(vibor, (i,tov))
      records = cur.fetchall()
      for row in records:
        res = "Код: {}".format(row[0])+'\n'+"День:{}".format(row[1])+'\n'+"Категория:{}".format(row[2])+'\n'+"Товар:{}".format(row[3])+'\n'+'\n'
        text.insert(1.0, res)
    root.mainloop()

def graph1():
    vibor = """select * from groups where Den = ?"""
    for i in range(365):
      cur.execute(vibor, (i,))
      records = cur.fetchall()
      for row in records:
        b.append(row[1])
        c.append(row[4])
    plt.title("Расходы")
    plt.xlabel('Дни года')
    plt.ylabel('Потраченная сумма в рублях')
    plt.plot(b, c)
    plt.show()

def graph2():
    vibor = """select * from groups where Den = ?"""
    for i in range(365):
      cur.execute(vibor, (i,))
      records = cur.fetchall()
      for row in records:
        b.append(row[1])
        c.append(row[4])
    plt.bar(b, c, color='blue')
    plt.title("Расходы")
    plt.xlabel('Дни года')
    plt.ylabel('Потраченная сумма в рублях')
    plt.show()

def shellSort(array,c):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            temp1 = c[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                c[j] = c[j-interval]
                j -= interval
            array[j] = temp
            c[j] = temp1
        k -= 1
        interval = 2**k -1
    return array, c

def tablic():
    vetv2 = Tk()
    vetv2.geometry('400x400')
    textt1 = scrolledtext.ScrolledText(vetv2, width=30, height=50)
    textt1.grid(column=10, row=10)
    vibor = """select * from groups where Den = ?"""
    for i in range(365):
      cur.execute(vibor, (i,))
      records = cur.fetchall()
      for row in records:
        b.append(row[1])
        c.append(row[4])
    shellSort(b,c)
    b.reverse()
    c.reverse()
    res = 'День | Затраты(в рублях)'+'\n'
    textt1.insert(1.0, res)
    for i in range(len(b)):
        res1 = str(b[i])+'  |  '+str(c[i])+'\n'
        textt1.insert(2.0,res1)
    vetv2.mainloop()

def summall1():
    vibor = """select * from groups where Den = ?"""
    for i in range(365):
      cur.execute(vibor, (i,))
      records = cur.fetchall()
      for row in records:
        summall.append(row[4])
    txts2.insert(0,sum(summall))
    summall.clear()

def summcode1():
    vibor = """select * from groups where kod = ?"""
    kod1 = int(txts.get())
    cur.execute(vibor, (kod1,))
    records = cur.fetchall()
    for row in records:
        summcode.append(row[4])
    txts.delete(0,END)
    txts.insert(0,sum(summcode))
    summcode.clear()

def summkategor():
    vibor = """select * from groups where kategor = ?"""
    kategor1 = txts1.get()
    cur.execute(vibor, (kategor1,))
    records1 = cur.fetchall()
    for row in records1:
        summkat.append(row[4])
    txts1.delete(0, END)
    txts1.insert(0, sum(summkat))
    summkat.clear()



window = Tk()
window.geometry('625x500')
window["bg"] = "blue"
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
text = 'Введите данные нового элемента :(1.Код 2.День/Временной промежуток 3.Категория 4.Продукт 5.Затраты)'
tab_control.add(tab1, text='Изменение таблицы групп')
tab_control.add(tab2, text='Сортировка по дням')
tab_control.add(tab3, text='Информация по товару')
tab_control.add(tab4, text='График трат')
tab_control.add(tab5, text='Затраты')
lbl1 = Label(tab1, text=text,bg='yellow')
lbl1.grid(column=1, row=2)
window.update()
width = lbl1.winfo_width()
if width > 600:
    char_width = width / len(text)
    wrapped_text = '\n'.join(wrap(text, int(600 / char_width)))
    lbl1['text'] = wrapped_text
txt = Entry(tab1, width=23,bg='yellow')
txt.grid(column=1, rows=1)
txt1 = Entry(tab1, width=23,bg='yellow')
txt1.grid(column=1, rows=1)
txt2 = Entry(tab1, width=23,bg='yellow')
txt2.grid(column=1, rows=1)
txt3 = Entry(tab1, width=23,bg='yellow')
txt3.grid(column=1, rows=1)
txt4 = Entry(tab1, width=23,bg='yellow')
txt4.grid(column=1, rows=1)
btn = Button(tab1, text="Добавление", command=gruppchange)
btn.grid(column=1, row=10)
'''------------------------------------------'''
lbl2 = Label(tab2,text = 'Поиск по дням и товарам', bg = 'yellow')
lbl2.grid(column=1, row=2)
txtk = Entry(tab2, width=23,bg='yellow')
txtk.grid(column=1, rows=1)
txtk1 = Entry(tab2, width=23,bg='yellow')
txtk1.grid(column=1, rows=1)
txtk2 = Entry(tab2, width=23,bg='yellow')
txtk2.grid(column=1, rows=1)
lblt = Label(tab2,text ='(1,2 дни между которыми искать.3 Категория)',bg = 'yellow')
lblt.grid(column=1, row=1)
btn1 = Button(tab2, text="Считывание", command=vivodlingr)
btn1.grid(column=1, row=7)
'''------------------------------------------'''
lbl3 = Label(tab3, text = 'Введите интересующий ТОВАР', bg = 'yellow')
lbl3.grid(column=1, row=1)
txtt = Entry(tab3, width=23,bg='yellow')
txtt.grid(column=1, rows=1)
btnt = Button(tab3, text="Вывод информации по товару", command=info)
btnt.grid(column=1, row=7)
'''-------------------------------------------'''
btng = Button(tab4, text="Линейный график", command=graph1)
btng.grid(column=1, row=7)
btng1 = Button(tab4, text="Столбатый график", command=graph2)
btng1.grid(column=2, row=7)
btng2 = Button(tab4, text="Таблица", command=tablic)
btng2.grid(column=3, row=7)
'''--------------------------------------------'''
lbls = Label(tab5, text = 'Конечная сумма в рублях(1.По коду 2.По категории 3.Полная сумма на данный момент)', bg = 'yellow')
lbls.grid(column=1, row=1)
txts = Entry(tab5, width=23,bg='yellow')
txts.grid(column=1, rows=1)
btns1 = Button(tab5, text="Cумма по коду", command=summcode1)
btns1.grid(column=2, row=3)
txts1 = Entry(tab5, width=23,bg='yellow')
txts1.grid(column=1, rows=1)
btns2 = Button(tab5, text="Сумма по категории", command=summkategor)
btns2.grid(column=2, row=5)
txts2 = Entry(tab5, width=23,bg='yellow')
txts2.grid(column=1, rows=1)
btns3 = Button(tab5, text="Общая сумма", command=summall1)
btns3.grid(column=2, row=7)
tab_control.pack(expand=1, fill='both')
window.mainloop()