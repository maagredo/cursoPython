# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 09:55:33 2021

@author: aleja
"""

#Primer paso
# Crear Nodo
class Nodo:
    def __init__(self, dato):

        # Informacion que pondriamos en el nodo
        self.dato = dato
        #propiedad siguiente, donde guardamos el siguiente nodo
        # Se crea como un nodo vacio, porque aun no se ha conectado con otro
        self.siguiente = None

    def __repr__(self):
        return f'Nodo:|dato:{self.dato}|siguiente->|{self.siguiente}| '

#SEGUNDO PASO
#CREAR LISTAS
class ListaEnlazadaSimple:
    ## Inicializamos la cabeza de la lista como vacio
    ## No tenemos ningun nodo, el primer nodo lo metemos en la cabeza
    def __init__(self):
        self.head = None
    
    def __str__(self):
        return str(self.head)

    def insert(self, Nodo):
        ## Comprobar si la cabeza esta vacia o no
        if self.head:
            ## Asignar el nodo temporal a la cabeza
            temp_nodo = self.head

            while temp_nodo.siguiente: 
                temp_nodo = temp_nodo.siguiente
            ## Asignar el nuevo nodo al puntero del
