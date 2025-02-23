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

print("Hablaremos del slicing: ")#Rebanado de una lista, con esto podemos obtener una parte de la lista
listaSlicing1=["Apple", "samsung", "Huawei", "Xiaomi", "Motorola", "Sony", "LG", "Nokia"]
print(f"Lista original: ", listaSlicing1)
#Sintaxis: lista[inicio:fin:pasos]
#inicio: Le estamos diciendo desde que indice queremos iniciar, en este caso, el índice 1
#fin: Hasta que índice queremos llegar, en este caso, el índice 5. Sin embargo, este no lo cuenta, no nos lo devuelve, solamente nos devuelve hasta el índice anterior
#pasos: De cuanto en cuanto queremos que nos devuelva los elementos, en este caso, no se especifica, por lo que se toma el valor por defecto, que es 1
print("\nObteniendo del índice 1 al 5")
print(listaSlicing1[1:5])#['samsung', 'Huawei', 'Xiaomi', 'Motorola']
print("\nObteniendo solo los primeros 3 elementos")
print(listaSlicing1[:3])#['Apple', 'samsung', 'Huawei']
print("\nObteniendo solo los últimos 3 elementos")
print(listaSlicing1[-3:])#["Sony", "LG", "Nokia"], En este caso comentamos el -3, porque es el inicio de lo que nos va a traer, y no el final. Si quisieramos obtener todos los elementos, MENOS los últimos 3, sería algo como: print(listaSlicing1[:-3])
print("\nObteniendo solo los últimos 5 elementos")
print(listaSlicing1[3:])#A partir del índice 5, que es "Sony", nos devuelve todos los elementos hasta el final de la lista
print("\nGenerando una copia de la lista")
print("\nCopia de la lista original: ",listaSlicing1[:])#Funciona como un clon de la lista original, si modificamos la copia, no afectará a la lista original

print("\nJugando con los pasos de una Lista:")
lista_Slicing_2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(lista_Slicing_2[::-1])#Invierte la lista, el primer ':' indica que queremos todos los elementos, el segundo ':' indica que queremos todos los elementos, pero en orden inverso
print(lista_Slicing_2[::2])#Obtiene todos los elementos, pero de 2 en 2
print(lista_Slicing_2[1::2])#Iniciamos en el índice 1 y obtenemos los índices pares

#Modificando elementos de una lista
print("\nModificando elementos de una lista")
lista_modificar=[1,2,3,4,5]
print(lista_modificar)
lista_modificar[0]=20
#La sintaxis es: lista[indice]=nuevo_valor
print("El valor de la lista con el nuevo valor es: ",lista_modificar)

#Añadir elementos en una lista
lista_agregada=[1,2,3,4,5]
print("\nNuestra lista original: ",lista_agregada,end='->'". Queriendo llegar al 10")
#Primer método, forma larga y menos eficiente
print("\n\nPrimer método: concatenar listas")
lista_agregada = lista_agregada + [6,7,8,9,10]#crea una nueva lista, le asigna el valor, y luego la asigna a la lista original. Esto no es eficiente.
print(f"Nuestra lista final es: ",lista_agregada)
#Segundo método, corta y eficiente
print("\nSegundo método: concatenar listas")
lista_agregada += [6,7,8,9,10,11,12,13,14,15]#Este método es más eficiente, ya que no crea una nueva lista, sino que modifica la lista original
print(f"Nuestra lista final es: ",lista_agregada)

#Recuperar la longitud de una lista
print("La longitud de la lista es: ",len(lista_agregada))