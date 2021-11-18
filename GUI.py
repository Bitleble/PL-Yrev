from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import messagebox

def new_click():
    n=open('NewFile.txt','a+')
    messagebox.showinfo('Создание файла', 'Файл успешно сохранён под именем NewFile')


def edit_click():
    file = open('NewFile.txt', 'r')
    res = file.readline()
    lbl2.configure(text=res)
    text.insert(1.0, res)
    file.close()

def save_click():
    file1 = open('NewFile.txt', 'w')
    file1.write(text.get(1.0, END))
    text.delete(1.0, END)
    messagebox.showinfo('Редактирование файла','Файл успешно сохранён')






def zad1(chk_state, chk1_state, chk2_state):
    if ((chk_state == True) and (chk2_state == True) and (chk1_state == True)):
        return 1, 2, 3
    if ((chk1_state == True) and (chk_state == True)):
        return 1, 2
    if ((chk1_state == True) and (chk2_state == True)):
        return 2, 3
    if ((chk_state == True) and (chk2_state == True)):
        return 1, 3
    if (chk_state == True):
        return 1
    if (chk1_state == True):
        return 2
    if (chk2_state == True):
        return 3


def calkul(operation, operand1, operand2):
    result = 0
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    return result


def Chet1():
    messagebox.showinfo('Отчёт по нажатию',"Вы нажали : {}".format(zad1(chk_state.get(), chk1_state.get(), chk2_state.get())))


def Chet():
    res = "Результат: {}".format(calkul(combo.get(), int(txt.get()), int(txt1.get())))
    lbl1.configure(text=res)


window = Tk()
window.title("Юрьев С.В")
window.geometry('500x260')
window["bg"] = "blue"
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
style = ttk.Style(tab1)
style.configure('TLabel', background='blue', foreground='white')
style.configure('TFrame', background='blue')
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

main_menu = Menu()
file_menu = Menu(tearoff=False)
main_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_click)
file_menu.add_command(label="Open",command=edit_click)
file_menu.add_command(label="Save",command=save_click)
file_menu.add_separator()
file_menu.add_command(label="Exit")
window.config(menu=main_menu)
'''--------------------------------------'''
s = ttk.Style()
s.configure('custom.TRadiobutton',
        background='blue',
        foreground='yellow')
tab_control.add(tab1, text='Калькулятор')
txt = Entry(tab1, width=23,bg='yellow')
txt.grid(column=1, rows=1)
combo = Combobox(tab1)
combo['values'] = ('+', '-', '/', '*')
combo.current(0)  # установите вариант по умолчанию
combo.grid(column=1, row=2)
txt1 = Entry(tab1, width=23,bg='yellow')
txt1.grid(column=1, rows=3)
btn = Button(tab1, text="Счёт", command=Chet)
btn.grid(column=2, row=3)
lbl1 = Label(tab1, text='Результат: ',bg='yellow')
lbl1.grid(column=3, row=2)
'''---------------------------------------'''
tab_control.add(tab3, text='                                           ')
tab_control.add(tab2, text='Чекбоксы')
chk_state = BooleanVar()
chk_state.set(False)
chk1_state = BooleanVar()
chk1_state.set(False)
chk2_state = BooleanVar()
chk2_state.set(False)
chk = Checkbutton(tab2, text='Это первый', var=chk_state,style='custom.TRadiobutton')
chk1 = Checkbutton(tab2, text='Это второй', var=chk1_state,style='custom.TRadiobutton')
chk2 = Checkbutton(tab2, text='Это третий ', var=chk2_state,style='custom.TRadiobutton')
chk.grid(column=0, row=0)
chk1.grid(column=0, row=1)
chk2.grid(column=0, row=2)
btn1 = Button(tab2, text="Проверка нажатия", command=Chet1)
btn1.grid(column=1, row=0)
'''----------------------------------------'''
tab_control.add(tab4, text='                                           ')
tab_control.add(tab5, text='Чтение файла')
lbl2 = Label(tab5, text='Здесь будет ваш исходный текст ',bg='yellow')
lbl2.grid(column=0, row=0)
text = Text(width=50, height=10, bg="white",
            fg='blue', wrap=WORD)
text.pack()
'''----------------------------------------'''
tab_control.pack(expand=1, fill='both')
window.mainloop()