# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 20:23:17 2021

@author: aleja
"""
from vector import vector
import random
#import math

class matriz:
        
    def __init__(self, m, n):
                 self.m = m
                 self.n = n
                 self.mat = [] * (m + 1)
                 for i in range(m + 1):
                        a = [0] * (n + 1)
                        self.mat.append(a)
                        
    def numeroFilas (self):
        return self.m
    
    def numeroColumnas (self):
        return self.n
                        
    """genera datos cargados aleatoriamente"""
    def construyeMatriz(self, r = 100):
           for i in range(1, self.m + 1):
                 for j in range(1, self.n +1):
                          self.mat[i][j] = random.randint(1, r)
                          
    """Recorrido por filas"""                      
    def imprimeMatrizPorFilas(self, mensaje="Matriz sin nombre "):
            print("\n", mensaje)
            for i in range(1, self.m + 1):
                     for j in range(1, self.n + 1):
                               print(self.mat[i][j], "\t", end="")
                     print()
    
    """Recorrido por columnas"""
    def imprimeMatrizPorColumnas(self, mensaje="Matriz sin nombre "):
           print("\n", mensaje)
           for i in range(1, self.n + 1):
                    for j in range(1, self.m + 1):
                                print(self.mat[j][i], "\t", end="")
                    print()
                    
    def intercambiarFilas (self , i,j):
        for k in range (1, self.n):
                        aux = self.mat [i][k]
                        self.mat[i][k] = self.mat [j][k]
                        self.mat[j][k] = aux
                        
    def intercambiarColumnas (self , i,j):
        for k in range (1, self.m):
                        aux = self.mat [k][i]
                        self.mat [k][j] = self.mat [k][i]
                        self.mat [k][i] = aux
    
    """Una función que suma e imprime el total de los datos de las celdas de cada fila de una matriz"""                    
    def sumarFilas (self):
        v = vector( self.m)
        for i in range (1, self.m+1):
            s = 0
            for j in range (1, self.n +1):
                s = s + self.mat [i][j]
            v.agregarDato (s)
        return v
    
    """Para totalizar los datos de las celdas de cada columna de una matriz"""
    def sumarColumnas (self):
        v = vector( self.n)
        for i in range (1, self.n +1):
            s = 0
            for j in range (1, self.m +1):
                s = s + self.mat [j][i]
            v.agregarDato (s)
        return v
       
    def traspuesta (self):
        c = matriz( self.n , self.m)
        for i in range (1, self.m +1):
            for j in range (1, c.n +1):  #validar la c porque decía b
                c.mat [j][i] = self.mat [i][j]
        return c
          
    """Para sumar dos matrices"""
    def __add__(self, b):
        c = matriz(self.m, self.n)
        if self.m != b.m or self.n != b.n:
            print("Matrices no se pueden sumar. Son de dimensiones diferentes")
            return c
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                c.mat[i][j] = self.mat[i][j] + b.mat[i][j]
        return c
    
    """Producto de los datos en la diagonal principal"""    
    def productoDiagonalPrincipal(self):
        f = 1       
        for i in range(1, self.m + 1):
            f = f * self.mat[i][i]
        return f
    
    """Multiplicar matrices"""
    def __mul__(self, b):
        c = matriz(self.m, b.n)
        if self.n != b.m:
            print("Matrices no se pueden multiplicar. ", end = "")
            print("el número de columnas de self es diferente del número de columnas de b")
            return c
        for i in range(1, self.m + 1):
            for j in range(1, b.n + 1):
                c.mat[i][j] = 0
                for k in range(1, self.n + 1):
                    c.mat[i][j] = c.mat[i][j] + self.mat[i][k] * b.mat[k][j]
        return  c
    
    """Se presentan dos funciones: una para sumar los elementos 
    de triangular inferior y la otra para sumar los elementos de la 
    triangular estrictamente inferior."""
    def sumaTriangularInferior(self):
        s = 0
        for i in range(1, self.m + 1):
            for j in range(1, i + 1):
                s = s + self.mat[i][j]
            return s

    def sumaTriangularEstrictamenteInferior(self):
        s = 0
        for i in range(2, self.m + 1):
            for j in range(1, i):
                s = s + self.mat[i][j]
            return