# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 16:06:16 2021

@author: aleja
"""
#import random

class vector:

    def __init__(self, n):
        self.n = n
        self.V = [0] * (n + 1)
        
    def imprimeVector(self, mensaje = "vector sin nombre: \t"):
        print("\n", mensaje, end=" ")
        for i in range(1, self.V[0] + 1):
            print(self.V[i], end=", ")
#            print()

    def mayor(self):
        mayor = 1
        for i in range(1, self.V[0] + 1):
            if self.V[i] >= self.V[mayor]:
                mayor = i
        return mayor
            
    def menor(self):
        menor = 1
        for i in range(1, self.V[0] + 1):
            if self.V[i] < self.V[menor]:
                menor = i
        return menor
            
    def intercambiar(self, a, b):
        aux = self.V[a]
        self.V[a] = self.V[b]
        self.V[b] = aux
