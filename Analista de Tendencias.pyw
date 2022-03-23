#Librerias
from tkinter import *
import tkinter as tk
from sentiment_analysis_spanish import sentiment_analysis
from GoogleNews import GoogleNews
from utils import resource_path,save
from PIL import ImageTk, Image



#Config ventana

window = Tk()
window.title("Analista de Tendencias")
window.geometry("1024x764")
window.configure(bg = "#e9ebf2")
window.resizable(False, False)


# Config BG

canvas = Canvas(window,bg = "#e9ebf2",height = 526,width = 957,bd = 0,relief = "ridge")
path = resource_path("background.png")
bg = PhotoImage(file = path)
background = canvas.create_image(517, 330,image = bg)
canvas.pack(side='top', fill=BOTH, expand=YES)


#Funciones

def dictionary ():
    win = Toplevel(window)
    win.title("Diccionario")
    win.geometry("957x526")
    win.configure(bg ="#c8deed")
    win.resizable(False, False)

    path = resource_path("bgdict.png")
    img = PhotoImage(file=path)
    widget = Label(win, image=img).pack()

    win.mainloop()

def ficha():

    win2 = Toplevel(window)
    win2.title("Ficha técnica")
    win2.configure(bg ="#F4F3F3")
    win2.geometry("957x526")
    win2.resizable(False, False)

    path = resource_path("bgficha.png")
    img1 = PhotoImage(file=path)
    widget = Label(win2, image=img1).pack()

    win2.mainloop()

def about():

    win3 = Toplevel(window)
    win3.title("Acerca del Analista de Tendencias")
    win3.configure(bg ="#F4F3F3")
    win3.geometry("957x526")
    win3.resizable(False, False)

    path = resource_path("bgabout.png")
    img = PhotoImage(file=path)
    widget = Label(win3, image=img).pack()
    win3.mainloop()

def copy():

    win4 = Toplevel(window)
    win4.title("Copyright ©")
    win4.configure(bg ="#F4F3F3")
    win4.geometry("764x125")
    win4.resizable(False, False)

    Label(win4, text= "Copyright © 2021\n All Rights Reserved\n This product is protected by copyright and distributed under licenses restricting copying, distribution and decompilation. \n CF Cristiam Alfredo Castro Cano \n Maria Paula Herrera Silva \n Monica Tatiana Chimbi Gil \n Cesar Mauricio Huertas Rivera").pack()
    win4.mainloop()

def py_copy():

    win5 = Toplevel(window)
    win5.title("Derechos de librerías utilizadas ©")
    win5.configure(bg ="#F4F3F3")
    win5.geometry("784x150")
    win5.resizable(False, False)

    Label(win5, text= "Copyright © 2021\n\n***For Google News, Figpy and Sentiment-Spanish (packages with MIT License)***\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the ''Software''),\n to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, \n and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\n The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. ").pack()
    win5.mainloop()


#Menu

taskbar = Menu(window)
task_archive= Menu(taskbar)
task_help= Menu(taskbar)
task_copy = Menu(taskbar)

task_archive.add_command(label="Guardar", command=save)
task_help.add_command(label="Diccionario", command=dictionary)
task_help.add_command(label="Ficha técnica", command=ficha)
task_help.add_command(label="Acerca del Analista...", command=about)
task_copy.add_command(label="Copyright ©", command=copy)
task_copy.add_command(label="Derechos de librerías utilizadas", command=py_copy)

taskbar.add_cascade(label="Archivo", menu=task_archive)
taskbar.add_cascade(label="Ayuda", menu=task_help)
taskbar.add_cascade(label="Derechos de autor", menu=task_copy)

window.config(menu=taskbar)


#Outputs

lista = Listbox(bd = 0,bg = '#FFFFFF', justify="center")
lista.place(x = 120, y = 224,width= 582,height= 148)

lista1 = Listbox(bd = 0,bg = '#FFFFFF', justify="center")
lista1.place(x = 780, y = 281,width= 206,height= 20)

lista2 = Listbox(bd = 0,bg = '#FFFFFF', justify="center")
lista2.place(x = 350, y = 508,width= 349,height= 20)

lista3 = Listbox(bd = 0,bg = '#FFFFFF', justify="center")
lista3.place(x = 350, y = 582,width= 349,height= 20)

lista4 = Listbox(bd = 0,bg = '#FFFFFF', justify="center")
lista4.place(x = 406, y = 654,width= 223,height= 20)


