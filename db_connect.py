import math
import sqlite3
import pandas as pn
from tkinter import *
from tkinter import ttk, scrolledtext
from textwrap import wrap
import tkinter.messagebox as mb
from matplotlib import pyplot as plt

# База данных на год .

a = ''


def vv():
    global a
    a = str(txtv.get())
    vetvvv.destroy()


'''Функция для считывания имени db,для кнопки вводного окна'''


def importxls():
    exl = pn.read_sql('select * from groups', conn)
    exl.to_excel('{}.xlsx'.format(a), index=False)


'''В xlsx , для кнопки 1 вкладки основного окна,если названия одинаковы заменяет файл'''

vetvvv = Tk()
vetvvv["bg"] = '#90ee90'
vetvvv.title('Подключение к базе данных')
vetvvv.geometry('250x250')
txtv = Entry(vetvvv, width=23, bg='yellow')
txtv.grid(column=1, rows=1)
btnv = Button(vetvvv, text="  Добавление/Подключение к базе данных  ", command=vv)
btnv.grid(column=1, row=10)
vetvvv.mainloop()

conn = sqlite3.connect('{}.db'.format(a))
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS groups(
   Код INT,
   День INT,
   Категория TEXT,
   Товар TEXT,
   Расходы INT);
""")
conn.commit()
b = []
c = []
summall = []
summcode = []
summkat = []


def deletepokodu():
    vibort = '''delete from groups where Код = ? '''
    tovt = int(txt.get())
    cur.execute(vibort, (tovt,))
    conn.commit()


def deletepodnu():
    vibort = '''delete from groups where День = ? and Товар = ?'''
    tovt = int(txt1.get())
    tovt1 = txt3.get()
    cur.execute(vibort, (tovt, tovt1))
    conn.commit()


def deletepokat():
    vibort = '''delete FROM groups where Категория = ? '''
    tovt = txt2.get()
    cur.execute(vibort, (tovt,))
    conn.commit()


def deletetov():
    vibort = '''delete from groups where Товар = ? '''
    tovt = txt3.get()
    cur.execute(vibort, (tovt,))
    conn.commit()


'''Верхние 3 функции для удаления по данным'''


def shellsort(array, array1):
    n = len(array)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            temp1 = c[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                array1[j] = array1[j - interval]
                j -= interval
            array[j] = temp
            array1[j] = temp1
        k -= 1
        interval = 2 ** k - 1
    return array, array1


'''Сортировка Шелла'''


def dub(arr, arr1):
    lenn = len(arr)
    for i in range(lenn):
        if arr[i] == arr[i - 1]:
            cswap = i - 1
            arr1[cswap + 1] = arr1[cswap] + arr1[cswap + 1]
            arr[cswap] = 0
            arr1[cswap] = 0
    shellsort(arr, arr1)
    arr.reverse()
    arr1.reverse()
    for x in arr:
        if x == 0:
            arr.remove(0)
            arr1.remove(0)
    return arr, arr1


'''Одна из функций сложения суммы по дням, складывает суммы одинаковых дней и превращает в нули дубликаты'''


def gruppchange():
    dannie = (int(txt.get()), int(txt1.get()), txt2.get(), txt3.get(), int(txt4.get()))
    cur.execute("insert into groups VALUES(?,?,?,?,?);", dannie)
    conn.commit()


'''Запись в бузу данных'''


def info():
    tovt = txtt.get()
    proverka = False
    vetv1 = Tk()
    vetv1.title('Информация по товару')
    vetv1.geometry('400x400')
    vetv1["bg"] = '#90ee90'
    vibort = """select * from groups where Товар = ?"""
    cur.execute(vibort, (tovt,))
    records = cur.fetchall()
    textt = scrolledtext.ScrolledText(vetv1, width=30, height=50)
    textt.grid(column=10, row=10)
    for row in records:
        res = "Код: {}".format(row[0]) + '\n' + "Категория:{}".format(row[2]) + '\n' + '\n'
        textt.insert(1.0, res)
        proverka = True
        break
    if not proverka:
        mb.showerror(title='Ошибка', message='Такой товар не найден, проверьте написание')
        vetv1.destroy()
    vetv1.mainloop()


'''Информация по товару, для соответствующей кнопки'''


def vivodlingr():
    den = int(txtk.get())
    den1 = int(txtk1.get())
    tov = txtk2.get()
    proverka1 = False
    root = Tk()
    root["bg"] = '#90ee90'
    root.title('Сортировка по дням и категории')
    root.geometry('400x400')
    vibor = """select * from groups where День = ? and Категория = ?"""
    text1 = scrolledtext.ScrolledText(root, width=30, height=50)
    text1.grid(column=10, row=10)
    for i in range(den, den1 + 1):
        cur.execute(vibor, (i, tov))
        records = cur.fetchall()
        for row in records:
            res = "Код: {}".format(row[0]) + '\n' + "День:{}".format(row[1]) + '\n' + "Категория:{}".format(
                row[2]) + '\n' + "Товар:{}".format(row[3]) + '\n' + '\n'
            text1.insert(1.0, res)
            proverka1 = True
    if not proverka1:
        mb.showerror(title='Ошибка', message='Не найдено товаров по введённым данным')
        root.destroy()
    root.mainloop()


'''Сортировка по дням и категориям'''


def graph1():
    vibor = """select * from groups where День = ?"""
    for i in range(365):
        cur.execute(vibor, (i,))
        records = cur.fetchall()
        for row in records:
            b.append(row[1])
            c.append(row[4])
    shellsort(b, c)
    b.reverse()
    c.reverse()
    dub(b, c)
    for x in b and c:
        if x == 0:
            b.remove(x)
            c.remove(x)
    plt.title("Расходы")
    plt.xlabel('Дни года')
    plt.ylabel('Потраченная сумма в рублях')
    plt.plot(b, c, color='red')
    plt.show()
    b.clear()
    c.clear()


'''График 1(Линейный)'''


def graph2():
    vibor = """select * from groups where День = ?"""
    for i in range(365):
        cur.execute(vibor, (i,))
        records = cur.fetchall()
        for row in records:
            b.append(row[1])
            c.append(row[4])
    shellsort(b, c)
    b.reverse()
    c.reverse()
    dub(b, c)
    for x in b and c:
        if x == 0:
            b.remove(x)
            c.remove(x)
    plt.bar(b, c, color='blue')
    plt.title("Расходы")
    plt.xlabel('Дни года')
    plt.ylabel('Потраченная сумма в рублях')
    plt.show()
    b.clear()
    c.clear()


'''График2(Столбчатый)'''


def tablic():
    vetv2 = Tk()
    vetv2.title('Таблица расходов')
    vetv2.geometry('400x400')
    vetv2["bg"] = '#90ee90'
    textt1 = scrolledtext.ScrolledText(vetv2, width=30, height=30)
    textt1.grid(column=10, row=10)
    vibor = """select * from groups where День = ?"""
    for i in range(365):
        cur.execute(vibor, (i,))
        records = cur.fetchall()
        for row in records:
            b.append(row[1])
            c.append(row[4])
    shellsort(b, c)
    b.reverse()
    c.reverse()
    dub(b, c)
    for x in b and c:
        if x == 0:
            b.remove(x)
            c.remove(x)
    res = 'День | Затраты(в рублях)' + '\n'
    textt1.insert(1.0, res)
    for x in b and c:
        if x == 0:
            b.remove(x)
            c.remove(x)
    for i in range(len(b)):
        res1 = str(b[i]) + '  |  ' + str(c[i]) + '\n'
        textt1.insert(2.0, res1)
    b.clear()
    c.clear()
    vetv2.mainloop()


'''Таблица расходов'''


def summall1():
    vibor = """select * from groups where День = ?"""
    for i in range(365):
        cur.execute(vibor, (i,))
        records = cur.fetchall()
        for row in records:
            summall.append(row[4])
    txts2.insert(0, sum(summall))
    summall.clear()


def summcode1():
    vibor = """select * from groups where Код = ?"""
    kod1 = int(txts.get())
    cur.execute(vibor, (kod1,))
    records = cur.fetchall()
    for row in records:
        summcode.append(row[4])
    txts.delete(0, END)
    txts.insert(0, sum(summcode))
    summcode.clear()


def summkategor():
    vibor = """select * from groups where Категория = ?"""
    kategor1 = txts1.get()
    cur.execute(vibor, (kategor1,))
    records1 = cur.fetchall()
    for row in records1:
        summkat.append(row[4])
    txts1.delete(0, END)
    txts1.insert(0, sum(summkat))
    summkat.clear()


'''3 функции для сумм'''

window = Tk()
window.title('Учёт расходов')
window.geometry('725x425')
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
text = 'Введите данные нового элемента :(1.Код 2.День/Временной промежуток 3.Категория 4.Продукт 5.Затраты)' \
       'Удаление по коду удаляет все данные по это категории,удаление по категории работает аналогично,удаление' \
       ' по товару удаляет информацию по одному товару.' \
       'При удалении заполните только используемое окно(Например для удалении по коду заполните только код)'
tab_control.add(tab1, text='Изменение таблицы групп')
tab_control.add(tab2, text='Сортировка по дням')
tab_control.add(tab3, text='Информация по товару')
tab_control.add(tab4, text='График трат')
tab_control.add(tab5, text='Затраты')
lbl1 = Label(tab1, text=text, bg='yellow')
lbl1.grid(column=1, row=2)
window.update()
width = lbl1.winfo_width()
if width > 600:
    char_width = width / len(text)
    wrapped_text = '\n'.join(wrap(text, int(600 / char_width)))
    lbl1['text'] = wrapped_text
txt = Entry(tab1, width=23, bg='yellow')
txt.grid(column=1, rows=1)
txt1 = Entry(tab1, width=23, bg='yellow')
txt1.grid(column=1, rows=1)
txt2 = Entry(tab1, width=23, bg='yellow')
txt2.grid(column=1, rows=1)
txt3 = Entry(tab1, width=23, bg='yellow')
txt3.grid(column=1, rows=1)
txt4 = Entry(tab1, width=23, bg='yellow')
txt4.grid(column=1, rows=1)
btn = Button(tab1, text="Добавление", command=gruppchange, bg='#90ee90')
btn.grid(column=1, row=10)
btnd = Button(tab1, text="Удаление по коду", command=deletepokodu, bg='#90ee90')
btnd.grid(column=1, row=11)
btnd1 = Button(tab1, text="Удаление по дню+товару", command=deletepodnu, bg='#90ee90')
btnd1.grid(column=1, row=14)
btnd2 = Button(tab1, text="Удаление по категории", command=deletepokat, bg='#90ee90')
btnd2.grid(column=1, row=12)
btnd3 = Button(tab1, text="Удаление товара", command=deletetov, bg='#90ee90')
btnd3.grid(column=1, row=13)
btnxl = Button(tab1, text="Импорт в xlxs", command=importxls, bg='#90ee90')
btnxl.grid(column=2, row=13)
'''------------------------------------------'''
lbl2 = Label(tab2, text='Поиск по дням и товарам', bg='yellow')
lbl2.grid(column=1, row=2)
txtk = Entry(tab2, width=23, bg='yellow')
txtk.grid(column=1, rows=1)
txtk1 = Entry(tab2, width=23, bg='yellow')
txtk1.grid(column=1, rows=1)
txtk2 = Entry(tab2, width=23, bg='yellow')
txtk2.grid(column=1, rows=1)
lblt = Label(tab2, text='(1,2 дни между которыми искать.3 Категория)', bg='yellow')
lblt.grid(column=1, row=1)
btn1 = Button(tab2, text="Считывание", command=vivodlingr, bg='#90ee90')
btn1.grid(column=1, row=7)
'''------------------------------------------'''
lbl3 = Label(tab3, text='Введите интересующий ТОВАР', bg='yellow')
lbl3.grid(column=1, row=1)
txtt = Entry(tab3, width=23, bg='yellow')
txtt.grid(column=1, rows=1)
btnt = Button(tab3, text="Вывод информации по товару", command=info, bg='#90ee90')
btnt.grid(column=1, row=7)
'''-------------------------------------------'''
btng = Button(tab4, text="Линейный график", command=graph1, bg='#90ee90')
btng.grid(column=1, row=7)
btng1 = Button(tab4, text="Столбатый график", command=graph2, bg='#90ee90')
btng1.grid(column=2, row=7)
btng2 = Button(tab4, text="Таблица", command=tablic, bg='#90ee90')
btng2.grid(column=3, row=7)
'''--------------------------------------------'''
lbls = Label(tab5, text='Конечная сумма в рублях(1.По коду 2.По категории 3.Полная сумма на данный момент)',
             bg='yellow')
lbls.grid(column=1, row=1)
txts = Entry(tab5, width=23, bg='yellow')
txts.grid(column=1, rows=1)
btns1 = Button(tab5, text="Cумма по коду", command=summcode1, bg='#90ee90')
btns1.grid(column=2, row=3)
txts1 = Entry(tab5, width=23, bg='yellow')
txts1.grid(column=1, rows=1)
btns2 = Button(tab5, text="Сумма по категории", command=summkategor, bg='#90ee90')
btns2.grid(column=2, row=5)
txts2 = Entry(tab5, width=23, bg='yellow')
txts2.grid(column=1, rows=1)
btns3 = Button(tab5, text="Общая сумма", command=summall1, bg='#90ee90')
btns3.grid(column=2, row=7)
tab_control.pack(expand=1, fill='both')
window.mainloop()
