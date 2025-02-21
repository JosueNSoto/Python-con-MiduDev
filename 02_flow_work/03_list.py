#Listas, secuencias mutables de elementos, pueden ser de cualquier tipo
#Se definen con corchetes []

import os
os.system("cls")

lista1=[1,2,3,4,5]#enteros
lista2=["hola", "mundo", "python"]#cadenas
lista3=[1, "hola", 3.14, True]#lista de tipos de datos mixtos
#lista3: list[int | str | float | bool] = [1, "hola", 3.14, True]#Esto es opcional, pero es una forma de indicar que la lista puede contener elementos de diferentes tipos
lista4=[]#lsita vacía
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]#lista de listas o matriz

#Te lo imprime tal cual lo declaramos
#print(lista1)
print(lista2)
#print(lista3)
#print(lista4)
#print(matrix)

#Acceder a los elementos a través del índice
print("Accediendo al tercer elemento de la lista 2")
print(lista2[-1])#python
print("Accediendo al primer elemento de la lista 2")
print(lista2[0])#hola
print("Accediendo al segundo elemento de la lista 2")
print(lista2[-2])#mundo, sucede que accedemos al penúltimo elemento de la lista, con el -2

#accediendo a la matríz
print("Accediendo a la matriz, a la fila 2 y columna 3")
print(matrix[1][2])#6
"""
Trabaja de la siguiente manera: matriz[fila][columna]
matrix = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]#lista de listas o matriz
Para ingresar primero accede a la fila: siendo 0 la primera fila, 1 la segunda fila, 2 la tercera fila... 
Luego accede a la columna: siendo 0 la primera columna, 1 la segunda columna, 2 la tercera columna...
Para acceder al 9 de la matriz, sería: matrix[2][2]
"""