def get_trends():

    news = GoogleNews()
    news = GoogleNews(lang='es', region='CO')
    news.search("Colombia")
    news_list = news.get_texts()

    r = (news_list[0])
    r1 = (news_list[1])
    r2 = (news_list[2])   
    r3 = (news_list[3]) 
    r4 = (news_list[4]) 
    r5 = (news_list[5])
    r6 = (news_list[6])
    r7 = (news_list[7])   
    r8 = (news_list[8]) 

    lista.insert(0, r)
    lista.insert(1, r1)
    lista.insert(2, r2)
    lista.insert(3, r3)
    lista.insert(4, r4)
    lista.insert(5, r5)
    lista.insert(6, r6)
    lista.insert(7, r7)
    lista.insert(8, r8)

    src = str(news_list) 
    sentiment = sentiment_analysis.SentimentAnalysisSpanish()
    emocion = sentiment.sentiment(src) 

    if emocion > 6.5e-11:
        neg = 'Mayormente negativa \U0001F641'
        lista1.insert(END, neg) 
    elif emocion < 4.5e-12:
        pos = 'Mayormente positiva \U0001F600'
        lista1.insert(END, pos)            
    else:
        neu = 'Mayormente neutral \U0001F610'
        lista1.insert(END, neu)       

    p = open ('palabras.txt', 'rt', encoding='utf-8')
    i = open ('imagenes.txt', 'rt', encoding='utf-8')
    c = open ('colores.txt', 'rt', encoding='utf-8')

    if emocion > 9.5e-08:
           pal = p.readlines()[0]
           ima = i.readlines()[0]
           col = c.readlines()[0]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 9.1e-08:
           pal = p.readlines()[1]
           ima = i.readlines()[1]
           col = c.readlines()[1]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 8.5e-09:
           pal = p.readlines()[2]
           ima = i.readlines()[2]
           col = c.readlines()[2]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 8.1e-09:
           pal = p.readlines()[3]
           ima = i.readlines()[3]
           col = c.readlines()[3]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 7.5e-10:
           pal = p.readlines()[4]
           ima = i.readlines()[4]
           col = c.readlines()[4]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 7.1e-10:
           pal = p.readlines()[5]
           ima = i.readlines()[5]
           col = c.readlines()[5]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 6.5e-11:
           pal = p.readlines()[6]
           ima = i.readlines()[6]
           col = c.readlines()[6]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion > 5.5e-11:
           pal = p.readlines()[7]
           ima = i.readlines()[7]
           col = c.readlines()[7]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 5.1e-12:
           pal = p.readlines()[8]
           ima = i.readlines()[8]
           col = c.readlines()[8]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 4.5e-12:
           pal = p.readlines()[9]
           ima = i.readlines()[9]
           col = c.readlines()[9]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 4.1e-13:
           pal = p.readlines()[10]
           ima = i.readlines()[10]
           col = c.readlines()[10]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 3.5e-13:
           pal = p.readlines()[11]
           ima = i.readlines()[11]
           col = c.readlines()[11]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 3.1e-14:
           pal = p.readlines()[12]
           ima = i.readlines()[12]
           col = c.readlines()[12]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 2.5e-14:
           pal = p.readlines()[13]
           ima = i.readlines()[13]
           col = c.readlines()[13]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 2.1e-15:
           pal = p.readlines()[14]
           ima = i.readlines()[14]
           col = c.readlines()[14]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 1.5e-15:
           pal = p.readlines()[15]
           ima = i.readlines()[15]
           col = c.readlines()[15]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    elif emocion < 1.1e-16:
           pal = p.readlines()[16]
           ima = i.readlines()[16]
           col = c.readlines()[16]
           lista2.insert(END,pal)
           lista3.insert(END,ima)
           lista4.insert(END,col)
    else:
          None

def clean():
    lista.delete(0, END)
    lista1.delete(0, END)
    lista2.delete(0, END)
    lista3.delete(0, END)
    lista4.delete(0, END)


#Botones 

path = resource_path("img0.png")
b = PhotoImage(file = path)
button0 = Button(image = b,command = get_trends,relief = "flat")
button0.place(x = 305, y = 700,width = 182,height = 41)

path = resource_path("img1.png")
b1 = PhotoImage(file = path)
button1 = Button(image=b1,command = clean,relief = "flat")
button1.place(x = 562, y = 700,width = 168,height = 41)

#Entry point

if __name__ == '__main__':
    window.mainloop()
