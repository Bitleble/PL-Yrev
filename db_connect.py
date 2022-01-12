import sqlite3
from tkinter import *
from tkinter import ttk, scrolledtext
from textwrap import wrap

conn = sqlite3.connect('Build0.5.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS groups(
   kod INT,
   Den INT,
   kategor TEXT,
   zatrati INT);
""")
conn.commit()

def gruppchange():
    dannie = (int(txt.get()), int(txt1.get()), txt2.get(), int(txt3.get()))
    cur.execute("INSERT INTO groups VALUES(?,?,?,?);", dannie)
    conn.commit()

def vivodlingr():
    den = int(txtk.get())
    den1 = int(txtk1.get())
    root = Tk()
    root.geometry('600x500')
    vibor = """select * from groups where Den = ?"""
    text = scrolledtext.ScrolledText(root, width=30, height=25)
    text.grid(column=10, row=10)
    for i in range(den,den1+1):
      cur.execute(vibor, (i,))
      records = cur.fetchall()
      for row in records:
        res = "Код: {}".format(row[0])+'\n'+"День:{}".format(row[1])+'\n'+"Категория:{}".format(row[2])+'\n'+"Траты:{}".format(row[3])+'\n'+'\n'
        text.insert(1.0, res)
    root.mainloop()

window = Tk()
window.geometry('600x500')
window["bg"] = "blue"
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
text = 'Введите данные нового элемента :(1.Код 2.День/Временной промежуток 3.Категория 4.Затраты) Единожды нажав кнопку вы заполняете ОПРЕДЕЛЁННЫЙ ВРЕМЕННОЙ ПРОМЕЖУТОК,не забывайте распределять сумму '
tab_control.add(tab1, text='Изменение таблицы групп')
tab_control.add(tab2, text='Сортировка по дням')
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
btn = Button(tab1, text="Счёт", command=gruppchange)
btn.grid(column=1, row=7)
'''------------------------------------------'''
lbl2 = Label(tab2,text = 'Поиск по категории', bg = 'yellow')
lbl2.grid(column=1, row=2)
txtk = Entry(tab2, width=23,bg='yellow')
txtk.grid(column=1, rows=1)
txtk1 = Entry(tab2, width=23,bg='yellow')
txtk1.grid(column=1, rows=1)
btn1 = Button(tab2, text="Считывание", command=vivodlingr)
btn1.grid(column=1, row=7)
lbl2 = Label(tab2, text='Здесь Будут полученные данные',bg='yellow')
lbl2.grid(column=1,row=11)
tab_control.pack(expand=1, fill='both')
window.mainloop()