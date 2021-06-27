# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 12:11:39 2021

@author: aleja
"""

class Pila:
    def __init__(self):
        self.elemento=[] ##definir el elemento como algo vacio
    def elemento_vacio(self):
        return self.elemento == [] ##devolver un boleano
    def apilar(self,elemento):
        self.elemento.append(elemento)
    def remover(self): 
        self.elemento.pop() 
    def devolver(self): 
        print(self.elemento)

    
pila = Pila()
pila.elemento_vacio()
pila.apilar(1)
pila.apilar(2)
pila.devolver()
