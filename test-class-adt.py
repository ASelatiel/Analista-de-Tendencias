import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk
from types import DynamicClassAttribute
from GoogleNews import GoogleNews
from sentiment_analysis_spanish import sentiment_analysis
from PIL import Image, ImageTk
from utils import resource_path
import os
import re


class Recomendaciones:

    def __init__(self, palabra, imagen, color, punt):

        self.palabra = palabra
        self.imagen = imagen
        self.color = color
        self.punt = punt

    def __str__(self):
        return f'{self.palabra};{self.imagen};{self.color}'

class ArchivoRecomendaciones:

    def __init__(self):
        self.archivo = 'texto.txt'

        self.verificacion()
        self.recom_txt()
        self.puntu_txt()
        self.clf_txt()


    def verificacion(self):
        if not os.path.exists(self.archivo):
            with open(self.archivo, 'wt', encoding='UTF-8') as f:
                pass
    
    def puntu_txt(self, punt):
        for i in self.recom_txt():
            i.punt == punt
            return True
        return False

    def recom_txt(self):
        listado = []
        with open (self.archivo, 'rt', encoding='UTF-8') as f:
            for line in f:
                    division = line.split(';')
                    recom = Recomendaciones(division[0], division[1], division[2], division[3].strip())
                    listado.append(recom)              
            return recom
 
    
    def clf_txt(self, punt):

        for i in self.recom_txt():
            if i.punt == punt:
                return i
        return None


class Noticias: 

    def __init__(self, noticia, puntuacion):
        self.noticia = noticia
        self.puntuacion = puntuacion

        self.newsola()

    def newsola(self):


        self.news = GoogleNews()
        self.news = GoogleNews(lang='es', region='CO')
        self.news.search("Colombia")
        self.news_list = self.news.get_texts()

        self.calculate_emotion = str(self.news_list)
        self.sentiment = sentiment_analysis.SentimentAnalysisSpanish()
        self.emotion = self.sentiment.sentiment(self.calculate_emotion)
    
        


class Window(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.g_recom = ArchivoRecomendaciones()


        self.config_ventana()
        self.tendencias()
        self.eliminar()

    def config_ventana(self):

        self.lista_noticias = Listbox(self.master, bd = 0, bg = '#CBD4E7')
        self.lista_noticias.place(x = 27, y = 205, width= 386, height= 167)
        
        self.lista_punt = Listbox(self.master, bd = 0, bg = '#BDC0DC')
        self.lista_punt.place(x = 124, y = 420,width= 168,height= 24)
    
        self.lista_palabra = Listbox(self.master, bd = 0,bg = '#CBD4E7')
        self.lista_palabra.place(x = 424, y = 207,width= 284,height= 56)
    
        self.lista_imagen = Listbox(self.master, bd = 0,bg = '#CBD4E7')
        self.lista_imagen.place(x = 424, y = 288,width= 284,height= 56)
    
        self.lista_color = Listbox(self.master, bd = 0,bg = '#CBD4E7')
        self.lista_color.place(x = 424, y = 363,width= 284,height= 56)
    
    
        self.path = resource_path("img0.png")
        self.b = PhotoImage(file = self.path)
        self.button0 = Button(self.master, image = self.b, command = self.tendencias, relief = "flat")
        self.button0.place(x = 231, y = 460, width = 150, height = 38)
    
    
        self.path = resource_path("img1.png")
        self.b1 = PhotoImage(file = self.path)
        self.button1 = Button(self.master, image=self.b1, command = self.eliminar, relief = "flat")
        self.button1.place(x = 49, y = 460, width = 150, height = 38)

    
    def tendencias(self):
        noticia = self.lista_noticias
        puntos = self.lista_punt

        self.scrapper = Noticias(noticia, puntos)
        self.noticia = self.scrapper.news_list
        self.lista_noticias.insert(END, self.noticia)
        
        self.puntos = self.scrapper.emotion
        self.lista_punt.insert(END, self.puntos)

        puntu = self.g_recom.recom_txt
        self.data = self.g_recom.clf_txt(puntu)

        if self.puntos < 0.5:
            self.data = puntu
            return self.data
                    
        elif self.puntos < 1:
            self.data = puntu
            return self.data
                        
        elif self.puntos < 1.5:
            self.data = puntu
            return self.data
                        
        elif self.puntos < 2.5:
            self.data = puntu
            return self.data
                        
        elif self.puntos < 3:
            self.data = puntu
            return self.data                        
                    
        elif self.puntos < 3.5:
            self.data = puntu
            return self.data     
                    
        elif self.puntos == 4:
            self.data = puntu
            return self.data 
                    
        elif self.puntos == 4.5:
            self.data = puntu
            return self.data
                    
        elif self.puntos == 5:
            self.data = puntu
            return self.data
                        
        elif self.puntos == 5.5:
            self.data = puntu
            return self.data 
                        
        elif self.puntos == 6:
            self.data = puntu
            return self.data
                    
        elif self.puntos > 6.5:
            self.data = puntu
            return self.data  
                    
        elif self.puntos > 7:
            self.data = puntu
            return self.data
                        
        elif self.puntos > 7.5:
            self.data = puntu
            return self.data
                    
        elif self.puntos > 8:
            self.data = puntu
            return self.data
                    
        elif self.puntos > 8.5:
            self.data = puntu
            return self.data  
                    
        elif self.puntos > 9.5:
            self.data = puntu
            return self.data                          
                    
        else:
            None               


    def eliminar(self):
        self.lista_noticias.delete(0, END)
        self.lista_punt.delete(0, END)
        self.lista_palabra.delete(0, END)
        self.lista_imagen.delete(0, END)
        self.lista_color.delete(0, END)


def main_root():
    root = tk.Tk()
    root.title("Analista de Tendencias")
    root.geometry("957x526")
    root.configure(bg = "#e9ebf2")
    root.resizable(False, False)

    path = resource_path("background.png")
    bg = PhotoImage(file = path)
    canvas = tk.Label(root, image=bg).pack()
   
    taskbar = Menu(root)
    task_archive= Menu(taskbar)
    task_help= Menu(taskbar)


    def dictionary():
        win = tk.Toplevel(root)
        win.title("Diccionario")
        win.geometry("957x526")
        win.configure(bg ="#c8deed")
        win.resizable(False, False)

        path = resource_path("bgdict.png")
        img = tk.PhotoImage(file=path)
        widget = tk.Label(win, image=img).pack()
        win.mainloop()
        
    def info_sheet():
        win2 = Toplevel(root)
        win2.title("Ficha técnica")
        win2.configure(bg ="#F4F3F3")
        win2.geometry("957x526")
        win2.resizable(False, False)
        
        path = resource_path("bgficha.png")
        img1 = PhotoImage(file=path)
        widget = Label(win2, image=img1).pack()
        win2.mainloop()

    def save():
        file = filedialog.asksaveasfile (initialdir="/", defaultextension='.pdf',filetypes=[("PDF",".pdf"),("Todos los archivos", ".*")])

    task_archive.add_command(label="Guardar", command=save)
    task_archive.add_command(label="Imprimir")
    task_help.add_command(label="Diccionario", command=dictionary)
    task_help.add_command(label="Ficha técnica", command=info_sheet)
    
    taskbar.add_cascade(label="Archivo", menu=task_archive)
    taskbar.add_cascade(label="Ayuda", menu=task_help)
    root.config(menu=taskbar)


    adt = Window(root)
    adt.mainloop()
    

if __name__ == "__main__":
    main_root()













