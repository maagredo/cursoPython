# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 09:28:56 2021

@author: aleja
"""

from tkinter import *
"""
window_main = Tk() #Crear ventana
window_main.title("Mi primer ventana") #Título de ventana
window_main.geometry("520x480") #Tamaño de ventana
window_main.config(bg="blue") #Color ventana emergente
#window_main.iconbitmap('/path/to/ico/icon.ico')
window_main.mainloop()
"""

def accion(valor):
    entradas.config(text=valor)
    #text_label.config
  


# Botones
top = Tk()
top.geometry("200x200")

#Label1 = Label(top, text="calculadora")
text_label = Label(top)
text_label.pack()

Boton1 = Button(top, text = "1", fg="green", command= accion("1"))
Boton1.place(x = 50,y = 50)
Boton2 = Button(top, text = "2", fg="green", command= accion("2"))
Boton2.place(x = 80,y = 50)
Boton3 = Button(top, text = "3", fg="green", command= accion("3"))
Boton3.place(x = 110,y = 50)
Boton4 = Button(top, text = "4", fg="green", command= accion("4"))
Boton4.place(x = 50,y = 80)
Boton5 = Button(top, text = "5", fg="green", command= accion("5"))
Boton5.place(x = 80,y = 80)
Boton6 = Button(top, text = "6", fg="green", command= accion("6"))
Boton6.place(x = 110,y = 80)
Boton7 = Button(top, text = "7", fg="green", command= accion("7"))
Boton7.place(x = 50,y = 110)
Boton8 = Button(top, text = "8", fg="green", command= accion("8"))
Boton8.place(x = 80,y = 110)
Boton9 = Button(top, text = "9", fg="green", command= accion("9"))
Boton9.place(x = 110,y = 110)
Boton0 = Button(top, text = "0", fg="green", command= accion("0"))
Boton0.place(x = 80,y = 140)

Botonmas = Button(top, text = "+")
Botonmas.place(x = 160,y = 50)
Botonmenos = Button(top, text = "-")
Botonmenos.place(x = 160,y = 80)
Botonmultiplicar = Button(top, text = "x")
Botonmultiplicar.place(x = 160,y = 110)
Botondividir = Button(top, text = "/")
Botondividir.place(x = 160,y = 140)

entradas = Entry(top, font ="Arial"  , width = 15, bg = "light blue", justify = "right")
#entradas.place(padx=10,pady=10)
entradas.pack(side=TOP,padx=10, pady=10)


frame = Frame(top)
frame.pack()

bottomframe = Frame(top)
bottomframe.pack( side = BOTTOM )

top.mainloop()